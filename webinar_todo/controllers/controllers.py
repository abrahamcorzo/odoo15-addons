# -*- coding: utf-8 -*-
# from odoo import http


# class WebinarTodo(http.Controller):
#     @http.route('/webinar_todo/webinar_todo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/webinar_todo/webinar_todo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('webinar_todo.listing', {
#             'root': '/webinar_todo/webinar_todo',
#             'objects': http.request.env['webinar_todo.webinar_todo'].search([]),
#         })

#     @http.route('/webinar_todo/webinar_todo/objects/<model("webinar_todo.webinar_todo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('webinar_todo.object', {
#             'object': obj
#         })
