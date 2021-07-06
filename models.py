from odoo import models, fields


class Teachers(models.Model):
    _name = 'academy.teachers'
    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many(
        'product.template', 'teacher_id', string="Courses")


class Courses(models.Model):
    _inherit = ['product.template']
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
