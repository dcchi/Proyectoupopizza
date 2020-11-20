#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Pizza(models.Model):
    _name = 'upopizza.pizza'
    _description = 'Upopizza Pizza'

    name = fields.Char(string="Nombre pizza", size=60, required=True, help="Nombre de la Pizza")
    precio = fields.Integer("Precio por Unidad")
    descripcion = fields.Char(string="Descripcion", required=True, help="Descripcion de la Pizza")
    ingredientes= fields.Char(string="Ingredientes", required=True, help="Ingredientes")
    