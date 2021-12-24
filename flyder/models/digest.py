from odoo import models, fields, api


class Digest(models.Model):
    _inherit = 'digest.digest'

    # test = fields.Char()
    kpi_flyer_order = fields.Boolean('Flyer order')
    kpi_flyer_order_value = fields.Integer(compute='_compute_kpi_flyer_order_value')

    kpi_flyer_order_2 = fields.Boolean('Flyer overdue')
    kpi_flyer_order_2_value = fields.Integer(compute='_compute_kpi_flyer_order_overdue_value')

    # def _compute_kpi_room_rent_value(self):
    #     for record in self:
    #         start, end, company = record._get_kpi_compute_parameters()
    #         record.kpi_room_rent_value = self.env['roomster.booked'].search_count([
    #                 ('start_date', '>=', start),
    #                 ('end_date', '<', end)
    #         ])

    # for record in self:
    #     start, end, company = record._get_kpi_compute_parameters()
    #     record.kpi_crm_opportunities_won_value = self.env['crm.lead'].search_count([
    #         ('type', '=', 'opportunity'),
    #         ('probability', '=', '100'),
    #         ('date_closed', '>=', start),
    #         ('date_closed', '<', end),
    #         ('company_id', '=', company.id)
    #     ])

    def _compute_kpi_flyer_order_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_flyer_order_value = self.env['flyder.flyder'].search_count([
                ('date_order', '>=', start),
                ('date_order', '<', end)
            ])

    #
    def _compute_kpi_flyer_order_overdue_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_flyer_order_2_value = self.env['flyder.flyder'].search_count([
                ('failed', '=', True),
                ('date_finish', '>=', start),
                ('date_finish', '<', end)
            ])
