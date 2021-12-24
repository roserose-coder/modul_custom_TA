from odoo import fields, models, api

import datetime


class roomster_book_wizard(models.TransientModel):
    _name = "roomster.booked.wizard"

    name = fields.Many2one('roomster.room',
                           ondelete=False,
                           context={},
                           domain=[], string="Room Name")
    borrower = fields.Many2one('res.users', string="Borrower", default=lambda self: self.env.user)
    start_date = fields.Datetime(default=fields.Datetime.today)
    end_date = fields.Datetime(default=fields.Datetime.today)
    currency_id = fields.Many2one('res.currency', domain=[('name', 'in', ('IDR', 'USD'))],
                                  default=lambda self: self.env.user.company_id.currency_id.id)

    price_list = fields.Monetary(related='name.price', currency_field='currency_id')
    total_price = fields.Monetary(compute='_calculate_subtotal')

    @api.onchange('star_date','end_date')
    def onchange_start_end_date(self):
        daftar = self.env['roomster.booked'].search([('name', '=', self.name.id)])

        if daftar:
            for room in daftar:
                awal = datetime.datetime.strptime(str(self.start_date), '%Y-%m-%d %H:%M:%S')
                akhir = datetime.datetime.strptime(str(self.end_date), '%Y-%m-%d %H:%M:%S')

                latest_start = max(awal, room.start_date)
                earliest_end = min(akhir, room.end_date)

                if (earliest_end - latest_start).days + 1 > 0:
                    raise models.ValidationError(' overlapping')


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

    def add_room_rents(self):

        for wizard in self:
            # print(wizard.name.id, 'test')
            # d1 = datetime.strptime(str(self.birthday), "%Y-%m-%d").date()

            # 'start_date': datetime.datetime.strptime(str(wizard.start_date), '%Y-%m-%d %H:%M:%S'),
            # 'end_date': datetime.datetime.strptime(str(wizard.end_date), '%Y-%m-%d %H:%M:%S'),
            rnt_as_sudo =  self.env['roomster.booked'].sudo()
            rnt_as_sudo.create({
                'name': wizard.name.id,
                'borrower': wizard.borrower.id,
                'start_date': str(wizard.start_date),
                'end_date': str(wizard.end_date),
                'currency_id': wizard.currency_id.id,
                'price_list': wizard.price_list,
                'total_price': wizard.total_price
            })



