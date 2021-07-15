from odoo import fields , models , api



class Course(models.Model):
    _name = "courses.course"
    _description = "course_list"
    _rec_name = "course"





    course = fields.Char(string ="Course name", required=True)
    field_of_study=fields.Char(string = "Field of study ", required = True)
    semester = fields.Selection(
        [('first', 'first'),
         ('second', 'second'),
         ('third', 'third'),
         ('fourth', 'fourth'),
         ('fifth', 'fifth'),
         ('sixth', 'sixth'),
         ('seventh ', 'seventh'),
         ('eight', 'eight')],
        'Semester')
    state = fields.Selection(
        [('Draft', 'Draft'),
         ('Open', 'Open'),
         ('Finished', 'Finished')],
        string='State', default="Draft")

    description = fields.Text(string = "Description ")
    beginning_date = fields.Date('Beginning date')
    end_date = fields.Date('End date')
    grades_id = fields.One2many("insert.grades", "grades", string="Grades")
    teacher = fields.One2many("courses.teacher","course",string = "Teacher")
    students = fields.One2many("courses.student","students_courses",string="Students")
    attachment_ids = fields.Many2many('ir.attachment', 'car_rent_checklist_ir_attachments_rel',
                                      'rental_id', 'attachment_id', string="Attachments",
                                      help="lectures,test etc.")

    def action_confirm(self):
        for rec in self:
            rec.state = "Finished"

    def action_confirm1(self):
        for rec in self:
            rec.state = "Open"


    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):

        default = dict(default or {})

        default.update({

            'students': None})

        return super(Course, self).copy(default)









