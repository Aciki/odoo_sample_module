{
'name': "courses",
'summary': "Scholl ",
'description': """
Manage Library
==============
Description related to library.
""",
'author': "Aleksandar",
'website': "http://www.example.com",
'images': [
'static/description/courses.jpeg',],
'category': 'Courses',
'version': '14.0.1',
'depends': ['base'],
'data': ['security/ir.model.access.csv','views/student.xml','views/teacher.xml','wizards/insert_grades.xml','views/courses.xml','reports/report.xml','reports/course_card.xml',
         'reports/student_card.xml','security/security.xml',],
'installable': True,
'auto_install': False,
'application': True,
}