# -*- coding: utf-8 -*-
# from odoo import http


# class CptmModels(http.Controller):
#     @http.route('/cptm_models/cptm_models/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cptm_models/cptm_models/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cptm_models.listing', {
#             'root': '/cptm_models/cptm_models',
#             'objects': http.request.env['cptm_models.cptm_models'].search([]),
#         })

#     @http.route('/cptm_models/cptm_models/objects/<model("cptm_models.cptm_models"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cptm_models.object', {
#             'object': obj
#         })
