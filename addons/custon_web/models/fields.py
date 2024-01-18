from odoo import models, fields, api

class FieldsMove(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    # def compute_field(self):
    #     self.field_float = 2 + 2  # Prueba 1

    #     # self.field_float = self.id + 10 # Prueba 2

    # field_float = fields.Float('Campo Float', compute=compute_field)
        
    field_float = fields.Float('Campo Float', default=2)    


    # @api.depends('value')
    # def _value_pc(self):
    #     self.field_float = 2 + 2  # Prueba 1
    # field_float = fields.Float('Campo Float', compute=_value_pc)