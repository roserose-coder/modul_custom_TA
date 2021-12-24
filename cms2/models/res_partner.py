from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = ['res.partner']

    # test = fields.Char()
    program_id = fields.Many2many('cms2.program')
    #material_id = fields.Many2many('cms2.material')

    material_id = fields.One2many('cms2.material.partner','partner_id')
    score_id= fields.Float(related='material_id.score')
    sid = fields.Char("SID")
    # Add a new column to the res.partner model, by default partners are not
    # instructors
    # instructor = fields.Boolean("Instructor", default=False)
    #
    # session_ids = fields.Many2many('openacademy.session',
    #     string="Attended Sessions", readonly=True)
