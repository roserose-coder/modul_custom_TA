# -*- coding: utf-8 -*-
import base64
from datetime import timedelta

from odoo import models, fields, api
from random import randint


class cms2_program(models.Model):
    _name = 'cms2.program'
    _description = 'cms2.program'
    _rec_name = 'program_name'
    _inherit = ['mail.thread', 'base.archive', 'mail.activity.mixin', 'base.multicompany', 'image.mixin',
                'website.multi.mixin']
    program_name = fields.Char('Program Name')
    image_1920 = fields.Image('Program Image')
    # start_date = fields.Datetime(default=fields.Datetime.now)
    # end_date = fields.Datetime(default=fields.Datetime.now)

    start_date = fields.Date(default=fields.Date.today())
    end_date = fields.Date(default=fields.Date.today())
    description = fields.Text()
    session_id = fields.Many2many('cms2.session')
    partner_id = fields.Many2many('res.partner')
    material_id = fields.Many2many('cms2.material')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id)

    def _default_program_stage(self):
        Stage = self.env['cms2.program.stage']
        return Stage.search([], limit=1)

    @api.model
    def _group_expand_stages(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        'cms2.program.stage',
        default=_default_program_stage,
        group_expand='_group_expand_stages'
    )
    color = fields.Integer()
    popularity = fields.Selection([
        ('no', 'No Demand'),
        ('low', 'Low Demand'),
        ('medium', 'Average Demand'),
        ('high', 'High Demand')], default="no")
    tag_ids = fields.Many2many('cms2.program.tag')
    rates = fields.One2many('cms2.program.rating', 'program_id')

    @api.model
    def default_random_pin(self):

        # return "".join(choice(digits) for i in range(1))
        return randint(0, 10)

    @api.model
    def default_random_pin1(self):

        # return "".join(choice(digits) for i in range(1))

        number = randint(1, 5)
        # if number == 1:
        #     number = 'present'
        # elif number == 2:
        #     number = 'permission'
        # elif number == 3:
        #     number = 'on duty'
        # elif number == 4:
        #     number = 'on leave'
        # elif number == 5:
        #     number = 'no information'
        #
        return str(number)

    @api.model
    def data_res_part(self):
        all_program = self.search([])
        for program in all_program:
            for session in program.session_id:
                for person in program.partner_id:
                    self.env['cms2.session.partner'].create({
                        'program_id': program['id'],
                        'session_id': session['id'],
                        'partner_id': person['id'],
                        'attendance_status': self.default_random_pin1()

                    })

    @api.model
    def data_material_part(self):
        all_program = self.search([])
        for program in all_program:
            for material in program.material_id:
                for person in program.partner_id:
                    self.env['cms2.material.partner'].create({
                        'material_id': material['id'],
                        'partner_id': person['id'],
                        'score': self.default_random_pin()
                    })

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('-1', '0'),
                   ('0', '-1'),
                   ('0', '1'),
                   ('0', '-2'),
                   ('-2', '-1')]
        return (old_state, new_state) in allowed

    # def change_state(self, new_status):
    #     # for program in self:
    #     #     if program.is_allowed_transition(cms2_program.status, new_status):
    #     #         program.status = new_status
    #     #     else:
    #     #         continue
    #     for program in self:
    #         program.status = new_status
    #
    # def make_pending(self):
    #     self.change_state('0')
    #
    # def make_accepted(self):
    #     if self.user_has_groups('cms2.group_director'):
    #         self.change_state('1')
    #
    #     else:
    #         raise models.ValidationError(
    #             'Error! you are not allowed to change the status into accepted ! Director only.')
    #
    # def make_rejected(self):
    #     if self.user_has_groups('cms2.group_director'):
    #         self.change_state('-2')
    #
    #     else:
    #         raise models.ValidationError(
    #             'Error! you are not allowed to change the status into rejected ! Director only.')
    #
    # def make_prepare(self):
    #     self.change_state('-1')

    def write(self, vals):
        res = super(cms2_program, self).write(vals)
        if vals.get('stage_id') == 3 or vals.get('stage_id') == 4:
            if not self.user_has_groups('cms2.group_director'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the status into rejected or accepted ! Director only.')
        if vals.get('stage_id') == 3 and self.user_has_groups('cms2.group_director'):
            daftar_program = self.search([('id', '=', self.id)])

            self.create_absent_score(daftar_program)
            # for program in daftar_program:
            #     session_program = program.session_id
            #     partner_program = program.partner_id
            #     material_program = program.material_id
            #     for partner in partner_program:
            #         for session in session_program:
            #             self.env['cms2.session.partner'].sudo().create({
            #                 'session_id': session.id,
            #                 'partner_id': partner.id,
            #                 'program_id': program.id
            #             })
            #         for material in material_program:
            #             self.env['cms2.material.partner'].sudo().create({
            #                 'material_id': material.id,
            #                 'partner_id': partner.id,
            #             })
            # sudo karena yang mampu create di model tadi hanya user group teacher :))
        return res

    def _cron_absent_score(self):
        daftar_program = self.search([('start_date', '=', fields.Date.today() + timedelta(days=1)),('stage_id','=',1)])
        #daftar_program = self.search([])
        self.create_absent_score(daftar_program)

    def create_absent_score(self, daftar_program):
        test=[]
        test2=[]
        for program in daftar_program:
            session_program = program.session_id
            partner_program = program.partner_id
            material_program = program.material_id
            for partner in partner_program:
                for session in session_program:
                    # self.env['cms2.session.partner'].sudo().create({
                    #     'session_id': session.id,
                    #     'partner_id': partner.id,
                    #     'program_id': program.id
                    # })
                    test.append({'session_id':session.id,'partner_id':partner.id,'program_id':program.id})
                    # test['session_id'] = session.id
                    # test['partner_id'] = partner.id

                for material in material_program:
                    # self.env['cms2.material.partner'].sudo().create({
                    #     'material_id': material.id,
                    #     'partner_id': partner.id,
                    # })
                    test2.append({'material_id': material.id,'partner_id': partner.id,})



        print('test')

        self.env['cms2.session.partner'].sudo().create(test)
        self.env['cms2.material.partner'].sudo().create(test2)

    @api.model
    def get_partner_from_group(self, group_id):
        users_ids = []
        partners_ids = []
        sql_query = """select uid from res_groups_users_rel where gid = %s"""
        params = (group_id,)
        self.env.cr.execute(sql_query, params)
        results = self.env.cr.fetchall()
        for users_id in results:
            partners_ids.append(self.env['res.users'].browse(users_id[0]).partner_id.id)

            # users_ids.append(users_id[0])
        # return users_ids
        return partners_ids

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
        res = super(cms2_program, self).create(vals)
        # if vals['stage_id'] == 3 or vals['stage_id'] == 4:
        #     if not self.user_has_groups('cms2.group_director'):
        #         raise models.ValidationError(
        #             'Error! you are not allowed to change the status into rejected or accepted ! Director only.')

        if vals.get('stage_id') == 3 or vals.get('stage_id') == 4:
            if not self.user_has_groups('cms2.group_director'):
                raise models.ValidationError(
                    'Error! you are not allowed to change the status into rejected or accepted ! Director only.')

        domain = [('model', '=', 'res.groups'), ('name', '=', 'group_director')]
        model_data = self.env['ir.model.data'].search(domain, limit=1)
        staff = self.get_partner_from_group(model_data.res_id)
        staff_userid = self.get_user_from_group(model_data.res_id)
        res.message_subscribe(partner_ids=staff)
        if res.start_date:
            for user_id in staff_userid:
                res.activity_schedule('mail.mail_activity_data_meeting', user_id=user_id, date_deadline=res.start_date,
                                      summary='this program is starting')

        res.message_post_with_view('cms2.director_program_notif_qweb')
        return res


class cms2_program_rating(models.Model):
    _name = 'cms2.program.rating'
    program_id = fields.Many2one('cms2.program', string="Program Name")
    rate = fields.Integer('Rate')
    description = fields.Text('Description')
    name = fields.Char('Name')
    address = fields.Text('Address')


class cms2_program_stage(models.Model):
    _name = 'cms2.program.stage'
    _order = 'sequence,name'

    name = fields.Char()
    sequence = fields.Integer()
    fold = fields.Boolean()
    status = fields.Selection(
        [('-1', 'Preparation'),
         ('0', 'Pending'),
         ('1', 'Accepted'), ('-2', 'Rejected')],
        'State', default='-1')


class cms2_program_tag(models.Model):
    _name = 'cms2.program.tag'
    name = fields.Char()
    color = fields.Integer()
