
# -*- coding: utf-8 -*-
{
    "name": "product_vendor",
    'summary': """
        Mostrar los proveedores de un producto en la vista product.supplierinfo """,
    "category": "Uncategorized",
    "version": "0.2",
    "author": "A. Fernandez",
    "website": "https://www.linkedin.com/in/alberto-a-fern%C3%A1ndez-82948b31/",
    # "depends": [' '],
    'depends': ['purchase'],
    'depends': ['product'],
    "data": [
    #   'security/ir.model.access.csv',
        'views/product_vendor_view.xml',
        
    ],
    'application': False,
    # 'assets': {
    #     'web.report_assets_common': [
    #         'nacd_core/static/scss/**/*',
    #     ],
    # }
}

