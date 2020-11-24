# -*- coding: utf-8 -*-
{
    'name': "upopizza",

    'summary': """
        Módulo de Gestión de UPOPIZZA
        """,

    'description': """
        Módulo Gestión de Pizzería
    """,

    'author': "Miguel Esteban Barba, Daniel Costel Chivu , Ignacio Gallego Ruiz , María Cabrera Ripoll",
    'website': "http://www.github.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'upopizza',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cliente_view.xml',
        'views/cocinero_view.xml',
        'views/metododepago_view.xml',
        'views/pizza_view.xml',
        'views/repartidor_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
