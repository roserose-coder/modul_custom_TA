from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'
    session_id = fields.One2many('cms2.session','teacher_id')