# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cms2_session_partner(models.Model):
    _name = 'cms2.session.partner'
    _description = 'cms2.session.partner'
    _inherit = ['base.archive', 'base.multicompany', 'mail.thread', 'mail.activity.mixin', ]

    program_id = fields.Many2one('cms2.program')
    session_id = fields.Many2one('cms2.session')
    partner_id = fields.Many2one('res.partner')

    teacher_id = fields.Many2one('res.users', related='session_id.teacher_id',string ='Teacher Name')
    attendance_status = fields.Selection([
        ('5', 'Present'),  # success
        ('4', 'Permission'),
        ('3', 'on Duty'),
        ('2', 'Sick'),
        ('1', 'on Leave'),
        ('0', 'No Information'),
        ('-1', ''),

    ]
        , 'Attendance Status', default='-1', tracking=True)
    attendance_name = fields.Char()

    @api.onchange('attendance_status')
    def onchange_attendance_status(self):
        self.attendance_name = dict(self._fields['attendance_status'].selection).get(self.attendance_status)

    def book_return_reminder(self):
        message = dict(self._fields['attendance_status'].selection).get(self.attendance_status)
        self.message_post(body=message)

        template_id = self.env.ref('cms2.session_attendance_renewed')
        self.message_post_with_template(template_id.id)

    @api.model
    def create(self, vals):
        res = super(cms2_session_partner, self).create(vals)

        res.message_subscribe(partner_ids=[res.partner_id.id])
        return res
