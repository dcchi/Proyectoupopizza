# -*- coding: utf-8 -*-

from odoo import models, fields, api


class albaran(models.Model):
    _name = 'upopizza.albarán'
    _description = 'Upopizza Albaran'

    name = fields.Char('IDalbaran', size=60, required=True)
    observaciones = fields.Char(
        string="Observaciones", required=True, help="Observaciones del albarán")
    pedido_id = fields.One2many('upopizza.pedido', 'albaran_id', 'Pedidos')
    _sql_constraints = [('upopizza_albaran_name_unique',
                         'UNIQUE (name)', 'El ID albarán debe ser único')]
