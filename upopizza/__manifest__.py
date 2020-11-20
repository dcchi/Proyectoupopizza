# -*- coding: utf-8 -*-
{
    'name': "upopizza",

    'summary': """
        Módulo de Gestión de UPOpizza
        """,

    'description': """
        Módulo Gestión de Pizzería
    """,

    'author': "Miguel Esteban Barba, Daniel Costel Chivu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
   
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
