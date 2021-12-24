# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SlideQuestion(models.Model):
    _name = "slide.question"
    _inherit = ['slide.question', 'e_multicompany.e_multicompany']


class SlideAnswer(models.Model):
    _name = "slide.answer"
    _inherit = ['slide.answer', 'e_multicompany.e_multicompany']
