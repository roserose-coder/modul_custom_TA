from odoo import api, models


class ChannelUsersRelation(models.Model):
    _name = 'slide.channel.partner'
    # _description = 'Channel / Partners (Members)'

    _inherit = ['slide.channel.partner', 'e_multicompany.e_multicompany']


class Channel(models.Model):
    """ A channel is a container of slides. """
    _name = 'slide.channel'
    _inherit = ['slide.channel', 'e_multicompany.e_multicompany']
