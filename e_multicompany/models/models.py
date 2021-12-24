# -*- coding: utf-8 -*-

from odoo import models, fields, api


class e_multicompany(models.AbstractModel):
    _name = 'e_multicompany.e_multicompany'
    _description = 'e_multicompany.e_multicompany'

    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)
