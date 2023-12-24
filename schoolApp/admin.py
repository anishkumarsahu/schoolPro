from django.contrib import admin
from .models import *


# Register your models here.

class SchoolOwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'phoneNumber', 'username', 'datetime', 'lastUpdatedOn', ]


admin.site.register(SchoolOwner, SchoolOwnerAdmin)


class SchoolDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'phoneNumber', 'email', 'datetime', 'lastUpdatedOn', ]


admin.site.register(SchoolDetail, SchoolDetailAdmin)


class SchoolSocialLinkAdmin(admin.ModelAdmin):
    list_display = ['schoolID', 'facebook', 'twitter', 'googlePlus', 'datetime', 'lastUpdatedOn', ]


admin.site.register(SchoolSocialLink, SchoolSocialLinkAdmin)


class ComputerOperatorAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'middleName', 'lastName', 'phoneNumber', 'sessionID', 'isActive', 'datetime',
                    'lastUpdatedOn', ]


admin.site.register(ComputerOperator, ComputerOperatorAdmin)


class SchoolSessionAdmin(admin.ModelAdmin):
    list_display = ['sessionYear', 'isCurrent', 'datetime', 'lastUpdatedOn', ]


admin.site.register(SchoolSession, SchoolSessionAdmin)


class NonTeachingStaffAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'phoneNumber', 'EmployeeCode']

    list_display = ['firstName', 'phoneNumber', 'EmployeeCode', 'isActive', 'datetime', 'lastUpdatedOn', ]


admin.site.register(NonTeachingStaff, NonTeachingStaffAdmin)


class TeacherDetailAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'phoneNumber', 'EmployeeCode']

    list_display = ['firstName', 'phoneNumber', 'EmployeeCode', 'isActive', 'datetime', 'lastUpdatedOn', ]


admin.site.register(TeacherDetail, TeacherDetailAdmin)


class StandardAdmin(admin.ModelAdmin):
    search_fields = ['name', 'classLocation', 'hasSection']

    list_display = ['name', 'sessionID', 'classLocation', 'hasSection', 'startingRoll', 'endingRoll', 'datetime',
                    'lastUpdatedOn', ]


admin.site.register(Standard, StandardAdmin)


class SectionAdmin(admin.ModelAdmin):
    search_fields = ['name']

    list_display = ['name', 'standardID', 'sessionID', 'startingRoll', 'endingRoll', 'datetime', 'lastUpdatedOn', ]


admin.site.register(Section, SectionAdmin)


class AssignTeacherToClassOrSectionAdmin(admin.ModelAdmin):
    list_display = ['classTeacher', 'standardID', 'sessionID', 'datetime', 'lastUpdatedOn', ]


admin.site.register(AssignTeacherToClassOrSection, AssignTeacherToClassOrSectionAdmin)


class ParentDetailAdmin(admin.ModelAdmin):
    search_fields = ['fatherFirstName', 'fatherLastName']

    list_display = ['fatherFirstName', 'fatherLastName', 'phoneNumber', 'occupation', 'email', 'datetime',
                    'lastUpdatedOn', ]


admin.site.register(ParentDetail, ParentDetailAdmin)


class StudentDetailAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName']

    list_display = ['firstName', 'lastName', 'sessionID', 'gender', 'presentAddress', 'standardID', 'sectionID',
                    'rollNumber','isDeleted', 'datetime', 'lastUpdatedOn', ]


admin.site.register(StudentDetail, StudentDetailAdmin)


class TeacherAttendanceAdmin(admin.ModelAdmin):
    search_fields = ['attendanceDate', 'reason']

    list_display = ['teacherID', 'sessionID', 'attendanceDate', 'isAbsent', 'reason', 'datetime', 'lastUpdatedOn', ]


admin.site.register(TeacherAttendance, TeacherAttendanceAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName', 'sessionID', 'isDeleted', 'datetime', 'lastUpdatedOn', ]


admin.site.register(Subject, SubjectAdmin)


class AssignClassSubjectAdmin(admin.ModelAdmin):
    list_display = ['classID', 'subjectID', 'sessionID', 'isDeleted', 'datetime', 'lastUpdatedOn', ]


admin.site.register(AssignClassSubject, AssignClassSubjectAdmin)


class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ['studentID', 'standardID', 'attendanceDate', 'isAbsent', 'reason', 'sectionID', 'subjectID',
                    'sessionID', 'datetime', 'lastUpdatedOn', ]


admin.site.register(StudentAttendance, StudentAttendanceAdmin)


class AssignSubjectToTeacherAdmin(admin.ModelAdmin):
    list_display = ['teacherID', 'classID', 'sectionID', 'subjectID', 'sessionID', 'datetime', 'lastUpdatedOn', ]


admin.site.register(AssignSubjectToTeacher, AssignSubjectToTeacherAdmin)


class ExamListAdmin(admin.ModelAdmin):
    list_display = ['examName', 'datetime', 'lastUpdatedOn', ]


admin.site.register(ExamList, ExamListAdmin)


class ExamAdmin(admin.ModelAdmin):
    list_display = ['examID', 'classID', 'startExamDate', 'endExamDate', 'fullMark', 'passMark', 'isDeleted',
                    'datetime', 'lastUpdatedOn', ]


admin.site.register(Exam, ExamAdmin)


class AssignExamSubjectAdmin(admin.ModelAdmin):
    list_display = ['examID', 'sessionID', 'subject', 'fullMark', 'passMark', 'examDate', 'isDeleted', 'datetime',
                    'lastUpdatedOn', ]


admin.site.register(AssignExamSubject, AssignExamSubjectAdmin)


class MarkOfStudentsByExamAdmin(admin.ModelAdmin):
    list_display = ['examID', 'sessionID', 'studentID', 'standardID', 'sectionID', 'subjectID', 'mark', 'isDeleted',
                    'datetime', 'lastUpdatedOn', ]


admin.site.register(MarkOfStudentsByExam, MarkOfStudentsByExamAdmin)


class EventAdmin(admin.ModelAdmin):
    search_fields = ['title', 'message']
    list_display = ['sessionID', 'title', 'message', 'startDate', 'endDate', 'isDeleted', 'datetime', 'lastUpdatedOn', ]


admin.site.register(Event, EventAdmin)


class StudentFeeAdmin(admin.ModelAdmin):
    search_fields = ['month', 'note']
    list_display = ['studentID', 'sessionID', 'month', 'note', 'isPaid', 'payDate', 'isDeleted', 'datetime',
                    'lastUpdatedOn', ]


admin.site.register(StudentFee, StudentFeeAdmin)
