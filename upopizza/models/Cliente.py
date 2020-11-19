# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'upopizza.cliente'
    _description = 'upopizza Cliente'

    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del cliente")
    direccion = fields.Char(string="Direccion", required=False, help="Direccion del cliente")
    telefono = fields.Integer("Telefono")
    email = fields.Char(string="Email", required=True, help="Email del cliente")
    _sql_constraints = [('upopizza_cliente_name_unique', 'UNIQUE (dni)', 'El DNI debe ser único')]