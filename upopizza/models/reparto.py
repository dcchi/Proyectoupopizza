# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reparto(models.Model):
    _name = 'upopizza.reparto'
    _description = 'Upopizza Reparto'

    name = fields.Char(string="IDreparto", size=60, required=True)
    tiempoentrega = fields.Integer("Tiempo(min)")
    repartidor_id = fields.Many2one('upopizza.repartidor', 'Repartidor')
    pedido_id = fields.One2many('upopizza.pedido', 'reparto_id', 'Pedidos')
    _sql_constraints = [('repartos_name_unique','UNIQUE (name)','El identificador del reparto debe ser único')] 