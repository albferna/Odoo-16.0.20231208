from odoo import models, fields, api, _

class CustomizeResPartner(models.Model):
    _name = 'customize.res.partner.ext'


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    dec_legal_iva = fields.Boolean()
    agen_reten_iva = fields.Boolean('Es Agente de Retención (IVA)?')
    tasa_reten_iva = fields.Float('Tasa de Retención de IVA')
    agen_reten_ing = fields.Boolean('Agente de Retención de Ingresos?')
    soc_person_fis = fields.Boolean('¿Es una Sociedad de Personas Físicas?')
    exen_reten_ing = fields.Boolean('¿Está Exento de Retención de Ingresos?')


