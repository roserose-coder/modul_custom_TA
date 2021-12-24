from odoo import models, fields, api


class roomster_room(models.Model):
    _inherit = 'roomster.room'
    session_id = fields.One2many('cms2.session', 'room_id')
