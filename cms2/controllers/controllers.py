# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request
import werkzeug

# class Cms2(http.Controller):
#     @http.route('/cms2/cms2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cms2/cms2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cms2.listing', {
#             'root': '/cms2/cms2',
#             'objects': http.request.env['cms2.cms2'].search([]),
#         })

#     @http.route('/cms2/cms2/objects/<model("cms2.cms2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cms2.object', {
#             'object': obj
#         })

class Main(http.Controller):
    @http.route('/program_survey', type='http', auth="public", website=True)
    def books_issues(self, **post):
        if post.get('program_id'):
            program_id = int(post.get('program_id'))
            rate = int(post.get('star'))
            name = post.get('name')
            address= post.get('address')
            desc = post.get('description')
            request.env['cms2.program.rating'].sudo().create({
                'program_id': program_id,
                'rate': rate,
                'name':name,
                'address':address,
                'description': desc,

            })

            test ='/program_survey?submitted='+str(post.get('star'))
            # print('---------------it is a star ---------------',post.get('star'))
            return request.redirect(test)
            #return request.redirect('/program_survey?submitted=1')

        return request.render('cms2.program_form', {
            'programs': request.env['cms2.program'].search([]),
            'submitted': post.get('submitted', False)
        })
        # return request.render('cms2.program_form')

    @http.route('/program', type='http', auth="public", website=True)
    def books_issuess(self, **post):

        return request.render('cms2.program_list', {
            'programs': request.env['cms2.program'].search(request.website.website_domain()),
        })
        # return request.render('cms2.program_form')

    @http.route('/program/<model("cms2.program"):program>', type='http', auth="public", website=True)
    def library_book_detail(self, program):
        if not program.can_access_from_current_website():
            raise werkzeug.exceptions.NotFound()
        return request.render(
            'cms2.program_detail', {
                'program': program,

            })
