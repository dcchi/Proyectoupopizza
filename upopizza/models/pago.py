# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pago(models.Model):
    _name = 'upopizza.pago'
    _description = 'Upopizza Pago'

    name = fields.Char('Idpago', size=10, required=True)
    cantidad = fields.Integer('Cantidad')
    pedido_id = fields.One2many('upopizza.pedido', 'pago_id', 'Pedidos')
    factura_id = fields.One2many('upopizza.factura', 'pago_id', 'Facturas')
    metodopago_id = fields.Many2one('upopizza.metododepago', string="Métodos")
    _sql_constraints = [('upopizza_pago_name_unique',
                         'UNIQUE (Idpago)', 'El ID debe ser único')]
