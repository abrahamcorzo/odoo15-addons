# -*- coding: utf-8 -*-
# from odoo import http


# class BookFeatures(http.Controller):
#     @http.route('/book_features/book_features', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book_features/book_features/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('book_features.listing', {
#             'root': '/book_features/book_features',
#             'objects': http.request.env['book_features.book_features'].search([]),
#         })

#     @http.route('/book_features/book_features/objects/<model("book_features.book_features"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book_features.object', {
#             'object': obj
#         })
