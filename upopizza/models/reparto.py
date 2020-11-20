# -*- coding: utf-8 -*-

from odoo import models, fields, api


   class Reparto(models.Model):
   _name = 'upopizza.reparto'
    _description = 'Upopizza Reparto'

    tiempoentrega= fields.Integer('Tiempo')
    repartidor_id = fields.Many2one('upopizza.repartidor', 'Repartidor') 
    pedido_id= fields.One2many(upopizza.pedido', 'pedido_id', 'Pedidos')
