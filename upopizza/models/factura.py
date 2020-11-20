# -*- coding: utf-8 -*-

from odoo import models, fields, api


class factura(models.Model):
    _name = 'upopizza.factura'
    _description = 'Upopizza Factura'

    name = fields.Char('ID', size=10, required=True)
    descripcion = fields.Char(string="Descripcion",
                              required=True, help="Descripción de Factura")
    cantidadsinIVA = fields.Integer('sinIVA')
    cantidadconIVA = fields.Integer('conIVA')
    pedido_id = fields.One2many('upopizza.pedido', 'pedido_id', 'Pedidos')
    pago_id = fields.Many2one('upopizza.pago', string="Pago")
    _sql_constraints = [('upopizza_factura_name_unique',
                         'UNIQUE (ID)', 'El ID debe ser único')]
