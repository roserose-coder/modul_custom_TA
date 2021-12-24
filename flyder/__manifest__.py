# -*- coding: utf-8 -*-
{
    'name': "flyder",

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
    'category': 'Flyer',
    'version': '0.1',
    'sequence': -999,

    # any module necessary for this one to work correctly
    'depends': ['base','data_perusahaan','digest','mail','account'],

    # always loaded
    'data': [
'security/groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/flyder_stage.xml',
        'data/cron.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
