#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Pizza(models.Model):
    _name = 'upopizza.pizza'
<<<<<<< HEAD
    _description = 'Upopizza Pizza'

    name = fields.Char(string="Nombre pizza", size=60, required=True, help="Nombre de la Pizza")
    precio = fields.Integer("Precio por Unidad")
    descripcion = fields.Char(string="Descripcion", required=True, help="Descripcion de la Pizza")
    ingredientes= fields.Char(string="Ingredientes", required=True, help="Ingredientes")
=======
    _description = 'Pizzas'

    name = fields.Char(string="No", size=60, required=True, help="Nombre de la Pizza")
    precio = fields.Integer("Precio por Unidad")
    descripcion = fields.Char(string="Descripcion", required=True, help="Descripcion de la Pizza")
    #falta añadir ingredientes
>>>>>>> 284fc9b057b8e78abcf31d14c9ee607b9df4be46
    