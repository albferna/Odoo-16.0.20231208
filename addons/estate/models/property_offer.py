# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError

    # Example of absract model
# class TransientOffer(models.TransientModel):
#     _name = 'transient.model.offer'
#     _description = 'Transient Offers'
#     _transient_max_count = 0   # 0 significa infinito

#     @api.autovacuum
#     def _transient_vacuum(self):
#         return super()._transient_vacuum()


#     partner_email = fields.Char(string='Email')
#     partner_phone = fields.Char(string='Phone Number')
class PropertyOffer(models.Model):
    _name = ["estate.property.offer"]
    _description = "Property / Offers"

    @api.depends('property_id', 'partner_id')
    def _compute_name(self):
        for rec in self:
            if rec.property_id and rec.partner_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name}"
            else:
                rec.name = False

    name = fields.Char(string="Descripction", compute=_compute_name)
    price = fields.Float(string="Price", required=True)
    status = fields.Selection(
        string="Status",
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string='Validity', default=7)
    deadline = fields.Date(string="DeadLine", compute='_compute_deadline', inverse='_inverse_deadline')

    @api.model 
    def _set_create_date(self):
       return fields.Date.today()

    creation_date = fields.Date(string="Create Date", default=_set_create_date)

    # creation_date = fields.Date(string="Create Date")
     
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

    # @api.model_create_multi
    # def create(self, vals):
    #     for rec in vals:
    #         if not rec.get('creation_date'):
    #             rec['creation_date'] = fields.Date.today()
    #     return super(PropertyOffer, self).create(vals)

    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.creation_date:
                raise ValidationError("DeadLine cannot be before creation date") 
            
    def action_accept_offer(self):
        self._validate_accepted_offer()
        if self.property_id:
            self.property_id.write({
                'selling_price': self.price,
                'state': 'accepted'
            })
        self.status = 'accepted'

    def _validate_accepted_offer(self):
        offer_ids = self.env['estate.property.offer'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted'),
        ])
        if offer_ids:
            raise ValidationError("You have an accepted offer already")

    def action_decline_offer(self):
        self.status = 'refused'
        if all(self.property_id.offer_ids.mapped('status')):
            self.property_id.write({
                'selling_price': 0,
                'state': 'received'
            })


    # def write(self, vals):
    #     print(vals)
    #     return super(PropertyOffer, self).write(vals)

    # Este cron corre todos los días           
    # @api.autovacuum 
    # def _clean_offers(self):
    #     self.search([('status', '=', 'refused')]).unlink()