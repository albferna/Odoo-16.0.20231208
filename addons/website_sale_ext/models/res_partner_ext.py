# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Partner(models.Model):

    _inherit = "res.partner"
    
    passport = fields.Char(string="Passport", copy=False)






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
