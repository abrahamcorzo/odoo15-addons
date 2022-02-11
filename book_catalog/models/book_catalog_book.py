# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
      _name = 'book_catalog.book'

      title = fields.Char()
      publication_date = fields.Date()
      stock = fields.Integer()
      status = fields.Selection(
            selection=[
                  ('available', "Available"),
                  ('not available', "Not available")
            ], 
            store = True,
            compute = '_get_status'
      )
      collection = fields.Selection(
            selection=[
                  ('yes', 'Yes'),
                  ('no', 'No')
            ]
      )
      collection_name = fields.Char(
            store = True,
            compute = '_set_collection_name'
      )
      author_id = fields.Many2one("book_catalog.author", string="Author")

