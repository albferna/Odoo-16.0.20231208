# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_module(models.Model):
    _name = 'my_module.my_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    # Modificación 1
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    # Modificación 2 (error)
    # start_datetime = fields.Datetime('Start time', default=fields.Datetime.now, required=False, readonly=False, select=True)       
    # Modificación 3 
        # start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now(), required=False, readonly=False, select=True)
        # _defaults = {
        # 'date_action': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        # }
    # start_datetime = "Jan 27, 2020 4:36:02 PM GMT+0000"

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100