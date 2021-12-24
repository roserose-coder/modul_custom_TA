# -*- coding: utf-8 -*-
# from odoo import http


# class EMulticompany(http.Controller):
#     @http.route('/e_multicompany/e_multicompany/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/e_multicompany/e_multicompany/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('e_multicompany.listing', {
#             'root': '/e_multicompany/e_multicompany',
#             'objects': http.request.env['e_multicompany.e_multicompany'].search([]),
#         })

#     @http.route('/e_multicompany/e_multicompany/objects/<model("e_multicompany.e_multicompany"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('e_multicompany.object', {
#             'object': obj
#         })
