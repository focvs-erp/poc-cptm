# -*- coding: utf-8 -*-
{
    'name': "AX4B Accounting",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_asset', 'account_auto_transfer', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patrimonio_view.xml',
        'views/grupo_patrimonio_view.xml',
        'views/seguro_patrimonio_view.xml',
        'views/plano_conta_secundaria_view.xml',
        'views/plano_referencial_view.xml',
        'views/plano_conta_view.xml',
        'views/transferencia_automatica_view.xml',
        'views/fornecedor_view.xml',
        'views/templates.xml',
        'views/ecd_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
