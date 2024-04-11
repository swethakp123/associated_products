# -*- coding: utf-8 -*-
{
    'name': "Associated Products",
    'version': '17.0.1.0.0',
    'depends': ['base','contacts','product', 'stock', 'sale'],
    'category': '',
    'description': """
    summary of this app
    """,
    'data': ['security/ir.model.access.csv',
             'views/associated_products.xml',
             'views/customer_form_view.xml',
             'views/sale_order_view.xml',
             ],
    # 'demo': [],
    'application': 'True',
    'installable': True,
}