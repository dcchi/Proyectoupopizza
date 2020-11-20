# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetododePago(models.Model):
    _name = 'upopizza.métododepago'
    _description = 'Upopizza Método Pago'

    name = fields.Char(string="Nombre pago", size=20, required=True, help="Nombre del método pago")
    descripcion = fields.Char(string="Descripcion Pago", required=True, help="Descripción del Método")