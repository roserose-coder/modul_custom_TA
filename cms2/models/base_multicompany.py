# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseMultiCompany(models.AbstractModel):
    _name = 'base.multicompany'
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)