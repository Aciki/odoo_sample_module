from odoo import  models , fields, api

class InsertGrades(models.TransientModel):
    _name = "insert.grades"
    _description = "grades"







    student = fields.Many2one("courses.student")
    course_id = fields.Many2one("courses.course",default=lambda self: self.env.uid,domain = [('state', '=', 'Open')])



    # student = fields.Many2one("courses.student",)
    grades = fields.Selection(
        [('5', '5'),
         ('6', '6'),
         ('7', '7'),
         ('8', '8'),
         ('9', '9'),
         ('10', '10'),],
        string='State', default="Draft")



#

