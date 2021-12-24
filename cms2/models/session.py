# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError

import datetime


class cms2_session(models.Model):
    _name = 'cms2.session'
    _description = 'cms2.session'
    _rec_name = 'session_name'
    _inherit = ['base.archive', 'base.multicompany', 'mail.thread', 'mail.activity.mixin']
    session_name = fields.Char('Session Name')

    program_id = fields.Many2many('cms2.program')

    start_time = fields.Datetime(default=fields.Datetime.today)
    end_time = fields.Datetime(default=fields.Datetime.today)

    teacher_id = fields.Many2one('res.users',
                                 domain=lambda self: [("groups_id", "=", self.env.ref("cms2.group_teacher").id)])

    @api.model
    def create(self, vals):
        resa = super(cms2_session, self).create(vals)
        resa.message_subscribe(partner_ids=[resa.teacher_id.partner_id.id])
        # resa.message_subscribe(partner_ids=self.env['res.users'].browse(vals['owner_user_id']).partner_id.ids)
        resa.message_post_with_view('cms2.teacher_session_notif_qweb')
        return resa
