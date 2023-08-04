# -*- coding: utf-8 -*-
{
    'name': "Restrict Create and Edit",

    'summary': "add Restriction to Create and Edit",

    'description': """
        add Restriction to Create and Edit
    """,

    'author': "Mohamed Awad",
    'website': "",

    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': [
        'sale',
        'base',
        'product',
        'mail',
    ],
    'application': True,

    # always loaded
    'data': [
        'security/product_template_security.xml',
    ],

}
