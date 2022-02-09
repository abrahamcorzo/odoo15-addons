# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
      _name = 'library.book'

      title = fields.Char()
      publication_date = fields.Date()
      stock = fields.Integer()
      available = fields.Selection(
            selection=[
                  ('yes', "Yes"),
                  ('no', "No")
            ]
      )
      collection = fields.Selection(
            selection=[
                  ('yes', 'Yes')
            ]
      )
      collection_name = fields.Char()
      author_id = fields.Many2one("library.author", string="Author")

