# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = 'manage1.task'
    _description = 'manage1.task'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el Nombre") #Name
    description = fields.Text()
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one("manage1.sprint", ondelete="set null", help="Sprint Relacionado")
    technologies = fields.Many2many(comodel_name="manage1.technology",
                                    relation_name="technologies_tasks",
                                    column1="task_id",
                                    column2="technology_id")


class sprint(models.Model):
    _name = 'manage1.sprint'
    _description = "manage1.sprint"

    name = fields.Char() #Name
    description = fields.Text()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    tasks = fields.One2many(string="Tareas",comodel_name="manage1.task", inverse_name='sprint')

class technology(models.Model):
    _name = 'manage1.technology'
    _description = "manage1.technology"

    name = fields.Char() #Name
    description = fields.Text()

    photo = fields.Image(max_width=200, max_height=200)
    tasks = fields.Many2many(comodel_name="manage1.task",
                             relation_name="technologies_tasks",
                             column1="technology_id",
                             column2="task_id")


#     value = fields.Integer()  
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
