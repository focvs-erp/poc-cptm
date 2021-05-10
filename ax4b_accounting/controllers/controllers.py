# -*- coding: utf-8 -*-
# from odoo import http


# class Ax4bPatrimonio(http.Controller):
#     @http.route('/ax4b_patrimonio/ax4b_patrimonio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ax4b_patrimonio/ax4b_patrimonio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ax4b_patrimonio.listing', {
#             'root': '/ax4b_patrimonio/ax4b_patrimonio',
#             'objects': http.request.env['ax4b_patrimonio.ax4b_patrimonio'].search([]),
#         })

#     @http.route('/ax4b_patrimonio/ax4b_patrimonio/objects/<model("ax4b_patrimonio.ax4b_patrimonio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ax4b_patrimonio.object', {
#             'object': obj
#         })
