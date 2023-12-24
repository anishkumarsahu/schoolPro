from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^Dashboard/$', student_dashboard, name='student_dashboard')
    ]