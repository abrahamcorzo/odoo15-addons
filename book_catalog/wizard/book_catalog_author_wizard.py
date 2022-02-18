from odoo import models, fields, api

class AuthorWizard(models.TransientModel):
    _name = 'book_catalog.author_wizard'
    
    author_id = fields.Many2many("book_catalog.author", string="Author")

    def print_report(self):
        Author = self.env['book_catalog.author']


        data={
            'name': Author.name,
            'book_id': Author.book_id
        }

        return self.env.ref('book_catalog.report_author_external_layout').report_action(self, data=data)