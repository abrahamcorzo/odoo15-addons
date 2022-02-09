# -*- coding: utf-8 -*-

from odoo import models, fields


class Author(models.Model):
      _name = 'library.author'

      name = fields.Char()
      #book_id = fields.One2many("library.book", string="Book")