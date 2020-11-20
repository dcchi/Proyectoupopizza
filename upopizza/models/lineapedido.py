# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LineaPedido(models.Model):
    _name = 'upopizza.lineapedido'
    _description = 'Upopizza Linea'
    
    cantidad= fields.Integer('Cantidad')
    pedido_id= fields.One2many('upopizza.pedido', 'pedido_id', 'Pedidos')
    pizza_id = fields.Many2one('upopizza.lineapedido','pizza_id' ,'Lineas') 