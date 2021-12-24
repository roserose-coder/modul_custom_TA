
from odoo import models, fields, api


class Digest(models.Model):
    _inherit = 'digest.digest'

    #test = fields.Char()
    kpi_room_rent = fields.Boolean('Room Rent')
    kpi_room_rent_value = fields.Integer(compute='_compute_kpi_room_rent_value')

    # def _compute_kpi_room_rent_value(self):
    #     for record in self:
    #         start, end, company = record._get_kpi_compute_parameters()
    #         record.kpi_room_rent_value = self.env['roomster.booked'].search_count([
    #                 ('start_date', '>=', start),
    #                 ('end_date', '<', end)
    #         ])

    def _compute_kpi_room_rent_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_room_rent_value = self.env['roomster.booked'].search_count([
                ('start_date', '>=', start),
                ('start_date', '<', end)
            ])