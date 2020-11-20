# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repartidor(models.Model):
    _name = 'upopizza.repartidor'
    _description = 'Upopizza Albaran'

    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True,
                         help="Nombre del repartidor")
    apellidos = fields.Char(
        string="Apellidos", required=True, help="Apellidos  del repartidor")
    direccion = fields.Char(
        string="Direccion", required=False, help="Direccion  del repartidor")
    telefono = fields.Integer("Telefono")
    reparto_id = fields.One2many(
        'upopizza.reparto', 'repartidor_id', 'Repartos')
    photo = fields.Binary('Photo')
    email = fields.Char(string="Email", required=True,
                        help="Email del repartidor")
    _sql_constraints = [('upopizza_repartidor_name_unique',
                         'UNIQUE (name)', 'El DNI debe ser único')]
