# -*- coding: utf-8 -*-
{
    'name': "AX4B Purchase",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "AX4B",
    'website': "http://www.yourcompany.com",

    #  Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cotacao_compra.xml',
        'views/fornecedores_cotacao.xml',
        'views/cadastro_comprador_views.xml',  
        'views/grupo_comprador_views.xml',  
    ],
   
}
