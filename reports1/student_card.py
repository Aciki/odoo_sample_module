from odoo import models ,  api



class CourseReport(models.AbstractModel):
    _name = 'report.courses.student_report'
    _description = 'student_get_report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("test")
        docs = self.env['courses.student'].browse(docids[0])
        grades_of_students = self.env["insert.grades"].search([('student', '=', docids[0],)])
        course_of_students = self.env["insert.grades"].search([('course_id', '=', docids[0],)])
        print('docs',docs)
        print('grades_of_students', grades_of_students)
        print('course_of_students', course_of_students)

        course_list_students = []
        for cr in course_of_students:
            vals = {

                'course_name': cr.course_id.course

            }
            course_list_students.append(vals)
        print('course_list_students', course_list_students)

        grades_list_students = []
        for gr in grades_of_students:
            vals1 = {



                'student_name': gr.grades,
                'student_course': gr.course_id.course

            }
            grades_list_students.append(vals1)
        print('grades_list_students', grades_list_students)


        return {
            'doc_ids': docs.ids,
            'doc_model': 'courses.course',
            'data': data,
            'docs': docs,
            'grades_list_students':grades_list_students,
            'course_list_students':course_list_students,

        }