# -*- coding: utf-8 -*-
{
    'name': "LAR",

    'summary': """
        Limiting account receivable(AR) and providing its report""",

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
    'category': 'lar',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','digest','account','board','flyder','cms2','roomster'],

    # always loaded
    'data': [
         'security/security_rules.xml',
          'security/ir.model.access.csv',
         'views/limit.xml',
        'views/dasboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'application': True,
}