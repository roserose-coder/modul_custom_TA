# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_self_borrow = fields.Boolean(string="Self borrow", implied_group='roomster.group_self_borrow')

    # group_self_borrow = fields.Boolean(string="Self borrow" , implied_group='base.group_no_one')
