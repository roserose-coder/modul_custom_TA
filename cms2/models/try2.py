from odoo import models, fields, api


class try_try(models.Model):
    _name = 'cms2.try2'

    def _get_teacher(self):
        users_search = self.env['res.users'].search([])
        users = []
        for userz in users_search:
            if userz.user_has_groups('cms2.group_teacher'):
                users.append(userz.id)
        return [('id', 'in', users)]

    teach = fields.Many2one('res.users', domain=_get_teacher)
