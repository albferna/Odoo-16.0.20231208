from odoo import models, fields, api, _

class CustomizeResPartner(models.Model):
    _name = 'report.invoice.document.ext' 
    _description = 'ReportInvoiceDocumentExt'

class ReportInvoiceInherit(models.Model):
    _inherit = 'account.move'