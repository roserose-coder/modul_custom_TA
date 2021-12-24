# -*- coding: utf-8 -*-
{
    'name': "d_cms",

    'summary': """
        Auto Loaded CMS Data""",

    'description': """
        Data CMS
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'version': '0.1',
    'sequence': -1000,
    'category': 'data_data',

    # any module necessary for this one to work correctly
    'depends': ['base','data_perusahaan','cms2'],

    # always loaded
    'data': [
        'security/groups.xml',
        'data/res_partner.xml',
        'data/material.xml',
        'data/session.xml',
        'data/program.xml',
        'data/session_partner.xml',

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'application': True,
}
