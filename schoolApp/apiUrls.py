# from django.conf.urls import url
from django.urls import re_path
from .apiView import *

urlpatterns = [
    re_path(r'^UsernameList/$', get_username_list, name='home'),
    re_path(r'^SchoolDetail/$', get_owner_school_detail, name='SchoolDetail'),
    re_path(r'^PostSchoolDetail/$', post_school_detail, name='post_school_detail'),
    re_path(r'^PostSchoolLogo/$', post_school_logo, name='post_school_logo'),
    re_path(r'^GetSchoolSocialLinks/$', get_owner_school_social_link, name='get_owner_school_social_link'),
    re_path(r'^PostSchoolSocialLinks/$', post_school_social_link, name='post_school_social_link'),
    re_path(r'^PostNonTeacher/$', post_non_teaching_user, name='post_non_teaching_user'),
    # done dataTables
    re_path(r'^GetNonTeachingList/$', get_non_teaching_list, name='get_non_teaching_list'),
    # daniel
    re_path(r'^GetNonTeacherDetail/(?P<id>\d+)$', get_non_teacher_detail, name='get_non_teacher_detail'),
    re_path(r'^EditNonTeacherdetail/$', edit_nonteaching_detail, name='edit_nonteaching_detail'),
    re_path(r'^EditNonteacherPhoto/$', edit_nonteacher_photo, name='edit_nonteacher_photo'),

    re_path(r'^DeleteComputerOperator/$', delete_computer_operator, name='delete_computer_operator'),

    re_path(r'^PostSession/$', post_school_session, name='post_school_session'),
    re_path(r'^GetSession/$', get_session_list, name='get_session_list'),

    # student
    re_path(r'^PostNewStudentDetail/$', post_new_student_detail, name='post_new_student_detail'),
    #done
    re_path(r'^GetStudentList/$', get_student_list, name='get_student_list'),
    re_path(r'^GetStudentDetail/(?P<id>\d+)/$', get_student_detail, name='get_student_detail'),
    re_path(r'^GetStudentDetailForEdit/(?P<id>\d+)/$', get_student_detail_for_edit, name='get_student_detail_for_edit'),
    re_path(r'^EditStudentDetail/$', edit_student_detail, name='edit_student_detail'),
    re_path(r'^UpdateStudentPhoto/$', edit_student_photo, name='edit_student_photo'),
    re_path(r'^Delete/Student/$', delete_student, name='delete_student'),
    re_path(r'^GetStudentDetailByUniqueKey/$', get_student_detail_by_unique_key, name='get_student_detail_by_unique_key'),


    # parent
    re_path(r'^GetParentList/$', get_parent_list, name='get_parent_list'),
    re_path(r'^GetParentDetail/(?P<id>\d+)/$', get_parent_detail, name='get_parent_detail'),
    re_path(r'^GetParentDetailForEdit/(?P<id>\d+)/$', get_parent_detail_for_edit, name='get_parent_detail_for_edit'),
    re_path(r'^UpdateParentDetail/$', edit_parent_detail, name='edit_parent_detail'),
    re_path(r'^DeleteParentDetail/$', delete_parent_detail, name='delete_parent_detail'),

    # teacher
    re_path(r'^PostTeacherDetail/$', post_teacher_detail, name='post_teacher_detail'),

    #done
    re_path(r'^GetTeacherList/$', get_teacher_list, name='get_teacher_list'),
    re_path(r'^GetTeacherDetail/(?P<id>\d+)/$', get_teacher_detail, name='get_teacher_detail'),
    re_path(r'^GetTeacherDetailForEdit/(?P<id>\d+)/$', get_teacher_detail_for_edit, name='get_teacher_detail_for_edit'),
    re_path(r'^UpdateTeacherPhoto/$', edit_teacher_photo, name='edit_teacher_photo'),
    re_path(r'^UpdateTeacherDetail/$', update_teacher_detail, name='update_teacher_detail'),
    re_path(r'^DeleteTeacherDetail/$', delete_teacher_detail, name='delete_teacher_detail'),
    re_path(r'^GetUnassignedTeacherList/$', get_unassign_teacher_list_for_class,
        name='get_unassign_teacher_list_for_class'),

    # class
    re_path(r'^AddClassWithoutSection/$', add_class_without_section, name='add_class_without_section'),
    re_path(r'^AddClassWithSection/$', add_class_with_section, name='add_class_with_section'),
    re_path(r'^GetClassList/$', get_class_list, name='get_class_list'),
    re_path(r'^GetClassDetailWithoutSection/(?P<id>\d+)/$', get_class_detail_without_section,
        name='get_class_detail_without_section'),
    re_path(r'^GetClassDetailWithSection/(?P<id>\d+)/$', get_class_detail_with_section,
        name='get_class_detail_with_section'),
    re_path(r'^DeleteClassOrSection/$', delete_class_or_section, name='delete_class_or_section'),
    re_path(r'^UpdateClassOrSection/$', update_class_or_section_detail, name='update_class_or_section_detail'),
    re_path(r'^GetOnlyClassList/$', get_only_class, name='get_only_class'),
    re_path(r'^GetOnlyClassSectionDetail/(?P<id>\d+)/$', get_only_section_of_class, name='get_only_section_of_class'),


    # subject
    re_path(r'^PostNewSubjectDetail/$', add_subject, name='add_subject'),
    re_path(r'^GetSubjectList/$', get_subject_list, name='get_subject_list'),
    re_path(r'^GetSubjectDetail/(?P<id>\d+)/$', get_subject_detail, name='get_subject_detail'),
    re_path(r'^UpdateSubjectDetail/$', update_subject, name='update_subject'),
    re_path(r'^DeleteSubject/$', delete_subject, name='delete_subject'),
    re_path(r'^delete_class_assigned_subject/$', delete_class_assigned_subject, name='delete_class_assigned_subject'),
    re_path(r'^AssignSubjectsToClass/$', assign_subjects_to_class, name='assign_subjects_to_class'),
    re_path(r'^GetSubjectListWithClass/(?P<id>\d+)/$', get_subject_list_with_class, name='get_subject_list_with_class'),
    re_path(r'^PostSubjectsToClassToTeacher/$', assign_subjects_to_class_to_teacher, name='assign_subjects_to_class_to_teacher'),
    re_path(r'^GetAssignSubjectsToClassToTeacherList/$', get_assign_subjects_to_class_to_teacher_list, name='get_assign_subjects_to_class_to_teacher_list'),
    re_path(r'^GetAssignSubjectsToClassToTeacherDetailForEdit/(?P<id>\d+)/$', get_assign_subjects_to_class_to_teacher_detail, name='get_assign_subjects_to_class_to_teacher_detail'),
    re_path(r'^UpdateSubjectsToClassToTeacher/$', update_assign_subjects_to_class_to_teacher,
        name='update_assign_subjects_to_class_to_teacher'),

    #attendence
    re_path(r'^GetStudentListForAttendance/$', get_student_list_by_class_section_no_subject_by_date, name='get_student_list_by_class_section_no_subject_by_date'),
    re_path(r'^AddAttendanceOfStudentWithoutSubject/$', student_attendance_without_subject, name='student_attendance_without_subject'),
    re_path(r'^AddAttendanceOfStudentWithSubject/$', student_attendance_with_subject, name='student_attendance_with_subject'),
    re_path(r'^GetStudentListForAttendanceWithSubject/$', get_student_list_by_class_section_subject_by_date, name='get_student_list_by_class_section_subject_by_date'),

    # attendance list
    re_path(r'^GetStudentAttendanceListByDateRange/$', get_student_attendance_list_by_date_range,
        name='get_student_attendance_list_by_date_range'),
    re_path(r'^GetStudentListwithClassAndSection/$', get_student_list_with_class_and_section,
        name='get_student_list_with_class_and_section'),

    re_path(r'^GetStudentAttendanceListwithClassAndSectionAndStudent/$', get_student_attendance_list_by_student,
        name='get_student_attendance_list_by_student'),


    re_path(r'^GetTeacherAttendanceListForAttendance/$', get_teacher_attendance_list_by_date,
        name='get_teacher_attendance_list_by_date'),
    re_path(r'^AddTeacherAttendance/$', add_teacher_attendance_by_date,name='add_teacher_attendance_by_date'),
    re_path(r'^GetTeacherAttendanceHistoryByDateRange/$', get_teacher_attendance_list_by_date_range,name='get_teacher_attendance_list_by_date_range'),
    re_path(r'^GetTeacherAttendanceHistoryByTeacher/$', get_teacher_attendance_list_by_teacher,name='get_teacher_attendance_list_by_teacher'),



    re_path(r'^GetStudentFee/$', get_student_fee,name='get_student_fee'),
    re_path(r'^AddStudentFee/$', add_fee_for_student,name='add_fee_for_student'),
    re_path(r'^GetStudentFeeClassWise/$', get_class_wise_student_fee,name='get_class_wise_student_fee'),
    re_path(r'^GetStudentFeeDetail/$', get_student_fee_detail,name='get_student_fee_detail'),



    re_path(r'^AddExam/$', add_exam,name='add_exam'),
    re_path(r'^GetExamList/$', get_exam_list,name='get_exam_list'),
    re_path(r'^EditExam/$', edit_exam,name='edit_exam'),
    re_path(r'^DeleteExam/$', delete_exam,name='delete_exam'),

    re_path(r'^AssignExam/$', assign_exam,name='assign_exam'),
    re_path(r'^GetAssignExamList/$', get_assign_exam_list, name='get_assign_exam_list'),
    re_path(r'^AssignExamUpdate/$', update_assign_exam, name='update_assign_exam'),
    re_path(r'^AssignExamDelete/$', delete_assign_exam, name='delete_assign_exam'),



    re_path(r'^GetAssignExamListByClass/(?P<id>\d+)/$', get_assign_exam_list_by_class, name='get_assign_exam_list_by_class'),
    re_path(r'^AddMarkOfStudent/$', add_mark_of_student, name='add_mark_of_student'),
    re_path(r'^GetStudentListByClassSectionSubjectByExamForMarks/$', get_student_list_by_class_section_subject_by_exam_for_marks,
        name='get_student_list_by_class_section_subject_by_exam_for_marks'),

    re_path(r'^GetStudentMarksByClass/$', get_student_marks_by_class, name='get_student_marks_by_class'),
    re_path(r'^GetStudentMarksByStudent/$', get_student_marks_by_student, name='get_student_marks_by_student'),


    re_path(r'^AddEvent/$', add_event, name='add_event'),
    re_path(r'^GetEventsList/$', get_event_list, name='get_event_list'),
    re_path(r'^EditEvent/$', edit_event, name='edit_event'),
    re_path(r'^DeleteEvent/$', delete_event, name='delete_event'),


    re_path(r'^UpdateSession/$', update_session_by_admin, name='update_session_by_admin'),


    re_path(r'^SendSmsToSchool/$', send_sms_to_school, name='send_sms_to_school'),
    re_path(r'^SendSmsToClass/$', send_sms_to_class, name='send_sms_to_class'),
    re_path(r'^SendSmsToStudent/$', send_sms_to_student, name='send_sms_to_student'),
    re_path(r'^GetSmsList/$', get_sms_list, name='get_sms_list'),

    # analytic
    re_path(r'^getStudentCountByClassAndSection/$', get_student_count_by_class_and_section, name='get_student_count_by_class_and_section'),

]
