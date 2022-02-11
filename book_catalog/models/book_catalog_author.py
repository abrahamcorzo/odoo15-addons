# -*- coding: utf-8 -*-

from odoo import models, fields


class Author(models.Model):
      _name = 'book_catalog.author'

      name = fields.Char()
      book_id = fields.One2many("book_catalog.book", "author_id", string="Book")