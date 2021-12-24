# -*- coding: utf-8 -*-
# from odoo import http


# class Roomster(http.Controller):
#     @http.route('/roomster/roomster/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/roomster/roomster/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('roomster.listing', {
#             'root': '/roomster/roomster',
#             'objects': http.request.env['roomster.roomster'].search([]),
#         })

#     @http.route('/roomster/roomster/objects/<model("roomster.roomster"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('roomster.object', {
#             'object': obj
#         })
