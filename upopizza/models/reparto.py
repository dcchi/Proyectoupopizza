# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reparto(models.Model):
    _name = 'upopizza.reparto'
    _description = 'Upopizza Reparto'

    name = fields.Char('IDreparto', size=60, required=True)
    tiempoentrega = fields.Integer('Tiempo')
    repartidor_id = fields.Many2one('upopizza.repartidor', 'Repartidor')
    pedido_id = fields.One2many('upopizza.pedido', 'reparto_id', 'Pedidos')
    _sql_constraints = [('upopizza_reparto_name_unique',
                         'UNIQUE (name)', 'El ID  reparto debe ser único')]
