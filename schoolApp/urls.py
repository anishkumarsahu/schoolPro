# from django.conf.urls import url
from .views import *
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', home, name='home'),

    re_path(r'^addStudent/$', addStudent, name='addStudent'),
    re_path(r'^addNewStudent/$', get_new_student_form, name='get_new_student_form'),
    re_path(r'^addNewStudentFromSession/$', get_new_student_from_session, name='get_new_student_from_session'),
    re_path(r'^addStudentNew/$', addStudentNew, name='addStudentNew'),
    re_path(r'^studentList/$', studentList, name='studentList'),
    re_path(r'^Login/$', management_login, name='login'),
    re_path(r'^Logout/$', management_logout, name='logout'),
    re_path(r'^AddOwner/$', add_owner, name='AddOwner'),
    re_path(r'^setting/$', setting, name='setting'),
    re_path(r'^addTeacher/$', addTeacher, name='addTeacher'),
    re_path(r'^teacherList/$', teacherList, name='teacherList'),
    re_path(r'^parentsList/$', parentsList, name='parentsList'),
    re_path(r'^addClasses/$', addClasses, name='addClasses'),
    # re_path(r'^assignTeacherToClass/$', addTeacherToClass, name='addTeacherToClass'),
    re_path(r'^classList/$', classList, name='classList'),
    re_path(r'^addSubject/$', addSubject, name='addSubject'),
    re_path(r'^classAssignedSubjectList/$', classAssignedSubject, name='classAssignedSubject'),
    re_path(r'^assignSubject/$', assignSubject, name='assignSubject'),
    re_path(r'^addExam/$', addExam, name='addExam'),
    re_path(r'^assignExam/$', assignExam, name='assignExam'),
    re_path(r'^assignedSubject/$', assignedSubject, name='assignedSubject'),
    re_path(r'^examList/$', examList, name='examList'),
    re_path(r'^addMark/$', addMark, name='addMark'),
    re_path(r'^markList/$', markList, name='markList'),
    re_path(r'^event/$', event, name='event'),
    re_path(r'^studentAttendanceAdd/$', studentAttendanceAdd, name='studentAttendanceAdd'),
    re_path(r'^studentAttendanceHistory/$', studentAttendanceHistory, name='studentAttendanceHistory'),
    re_path(r'^teacherAddAttendance/$', teacherAddAttendance, name='teacherAddAttendance'),

    re_path(r'^teacherAttendanceHistory/$', tecaherAttendanceHistory, name='tecaherAttendanceHistory'),
    re_path(r'^updateFees/$', updateFees, name='updateFees'),
    re_path(r'^feesDetailList/$', feesDetailList, name='feesDetailList'),

    re_path(r'^SchoolSMS/$', SchoolSMS, name='SchoolSMS'),
    re_path(r'^ClassSMS/$', ClassSMS, name='ClassSMS'),
    re_path(r'^StudentSMS/$', StudentSMS, name='StudentSMS'),
    re_path(r'^SMSList/$', SMSList, name='SMSList'),
    re_path(r'^LockScreen/$', LockScreen, name='LockScreen'),
]
