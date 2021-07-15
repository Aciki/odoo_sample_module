from odoo import fields , models , api




class Teachers(models.Model):
    _name = "courses.teacher"
    _description = "teacher_list"



    name = fields.Char(string = "Name", required = True)
    surname = fields.Char(string="Surname", required=True)
    email = fields.Char(string = "Email")
    course = fields.Many2one("courses.course",string="course")

    @api.depends('surname', 'name')
    def name_get(self):
        result = []
        for account in self:
            name = account.surname + ' ' + account.name
            result.append((account.id, name))
        return result