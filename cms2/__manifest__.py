# -*- coding: utf-8 -*-
{
    'name': "cms2",

    'summary': """
        Course Management System """,

    'description': """
        Handle offline - based learning
    """,

    'author': "Roseline Alim Santoso",
    'website': "http://www.yourcompany.com",
    'images': [
        'static/description/no_pic.png',
    ],
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CMS',
    'version': '14.0',
    'sequence': -997,

    # any module necessary for this one to work correctly
    # 'depends': ['base','data_perusahaan','digest','website'],
    'depends': ['base','digest', 'website'],

    # always loaded
    'data': [
        #'data/res_partner.xml',



        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/main.xml',
        'views/program.xml',
        'views/session.xml',
        'views/session_partner.xml',
        'views/material.xml',
        'views/material_partner.xml',
        'views/res_partner.xml',
        'views/res_users.xml',

        'views/digest.xml',

        #'data/material.xml',
        #'data/session.xml',
        #'data/program.xml',
        #'data/session_partner.xml',


        'data/program_stage.xml',
        'data/mail_template.xml',

        'views/templates.xml',
        'views/form_templates.xml',
        'data/cron.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
