# -*- coding: utf-8 -*-

from odoo import models, fields, api

#material sessionya
class cms2_material_session_partner(models.Model):
      _name = 'cms2.material.session.partner'
      _description = 'cms2.material.session.partner'

      session_id = fields.Many2one('cms2.session')
      partner_id = fields.Many2one('res.partner')
      material_id = fields.Many2one('cms2.material')
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
