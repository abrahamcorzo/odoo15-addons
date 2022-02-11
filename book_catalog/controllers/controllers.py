# -*- coding: utf-8 -*-
# from odoo import http


# class Bookshelf(http.Controller):
#     @http.route('/bookshelf/bookshelf', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookshelf/bookshelf/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookshelf.listing', {
#             'root': '/bookshelf/bookshelf',
#             'objects': http.request.env['bookshelf.bookshelf'].search([]),
#         })

#     @http.route('/bookshelf/bookshelf/objects/<model("bookshelf.bookshelf"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookshelf.object', {
#             'object': obj
#         })
