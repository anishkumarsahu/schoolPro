from functools import wraps

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import *
from .apiView import get_current_session_year, get_current_session


def login_required_sms():
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('/Login/')
            return view_func(request, *args, **kwargs)

        return wrapper

    return _check_group


def is_locked():
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # if not request.user.is_authenticated:
            #     return redirect('/Login/')

            if request.user.is_authenticated and request.session['isLocked'] == 'Yes':
                return redirect('/LockScreen/')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group


def get_current_session_html():
    current = SchoolSession.objects.get(isCurrent__exact=True)
    return {'currentSessionYear': current.sessionYear, 'Id': current.pk}


# Create your views here.
# done


def management_login(request):

    s_account = SchoolOwner.objects.all()

    context = {
        'count':s_account.count()
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            sess = SchoolSession.objects.all().order_by('-id')
            s_list = []
            for s in sess:
                s_dic = {
                    'sessionYear': s.sessionYear,
                    'ID': s.pk
                }
                s_list.append(s_dic)

            request.session['CurrentSchoolSession'] = get_current_session_html()
            request.session['schoolSession'] = s_list
            request.session['isLocked'] = 'No'

            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "Wrong Credential! Please try again.")

            return render(request, "login.html", context)
    return render(request, 'login.html',context)


# done
def management_logout(request):
    logout(request)
    request.session['CurrentSchoolSession'] = ''
    request.session['schoolSession'] = ''
    request.session['isLocked'] = ''
    return redirect('/Login/')


# done
def add_owner(request):
    if request.method == 'POST':
        name = request.POST['nameSign']
        username = request.POST['usernameSign']
        password = request.POST['passwordSign']
        phoneNumber = request.POST['phoneNumberSign']
        email = request.POST['emailSign']

        owner = SchoolOwner()
        owner.name = name
        owner.username = username
        owner.password = password
        owner.email = email
        owner.phoneNumber = phoneNumber
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        g = Group.objects.get(name='Owner')
        g.user_set.add(user.pk)
        g.save()
        owner.userID_id = user.pk
        owner.userGroup = g.name
        owner.save()
        school_detail = SchoolDetail()
        school_detail.ownerID_id = owner.pk
        school_detail.save()

        social_link = SchoolSocialLink()
        social_link.ownerID_id = owner.pk
        social_link.schoolID_id = school_detail.pk
        social_link.save()

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('/')
        return redirect('/Login/')

@is_locked()
@login_required_sms()
def home(request):
    students = StudentDetail.objects.filter(isDeleted__exact=False,
                                            sessionID_id=request.session['CurrentSchoolSession']['Id'])
    studentsM = StudentDetail.objects.filter(isDeleted__exact=False,
                                             sessionID_id=request.session['CurrentSchoolSession']['Id'],
                                             gender__exact='Male')
    studentsF = StudentDetail.objects.filter(isDeleted__exact=False,
                                             sessionID_id=request.session['CurrentSchoolSession']['Id'],
                                             gender__exact='Female')
    teachers = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True)
    teachersM = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True, gender__exact='Male')
    teachersF = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True, gender__exact='Female')
    nonTeaching = NonTeachingStaff.objects.filter(isDeleted__exact=False)
    context = {
        'students': students,
        'studentsM': studentsM,
        'studentsF': studentsF,
        'teachers': teachers,
        'teachersM': teachersM,
        'teachersF': teachersF,
        'nonTeaching': nonTeaching
    }

    return render(request, 'index.html', context)


@is_locked()
@login_required_sms()
def addStudent(request):
    return render(request, 'Add_student_new.html')


@is_locked()
@login_required_sms()
def addStudentNew(request):
    return render(request, 'Add_student_new.html')


@is_locked()
@login_required_sms()
def get_new_student_form(request):
    return render(request, 'ajaxData/new_student.html')


@is_locked()
@login_required_sms()
def get_new_student_from_session(request):
    return render(request, 'ajaxData/session_student.html')


@is_locked()
@login_required_sms()
def studentList(request):
    return render(request, 'Student_list.html')


@is_locked()
@login_required_sms()
def setting(request):
    return render(request, 'setting.html')


@is_locked()
@login_required_sms()
def addTeacher(request):
    return render(request, 'addTeachers.html')


@is_locked()
@login_required_sms()
def teacherList(request):
    return render(request, 'teacherList.html')


