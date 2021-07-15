from odoo import fields, models, api
from datetime import datetime
import random


class Student(models.Model):
    _name = "courses.student"
    _description = "student_table"





    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    email = fields.Char(string="Email")
    Field_of_study = fields.Char(string="Field od study")

    birth_date = fields.Date('Birth Date')
    current_year = fields.Integer(string="current_year", default=datetime.now().year)
    user_id = fields.Many2one('res.users',"Student_Id")


    @api.model
    def year_selection(self):
        enrolled_year = 2021  # replace 2000 with your a start year
        year_list = []
        while enrolled_year != 2030:  # replace 2030 with your end year
            year_list.append((str(enrolled_year), str(enrolled_year)))
            enrolled_year += 1
        return year_list

    enrolled_year = fields.Selection(
        year_selection,
        string="enrolled_year",
        default="2021",  # as a default value it would be 2021
    )
    index_number = fields.Char(string="Index number")



    # @api.model
    # def create(self):
    #     num = random.randrange(1, 10 ** 3)
    #
    #     num_with_zeros = str(num).zfill(3)
    #     year = datetime.date.today().year
    #     index_number = num_with_zeros + "/" + str(year)
    #     print(index_number)

        # return index_number
    students_courses = fields.Many2one("courses.course", "course")
    index_number = fields.Char(string="index_number", readonly=True, required=True, copy=False, default='New')
    grades = fields.One2many("insert.grades","grades",string = "Grades")
    @api.model
    def create(self, vals):
        if vals.get('index_number', 'New') == 'New':
            vals['index_number'] = self.env['ir.sequence'].next_by_code(
                'self.service') or 'New'
        result = super(Student, self).create(vals)
        return result


    @api.depends('surname', 'name','index_number')
    def name_get(self):
        result = []
        for account in self:
            name = account.surname + ' ' + account.name + ' ' + account.index_number
            result.append((account.id, name))
        return result




