# -*- coding: utf-8 -*-
# from odoo import http


# class CptmCustom(http.Controller):
#     @http.route('/cptm_custom/cptm_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cptm_custom/cptm_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cptm_custom.listing', {
#             'root': '/cptm_custom/cptm_custom',
#             'objects': http.request.env['cptm_custom.cptm_custom'].search([]),
#         })

#     @http.route('/cptm_custom/cptm_custom/objects/<model("cptm_custom.cptm_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cptm_custom.object', {
#             'object': obj
#         })
