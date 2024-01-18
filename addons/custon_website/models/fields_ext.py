from odoo import models, fields, api, _

class FieLdsModelExt(models.Model):
    ## _name = 'sale.order.ext'
    _inherit = 'sale.order'

    many_to_one = fields.Many2one('product.template', 'Campo Many2one')
    one_to_many = fields.One2many('sale.order', 'many_to_one', 'Campo One2many')
    many_to_many = fields.Many2many('sale.order', 'sale_handle', 'order_id', 'order_handle_id', 'Campo Many2many')
    ## many_to_many = fields.Many2many('sale.order', 'sale_handle', 'order_id', 'order_line', 'Campo Many2many')
