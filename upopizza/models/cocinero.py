# -*- coding: utf-8 -*-
import re
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
    photo = fields.Binary('Fotografía')
    email = fields.Char(string="Email", required=True,
                        help="Email del Cocinero")
    telefono = fields.Integer("Telefono")
    pedido_id = fields.One2many('upopizza.pedido', 'cocinero_id', 'Pedidos')
    _sql_constraints = [
        ('cocineros_name_unique', 'UNIQUE (name)', 'El DNI debe ser único')]

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
