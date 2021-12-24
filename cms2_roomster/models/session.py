# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cms2_session(models.Model):
    _inherit = 'cms2.session'

    room_id = fields.Many2one('roomster.room', string="Room Name")
    currency_id = fields.Many2one('res.currency', domain=[('name', 'in', ('IDR', 'USD'))],
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    price = fields.Monetary(related='room_id.price', currency_field='currency_id')
    total_price = fields.Monetary(compute='_calculate_subtotal')

    @api.depends('start_time', 'end_time')
    def _calculate_subtotal(self):
        for booked in self:
            delta = booked.end_time - booked.start_time
            booked.total_price = delta.days * booked.price


    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""

        self.env['roomster.booked'].create({
            'name':values['room_id'],
            'currency_id':values['currency_id'],
            'start_date': values['start_time'],
            'end_date': values['end_time'],
            'borrower': self.env.uid
        })

        return super(cms2_session, self).create(values)
