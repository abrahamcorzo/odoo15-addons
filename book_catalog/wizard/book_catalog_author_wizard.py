from odoo import models, fields, api

class AuthorWizard(models.TransientModel):
    _name = 'book_catalog.author_wizard'
    
    author_ids = fields.Many2many("book_catalog.author", string="Author")

    def print_report(self):
        return {
            'type': 'ir.actions.report',
            'report_name': 'book_catalog.report_authors',
            'report_type':"qweb-pdf"
        }

