# -*- coding: utf-8 -*-

from odoo import models, fields, api


class reparto(models.Model):
    _name = 'upopizza.reparto'
    _description = 'Upopizza Reparto'

    name = fields.Char(string="IDreparto", size=10, required=True)
    tiempoentrega = fields.Integer("Tiempo(min)",required=True)
    repartidor_id = fields.Many2one('upopizza.repartidor', 'Repartidor',required=True)
    pedido_id = fields.One2many('upopizza.pedido', 'reparto_id', 'Pedidos')
    _sql_constraints = [('repartos_name_unique','UNIQUE (name)','El identificador del reparto debe ser único')]


    @api.constrains('tiempoentrega')
    def check_cantidad(self):
        if self.tiempoentrega > 1000:
            raise models.ValidationError(
                'El tiempo de entrega es superior al máximo permitido.')
        if self.tiempoentrega < 0 or self.tiempoentrega == 0:
            raise models.ValidationError(
                'El tiempo de entrega no puede ser inferior a ó igual 0.')
 