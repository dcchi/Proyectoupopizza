#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Pago(models.Model):
    _name = 'upopizza.pago'
   _description = 'Upopizza Pago'

    name = fields.Char('Idpago', size=10, required=True)
    cantidad= fields.Integer('Cantidad')
    pedido_id= fields.One2many('upopizza.pedido', 'pedido_id', 'Pedidos')
    
    _sql_constraints = [('upopizza_pago_name_unique', 'UNIQUE (Idpago)', 'El ID debe ser único')]