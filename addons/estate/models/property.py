# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "CRM Estate Property"
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id = fields.Many2one('estate.property.type', string="Property Type")

    name = fields.Char(required=True, string="Name")
    state = fields.Selection(
        string="Status",
        selection=[
             ('new', 'New'), 
             ('received', 'Offer Received'), 
             ('accepted', 'Offer Accepted'), 
             ('sold', 'Sold'), 
             ('cancel', 'cancelled')], 
        default='new')

    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(required=True)
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Garden Orientation", default='north',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East')
                   , ('west', 'West')],
        help="Garden Orientation is used to describe cardinal points")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")

    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', True)]) 
    phone = fields.Char(string="Phone", related='buyer_id.phone')

    buyer_id = fields.Many2one('res.partner', string="Buyer") 


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    total_area = fields.Integer(string="Total Area", compute='_compute_total_area')
    # Usando onchange --> Funciona sólo dentro de la vista
    # @api.onchange('living_area', 'garden_area')
    # def _onchange_total_area(self):
    #     self.total_area = self.living_area + self.garden_area

    # total_area = fields.Integer(string="Total Area")
    # Fin Usando onchange -----

    def action_sold(self):
        self.state = 'sold'

    def action_cancel(self):
            self.state = 'cancel'

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    offer_count = fields.Integer(string='Offer Count', compute=_compute_offer_count)

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(required=True, string="Name")

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"
    
    name = fields.Char(required=True, string="Name")