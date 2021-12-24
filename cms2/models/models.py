# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cms2(models.Model):
#     _name = 'cms2.cms2'
#     _description = 'cms2.cms2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
