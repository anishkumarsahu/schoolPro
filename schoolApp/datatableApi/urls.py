from django.urls import re_path
from .views import *

urlpatterns = [
    # buyer
    re_path(r'^getNonTeachingStaffListJson/$', getNonTeachingStaffListJson.as_view(), name='getNonTeachingStaffListJson'),
    re_path(r'^getStudentListJson/$', getStudentListJson.as_view(), name='getStudentListJson'),
    re_path(r'^getTeacherListJson/$', getTeacherListJson.as_view(), name='getTeacherListJson'),
    re_path(r'^getParentListJson/$', getParentListJson.as_view(), name='getParentListJson'),
    re_path(r'^getClassListJson/$', getClassListJson.as_view(), name='getClassListJson'),
    re_path(r'^getStudentListForAttendanceJson/$', getStudentListForAttendanceJson.as_view(), name='getStudentListForAttendanceJson'),
    re_path(r'^getEventsListJson/$', getEventsListJson.as_view(), name='getEventsListJson'),
    re_path(r'^getClassAssignedSubjectsJson/$', getClassAssignedSubjectsJson.as_view(), name='getClassAssignedSubjectsJson'),
]