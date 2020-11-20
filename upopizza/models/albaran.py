# -*- coding: utf-8 -*-

from odoo import models, fields, api


   class Albaran(models.Model):
   _name = 'upopizza.albarán'
   _description = 'Upopizza Albaran'
    
    observaciones = fields.Char(string="Observaciones", required=True, help="Observaciones del albarán")
    pedido_id= fields.One2many(upopizza.pedido', 'pedido_id', 'Pedidos')
    
