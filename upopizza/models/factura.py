# -*- coding: utf-8 -*-

from odoo import models, fields, api


class factura(models.Model):
    _name = 'upopizza2.factura'
    _description = 'Upopizza Factura'

    name = fields.Char(string="ID", size=10, required=True)
    descripcion = fields.Char(string="Descripcion",
                              required=True, help="Descripción de Factura")
    cantidadsinIVA = fields.Integer('sinIVA')
    cantidadconIVA = fields.Integer('conIVA')
    pago_id = fields.Many2one('upopizza.pago', string="Pago")