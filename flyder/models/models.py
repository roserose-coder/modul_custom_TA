# -*- coding: utf-8 -*-

from odoo import models, fields, api


class flyder(models.Model):
    _name = 'flyder.flyder'
    _description = 'flyder.flyder'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')
    date_order = fields.Date('Date Order', default=fields.Date.today())
    date_finish = fields.Date('Finish Date',default=fields.Date.today())
    deadline = fields.Date('Deadline', default=fields.Date.today())
    description = fields.Html('Description')
    # background_color = fields.Integer('Background Color')
    failed = fields.Boolean(default=False)
    qty = fields.Integer('Quantity')
    data = fields.Binary('File to Upload')
    # currency_id = fields.Many2one('res.currency', domain=[('name', 'in', ('IDR', 'USD'))],
    #                               default=lambda self: self.env.user.company_id.currency_id.id)
    # price = fields.Monetary("Price", currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        # required=True,
        domain=[('name', 'in', ('USD', 'IDR'))],
        default=lambda self: self.env['res.currency'].search([('name', '=', 'IDR')]))

    price = fields.Monetary(string="Price", currency_field='currency_id')

    def _default_flyder_stage(self):
        Stage = self.env['flyder.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)

    status = fields.Many2one('flyder.stage', default=_default_flyder_stage, group_expand='_group_expand_stages')
    # status_order = fields.Selection([
    #     ('3', 'Rejected'),
    #     ('2', 'Accepted'),
    #     ('1', 'Pending'),
    #     ('0', 'Prepare'),
    # ],default='1')

    # price = fields.Integer()
    responsible = fields.Many2one('res.users')
    customer = fields.Many2one('res.partner', default=lambda self: self.env.user.partner_id)

    color = fields.Integer()
    popularity = fields.Selection([
        ('no', 'No Demand'),
        ('low', 'Low Demand'),
        ('medium', 'Average Demand'),
        ('high', 'High Demand')], default="no")
    tag_ids = fields.Many2many('flyder.tag')

    @api.model
    def change_state(self, new_status):
        for order in self:
            order.status_order = new_status

    def make_pending(self):
        if self.user_has_groups('flyder.group_flyder_handler'):
            self.change_state('1')

    def make_accepted(self):
        if self.user_has_groups('flyder.group_flyder_order'):
            self.change_state('2')
            flyer = self.env['flyder.flyder'].search([('id', '=', self.id)])
            flyer.date_finish = fields.Datetime.now()

    def make_rejected(self):
        if self.user_has_groups('flyder.group_flyder_order'):
            self.change_state('3')

    def make_prepare(self):
        if self.user_has_groups('flyder.group_flyder_handler'):
            self.change_state('0')

    def _check_overdue(self):
        #self.env['flyder.flyder'].search([('deadline','=',fields.Date.today())]).write({'status':5})

        recs = self.env['flyder.flyder'].search([('deadline','=',fields.Date.today())])
        for rec in recs:
            rec.write({'failed':True})
        # for flyer in self:
        #     print(flyer)
        #     if flyer.deadline == fields.Date.today():
        #         flyer.status = 5
        #         print(flyer.status)
        # print('cron should be working rn')

    def action_view_partner_invoices(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("account.action_move_out_invoice_type")
        action['domain'] = [
            ('move_type', 'in', ('out_invoice', 'out_refund')),
            ('partner_id', 'child_of', self.customer.id),
        ]
        action['context'] = {'default_move_type': 'out_invoice', 'move_type': 'out_invoice', 'journal_type': 'sale',
                             'search_default_unpaid': 1}
        return action

    def write(self, vals):
        # try:
        #     if vals['status']:
        # flyer = self.search([('id', '=', self.id)])
        # if flyer.customer.id != self.env.user.id and flyer.responsible.id != self.env.user.id:
        #     raise models.ValidationError(
        #         'cant do that')

        # user_now = self.env.user
        partner_now = self.env.user.partner_id
        flyer = self.search([('id', '=', self.id)])

        if self.user_has_groups('flyder.group_flyder_order'):
            if partner_now != flyer.customer :
                raise models.ValidationError('Error Cannot')
        # if user_now != flyer.responsible and partner_now != flyer.customer :
        #     raise models.ValidationError(
        #         'Error Cannot')

        if vals.get('status'):
            if vals['status'] == 3 or vals['status'] == 4:
                if not self.user_has_groups('flyder.group_flyder_order'):
                    raise models.ValidationError(
                        'Error! you are not allowed to change the status into rejected or accepted ! Customer only.')

                flyer.date_finish = fields.Date.today()
            elif vals['status'] == 1 or vals['status'] == 2:
                if not self.user_has_groups('flyder.group_flyder_handler'):
                    raise models.ValidationError(
                        'Error! you are not allowed to change the status into pending or prepare ! Admin only.')
            # else:
            #     return super(flyder, self).write(vals)
        # if vals['price']:
        if vals.get('price'):
            if not self.user_has_groups('flyder.group_flyder_handler'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the price ! Admin only.')

        return super(flyder, self).write(vals)

    # except:
    #     print('something wrong')

    # return super(flyder, self).write(vals)

    @api.model
    def get_user_from_group(self, group_id):
        users_ids = []
        sql_query = """select uid from res_groups_users_rel where gid = %s"""
        params = (group_id,)
        self.env.cr.execute(sql_query, params)
        results = self.env.cr.fetchall()
        for users_id in results:
            users_ids.append(users_id[0])
        return users_ids

    @api.model
    def create(self, vals):
        if vals['status']:
            if vals['status'] == 3 or vals['status'] == 4:
                if not self.user_has_groups('flyder.group_flyder_order'):
                    raise models.ValidationError(
                        'Error! you are not allowed to change the status into rejected or accepted ! Customer only.')

            # if vals['status'] == 1 or vals['status'] == 2:
            #     if not self.user_has_groups('flyder.group_flyder_handler'):
            #         raise models.ValidationError(
            #             'Error! you are not allowed to change the status into pending or prepare ! Admin only.')

            # except:
            #     print('something wrong')
        #  followers_1 = self.get_users_from_group('group_flyder_handler')
        # followers_2 = self.get_users_from_group('group_flyder_order')

        if vals['price']:
            if not self.user_has_groups('flyder.group_flyder_handler'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the price ! Admin only.')

        resa = super(flyder, self).create(vals)
        resa.message_subscribe(partner_ids=[resa.customer.id])

        domain = [('model', '=', 'res.groups'), ('name', '=', 'group_flyder_handler')]
        model_data = self.env['ir.model.data'].search(domain, limit=1)
        staff_userid = self.get_user_from_group(model_data.res_id)
        if resa.deadline:
            for user_id in staff_userid:
                resa.activity_schedule('mail.mail_activity_data_meeting', user_id=user_id, date_deadline=resa.deadline,
                                       summary='Flyers order deadline')

        return resa


class flyder_stage(models.Model):
    _name = 'flyder.stage'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    # status = fields.Selection(
    #         [('-1', 'Preparation'),
    #          ('0', 'Pending'),
    #          ('1', 'Accepted'), ('-2', 'Rejected')],
    #         'State', default='-1')

    status_order = fields.Selection([
        ('3', 'Rejected'),
        ('2', 'Accepted'),
        ('1', 'Pending'),
        ('0', 'Prepare'),

    ], default='1')


class flyder_tag(models.Model):
    _name = 'flyder.tag'
    name = fields.Char()
    color = fields.Integer()
