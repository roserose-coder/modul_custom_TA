# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cms2_material_partner(models.Model):
    _name = 'cms2.material.partner'
    _description = 'cms2.material.partner'

    _inherit = ['base.archive', 'base.multicompany', 'mail.thread', 'mail.activity.mixin', ]
    teacher_name = fields.Many2one('res.users',related='material_id.teacher_id',string="Teacher")
    partner_id = fields.Many2one('res.partner')
    material_id = fields.Many2one('cms2.material')
    score = fields.Float()

    @api.model
    def create(self, vals):
        res = super(cms2_material_partner, self).create(vals)

        res.message_subscribe(partner_ids=[res.partner_id.id])
        return res

    def book_return_reminder(self):
        self.message_post_with_view('cms2.material_score_qweb')