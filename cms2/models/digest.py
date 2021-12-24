from odoo import models, fields, api


class Digest(models.Model):
    _inherit = 'digest.digest'

    # test = fields.Char()
    kpi_offline_course = fields.Boolean('Created Course')
    kpi_offline_course_value = fields.Integer(compute='_compute_kpi_offline_course_value')

    kpi_session_course = fields.Boolean('Created Session')
    kpi_session_course_value = fields.Integer(compute='_compute_kpi_session_course_value')

    #
    # def _compute_kpi_offline_course_value(self):
    #     for record in self:
    #         start, end, company = record._get_kpi_compute_parameters()
    #         record.kpi_offline_course_value = self.env['cms2.program'].search_count([
    #             ('start_date', '>=', start),
    #             ('end_date', '<', end)
    #         ])
    #
    # def _compute_kpi_session_course_value(self):
    #     for record in self:
    #         start, end, company = record._get_kpi_compute_parameters()
    #         record.kpi_session_course_value = self.env['cms2.session'].search_count([
    #             ('start_time', '>=', start),
    #             ('end_time', '<', end)
    #         ])

    def _compute_kpi_offline_course_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_offline_course_value = self.env['cms2.program'].search_count([
                ('start_date', '>=', start),
                ('start_date', '<', end)
            ])

    def _compute_kpi_session_course_value(self):
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            record.kpi_session_course_value = self.env['cms2.session'].search_count([
                ('start_time', '>=', start),
                ('start_time', '<', end)
            ])
