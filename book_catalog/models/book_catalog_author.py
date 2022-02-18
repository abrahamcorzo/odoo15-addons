# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Author(models.Model):
      _name = 'book_catalog.author'

      name = fields.Char()
      book_id = fields.One2many("book_catalog.book", "author_id", string="Book")


      def wiz_open(self):
            
            return {'type': 'ir.actions.act_window',
            'res_model': 'book_catalog.author_wizard',
            'view_mode': 'form',
            'target': 'new'}
