# -*- coding: utf-8 -*-
# from odoo import http


# class Mimodulo1(http.Controller):
#     @http.route('/mimodulo1/mimodulo1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mimodulo1/mimodulo1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mimodulo1.listing', {
#             'root': '/mimodulo1/mimodulo1',
#             'objects': http.request.env['mimodulo1.mimodulo1'].search([]),
#         })

#     @http.route('/mimodulo1/mimodulo1/objects/<model("mimodulo1.mimodulo1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mimodulo1.object', {
#             'object': obj
#         })
