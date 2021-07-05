# -*- encoding: utf-8 -*-
{
    'name': 'Academy',
    'version': '0.1',
    'summary': 'Build a website in Odoo',
    'category': 'Website/Website',
    'license': 'AGPL-3',
    'author': 'Ewetoye Ibrahim',
    'website': 'https://EwetoyeIbrahim.github.io',
    'description': '''
    This module is used to show how to build a website
    in Odoo ERP system
    ''',
    'depends': ['website', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        'views.xml'
    ],
    'demo': [
        'demo.xml',
    ],
    'installable': True,
}
