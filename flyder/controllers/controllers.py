# -*- coding: utf-8 -*-
# from odoo import http


# class Flyder(http.Controller):
#     @http.route('/flyder/flyder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flyder/flyder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flyder.listing', {
#             'root': '/flyder/flyder',
#             'objects': http.request.env['flyder.flyder'].search([]),
#         })

#     @http.route('/flyder/flyder/objects/<model("flyder.flyder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flyder.object', {
#             'object': obj
#         })
