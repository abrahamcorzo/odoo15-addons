# -*- coding: utf-8 -*-

from odoo import models, fields, api


class webinar_todo(models.Model):
      _name = 'wb.todo'   #Con este atributo defino el modelo. 
      _description = 'Estos son metadatos.'

      name = fields.Char("Nombre")
      status = fields.Selection(selection=[
          ("borrador", "Borrador"),
          ("hecho", "Hecho")
           
      ])
