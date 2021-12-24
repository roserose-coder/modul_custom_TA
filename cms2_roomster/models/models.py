# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cms2_roomster(models.Model):
#     _name = 'cms2_roomster.cms2_roomster'
#     _description = 'cms2_roomster.cms2_roomster'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
