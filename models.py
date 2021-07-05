from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()
    biography = fields.Html()

class Courses(models.Model):
    _name = 'academy.courses'
    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")