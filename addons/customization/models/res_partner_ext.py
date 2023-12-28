from odoo import models, fields, api, _

class CustomizeResPartner(models.Model):
    _name = 'customize.res.partner.ext'

    # mot_start_date = fields.Date(string='MOT Start Date')
    # mot_exp_date = fields.Date(string='MOT Expiry Date')
    dec_legal_iva = fields.Boolean(string="Declaración Legal de IVA")
    agen_reten_iva = fields.Boolean(string="Es Agente de Retención (IVA)?")
    tasa_reten_iva = fields.Float(string="Tasa de Retención de IVA")

    agen_reten_ing = fields.Boolean(string="Agente de Retención de Ingresos?")
    soc_person_fis = fields.Boolean(string="¿Es una Sociedad de Personas Físicas?")
    exen_reten_ing = fields.Boolean(string="¿Está Exento de Retención de Ingresos?")

#    mot_service_centre = fields.Many2one('res.partner', string='MOT Service Centre')
#    vehicle_id = fields.Many2one('fleet.vehicle')


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

#    vehicle_mot_ids = fields.One2many('customize.fleet.mot', 'vehicle_id')