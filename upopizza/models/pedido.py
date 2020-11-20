#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedido(models.Model):
    _name = 'upopizza.pedido'
   _description = 'Upopizza Pedido'

    name = fields.Char('Idpedido', size=9, required=True)
    observaciones = fields.Char(string="Observaciones Pedido", required=True, help="Observaciones del Pedido")
    cliente_id = fields.Many2one('upopizza.cliente', 'cliente_id', 'Clientes')
    reparto_id = fields.Many2one('upopizza.reparto', 'reparto_id', 'Repartos')
    pago_id = fields.Many2one('upopizza.pago', 'pago_id', 'Pagos')
    factura_id = fields.Many2one('upopizza.factura', 'factura_id', 'Facturas')

      _sql_constraints = [('upopizza_pedido_name_unique', 'UNIQUE (Idpedido)', 'El Idpedido debe ser único')]