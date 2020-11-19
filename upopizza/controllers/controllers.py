# -*- coding: utf-8 -*-
# from odoo import http


# class Upopizza(http.Controller):
#     @http.route('/upopizza/upopizza/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upopizza/upopizza/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upopizza.listing', {
#             'root': '/upopizza/upopizza',
#             'objects': http.request.env['upopizza.upopizza'].search([]),
#         })

#     @http.route('/upopizza/upopizza/objects/<model("upopizza.upopizza"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upopizza.object', {
#             'object': obj
#         })
