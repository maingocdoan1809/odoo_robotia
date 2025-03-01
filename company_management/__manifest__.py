# -*- coding: utf-8 -*-
{
    'name': "Robito - Test",

    'summary': "This module is for Robito Odoo testing purpose.",

    'author': "Mai Ngoc Doan",
   
    'category': 'Uncategorized',

    'version': '0.1',
    
    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
          'company_management/static/src/*'
        ]
    }
}

