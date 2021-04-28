# -*- coding: utf-8 -*-
# from odoo import http


# class CptmInventory(http.Controller):
#     @http.route('/cptm_inventory/cptm_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cptm_inventory/cptm_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cptm_inventory.listing', {
#             'root': '/cptm_inventory/cptm_inventory',
#             'objects': http.request.env['cptm_inventory.cptm_inventory'].search([]),
#         })

#     @http.route('/cptm_inventory/cptm_inventory/objects/<model("cptm_inventory.cptm_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cptm_inventory.object', {
#             'object': obj
#         })
