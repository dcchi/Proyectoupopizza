# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cocinero(models.Model):
    _name = 'upopizza.cocinero'
    _description = ' Upopizza Cocinero'

    name = fields.Char(string="DNI", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True,
                         help="Nombre del cocinero")
    apellidos = fields.Char(
        string="Apellidos", required=True, help="Apellidos del cocinero")
    direccion = fields.Char(
        string="Direccion", required=False, help="Direccion del cocinero")
    email = fields.Char(string="Email", required=True,
                        help="Email del Cocinero")
    telefono = fields.Integer("Telefono")
    #pedido_id = fields.One2many('upopizza2.pedido', 'cocinero_id', 'Pedidos')
