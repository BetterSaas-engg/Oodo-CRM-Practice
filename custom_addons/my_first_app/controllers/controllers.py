# -*- coding: utf-8 -*-
# from odoo import http


# class MyFirstApp(http.Controller):
#     @http.route('/my_first_app/my_first_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_first_app/my_first_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_first_app.listing', {
#             'root': '/my_first_app/my_first_app',
#             'objects': http.request.env['my_first_app.my_first_app'].search([]),
#         })

#     @http.route('/my_first_app/my_first_app/objects/<model("my_first_app.my_first_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_first_app.object', {
#             'object': obj
#         })

