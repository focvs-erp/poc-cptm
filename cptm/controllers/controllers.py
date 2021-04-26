# -*- coding: utf-8 -*-
# from odoo import http


# class Cptm(http.Controller):
#     @http.route('/cptm/cptm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cptm/cptm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cptm.listing', {
#             'root': '/cptm/cptm',
#             'objects': http.request.env['cptm.cptm'].search([]),
#         })

#     @http.route('/cptm/cptm/objects/<model("cptm.cptm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cptm.object', {
#             'object': obj
#         })
