# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repartidor(models.Model):
    _name = 'upopizza.repartidor'
    _description = 'upopizza Repartidor'

    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos del cliente")
    DNI = fields.Char(string="DNI", required=True, help="DNI del cliente")
    direccion = fields.Char(string="Direccion", required=False, help="Direccion del cliente")
    telefono = fields.Integer("Telefono")
    email = fields.Char(string="Email", required=True, help="Email del cliente")
    idRepartidor = fields.Integer("ID")
    _sql_constraints = [('upopizza_repartidor_name_unique', 'UNIQUE (name)', 'El DNI debe ser único')]
