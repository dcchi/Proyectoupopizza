# -*- coding: utf-8 -*-

from odoo import models, fields, api


class factura(models.Model):
    _name = 'upopizza.factura'
    _description = 'Upopizza Factura'

    name = fields.Char(string="IdFactura", size=10, required=True)
    descripcion = fields.Char(string="Descripcion",
                              required=True, help="Descripción de Factura")
    cantidadsinIVA = fields.Float('sinIVA')
    cantidadconIVA = fields.Float('conIVA')
    pago_id = fields.Many2one('upopizza.pago', string="Pago")
    comienzo = fields.Datetime('Comienzo', required=True, autodate=True)
    fin = fields.Datetime('Fin', required=True, autodate=True)
    _sql_constraints = [('facturas_name_unique','UNIQUE (name)','El identificador de la factura debe ser único')]