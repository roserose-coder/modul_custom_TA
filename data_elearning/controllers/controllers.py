# -*- coding: utf-8 -*-
# from odoo import http


# class DataElearning(http.Controller):
#     @http.route('/data_elearning/data_elearning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/data_elearning/data_elearning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('data_elearning.listing', {
#             'root': '/data_elearning/data_elearning',
#             'objects': http.request.env['data_elearning.data_elearning'].search([]),
#         })

#     @http.route('/data_elearning/data_elearning/objects/<model("data_elearning.data_elearning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('data_elearning.object', {
#             'object': obj
#         })
