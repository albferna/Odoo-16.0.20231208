# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    stock_name = fields.Char('Nombre de Stock')
    lista_stock = fields.Many2one('stock.lot', string='Lsta de Stock', index=True)



# class custon_web(models.Model):
#     _name = 'custon_web.custon_web'
#     _description = 'custon_web.custon_web'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
