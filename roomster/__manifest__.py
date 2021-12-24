# -*- coding: utf-8 -*-
{
    'name': "roomster",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'version': '0.1',
    'sequence': -1000,
    'category': 'Roomster',

    # any module necessary for this one to work correctly
    'depends': ['base','data_perusahaan','mail','digest','account'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'wizard/room_booked_wizard.xml',
        'views/main.xml',
        'views/room.xml',
        'views/room_booked.xml',
        'views/res_config_settings_views.xml',
        'views/digest.xml',
        'views/room_renting_statistik.xml',
        'views/room_form.xml',
        'report/booked_report.xml',
        'report/booked_report_template.xml',
        'data/room.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'currency': 'IDR',
    'application': True,
}
