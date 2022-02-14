# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Book(models.Model):
    _inherit = 'book_catalog.book'


    @api.depends('stock')
    def _get_status(self):
        if self.stock <= 0: 
            self.status = 'not available'
        else: 
            self.status = 'available'
    
    @api.onchange('collection')
    def _erase_collection_name(self):
        if self.collection == 'no':
            self.collection_name = None
    