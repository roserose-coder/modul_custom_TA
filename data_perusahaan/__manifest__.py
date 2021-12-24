# -*- coding: utf-8 -*-
{
    'name': "dp",

    'summary': """
        Auto Loaded Company Data""",

    'description': """
        Data Perusahaan 
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
    'depends': ['base'],

    # always loaded
    'data': [
        'data/res_partner_real.xml',
        'data/res_worker_real.xml',
        'data/res_company_data_real.xml',
        'data/res_users_real.xml',
        'data/data_partner_group.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
