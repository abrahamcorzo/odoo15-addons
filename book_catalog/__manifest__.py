# -*- coding: utf-8 -*-
{
    'name': "Book catalog",

    'summary': """
        Contiene información sobre un catálogo de libros con sus autores correspondientes.""",

    'description': """
        Este módulo permite la creación de libros y autores. Del mismo modo, muestra la correspondencia
        que hay entre cada uno de ellos. 
    """,

    'author': "Abraham Corzo Castillo",
    'website': "https://ve.linkedin.com/in/abrahamcorzo",

    'category': 'Uncategorized',
    'version': '0.1',

    # 'depends': ['base'],

    # always loaded
    'data': [
        'views\\book_catalog_author_view.xml',
        'views\\book_catalog_book_view.xml',
        'report\\book_catalog_author_report_view.xml',
        'report\\book_catalog_author_report.xml',
        'report\\book_catalog_author_external_layout.xml',
        'security\\ir.model.access.csv',
        'wizard\\book_catalog_author_wizard_view.xml'
    ]

}