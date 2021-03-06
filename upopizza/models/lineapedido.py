# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lineapedido(models.Model):
    _name = 'upopizza.lineapedido'
    _description = 'Upopizza Linea'

    name = fields.Char('IdLinea',size=10 ,required=True)
    cantidad = fields.Integer("Cantidad",required=True)
    pizza_id = fields.Many2one('upopizza.pizza', string="Pizza",required=True)
    pedido_id = fields.One2many('upopizza.pedido', 'linea_id', 'Pedidos')
    _sql_constraints = [('lineasdepedidos_name_unique','UNIQUE (name)','El identificador de la línea debe ser único')]


    @api.constrains('cantidad')
    def check_cantidad(self):
        if self.cantidad > 1000:
            raise models.ValidationError(
                'La cantidad es superior a la máxima permitida.')
        if self.cantidad < 0 or self.cantidad == 0:
            raise models.ValidationError(
                'La cantidad no puede ser inferior o igual a 0.')
