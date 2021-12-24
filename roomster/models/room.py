# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError

import datetime


class roomster_room(models.Model):
    _name = "roomster.room"
    _rec_name = 'name'
    name = fields.Char(required=True, string="Room Name")
    floor = fields.Integer(string='Room Floor')
    capacity = fields.Integer(string='Room Capacity')
    building = fields.Char(string='Room Building')
    description = fields.Text(string='Room Description')
    responsible = fields.Many2one('res.users', string="Responsible", default=lambda self: self.env.user)
    ress = fields.Char(related='responsible.name')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        # required=True,
        domain=[('name', 'in', ('USD', 'IDR'))],
        default=lambda self: self.env['res.currency'].search([('name', '=', 'IDR')]))

    price = fields.Monetary(string="Price", currency_field='currency_id')
    booked_schedule = fields.One2many('roomster.booked', 'name')

    # session_id = fields.One2many('cms2.session', 'room_id')
    rent_count = fields.Integer(compute="_compute_rent_count")

    def _compute_rent_count(self):
        Roomrent = self.env['roomster.booked']
        for room in self:
            # room.rent_count = Roomrent.search_count(
            #     [('start_date', '>', fields.Datetime.today)]
            # )
            room.rent_count = Roomrent.search_count(
                [(1, '=', 1)]
            )

    def save(self, vals):
        return True


class roomster_room_booked(models.Model):
    _name = "roomster.booked"
    _inherit = ['mail.thread', 'base.archive', 'mail.activity.mixin']
    _rec_name = 'name'
    name = fields.Many2one('roomster.room',
                           ondelete=False,
                           context={},
                           domain=[], string="Room Name")
    borrower = fields.Many2one('res.users', string="Borrower")
    start_date = fields.Datetime(default=fields.Datetime.today)
    end_date = fields.Datetime(default=fields.Datetime.today)
    currency_id = fields.Many2one('res.currency', domain=[('name', 'in', ('IDR', 'USD'))],
                                  default=lambda self: self.env.user.company_id.currency_id.id)

    price_list = fields.Monetary(related='name.price', currency_field='currency_id')
    total_price = fields.Monetary(compute='_calculate_subtotal')
    responsible = fields.Many2one(related='name.responsible')

    @api.depends('start_date', 'end_date')
    def _calculate_subtotal(self):
        for booked in self:
            delta = booked.end_date - booked.start_date
            booked.total_price = delta.days * booked.price_list

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        for record in self:
            if record.start_date and record.start_date > record.end_date:
                raise models.ValidationError('End date can not be earlier than start date')

    @api.model
    def create(self, vals):

        daftar = self.env['roomster.booked'].search([('name', '=', vals['name'])])

        if daftar:
            for room in daftar:
                awal = datetime.datetime.strptime(vals['start_date'], '%Y-%m-%d %H:%M:%S')
                akhir = datetime.datetime.strptime(vals['end_date'], '%Y-%m-%d %H:%M:%S')

                latest_start = max(awal, room.start_date)
                earliest_end = min(akhir, room.end_date)

                if (earliest_end - latest_start).days + 1 > 0:
                    raise models.ValidationError('overlapping')

        resa = super(roomster_room_booked, self).create(vals)
        resa.message_subscribe(partner_ids=[resa.responsible.partner_id.id, resa.borrower.partner_id.id])
        resa.activity_schedule('mail.mail_activity_data_meeting', user_id=resa.responsible.id and resa.borrower.id,
                               date_deadline=resa.end_date,
                               summary='room is borrowed')
        resa.activity_schedule('mail.mail_activity_data_meeting', user_id=resa.responsible.id,
                               summary='do not forget to create an invoice')
        resa.activity_schedule('mail.mail_activity_data_meeting', user_id=resa.responsible.id,
                               date_deadline=resa.start_date,
                               summary='check whether the invoice has been paid')

        return resa

    def action_view_partner_invoices(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("account.action_move_out_invoice_type")
        action['domain'] = [
            ('move_type', 'in', ('out_invoice', 'out_refund')),
            ('partner_id', 'child_of', self.borrower.id),
        ]
        action['context'] = {'default_move_type': 'out_invoice', 'move_type': 'out_invoice', 'journal_type': 'sale',
                             'search_default_unpaid': 1}
        return action

    # @api.model
    # def create(self, vals):
    #     for x in  self.env['roomster.booked'].search(['name']) :
    #         print(x)
    #     result = super(roomster_room_booked, self).create(vals)
    #
    #     return result
    # @api.model
    # def create(self, vals):
    #
    #     domain = [
    #         '|', ('end_date', '<', vals['start_date']),
    #         (vals['end_date'], '<', 'start_date')
    #     ]
    #     list = self.env['roomster.booked'].search(domain)
    #     if not list :
    #
    #         result = super(roomster_room_booked, self).create(vals)
    #
    #         return result
    #     else :
    #         raise models.ValidationError('Overlapping date')

    # @api.model
    # def create(self, vals):
    #     # print(self)
    #     # print(vals)
    #     vals['status'] = True
    #     result = super(roomster_room_booked, self).create(vals)
    #
    #     return result

    # @api.model
    # def create(self,vals):
    # self.env.cr.execute("update roomster_room set status = TRUE")
    # self.env.cr.commit()
    # record = self.env['roomster.room'].search([])
    # record.update({'status': True})
    # category_books = self.search([('category_id', '=',
    #                                category.id)])
    # record_to_update = self.env['roomster.room'].search([('name', 'in', self.name)]).id
    # record_to_update.update({'status': True})
    # res = super(roomster.booked).create(vals)
    # return res
