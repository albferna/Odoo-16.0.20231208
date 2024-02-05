
# -*- coding: utf-8 -*-
{
    "name": "report_invoice_document_ext",
    'summary': """
        Cambiar nombre a Notas de Crédito """,
    "category": "Uncategorized",
    "version": "0.1",
    "author": "AAF",
    "website": "https://www.linkedin.com/in/alberto-a-fern%C3%A1ndez-82948b31/",
#    "depends": ['fleet'],
    'depends': ['base', 'account'],
    "data": [
     #   'security/ir.model.access.csv',
        'views/report_invoice_document_ext.xml',
        
    ],
    'application': False,
    # 'assets': {
    #     'web.report_assets_common': [
    #         'nacd_core/static/scss/**/*',
    #     ],
}

