# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedido(models.Model):

    _name = 'upopizza.pedido'
    _description = 'Upopizza Pedido'

    name = fields.Char(string="Idpedido", size=10, required=True)
    observaciones = fields.Char(
        string="Observaciones Pedido", required=True, help="Observaciones del Pedido")
    cliente_id = fields.Many2one('upopizza.cliente', string="Cliente",required=True)
    reparto_id = fields.Many2one('upopizza.reparto', string="Reparto",required=True)
    pago_id = fields.Many2one('upopizza.pago', string="Pago",required=True)
    albaran_id = fields.Many2one('upopizza.albaran', string="Albaran",required=True)
    linea_id = fields.Many2one('upopizza.lineapedido', string="Linea",required=True)
    cocinero_id = fields.Many2one('upopizza.cocinero', string="Cocinero",required=True)
    diaPedido = fields.Datetime('DiadelPedido', required=True, autodate=True)
    entregaAproximada = fields.Datetime(
        'EntregaAprox', required=True, autodate=True)
    _sql_constraints = [('pedidos_name_unique','UNIQUE (name)','El identificador del pedido debe ser único')]
