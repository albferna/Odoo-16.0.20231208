# -*- coding: utf-8 -*-
# from odoo import http


# class Manage1(http.Controller):
#     @http.route('/manage1/manage1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manage1/manage1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manage1.listing', {
#             'root': '/manage1/manage1',
#             'objects': http.request.env['manage1.manage1'].search([]),
#         })

#     @http.route('/manage1/manage1/objects/<model("manage1.manage1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manage1.object', {
#             'object': obj
#         })
