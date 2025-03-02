# -*- coding: utf-8 -*-
{
    "name": "Robotia - Test",
    "summary": "This module is for Robotia Odoo testing purpose.",
    "author": "Mai Ngoc Doan",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base", "phone_validation"],
    "data": [
        "security/ir.model.access.csv",
        "views/templates.xml",
        "views/menu.xml",
        "views/robotia_company.xml",
        "data/mock_data.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "company_management/static/src/**/*.js",
            "company_management/static/src/**/*.xml",
            "company_management/static/src/**/*.scss"   
        ]
    },
}
