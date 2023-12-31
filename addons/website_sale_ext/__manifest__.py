# -*- coding: utf-8 -*-
{
    'name': "Website Sale Ext - Demo Curso",

    'summary': """
        Módulo de Demostación
        para curso """,

    'description': """
        Módulo de Demostación para curso
    """,

    'author': "AAF Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/website_sale.xml',
        'views/res_partner_view.xml',
    ],
}
