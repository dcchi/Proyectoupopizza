# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedido(models.Model):


    _name = 'upopizza.pedido'
    _description = 'Upopizza Pedido'

    name = fields.Char(string="Idpedido", size=9, required=True)
    observaciones = fields.Char(
    string="Observaciones Pedido", required=True, help="Observaciones del Pedido")
    cliente_id = fields.Many2one('upopizza.cliente',string="Cliente")
    reparto_id = fields.Many2one('upopizza.reparto', string="Reparto")
    pago_id = fields.Many2one('upopizza.pago', string="Pago")
    albaran_id = fields.Many2one('upopizza.albaran', string="Albaran")
    linea_id = fields.Many2one('upopizza.lineapedido', string="Linea")
    cocinero_id = fields.Many2one('upopizza.cocinero', string="Cocinero")
