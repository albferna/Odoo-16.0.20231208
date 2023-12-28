from odoo import models, fields, api, _

class CustomizeResPartner(models.Model):
    _name = 'customize.res.partner.ext'

    # mot_start_date = fields.Date(string='MOT Start Date')
    # mot_exp_date = fields.Date(string='MOT Expiry Date')
    


#    mot_service_centre = fields.Many2one('res.partner', string='MOT Service Centre')
#    vehicle_id = fields.Many2one('fleet.vehicle')


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    # dec_legal_iva = fields.Boolean(string='Declaración Legal de IVA')
    dec_legal_iva = fields.Boolean('Declaración Legal de IVA')
    agen_reten_iva = fields.Boolean('Es Agente de Retención (IVA)?')
    tasa_reten_iva = fields.Float('Tasa de Retención de IVA')

    agen_reten_ing = fields.Boolean('Agente de Retención de Ingresos?')
    soc_person_fis = fields.Boolean('¿Es una Sociedad de Personas Físicas?')
    exen_reten_ing = fields.Boolean('¿Está Exento de Retención de Ingresos?')




#    vehicle_mot_ids = fields.One2many('customize.fleet.mot', 'vehicle_id')