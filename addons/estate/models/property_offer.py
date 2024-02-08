# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property / Offers"

    price = fields.Float(string="Price", required=True)
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Acceptted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string='Validity')
    deadline = fields.Date(string="DeadLine", compute='_compute_deadline', inverse='_inverse_deadline')

#     @api.model 
#     def _set_create_date(self):
# ````   return fields.Date.today()

    # creation_date = fields.Date(string="Create Date", default=_set_create_date)

    creation_date = fields.Date(string="Create Date")
    
    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False

    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
        return super(PropertyOffer, self).create(vals)

    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.creation_date:
                raise ValidationError("DeadLine cannot be before creation date") 

    # Este cron corre todos los días           
    # @api.autovacuum 
    # def _clean_offers(self):
    #     self.search([('status', '=', 'refused')]).unlink()       