@is_locked()
@login_required_sms()
def parentsList(request):
    return render(request, 'parentsList.html')


@is_locked()
@login_required_sms()
def addClasses(request):
    return render(request, 'addClasses.html')


# def addTeacherToClass(request):
#     return render(request, 'assignTeacherToClass.html')
@is_locked()
@login_required_sms()
def classList(request):
    std_list = Standard.objects.filter(isDeleted=False, sessionID=get_current_session(request))

    context = {
        'ClassData': std_list
    }

    return render(request, 'classList.html', context)


@is_locked()
@login_required_sms()
def addSubject(request):
    return render(request, 'addSubject.html')


@is_locked()
@login_required_sms()
def classAssignedSubject(request):
    std_list = Standard.objects.filter(isDeleted=False, sessionID=get_current_session(request))

    context = {
        'ClassData': std_list
    }

    return render(request, 'classAssignedSubjectList.html',context)



@is_locked()
@login_required_sms()
def assignSubject(request):
    return render(request, 'assignSubject.html')


@is_locked()
@login_required_sms()
def addExam(request):
    return render(request, 'addExam.html')


@is_locked()
@login_required_sms()
def assignExam(request):
    return render(request, 'assignExam.html')


@is_locked()
@login_required_sms()
def examList(request):
    return render(request, 'examsList.html')


@is_locked()
@login_required_sms()
def assignedSubject(request):
    return render(request, 'Assigned_Subjects.html')


@is_locked()
@login_required_sms()
def addMark(request):
    return render(request, 'addMark.html')


@is_locked()
@login_required_sms()
def markList(request):
    return render(request, 'markList.html')


@is_locked()
@login_required_sms()
def event(request):
    return render(request, 'event.html')


@is_locked()
@login_required_sms()
def studentAttendanceAdd(request):
    return render(request, 'StudentAddAttendance.html')


@is_locked()
@login_required_sms()
def studentAttendanceHistory(request):
    return render(request, 'StudentAttendenceHistory.html')


@is_locked()
@login_required_sms()
def teacherAddAttendance(request):
    return render(request, 'teacherAddAttendance.html')


@is_locked()
@login_required_sms()
def studentAttendanceHistoryMWise(request):
    return render(request, 'studentAttendanceHistoryMWise.html')


@is_locked()
@login_required_sms()
def tecaherAttendanceHistory(request):
    return render(request, 'TeachersAttendanceHistory.html')


@is_locked()
@login_required_sms()
def studentAttendanceHistoryDWise(request):
    return render(request, 'studentAttendanceHistoryDWise.html')


@is_locked()
@login_required_sms()
def studentAttendanceHistorySubWise(request):
    return render(request, 'studentAttendanceHistorySubWise.html')


@is_locked()
@login_required_sms()
def studentAttendanceHistoryStuWise(request):
    return render(request, 'studentAttendanceHistoryStuWise.html')


@is_locked()
@login_required_sms()
def teacherAttendanceHistoryTeachWise(request):
    return render(request, 'teacherAttendanceHistoryTeachWise.html')


@is_locked()
@login_required_sms()
def tecaherAttendanceHistoryMWise(request):
    return render(request, 'tecaherAttendanceHistoryMWise.html')


@is_locked()
@login_required_sms()
def tecaherAttendanceHistoryDWise(request):
    return render(request, 'tecaherAttendanceHistoryDWise.html')


@is_locked()
@login_required_sms()
def updateFees(request):
    return render(request, 'updateFees.html')


@is_locked()
@login_required_sms()
def feesDetailList(request):
    return render(request, 'feesDetailList.html')


@is_locked()
@login_required_sms()
def SchoolSMS(request):
    return render(request, 'SchoolSMS.html')


@is_locked()
@login_required_sms()
def ClassSMS(request):
    return render(request, 'ClassSMS.html')


@is_locked()
@login_required_sms()
def StudentSMS(request):
    return render(request, 'StudentSMS.html')


@is_locked()
@login_required_sms()
def SMSList(request):
    return render(request, 'smsList.html')

@login_required_sms()
def LockScreen(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['isLocked'] = 'No'
            login(request, user)
            return redirect('/')


    request.session['isLocked'] = 'Yes'
    return render(request, 'lockscreen.html')
