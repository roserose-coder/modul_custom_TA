# -*- coding: utf-8 -*-
# from odoo import http


# class Cms2Roomster(http.Controller):
#     @http.route('/cms2_roomster/cms2_roomster/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cms2_roomster/cms2_roomster/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cms2_roomster.listing', {
#             'root': '/cms2_roomster/cms2_roomster',
#             'objects': http.request.env['cms2_roomster.cms2_roomster'].search([]),
#         })

#     @http.route('/cms2_roomster/cms2_roomster/objects/<model("cms2_roomster.cms2_roomster"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cms2_roomster.object', {
#             'object': obj
#         })
