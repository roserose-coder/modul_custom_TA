# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cms2_material(models.Model):
    _name = 'cms2.material'
    _description = 'cms2.material'
    _inherit = ['base.archive', 'base.multicompany', 'mail.thread', 'mail.activity.mixin']

    name = fields.Char("Material Name")
    content = fields.Binary("Content")
    description = fields.Text("Material Description")
    teacher_id = fields.Many2one('res.users',domain=lambda self: [("groups_id", "=", self.env.ref( "cms2.group_teacher" ).id)])

    @api.model
    def create(self, vals):
        resa = super(cms2_material, self).create(vals)
        resa.message_subscribe(partner_ids=[resa.teacher_id.partner_id.id])
        # resa.message_subscribe(partner_ids=self.env['res.users'].browse(vals['owner_user_id']).partner_id.ids)
        resa.message_post_with_view('cms2.teacher_notif_qweb')
        return resa
