# -*- coding: utf-8 -*-
{
    'name': "invoice_cust_subtotal",

    'summary': """
       des fonctionnalié  a ajouter au module facturation""",

    'description': """
        Calculer total des commandes par client
        Calcules=r les moyennes des notes et sections
    """,

    'author': "ihsen ",
    'website': "ihsen@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
