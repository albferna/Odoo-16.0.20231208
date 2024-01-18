## product_vendor.access_product_vendor_ext,access_product_vendor_ext,product_vendor.model_product_vendor_ext,base.group_user,1,1,1,1

from odoo import models, fields, api, _

class ProductVendorExt(models.Model):
    _name = 'product.vendor.ext'
    _inherit = 'product.supplierinfo'

    vendor_id = fields.Many2one('product.supplierinfo')
    # vendor_id = fields.Many2one('product.supplierinfo.partner_id')
    # vendor_id = fields.Many2one('purchase.order.partner_id')
    # vendor_id = fields.Many2one('product.supplierinfo')
    # vendor_id = fields.Many2one('product.template.company_id')
    ## vendor_id = fields.Many2one('res.partner.display_name')

class VendorInherit(models.Model):
    # _inherit = 'product.supplierinfo'
    # _inherit = 'purchase.order.line'
    _inherit = 'product.template'
    vendor_ids = fields.One2many('product.vendor.ext', inverse_name='vendor_id', string='Vendor Name')