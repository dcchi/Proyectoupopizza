# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pizza(models.Model):
    _name = 'upopizza.pizza'
    _description = 'Upopizza Pizza'

    name = fields.Char(string="Nombre pizza", size=60,
                       required=True, help="Nombre de la Pizza")
    precio = fields.Float("PrecioporUnidad", required= True)
    descripcion = fields.Char(string="Descripcion",
                              required=True, help="Descripcion de la Pizza")
    imagen= fields.Binary("Foto de la pizza")
    ingredientes = fields.Char(
        string="Ingredientes", required=True, help="Ingredientes")
    linea_id = fields.One2many(
        'upopizza.lineapedido', 'pizza_id', 'Lineas')
    _sql_constraints = [('pizzas_name_unique', 'UNIQUE (name)',
                         'El nombre de la pizza debe ser único')]

    @api.constrains('precio')
    def check_precio(self):
        if self.precio > 100 or self.precio < 0:
            raise models.ValidationError(
                'El precio de la pizza no puede ser superior a 100 euros o inferior a 0.')
