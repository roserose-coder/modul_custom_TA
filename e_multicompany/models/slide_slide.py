from odoo import api, models


class Slide(models.Model):
    _name = 'slide.slide'
    _inherit = [
        'slide.slide', 'e_multicompany.e_multicompany']
