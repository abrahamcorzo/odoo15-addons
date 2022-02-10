# -*- coding: utf-8 -*-
{
    'name': "Library",

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
        'views\library_author_view.xml',
        'views\library_book_view.xml',
        'security.xml'
    ]

}