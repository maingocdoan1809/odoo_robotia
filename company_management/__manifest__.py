# -*- coding: utf-8 -*-
{
    'name': "Robotia - Test",

    'summary': "This module is for Robotia Odoo testing purpose.",

    'author': "Mai Ngoc Doan",
   
    'category': 'Uncategorized',

    'version': '0.1',
    
    'depends': ['base', 'phone_validation'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/robotia_company.xml'
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

