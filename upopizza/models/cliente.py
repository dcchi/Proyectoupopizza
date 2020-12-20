# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api


class cliente(models.Model):
    _name = 'upopizza.cliente'
    _description = 'Upopizza Cliente'

    name = fields.Char(string="DNI", size=9, required=True)
    nombre = fields.Char(string="Nombre", required=True,
                         help="Nombre del cliente")
    apellidos = fields.Char(string="Apellidos", required=True,
                            help="Apellidos del cliente")
    direccion = fields.Char(string="Direccion", required=False,
                            help="Direccion del cliente")
    photo = fields.Binary('Fotografía')
    telefono = fields.Char(string="Telefono", size=9, required=True)
    email = fields.Char(string="Email", required=True,
                        help="Email del cliente")
    pedido_id = fields.One2many('upopizza.pedido', 'cliente_id', 'Pedidos')
    _sql_constraints = [
        ('clientes_name_unique', 'UNIQUE (name)', 'El DNI debe ser único')]

    @api.onchange('email')
    def validar_email(self):
        if self.email:
            match = re.match(
                '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise models.ValidationError('No es un email válido.')

    @api.onchange('name')
    def validar_dni(self):
        if self.name:
            match = re.match('\d{8}[a-zA-Z]$', self.name)
            if match == None:
                raise models.ValidationError('No es un DNI válido.')

    @api.onchange('telefono')
    def validar_dni(self):
        if self.telefono:
            match = re.match('\d{9}', self.telefono)
            if match == None:
                raise models.ValidationError('No es un teléfono válido.')
