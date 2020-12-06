# -*- coding: utf-8 -*-

from odoo import models, fields, api


class albaran(models.Model):
    _name = 'upopizza.albaran'
    _description = 'Upopizza Albaran'

    name = fields.Char(string="IDalbaran", size=60, required=True)
    observaciones = fields.Char(
        string="Observaciones", required=True, help="Observaciones del albarán")
    pedido_id = fields.One2many('upopizza.pedido', 'albaran_id', 'Pedidos')
 