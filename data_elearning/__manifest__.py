# -*- coding: utf-8 -*-
{
    'name': "data_elearning",

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
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','website_slides','website_sale'],


    'depends': ['base','website_slides','website_sale_slides','website_slides_forum','website_slides_survey'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'data/slide_tag.xml',

        'data/product.xml',
        'data/slide_channel.xml',
        'data/slide_product.xml',
        'data/slide_slide.xml',
        'data/slide_qna.xml',
        'data/forum.xml',
        'data/survey.xml',
        'data/slide_certification.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
