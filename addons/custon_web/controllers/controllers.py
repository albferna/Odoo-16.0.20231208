# -*- coding: utf-8 -*-
# from odoo import http


# class CustonWeb(http.Controller):
#     @http.route('/custon_web/custon_web', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custon_web/custon_web/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custon_web.listing', {
#             'root': '/custon_web/custon_web',
#             'objects': http.request.env['custon_web.custon_web'].search([]),
#         })

#     @http.route('/custon_web/custon_web/objects/<model("custon_web.custon_web"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custon_web.object', {
#             'object': obj
#         })
