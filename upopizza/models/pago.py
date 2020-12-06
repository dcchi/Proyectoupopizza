# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pago(models.Model):
    _name = 'upopizza.pago'
    _description = 'Upopizza Pago'

    name = fields.Char(string="Idpago", size=10, required=True)
    cantidad = fields.Float('Cantidad')
    pedido_id = fields.One2many('upopizza.pedido', 'pago_id', 'Pedidos')
    factura_id = fields.One2many('upopizza.factura', 'pago_id', 'Facturas')
    metodopago_id = fields.Many2one('upopizza.metododepago', string="Metodos")
