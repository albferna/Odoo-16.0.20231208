# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):

    _inherit = 'sale.order'
    
    to_check = fields.Boolean(string="To Check", copy=False)






#     _name = 'website_sale_ext.website_sale_ext'
#     _description = 'website_sale_ext.website_sale_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
