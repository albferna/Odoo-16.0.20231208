# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate Ads',
    'version': '0.1',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': """
        Track leads and close opportunities --- For learning objetives.         
        The Real Estate Advertisement module. 
        Our new module will cover a business area which is very specific and therefore not included in the standard set of modules: real estate. It is worth noting that before developing a new module, it is good practice to verify that Odoo doesn’t already provide a way to answer the specific business case.
        """,
    'description': "AAF - This is a testing module",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'base',
        # 'sales_team',
        # 'mail',
        # 'calendar',
        # 'resource',
        # 'fetchmail',
        # 'utm',
        # 'web_tour',
        # 'contacts',
        # 'digest',
        # 'phone_validation',
    ],
    'data': [
        # 'security/crm_security.xml',
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/menu_items.xml',
        
        # data files
        # 'data/property_type.xml',
        'data/estate.property.type.csv',
    ],
     'demo': [
         'demo/property_tag.xml',
        # 'data/crm_team_demo.xml',
        # 'data/mail_activity_demo.xml',
        # 'data/crm_lead_demo.xml',
     ],
    # 'css': ['static/src/css/crm.css'],
    'installable': True,
    # ----------------------------
    # Para convertir en aplicación
    'application': True,      
    # ----------------------------
    'License': 'LGPL-3',    
    # 'auto_install': False
}