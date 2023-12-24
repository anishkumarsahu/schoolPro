import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string


def get_current_session(request):
    if 'CurrentSchoolSession' not in request.session:
        try:
            current = SchoolSession.objects.get(isCurrent__exact=True)
        except:
            current = SchoolSession.objects.all().order_by('-id')[0]

        return current.pk

    else:
        return request.session['CurrentSchoolSession']['Id']


def get_current_session_year():

    try:
        current = SchoolSession.objects.get(isCurrent__exact=True)
    except:
        current = SchoolSession.objects.all().order_by('-id')[0]

    return current.pk



def get_username_list(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return JsonResponse({'response': 'ok', 'message': 'Username already exist.'})
        except:

            return HttpResponse('')


def get_owner_school_detail(request):
    school_detail = SchoolDetail.objects.all()[0]

    data = {
        'ID': school_detail.pk,
        'SchoolName': school_detail.name,
        'PhoneNumber': school_detail.phoneNumber,
        'Email': school_detail.email,
        'Address': school_detail.address,
        'City': school_detail.city,
        'Country': school_detail.country,
        'State': school_detail.state,
        'PinCode': school_detail.pinCode,
        'Website': school_detail.website,
        'Logo': school_detail.logo.url,
    }
    return JsonResponse(data)


def post_school_detail(request):
    if request.method == 'POST':
        SDid = request.POST.get('SDid')
        SDschoolName = request.POST.get('SDschoolName')
        SDcity = request.POST.get('SDcity')
        SDemail = request.POST.get('SDemail')
        SDaddress = request.POST.get('SDaddress')
        SDphone = request.POST.get('SDphone')
        SDcountry = request.POST.get('SDcountry')
        SDstate = request.POST.get('SDstate')
        SDpin = request.POST.get('SDpin')
        SDwebsite = request.POST.get('SDwebsite')
        try:
            school_data = SchoolDetail.objects.get(pk=int(SDid))
            school_data.name = SDschoolName
            school_data.city = SDcity
            school_data.email = SDemail
            school_data.address = SDaddress
            school_data.phoneNumber = SDphone
            school_data.country = SDcountry
            school_data.state = SDstate
            school_data.pinCode = SDpin
            school_data.website = SDwebsite
            school_data.save()
            return JsonResponse({'response': 'ok'})
        except:

            return HttpResponse({'response': 'error'})


@csrf_exempt
def post_school_logo(request):
    if request.method == 'POST':
        SDid = request.POST.get('SDid')
        image = request.FILES['file']
        try:
            school_data = SchoolDetail.objects.get(pk=int(SDid))
            school_data.logo = image
            school_data.save()
            return JsonResponse({'response': 'ok'})
        except:

            return HttpResponse({'response': 'error'})


def get_owner_school_social_link(request):
    social_link = SchoolSocialLink.objects.all()[0]
    data = {
        'ID': social_link.pk,
        'Facebook': social_link.facebook,
        'Twitter': social_link.twitter,
        'Playstore': social_link.googlePlus,

    }
    return JsonResponse(data)


def post_school_social_link(request):
    if request.method == 'POST':
        SLid = request.POST.get('SLid')
        SLfacebook = request.POST.get('SLfacebook')
        SLtwitter = request.POST.get('SLtwitter')
        SLplaystore = request.POST.get('SLplaystore')

        try:
            social_link = SchoolSocialLink.objects.get(pk=int(SLid))
            social_link.facebook = SLfacebook
            social_link.twitter = SLtwitter
            social_link.googlePlus = SLplaystore
            social_link.save()
            return JsonResponse({'response': 'ok'})
        except:

            return HttpResponse({'response': 'error'})


def post_non_teaching_user(request):
    if request.method == 'POST':
        UAfirstname = request.POST.get('UAfirstname')
        UAmiddlename = request.POST.get('UAmiddlename')
        UAlastname = request.POST.get('UAlastname')
        UAphone = request.POST.get('UAphone')
        UAemail = request.POST.get('UAemail')
        AUdob = request.POST.get('AUdob')
        UAqualification = request.POST.get('UAqualification')
        UAadhaar = request.POST.get('UAadhaar')
        UAaddress = request.POST.get('UAaddress')
        UAcity = request.POST.get('UAcity')
        UACountry = request.POST.get('UACountry')
        UAState = request.POST.get('UAState')
        UApin = request.POST.get('UApin')
        UAjoindate = request.POST.get('UAjoindate')
        UAreleave = request.POST.get('UAreleave')
        UAgender = request.POST.get('UAgender')
        UAcurrentPosition = request.POST.get('UAcurrentPosition')
        UAemployeeCode = request.POST.get('UAemployeeCode')
        UAbloodGroup = request.POST.get('UAbloodGroup')
        if UAreleave == "":
            UAreleave = None
        image = request.FILES['photo']
        try:
            non_tea = NonTeachingStaff()
            non_tea.firstName = UAfirstname
            non_tea.middleName = UAmiddlename
            non_tea.lastName = UAlastname
            non_tea.phoneNumber = UAphone
            non_tea.email = UAemail
            non_tea.DOB = AUdob
            non_tea.qualification = UAqualification
            non_tea.address = UAaddress
            non_tea.aadhar = UAadhaar
            non_tea.city = UAcity
            non_tea.country = UACountry
            non_tea.state = UAState
            non_tea.pinCode = UApin
            non_tea.joinDate = UAjoindate
            non_tea.releaveDate = UAreleave
            non_tea.gender = UAgender
            non_tea.currentPosition = UAcurrentPosition
            non_tea.EmployeeCode = UAemployeeCode
            non_tea.bloodGroup = UAbloodGroup
            username = 'NT' + get_random_string(length=3,
                                                 allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
                length=3, allowed_chars='1234567890')
            password = get_random_string(length=10, allowed_chars='1234567890')
            while User.objects.filter(username__exact=username).count() > 0:
                username = 'NT' + get_random_string(length=3,
                                                    allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
                    length=3, allowed_chars='1234567890')
                password = get_random_string(length=10, allowed_chars='1234567890')
            else:
                user =User()
                user.username = username
                user.set_password(password)
                non_tea.password = password
                non_tea.username = username
                user.save()

            try:
                g = Group.objects.get(name='NonTeaching')
                g.user_set.add(user.pk)
                g.save()
            except:
                g = Group()
                g.name = "NonTeaching"
                g.save()
                g.user_set.add(user.pk)
                g.save()
            non_tea.userID_id = user.id
            non_tea.isActive = True
            non_tea.photo = image
            non_tea.userID_id = user.pk
            non_tea.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'error'})


def get_non_teaching_list(request):
    nonTeaching = NonTeachingStaff.objects.filter(isDeleted__exact=False)
    nonteaching_list = []
    for obj in nonTeaching:
        if obj.isActive == True:
            active = "Yes"
        else:
            active = "No"
        nonteaching_dic = {
            'ID': obj.pk,
            'Name': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Photo': '<img src="{}" class="avatar" alt="Photo">'.format(obj.photo.thumbnail.url),
            'Phone': obj.phoneNumber,
            'EmployeeCode': obj.EmployeeCode,
            'DOB': obj.DOB,
            'DateOfJoining': obj.joinDate,
            'Gender': obj.gender,
            'IsActive': active,
            'Action': '<a onclick ="userDetailId({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myViewModal"><i class="fa fa-eye"></i> View </a> <a onclick ="EditUserComputerOperator({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="getIdFordeletingComputerOperator({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        nonteaching_list.append(nonteaching_dic)
    return JsonResponse({'data': nonteaching_list}, safe=False)


# Date: 31 Aug 2018, To get Computer_operator(user) detail
def get_non_teacher_detail(request, id=None):
    if request.method == 'GET':
        try:
            nonTeacher = NonTeachingStaff.objects.get(pk=int(id), isDeleted__exact=False)
            context = {
                'opId': nonTeacher.pk,
                'opImage': nonTeacher.photo.url,
                'name': nonTeacher.firstName + ' ' + nonTeacher.middleName + ' ' + nonTeacher.lastName,
                'qualification': nonTeacher.qualification,
                'email': nonTeacher.email,
                'mobileno': nonTeacher.phoneNumber,
                'dob': nonTeacher.DOB,
                'doj': nonTeacher.joinDate,
                'aadhar': nonTeacher.aadhar,
                'pin': nonTeacher.pinCode,
                'taddress': nonTeacher.city + '' + nonTeacher.address,
                'opaddress': nonTeacher.address,
                'paddress': nonTeacher.city + '' + nonTeacher.address,
                'state': nonTeacher.state,  # -------Till here for View User(Computer Operator)
                'cityname': nonTeacher.city,  # -------including Edit view User(Computer Operator)
                'dateofreleaving': nonTeacher.releaveDate,
                'firstname': nonTeacher.firstName,
                'middlename': nonTeacher.middleName,
                'lastname': nonTeacher.lastName,
                'gender': nonTeacher.gender,
                'bloodGroup': nonTeacher.bloodGroup,
                'isActive': nonTeacher.isActive,
            }
            return JsonResponse(context, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# Date: 31 Aug 2018, To edit Computer_operator(user) detail -- Daniel
@csrf_exempt
def edit_nonteacher_photo(request):
    if request.method == 'POST':
        opeditUserId = request.POST.get('opeditUserId')
        image = request.FILES['file']
        try:
            computerOperatorImage = NonTeachingStaff.objects.get(pk=int(opeditUserId))
            computerOperatorImage.photo = image
            computerOperatorImage.save()
            return JsonResponse({'response': 'ok'})
        except:

            return HttpResponse({'response': 'error'})


def edit_nonteaching_detail(request):
    if request.method == 'POST':
        opeditUserId = request.POST.get('opeditUserId')
        opfirstnameedit = request.POST.get('opfirstnameedit')
        opmiddlenameedit = request.POST.get('opmiddlenameedit')
        oplastnameedit = request.POST.get('oplastnameedit')
        mnoedit = request.POST.get('mnoedit')
        opemailedit = request.POST.get('opemailedit')
        dobedit = request.POST.get('dobedit')
        opqualificationedit = request.POST.get('opqualificationedit')
        aadharedit = request.POST.get('aadharedit')
        dojedit = request.POST.get('dojedit')
        taddedit = request.POST.get('taddedit')
        opcityedit = request.POST.get('opcityedit')
        opstateedit = request.POST.get('opstateedit')
        oppinedit = request.POST.get('oppinedit')
        doledit = request.POST.get('doledit')
        active = request.POST.get('active')

        try:
            computerOperator = NonTeachingStaff.objects.get(pk=int(opeditUserId))
            computerOperator.firstName = opfirstnameedit
            computerOperator.middleName = opmiddlenameedit
            computerOperator.lastName = oplastnameedit
            computerOperator.phoneNumber = mnoedit
            computerOperator.email = opemailedit
            computerOperator.DOB = dobedit
            computerOperator.qualification = opqualificationedit
            computerOperator.aadhar = aadharedit
            computerOperator.joinDate = dojedit
            computerOperator.address = taddedit
            computerOperator.city = opcityedit
            computerOperator.state = opstateedit
            computerOperator.pinCode = oppinedit
            if active == 'False':
                computerOperator.isActive = False
            if active == 'True':
                computerOperator.isActive =True
            if doledit != '':
                computerOperator.releaveDate = doledit
            else:
                computerOperator.releaveDate = None

            computerOperator.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# ------------------------------


def delete_computer_operator(request):
    if request.method == 'POST':
        ID = request.POST.get('COuserID')
        try:
            operator = NonTeachingStaff.objects.get(pk=int(ID))
            operator.isDeleted = True
            operator.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def post_school_session(request):
    if request.method == 'POST':
        Session = request.POST.get('Session')
        try:
            ses = SchoolSession()
            ses.sessionYear = Session
            ses.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'error'})


def get_session_list(request):
    ses = SchoolSession.objects.all()
    session_list = []
    for obj in ses:
        session_dic = {
            'Session': obj.sessionYear,

        }
        session_list.append(session_dic)
    return JsonResponse(session_list, safe=False)


# ------------------------- Teacher Module ----------------------------------------

def post_teacher_detail(request):
    if request.method == 'POST':
        TfirstName = request.POST.get('TfirstName')
        TmiddleName = request.POST.get('TmiddleName')
        TlastName = request.POST.get('TlastName')
        Temail = request.POST.get('Temail')
        Tphone = request.POST.get('Tphone')
        TbloodGroup = request.POST.get('TbloodGroup')
        Tdob = request.POST.get('Tdob')
        Tqualification = request.POST.get('Tqualification')
        Taadhar = request.POST.get('Taadhar')
        Tgender = request.POST.get('Tgender')
        Tdoj = request.POST.get('Tdoj')
        Tdor = request.POST.get('Tdor')
        if Tdor == "":
            Tdor = None

        TcurrentPosition = request.POST.get('TcurrentPosition')
        TemployeeCode = request.POST.get('TemployeeCode')
        Taddress = request.POST.get('Taddress')
        Tcity = request.POST.get('Tcity')
        Tstate = request.POST.get('Tstate')
        Tcountry = request.POST.get('Tcountry')
        Tpin = request.POST.get('Tpin')
        TPaddress = request.POST.get('TPaddress')
        TPcity = request.POST.get('TPcity')
        TPstate = request.POST.get('TPstate')
        TPcountry = request.POST.get('TPcountry')
        TPpin = request.POST.get('TPpin')
        image = request.FILES['Timage']
        try:
            teacher = TeacherDetail()
            teacher.firstName = TfirstName
            teacher.middleName = TmiddleName
            teacher.lastName = TlastName
            teacher.email = Temail
            teacher.phoneNumber = Tphone
            teacher.bloodGroup = TbloodGroup
            teacher.DOB = Tdob
            teacher.qualification = Tqualification
            teacher.aadhar = Taadhar
            teacher.gender = Tgender
            teacher.dateOfJoining = Tdoj
            teacher.dateOfLeaving = Tdor
            teacher.currentPosition = TcurrentPosition
            teacher.EmployeeCode = TemployeeCode
            teacher.presentAddress = Taddress
            teacher.presentCity = Tcity
            teacher.presentState = Tstate
            teacher.presentCountry = Tcountry
            teacher.presentPinCode = Tpin
            teacher.permanentAddress = TPaddress
            teacher.permanentCity = TPcity
            teacher.permanentState = TPstate
            teacher.permanentCountry = TPcountry
            teacher.permanentPinCode = TPpin
            teacher.photo = image


            username = 'T' + get_random_string(length=3,
                                                allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
                length=3, allowed_chars='1234567890')
            password = get_random_string(length=10, allowed_chars='1234567890')
            while User.objects.filter(username__exact=username).count() > 0:
                username = 'T' + get_random_string(length=3,
                                                    allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
                    length=3, allowed_chars='1234567890')
                password = get_random_string(length=10, allowed_chars='1234567890')
            else:
                user = User()
                user.username = username
                user.set_password(password)
                teacher.password = password
                teacher.username = username
                user.save()

            try:
                g = Group.objects.get(name='Teacher')
                g.user_set.add(user.pk)
                g.save()
            except:
                g = Group()
                g.name = "Teacher"
                g.save()
                g.user_set.add(user.pk)
                g.save()
            teacher.userID_id = user.id

            teacher.save()

            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_teacher_list(request):
    teachers = TeacherDetail.objects.filter(isDeleted__exact=False)
    teacher_list = []
    for obj in teachers:
        if obj.isActive == True:
            active = "Yes"
        else:
            active = "No"

        teacher_dic = {
            'TeacherID': obj.pk,
            'Name': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Photo': '<img src="{}" class="avatar" alt="Photo">'.format(obj.photo.thumbnail.url),
            'Phone': obj.phoneNumber,
            'DOB': obj.DOB,
            'DateOfJoining': obj.dateOfJoining,
            'Gender': obj.gender,
            'IsActive': active,
            'Action': '<a onclick ="getTeacherDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editTeacherDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteTeacherDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        teacher_list.append(teacher_dic)
    return JsonResponse({'data': teacher_list}, safe=False)


def get_teacher_detail(request, id=None):
    query = get_object_or_404(TeacherDetail, pk=id)
    if query.isActive == True:
        active = "Yes"
    else:
        active = "No"

    teacher_dic = {
        'TeacherID': query.pk,
        'Name': query.firstName + ' ' + query.middleName + ' ' + query.lastName,
        'DOB': query.DOB,
        'Aadhar': query.aadhar,
        'Gender': query.gender,
        'BloodGroup': query.bloodGroup,
        'PhoneNumber': query.phoneNumber,
        'Email': query.email,
        'PresentAddress': query.presentAddress + ',' + query.presentCity + ',' + query.presentState + ',' + query.presentCountry + '-' + query.presentPinCode,
        'PermanentAddress': query.permanentAddress + ',' + query.permanentCity + ',' + query.permanentState + ',' + query.permanentCountry + '-' + query.permanentPinCode,
        'Qualification': query.qualification,
        'EmployeeCode': query.EmployeeCode,
        'DateOfJoining': query.dateOfJoining,
        'DateOfLeaving': query.dateOfLeaving,
        'CurrentPosition': query.currentPosition,
        'Photo': query.photo.url,
        'IsActive': active,
        'UserName': query.username,
        'Password': query.password
    }
    return JsonResponse({'data': teacher_dic}, safe=False)


def get_teacher_detail_for_edit(request, id=None):
    query = get_object_or_404(TeacherDetail, pk=id)
    if query.isActive == True:
        active = "Yes"
    else:
        active = "No"

    teacher_dic = {
        'TeacherID': query.pk,
        'FirstName': query.firstName,
        'MiddleName': query.middleName,
        'LastName': query.lastName,
        'DOB': query.DOB,
        'Aadhar': query.aadhar,
        'Gender': query.gender,
        'BloodGroup': query.bloodGroup,
        'PhoneNumber': query.phoneNumber,
        'Email': query.email,
        'PresentAddress': query.presentAddress,
        'PresentCity': query.presentCity,
        'PresentState': query.presentState,
        'PresentCountry': query.presentCountry,
        'PresentPin': query.presentPinCode,
        'PermanentAddress': query.permanentAddress,
        'PermanentCity': query.permanentCity,
        'PermanentState': query.permanentState,
        'PermanentCounty': query.permanentCountry,
        'PermanentPin': query.permanentPinCode,
        'Qualification': query.qualification,
        'EmployeeCode': query.EmployeeCode,
        'DateOfJoining': query.dateOfJoining,
        'DateOfLeaving': query.dateOfLeaving,
        'CurrentPosition': query.currentPosition,
        'Photo': query.photo.url,
        'IsActive': active,
        'UserName': query.username,
        'Password': query.password
    }
    return JsonResponse({'data': teacher_dic}, safe=False)


@csrf_exempt
def edit_teacher_photo(request):
    if request.method == 'POST':
        TeacherID = request.POST.get('TeacherID')
        image = request.FILES['file']
        try:
            teacher_data = TeacherDetail.objects.get(pk=int(TeacherID))
            teacher_data.photo = image
            teacher_data.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'ok'})


def update_teacher_detail(request):
    if request.method == 'POST':
        TeacherID = request.POST.get('TeacherID')
        TisActive = request.POST.get('TisActive')
        TfirstName = request.POST.get('TfirstName')
        TmiddleName = request.POST.get('TmiddleName')
        TlastName = request.POST.get('TlastName')
        Temail = request.POST.get('Temail')
        Tphone = request.POST.get('Tphone')
        TbloodGroup = request.POST.get('TbloodGroup')
        Tdob = request.POST.get('Tdob')
        Tqualification = request.POST.get('Tqualification')
        Taadhar = request.POST.get('Taadhar')
        Tgender = request.POST.get('Tgender')
        Tdoj = request.POST.get('Tdoj')
        Tdor = request.POST.get('Tdor')
        if Tdor == "":
            Tdor = None

        if TisActive == 'Yes':
            TisActive = True
        else:
            TisActive = False
        TcurrentPosition = request.POST.get('TcurrentPosition')
        TemployeeCode = request.POST.get('TemployeeCode')
        Taddress = request.POST.get('Taddress')
        Tcity = request.POST.get('Tcity')
        Tstate = request.POST.get('Tstate')
        Tcountry = request.POST.get('Tcountry')
        Tpin = request.POST.get('Tpin')
        TPaddress = request.POST.get('TPaddress')
        TPcity = request.POST.get('TPcity')
        TPstate = request.POST.get('TPstate')
        TPcountry = request.POST.get('TPcountry')
        TPpin = request.POST.get('TPpin')

        try:
            teacher = TeacherDetail.objects.get(pk=int(TeacherID))
            teacher.firstName = TfirstName
            teacher.middleName = TmiddleName
            teacher.lastName = TlastName
            teacher.email = Temail
            teacher.phoneNumber = Tphone
            teacher.bloodGroup = TbloodGroup
            teacher.DOB = Tdob
            teacher.qualification = Tqualification
            teacher.aadhar = Taadhar
            teacher.gender = Tgender
            teacher.dateOfJoining = Tdoj
            teacher.dateOfLeaving = Tdor
            teacher.currentPosition = TcurrentPosition
            teacher.EmployeeCode = TemployeeCode
            teacher.presentAddress = Taddress
            teacher.presentCity = Tcity
            teacher.presentState = Tstate
            teacher.presentCountry = Tcountry
            teacher.presentPinCode = Tpin
            teacher.permanentAddress = TPaddress
            teacher.permanentCity = TPcity
            teacher.permanentState = TPstate
            teacher.permanentCountry = TPcountry
            teacher.permanentPinCode = TPpin
            teacher.isActive = TisActive
            teacher.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# done
@csrf_exempt
def delete_teacher_detail(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        teacher = TeacherDetail.objects.get(pk=int(id))
        teacher.isDeleted = True
        teacher.save()

        return JsonResponse({'data': 'ok'}, safe=False)


# -------------------------End Teacher Module-------------------------------
# ------------------------class Module ---------------------------------

# done
def get_unassign_teacher_list_for_class(request):
    teachers = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True)
    teacher_list = []
    for obj in teachers:
        teacher_dic = {
            'ID': obj.pk,
            'Name': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
        }

        teacher_list.append(teacher_dic)
    return JsonResponse(teacher_list, safe=False)


# done
def add_class_without_section(request):
    if request.method == 'POST':
        ClassName = request.POST.get('ClassName')
        ClassLocation = request.POST.get('ClassLocation')
        HaveClassSection = request.POST.get('HaveClassSection')
        ClassStartRoll = request.POST.get('ClassStartRoll')
        ClassEndRoll = request.POST.get('ClassEndRoll')
        try:
            try:
                std = Standard.objects.get(name__iexact=ClassName, isDeleted__exact=False,sessionID=get_current_session(request))
                return JsonResponse({'response': 'Class name already exist. Please try agein'}, safe=False)

            except:
                if int(get_current_session_year()) == int(get_current_session(request)):
                    standard = Standard()
                    standard.name = ClassName
                    standard.classLocation = ClassLocation
                    standard.hasSection = HaveClassSection
                    standard.startingRoll = ClassStartRoll
                    standard.endingRoll = ClassEndRoll
                    standard.sessionID_id = get_current_session_year()
                    standard.save()
                else:
                    pass

                return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# done
def add_class_with_section(request):
    if request.method == 'POST':
        ClassName = request.POST.get('ClassName')
        ClassLocation = request.POST.get('ClassLocation')
        HaveClassSection = request.POST.get('HaveClassSection')
        SecDetail = request.POST.get('SecDetail')

        detail = str(SecDetail).split('|')

        try:
            try:
                std = Standard.objects.get(name__iexact=ClassName, isDeleted__exact=False, sessionID=get_current_session(request))
                return JsonResponse({'response': 'Class name already exist. Please try agein'}, safe=False)

            except:
                if int(get_current_session_year()) == int(get_current_session(request)):
                    standard = Standard()
                    standard.name = ClassName
                    standard.classLocation = ClassLocation
                    standard.hasSection = HaveClassSection
                    standard.sessionID_id = get_current_session_year()
                    standard.save()

                    for d in detail[:-1]:
                        s_detail = d.split(',')
                        try:
                            class_sec = Section.objects.get(standardID_id=standard.pk, name__iexact=s_detail[0], isDeleted__exact=False)
                        except:
                            class_section = Section()

                            class_section.standardID_id = standard.pk
                            class_section.name = s_detail[0]
                            class_section.startingRoll = s_detail[1]
                            class_section.endingRoll = s_detail[2]
                            class_section.sessionID_id = get_current_session_year()
                            class_section.save()
                    else:
                        pass
                return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# done
def get_class_list(request, *args, **kwargs):
    query = request.GET.get('query')
    if query == 'all':
        class_list = Standard.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request)).order_by('datetime')
    else:
        class_list = Standard.objects.filter(isDeleted__exact=False, pk=int(query),sessionID=get_current_session(request)).order_by('datetime')
    teachers =''
    std_list = []
    for obj in class_list:
        if obj.hasSection == 'No':
            try:
                teachers = AssignTeacherToClassOrSection.objects.get(standardID_id=obj.pk, sessionID=get_current_session(request))
            except:

                if int(get_current_session_year()) == int(get_current_session(request)):
                    assign_teacher = AssignTeacherToClassOrSection()
                    assign_teacher.standardID_id = obj.pk
                    assign_teacher.sessionID_id = get_current_session_year()
                    assign_teacher.save()
                else:
                    pass
            if teachers.classTeacher == None:
                teacher = 'No Data'
            else:
                teacher = teachers.classTeacher.firstName + ' ' + teachers.classTeacher.middleName + ' ' + teachers.classTeacher.lastName

            std_dic = {
                'Class': obj.name,
                'Section': 'N/A',
                'StartRoll': obj.startingRoll,
                'EndRoll': obj.endingRoll,
                'Teacher': teacher,
                'Action': '<a class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal" onclick="getClassDetail({})"><i class="fa fa-eye"></i> View </a> <a href="#" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditClass" onclick="editClassDetail({})"><i class="fa fa-pencil"></i> Edit </a> <a href="#" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete" onclick = "deleteClass({})" ><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(obj.pk), str(obj.pk), str(obj.pk))
            }

            std_list.append(std_dic)
        if obj.hasSection == 'Yes':
            sec = Section.objects.filter(standardID_id=obj.pk, isDeleted__exact=False, sessionID=get_current_session(request))
            for objs in sec:
                try:
                    teachers = AssignTeacherToClassOrSection.objects.get(sectionID_id=objs.pk, sessionID=get_current_session(request))
                except:
                    if int(get_current_session_year()) == int(get_current_session(request)):

                        teacher = AssignTeacherToClassOrSection()
                        teacher.sectionID_id = objs.pk
                        teacher.sessionID_id = get_current_session_year()
                        teacher.save()
                    else:
                        pass
                if teachers.classTeacher_id == None:
                    teacher = 'No Data'
                else:
                    teacher = teachers.classTeacher.firstName + ' ' + teachers.classTeacher.middleName + ' ' + teachers.classTeacher.lastName

                std_dic = {
                    'Class': objs.standardID.name,
                    'Section': objs.name,
                    'StartRoll': objs.startingRoll,
                    'EndRoll': objs.endingRoll,
                    'Teacher': teacher,
                    'Action': '<a href="#" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"  onclick="getClassDetailWithSection({},{})"><i class="fa fa-eye"></i> View </a> <a href="#" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditClass"  onclick="editClassDetailWithSection({},{})"><i class="fa fa-pencil"></i> Edit </a> <a href="#" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete" onclick = "deleteClassSection({})"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                        str(objs.standardID_id), objs.pk, str(objs.standardID_id), objs.pk, objs.pk)
                }

                std_list.append(std_dic)
    return JsonResponse({'data': std_list}, safe=False)


# done
def get_class_detail_without_section(request, id=None):
    query = get_object_or_404(Standard, pk=id)
    try:
        teachers = AssignTeacherToClassOrSection.objects.get(standardID_id=query.pk, sessionID=get_current_session(request))
        teacher = teachers.classTeacher.firstName + ' ' + teachers.classTeacher.middleName + ' ' + teachers.classTeacher.lastName
        teacherID = str(teachers.classTeacher_id)
    except:
        teacher = 'No Data'
        teacherID = ''

    std_dic = {
        'ClassID': query.pk,
        'Class': query.name,
        'Location': query.classLocation,
        'Section': 'N/A',
        'StartRoll': query.startingRoll,
        'EndRoll': query.endingRoll,
        'Teacher': teacher,
        'TeacherID': str(teacherID)
    }
    return JsonResponse({'data': std_dic}, safe=False)


# done
def get_class_detail_with_section(request, id=None):
    query = get_object_or_404(Section, pk=id)

    try:
        teachers = AssignTeacherToClassOrSection.objects.get(sectionID_id=query.pk, sessionID=get_current_session(request))
        teacher = teachers.classTeacher.firstName + ' ' + teachers.classTeacher.middleName + ' ' + teachers.classTeacher.lastName
        teacherID = str(teachers.classTeacher_id)

    except:
        teacher = 'No Data'
        teacherID = ''

    std_dic = {
        'ClassID': query.standardID_id,
        'SectionID': query.pk,
        'Class': query.standardID.name,
        'Location': query.standardID.classLocation,
        'Section': query.name,
        'StartRoll': query.startingRoll,
        'EndRoll': query.endingRoll,
        'Teacher': teacher,
        'TeacherID': str(teacherID)

    }
    return JsonResponse({'data': std_dic}, safe=False)


# done
@csrf_exempt
def delete_class_or_section(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        sec = request.POST.get('sec')

        if sec == 'NO':
            std = Standard.objects.get(pk=int(id))

            std.isDeleted = True
            std.save()

        else:
            std_sec = Section.objects.get(pk=int(id))
            std_sec.isDeleted = True
            std_sec.save()
            std_id = std_sec.standardID_id

            is_more_section = Section.objects.filter(standardID_id=std_id, isDeleted__exact=False).count()
            if is_more_section == 0:
                del_standard = Standard.objects.get(pk=std_id)
                del_standard.isDeleted = True
                del_standard.save()
            else:
                pass

        return JsonResponse({'data': 'ok'}, safe=False)


# done
@csrf_exempt
def update_class_or_section_detail(request):
    if request.method == 'POST':
        ClassID = request.POST.get('ClassID')
        SectionID = request.POST.get('SectionID')
        HasSection = request.POST.get('HasSection')
        CLassName = request.POST.get('CLassName')
        SectionName = request.POST.get('SectionName')
        StartRoll = request.POST.get('StartRoll')
        EndRoll = request.POST.get('EndRoll')
        Location = request.POST.get('Location')
        TeacherID = request.POST.get('TeacherID')

        if HasSection == 'NO':
            std = Standard.objects.get(pk=int(ClassID), sessionID=get_current_session(request))
            std.name = CLassName
            std.startingRoll = StartRoll
            std.endingRoll = EndRoll
            std.classLocation = Location
            std.save()

            teacher = AssignTeacherToClassOrSection.objects.get(standardID_id=int(ClassID), sessionID=get_current_session(request))

            if TeacherID != '':
                teacher.classTeacher_id = int(TeacherID)
            else:
                teacher.classTeacher = None
            teacher.save()

        else:
            std_sec = Section.objects.get(pk=int(SectionID))
            std_sec.startingRoll = StartRoll
            std_sec.endingRoll = EndRoll
            std_sec.name = SectionName
            std_sec.save()
            std = Standard.objects.get(pk=int(ClassID))
            std.name = CLassName
            std.classLocation = Location
            std.save()
            teacher = AssignTeacherToClassOrSection.objects.get(sectionID_id=int(SectionID), sessionID=get_current_session(request))
            if TeacherID != '':
                teacher.classTeacher_id = int(TeacherID)
            else:
                teacher.classTeacher = None
            teacher.save()

    return JsonResponse({'data': 'ok'}, safe=False)


# --------------------Class Module End ------------------------------------------------


def get_only_class(request):
    class_list = Standard.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    class_ar = []
    for obj in class_list:
        class_dic = {
            'ClassID': obj.pk,
            'Standard': obj.name
        }
        class_ar.append(class_dic)

    return JsonResponse({'data': class_ar}, safe=False)


def get_only_section_of_class(request, id=None):
    class_list = Standard.objects.get(isDeleted__exact=False, pk=int(id), sessionID=get_current_session(request))
    class_ar = []
    try:
        sec_list = Section.objects.filter(isDeleted__exact=False, standardID_id=class_list.pk)
        if sec_list.count() > 0:
            for obj in sec_list:
                sec_dic = {
                    'SectionID': obj.pk,
                    'Section': obj.name
                }
                class_ar.append(sec_dic)
        else:
            sec_dic = {
                'SectionID': '',
                'Section': 'No Section Available'
            }
            class_ar.append(sec_dic)

    except:
        sec_dic = {
            'SectionID': '',
            'Section': 'No Section Available'
        }
        class_ar.append(sec_dic)

    return JsonResponse({'data': class_ar}, safe=False)


# -------------------------------End Class-------------------------------
# -------------------------------Start Student -------------------------------


def post_new_student_detail(request):
    if request.method == 'POST':
        studentByKey = request.POST.get('studentByKey')
        key = request.POST.get('key')
        TfirstName = request.POST.get('TfirstName')
        TmiddleName = request.POST.get('TmiddleName')
        TlastName = request.POST.get('TlastName')
        Temail = request.POST.get('Temail')
        Tphone = request.POST.get('Tphone')
        TbloodGroup = request.POST.get('TbloodGroup')
        Tdob = request.POST.get('Tdob')
        Taadhar = request.POST.get('Taadhar')
        Tgender = request.POST.get('Tgender')

        Taddress = request.POST.get('Taddress')
        Tcity = request.POST.get('Tcity')
        Tstate = request.POST.get('Tstate')
        Tcountry = request.POST.get('Tcountry')
        Tpin = request.POST.get('Tpin')
        TPaddress = request.POST.get('TPaddress')
        TPcity = request.POST.get('TPcity')
        TPstate = request.POST.get('TPstate')
        TPcountry = request.POST.get('TPcountry')
        TPpin = request.POST.get('TPpin')

        stuFatherFirstName = request.POST.get('stuFatherFirstName')
        stuFatherMiddleName = request.POST.get('stuFatherMiddleName')
        stuFatherLastName = request.POST.get('stuFatherLastName')
        stuMotherFirstName = request.POST.get('stuMotherFirstName')
        stuMotherMiddleName = request.POST.get('stuMotherMiddleName')
        stuMotherLastName = request.POST.get('stuMotherLastName')
        stuFatherEmail = request.POST.get('stuFatherEmail')
        stuFatherPhone = request.POST.get('stuFatherPhone')
        stuFatherProfession = request.POST.get('stuFatherProfession')

        stuClass = request.POST.get('stuClass')
        stuSection = request.POST.get('stuSection')
        stuRoll = request.POST.get('stuRoll')
        stuDOJ = request.POST.get('stuDOJ')



        student = StudentDetail()


        try:
            available = StudentDetail.objects.filter(uniqueKey__exact= key).order_by('-id').first()
            student.uniqueKey = available.uniqueKey
            try:
                image = request.FILES['Timage']
                student.photo = image
            except:
                student.photo = available.photo

        except:

            unique_key = get_random_string(length=8, allowed_chars='1234567890')
            while StudentDetail.objects.filter(uniqueKey__exact=unique_key).count() > 0:
                unique_key = get_random_string(length=8, allowed_chars='1234567890')
            else:
                student.uniqueKey = unique_key
                image = request.FILES['Timage']
                student.photo = image



        student.firstName = TfirstName
        student.middleName = TmiddleName
        student.lastName = TlastName
        student.email = Temail
        student.phoneNumber = Tphone
        student.bloodGroup = TbloodGroup
        student.DOB = Tdob
        student.aadhar = Taadhar
        student.gender = Tgender

        student.presentAddress = Taddress
        student.presentCity = Tcity
        student.presentState = Tstate
        student.presentCountry = Tcountry
        student.presentPinCode = Tpin
        student.permanentAddress = TPaddress
        student.permanentCity = TPcity
        student.permanentState = TPstate
        student.permanentCountry = TPcountry
        student.permanentPinCode = TPpin

        student.standardID_id = stuClass
        student.sectionID_id = stuSection
        student.rollNumber = stuRoll
        student.dateOfJoining = stuDOJ

        try:
            parent = ParentDetail.objects.filter(phoneNumber__exact=stuFatherPhone).order_by('-id').first()
            parent.fatherFirstName = stuFatherFirstName
            parent.fatherMiddleName = stuFatherMiddleName
            parent.fatherLastName = stuFatherLastName
            parent.motherFirstName = stuMotherFirstName
            parent.motherMiddleName = stuMotherMiddleName
            parent.motherLastName = stuMotherLastName
            parent.occupation = stuFatherProfession
            parent.phoneNumber = stuFatherPhone
            parent.email = stuFatherEmail
            parent.save()
            student.parentID_id = parent.pk
        except:
            parent = ParentDetail()
            parent.fatherFirstName = stuFatherFirstName
            parent.fatherMiddleName = stuFatherMiddleName
            parent.fatherLastName = stuFatherLastName
            parent.motherFirstName = stuMotherFirstName
            parent.motherMiddleName = stuMotherMiddleName
            parent.motherLastName = stuMotherLastName
            parent.occupation = stuFatherProfession
            parent.phoneNumber = stuFatherPhone
            parent.email = stuFatherEmail
            parent.save()
            student.parentID_id = parent.pk


        username = 'ST' + get_random_string(length=3,
                                            allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
            length=3, allowed_chars='1234567890')
        password = get_random_string(length=10, allowed_chars='1234567890')
        while User.objects.filter(username__exact=username).count() > 0:
            username = 'ST' + get_random_string(length=3,
                                                allowed_chars='ABCDEFGHJKLMNOPQRSTUVWXYZ') + get_random_string(
                length=3, allowed_chars='1234567890')
            password = get_random_string(length=10, allowed_chars='1234567890')
        else:
            user = User()
            user.username = username
            user.set_password(password)
            student.password = password
            student.username = username
            user.save()

        try:
            g = Group.objects.get(name='Student')
            g.user_set.add(user.pk)
            g.save()
        except:
            g = Group()
            g.name = "Student"
            g.save()
            g.user_set.add(user.pk)
            g.save()

        student.userID_id = user.pk
        student.sessionID_id = get_current_session_year()
        student.save()

        return JsonResponse({'response': 'ok'}, safe=False)
        # except:
        #     return JsonResponse({'response': 'error'}, safe=False)


def get_student_list(request):
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    if sectionID == "":
        sectionID = None

    students = StudentDetail.objects.filter(sessionID_id=get_current_session(request), isDeleted__exact=False,
                                            sectionID_id=sectionID, standardID_id=classID)
    student_list = []
    for obj in students:
        parent = ParentDetail.objects.get(pk=obj.parentID_id)
        try:
            section = obj.sectionID.name
        except:
            section = '-'

        student_dic = {
            'StudentID': obj.pk,
            'Name': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Photo': '<img src="{}" class="avatar" alt="Photo">'.format(obj.photo.thumbnail.url),
            'Phone': parent.phoneNumber,
            'Standard': obj.standardID.name,
            'Section': section,
            'Roll': obj.rollNumber,
            'Gender': obj.gender,
            'UniqueKey': obj.uniqueKey,
            'FatherName': parent.fatherFirstName + ' ' + parent.fatherMiddleName + ' ' + parent.fatherLastName,
            'Action': '<a onclick ="getStudentDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editStudentDetail({})" data-toggle="modal" data-target="#myModalStudentEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteStudentDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        student_list.append(student_dic)
    return JsonResponse({'data': student_list}, safe=False)


def get_student_detail(request, id=None):
    query = get_object_or_404(StudentDetail, pk=id)
    if query.isActive == True:
        active = "Yes"
    else:
        active = "No"
    try:
        section = query.sectionID.name
    except:
        section = '-'

    student_dic = {
        'StudentID': query.pk,
        'Name': query.firstName + ' ' + query.middleName + ' ' + query.lastName,
        'DOB': query.DOB,
        'Aadhar': query.aadhar,
        'Gender': query.gender,
        'BloodGroup': query.bloodGroup,
        'PhoneNumber': query.phoneNumber,
        'Email': query.email,
        'PresentAddress': query.presentAddress + ',' + query.presentCity + ',' + query.presentState + ',' + query.presentCountry + '-' + query.presentPinCode,
        'PermanentAddress': query.permanentAddress + ',' + query.permanentCity + ',' + query.permanentState + ',' + query.permanentCountry + '-' + query.permanentPinCode,
        'Standard': query.standardID.name,
        'Section': section,
        'Roll': query.rollNumber,
        'DateOfJoining': query.dateOfJoining,
        'FatherName': query.parentID.fatherFirstName + ' ' + query.parentID.fatherMiddleName + ' ' + query.parentID.fatherLastName,
        'MotherName': query.parentID.motherFirstName + ' ' + query.parentID.motherMiddleName + ' ' + query.parentID.motherLastName,
        'Occupation': query.parentID.occupation,
        'FatherPhone': query.parentID.phoneNumber,
        'FatherEmail': query.parentID.email,
        'Photo': query.photo.url,
        'IsActive': active,
        'UserName': query.username,
        'Password': query.password
    }
    return JsonResponse({'data': student_dic}, safe=False)


def get_student_detail_for_edit(request, id=None):
    query = get_object_or_404(StudentDetail, pk=id)
    if query.isActive == True:
        active = "Yes"
    else:
        active = "No"
    try:
        section = query.sectionID_id
    except:
        section = '-'

    student_dic = {
        'StudentID': query.pk,
        'FirstName': query.firstName,
        'MiddleName': query.middleName,
        'LastName': query.lastName,
        'DOB': query.DOB,
        'Aadhar': query.aadhar,
        'Gender': query.gender,
        'BloodGroup': query.bloodGroup,
        'PhoneNumber': query.phoneNumber,
        'Email': query.email,
        'PresentAddress': query.presentAddress,
        'PresentCity': query.presentCity,
        'PresentState': query.presentState,
        'PresentCountry': query.presentCountry,
        'PresentPin': query.presentPinCode,
        'PermanentAddress': query.permanentAddress,
        'PermanentCity': query.permanentCity,
        'PermanentState': query.permanentState,
        'PermanentCounty': query.permanentCountry,
        'PermanentPin': query.permanentPinCode,
        'StandardID': query.standardID_id,
        'Section': section,
        'Roll': query.rollNumber,
        'DateOfJoining': query.dateOfJoining,
        'FatherFirstName': query.parentID.fatherFirstName,
        'FatherMiddleName': query.parentID.fatherMiddleName,
        'FatherLastName': query.parentID.fatherLastName,
        'MotherFirstName': query.parentID.motherFirstName,
        'MotherMiddleName': query.parentID.motherMiddleName,
        'MotherLastName': query.parentID.motherLastName,
        'Occupation': query.parentID.occupation,
        'FatherPhone': query.parentID.phoneNumber,
        'FatherEmail': query.parentID.email,
        'Photo': query.photo.url,
        'IsActive': active,
        'UserName': query.username,
        'Password': query.password
    }
    return JsonResponse({'data': student_dic}, safe=False)


def edit_student_detail(request):
    if request.method == 'POST':
        TStudentID = request.POST.get('TStudentID')
        TfirstName = request.POST.get('TfirstName')
        TmiddleName = request.POST.get('TmiddleName')
        TlastName = request.POST.get('TlastName')
        Temail = request.POST.get('Temail')
        Tphone = request.POST.get('Tphone')
        TbloodGroup = request.POST.get('TbloodGroup')
        Tdob = request.POST.get('Tdob')
        Taadhar = request.POST.get('Taadhar')
        Tgender = request.POST.get('Tgender')

        Taddress = request.POST.get('Taddress')
        Tcity = request.POST.get('Tcity')
        Tstate = request.POST.get('Tstate')
        Tcountry = request.POST.get('Tcountry')
        Tpin = request.POST.get('Tpin')
        TPaddress = request.POST.get('TPaddress')
        TPcity = request.POST.get('TPcity')
        TPstate = request.POST.get('TPstate')
        TPcountry = request.POST.get('TPcountry')
        TPpin = request.POST.get('TPpin')

        stuFatherFirstName = request.POST.get('stuFatherFirstName')
        stuFatherMiddleName = request.POST.get('stuFatherMiddleName')
        stuFatherLastName = request.POST.get('stuFatherLastName')
        stuMotherFirstName = request.POST.get('stuMotherFirstName')
        stuMotherMiddleName = request.POST.get('stuMotherMiddleName')
        stuMotherLastName = request.POST.get('stuMotherLastName')
        stuFatherEmail = request.POST.get('stuFatherEmail')
        stuFatherPhone = request.POST.get('stuFatherPhone')
        stuFatherProfession = request.POST.get('stuFatherProfession')

        stuClass = request.POST.get('stuClass')
        stuSection = request.POST.get('stuSection')
        stuRoll = request.POST.get('stuRoll')
        stuDOJ = request.POST.get('stuDOJ')

        try:
            student = StudentDetail.objects.get(pk=int(TStudentID))
            student.firstName = TfirstName
            student.middleName = TmiddleName
            student.lastName = TlastName
            student.email = Temail
            student.phoneNumber = Tphone
            student.bloodGroup = TbloodGroup
            student.DOB = Tdob
            student.aadhar = Taadhar
            student.gender = Tgender

            student.presentAddress = Taddress
            student.presentCity = Tcity
            student.presentState = Tstate
            student.presentCountry = Tcountry
            student.presentPinCode = Tpin
            student.permanentAddress = TPaddress
            student.permanentCity = TPcity
            student.permanentState = TPstate
            student.permanentCountry = TPcountry
            student.permanentPinCode = TPpin

            student.standardID_id = stuClass
            student.sectionID_id = stuSection
            student.rollNumber = stuRoll
            student.dateOfJoining = stuDOJ

            parent = ParentDetail.objects.get(pk=student.parentID_id)
            parent.fatherFirstName = stuFatherFirstName
            parent.fatherMiddleName = stuFatherMiddleName
            parent.fatherLastName = stuFatherLastName
            parent.motherFirstName = stuMotherFirstName
            parent.motherMiddleName = stuMotherMiddleName
            parent.motherLastName = stuMotherLastName
            parent.occupation = stuFatherProfession
            parent.phoneNumber = stuFatherPhone
            parent.email = stuFatherEmail
            parent.save()
            student.parentID_id = parent.pk

            # school_data = ComputerOperator.objects.get(userID_id=int(request.user.id))
            # teacher.schoolID_id = school_data.schoolID_id
            student.save()

            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def edit_student_photo(request):
    if request.method == 'POST':
        StudentID = request.POST.get('StudentID')
        image = request.FILES['file']
        try:
            student_data = StudentDetail.objects.get(pk=int(StudentID))
            student_data.photo = image
            student_data.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'ok'})


@csrf_exempt
def delete_student(request):
    if request.method == 'POST':
        deleteID = request.POST.get('deleteID')
        try:

            student = StudentDetail.objects.get(pk=int(deleteID))
            student.isDeleted = True
            student.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)

def get_student_detail_by_unique_key(request):
    if request.method =='POST':
        unique_key = request.POST.get('key')
        try:
            query = StudentDetail.objects.filter(uniqueKey__exact=unique_key).order_by('-id').first()
            if query.isActive == True:
                active = "Yes"
            else:
                active = "No"
            try:
                section = query.sectionID_id
            except:
                section = '-'

            student_dic = {
                'StudentID': query.pk,
                'FirstName': query.firstName,
                'MiddleName': query.middleName,
                'LastName': query.lastName,
                'DOB': query.DOB,
                'Aadhar': query.aadhar,
                'Gender': query.gender,
                'BloodGroup': query.bloodGroup,
                'PhoneNumber': query.phoneNumber,
                'Email': query.email,
                'PresentAddress': query.presentAddress,
                'PresentCity': query.presentCity,
                'PresentState': query.presentState,
                'PresentCountry': query.presentCountry,
                'PresentPin': query.presentPinCode,
                'PermanentAddress': query.permanentAddress,
                'PermanentCity': query.permanentCity,
                'PermanentState': query.permanentState,
                'PermanentCounty': query.permanentCountry,
                'PermanentPin': query.permanentPinCode,
                'StandardID': query.standardID_id,
                'Section': section,
                'Roll': query.rollNumber,
                'DateOfJoining': query.dateOfJoining,
                'FatherFirstName': query.parentID.fatherFirstName,
                'FatherMiddleName': query.parentID.fatherMiddleName,
                'FatherLastName': query.parentID.fatherLastName,
                'MotherFirstName': query.parentID.motherFirstName,
                'MotherMiddleName': query.parentID.motherMiddleName,
                'MotherLastName': query.parentID.motherLastName,
                'Occupation': query.parentID.occupation,
                'FatherPhone': query.parentID.phoneNumber,
                'FatherEmail': query.parentID.email,
                'Photo': query.photo.url,
                'IsActive': active,
                'UserName': query.username,
                'Password': query.password
            }
            return JsonResponse({'data': student_dic, 'response':'ok'}, safe=False)

        except:
            return JsonResponse({'response':'No student detail available by this unique key.'}, safe=False)
# -------------------------------End Student-------------------------------
# -------------------------------start parent-------------------------------


def get_parent_list(request):
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    if sectionID == "":
        sectionID = None

    parents = ParentDetail.objects.filter(isDeleted__exact=False)
    parent_list = []
    for obj in parents:
        students = StudentDetail.objects.filter(parentID__id=obj.pk, isDeleted__exact=False, standardID_id=classID,
                                                sectionID_id=sectionID, sessionID_id=get_current_session(request))
        student_detail = ''
        for stu in students:
            try:
                section = stu.sectionID.name
            except:
                section = '-'

            student_detail = stu.firstName + ' ' + stu.middleName + ' ' + stu.lastName + ' - ' + stu.standardID.name + '-' + section + '- Roll no:' + stu.rollNumber
            "\n".join(student_detail)
        if students.count() > 0:
            parent_dic = {
                'ParentID': obj.pk,
                'FatherName': obj.fatherFirstName + ' ' + obj.fatherMiddleName + ' ' + obj.fatherLastName,
                'MotherName': obj.motherFirstName + ' ' + obj.motherMiddleName + ' ' + obj.motherLastName,
                'Pofession': obj.occupation,
                'Phone': obj.phoneNumber,
                'WardDetail': student_detail,
                'Action': '<a onclick ="getParentDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editParentDetail({})" data-toggle="modal" data-target="#myModalEditParent" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteParentDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(obj.pk), str(obj.pk), str(obj.pk))
            }

            parent_list.append(parent_dic)
    return JsonResponse({'data': parent_list}, safe=False)


def get_parent_detail(request, id=None):
    query = get_object_or_404(ParentDetail, pk=id)

    students = StudentDetail.objects.filter(parentID__id=query.pk, isDeleted__exact=False)
    student_detail = ''
    PresentAddress = ''
    PermanentAddress = ''
    for stu in students:
        try:
            section = stu.sectionID.name
        except:
            section = '-'

        student_detail = stu.firstName + ' ' + stu.middleName + ' ' + stu.lastName + ' - ' + stu.standardID.name + '-' + section + '-Roll no:' + stu.rollNumber
        "\n".join(student_detail)
        PresentAddress = stu.presentAddress + ',' + stu.presentCity + ',' + stu.presentState + ',' + stu.presentCountry + '-' + stu.presentPinCode
        PermanentAddress = stu.permanentAddress + ',' + stu.permanentCity + ',' + stu.permanentState + ',' + stu.permanentCountry + '-' + stu.permanentPinCode,

    student_dic = {
        'ParentID': query.pk,
        'FatherName': query.fatherFirstName + ' ' + query.fatherMiddleName + ' ' + query.fatherLastName,
        'MotherName': query.motherFirstName + ' ' + query.motherMiddleName + ' ' + query.motherLastName,
        'Profession': query.occupation,
        'Phone': query.phoneNumber,
        'Email': query.email,
        'PresentAddress': PresentAddress,
        'PermanentAddress': PermanentAddress,
        'WardDetail': student_detail,

    }
    return JsonResponse({'data': student_dic}, safe=False)


def get_parent_detail_for_edit(request, id=None):
    query = get_object_or_404(ParentDetail, pk=id)
    student_dic = {
        'ParentID': query.pk,
        'FatherFirstName': query.fatherFirstName,
        'FatherMiddleName': query.fatherMiddleName,
        'FatherLastName': query.fatherLastName,
        'MotherFirstName': query.motherFirstName,
        'MotherMiddleName': query.motherMiddleName,
        'MotherLastName': query.motherLastName,
        'Profession': query.occupation,
        'Phone': query.phoneNumber,
        'Email': query.email,

    }
    return JsonResponse({'data': student_dic}, safe=False)


def edit_parent_detail(request):
    if request.method == 'POST':
        eParentID = request.POST.get('eParentID')
        ePhoneNumber = request.POST.get('ePhoneNumber')
        eEmail = request.POST.get('eEmail')
        eFatherFirstName = request.POST.get('eFatherFirstName')
        eFatherMiddleName = request.POST.get('eFatherMiddleName')
        eFatherLastName = request.POST.get('eFatherLastName')
        eMotherFirstName = request.POST.get('eMotherFirstName')
        eMotherMiddleName = request.POST.get('eMotherMiddleName')
        eMotherLastName = request.POST.get('eMotherLastName')
        eProfession = request.POST.get('eProfession')

        try:
            parent = ParentDetail.objects.get(pk=int(eParentID))
            parent.phoneNumber = ePhoneNumber
            parent.email = eEmail
            parent.fatherFirstName = eFatherFirstName
            parent.fatherMiddleName = eFatherMiddleName
            parent.fatherLastName = eFatherLastName
            parent.motherFirstName = eMotherFirstName
            parent.motherMiddleName = eMotherMiddleName
            parent.motherLastName = eMotherLastName
            parent.occupation = eProfession
            parent.save()

            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_parent_detail(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        parent = ParentDetail.objects.get(pk=int(id))
        parent.isDeleted = True
        parent.save()

        return JsonResponse({'data': 'ok'}, safe=False)


# -------------------------------end parent-------------------------------
# -------------------------------Add Subject -------------------------------


def add_subject(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        add_sub = Subject()
        add_sub.subjectName = subject
        add_sub.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_subject_list(request):
    subjects = Subject.objects.filter(isDeleted__exact=False)
    subject_list = []
    for obj in subjects:
        subject_dic = {
            'SubjectID': obj.pk,
            'Subject': obj.subjectName,
            'SubjectSelect': '<input type="checkbox" id="{}" class="flat">'.format(str(obj.pk)),
            'Action': '<a onclick ="editSubjectDetail({})" data-toggle="modal" data-target="#myModalEditSubject" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditSubject"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteSubjectDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk))
        }

        subject_list.append(subject_dic)
    return JsonResponse({'data': subject_list}, safe=False)


def get_subject_detail(request, id=None):
    query = get_object_or_404(Subject, pk=id)

    subject_dic = {
        'SubjectID': query.pk,
        'SubjectName': query.subjectName,

    }
    return JsonResponse({'data': subject_dic}, safe=False)


def update_subject(request):
    if request.method == 'POST':
        EditSubjectName = request.POST.get('EditSubjectName')
        SubjectIDEdit = request.POST.get('SubjectIDEdit')
        has_subject = Subject.objects.filter(subjectName__iexact=EditSubjectName, isDeleted__exact=False).exclude(
            pk=int(SubjectIDEdit))

        if has_subject.count() > 0:
            return JsonResponse({'response': 'Subject name already exist. Please try again.'}, safe=False)
        else:
            add_sub = Subject.objects.get(pk=int(SubjectIDEdit))
            add_sub.subjectName = EditSubjectName
            add_sub.save()

            return JsonResponse({'response': 'ok'}, safe=False)


@csrf_exempt
def delete_subject(request):
    if request.method == 'POST':
        subjectID = request.POST.get('subjectID')
        try:

            sub = Subject.objects.get(pk=int(subjectID))
            sub.isDeleted = True
            sub.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_class_assigned_subject(request):
    if request.method == 'POST':
        subjectID = request.POST.get('subjectID')
        try:

            sub = AssignClassSubject.objects.get(pk=int(subjectID))
            sub.isDeleted = True
            sub.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def assign_subjects_to_class(request):
    if request.method == 'POST':
        sub_data = request.POST.get('sub_data')
        classID = request.POST.get('classID')
        for i in str(sub_data).split(','):
            try:
                sub_in_class = AssignClassSubject.objects.get(subjectID_id=int(i), classID_id=int(classID),
                                                              isDeleted__exact=False, sessionID=get_current_session(request))
            except:
                if int(get_current_session_year()) == int(get_current_session(request)):
                    assign_sub = AssignClassSubject()
                    assign_sub.classID_id = int(classID)
                    assign_sub.subjectID_id = int(i)
                    assign_sub.sessionID_id = get_current_session_year()
                    assign_sub.save()
                else:
                    pass
        return JsonResponse({'response': 'ok'}, safe=False)


def get_subject_list_with_class(request, id=None):
    query = AssignClassSubject.objects.filter(classID_id=int(id), isDeleted__exact=False, sessionID=get_current_session(request))
    subject_list = []
    for obj in query:
        subject_dic = {
            'ID': obj.pk,
            'SubjectID': obj.subjectID_id,
            'SubjectName': obj.subjectID.subjectName,

        }
        subject_list.append(subject_dic)
    return JsonResponse({'data': subject_list}, safe=False)


def assign_subjects_to_class_to_teacher(request):
    if request.method == 'POST':
        classID = request.POST.get('classID')
        sectionID = request.POST.get('sectionID')
        subjectID = request.POST.get('subjectID')
        teacherID = request.POST.get('teacherID')


        try:
            if sectionID == "":
                assign = AssignSubjectToTeacher.objects.get(classID_id=classID,
                                                            sessionID_id=get_current_session_year(),
                                                            subjectID_id=subjectID)
            else:
                assign = AssignSubjectToTeacher.objects.get(sectionID=sectionID, classID_id=classID,
                                                            sessionID_id=get_current_session_year(),
                                                            subjectID_id=subjectID)
            assign.teacherID_id = int(teacherID)
            if int(get_current_session_year()) == int(get_current_session(request)):
                assign.sessionID_id = get_current_session_year()
                assign.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Please select the current session to assign teacher.'}, safe=False)


        except:
            assign = AssignSubjectToTeacher()
            assign.classID_id = int(classID)
            assign.subjectID_id = int(subjectID)
            assign.teacherID_id = int(teacherID)

            if sectionID == "":
                assign.sectionID_id = ''
            else:
                assign.sectionID_id = int(sectionID)
            if int(get_current_session_year()) == int(get_current_session(request)):
                assign.sessionID_id = get_current_session_year()
                assign.save()

                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Please select the current session to assign teacher.'}, safe=False)


def get_assign_subjects_to_class_to_teacher_list(request):
    try:
        assigned_sub = AssignSubjectToTeacher.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
        assigned_sub_list = []
        for obj in assigned_sub:
            try:
                section = obj.sectionID.name
            except:
                section = '-'

            student_dic = {
                'ID': obj.pk,
                'Subject': obj.subjectID.subjectID.subjectName,
                'Standard': obj.classID.name,
                'Section': section,
                'Teacher': obj.teacherID.firstName + " " + obj.teacherID.middleName + " " + obj.teacherID.lastName,
                'Action': ' <a onclick ="editAssignDetail({})" data-toggle="modal" data-target="#myModalAssignEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(obj.pk), str(obj.pk))
            }

            assigned_sub_list.append(student_dic)
        return JsonResponse({'data': assigned_sub_list}, safe=False)
    except:
        return JsonResponse({'data': []}, safe=False)


def get_assign_subjects_to_class_to_teacher_detail(request, id=None):
    query = get_object_or_404(AssignSubjectToTeacher, pk=id)
    try:
        section = query.sectionID.name
    except:
        section = 'No Section Available'
    assign_dic = {
        'ID': query.pk,
        'Standard': query.classID.name,
        'StandardID': str(query.classID_id),
        'Section': section,
        'TeacherID': query.teacherID_id,
        'SubjectID': query.subjectID_id

    }
    return JsonResponse({'data': assign_dic}, safe=False)


def update_assign_subjects_to_class_to_teacher(request):
    if request.method == 'POST':
        eID = request.POST.get('eID')
        subjectID = request.POST.get('subjectID')
        teacherID = request.POST.get('teacherID')
        assign = AssignSubjectToTeacher.objects.get(pk=int(eID))
        assign.subjectID_id = int(subjectID)
        assign.teacherID_id = int(teacherID)
        assign.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_student_list_by_class_section_no_subject_by_date(request):
    date = request.GET.get('date')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')

    if sectionID == "":
        sectionID = None
    student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(request))

    for obj in student_list:
        try:
            StudentAttendance.objects.get(studentID_id=obj.pk, standardID_id=classID, sectionID_id=sectionID,
                                          attendanceDate__icontains=date, subjectID=None)
        except:
            if int(get_current_session_year()) == int(get_current_session(request)):
                stu = StudentAttendance()
                stu.sectionID_id = sectionID
                stu.studentID_id = obj.pk
                stu.standardID_id = classID
                stu.attendanceDate = date
                stu.sessionID_id = get_current_session(request)
                stu.save()
            else:
                pass
    at_least = StudentAttendance.objects.filter(standardID_id=classID, sectionID_id=sectionID,
                                                attendanceDate__icontains=date, subjectID=None, sessionID=get_current_session(request))

    assigned_sub_list = []
    for obj_s in at_least:
        # try:
        #     section = obj_s.sectionID.name
        # except:
        #     section = '-'
        if obj_s.isAbsent == True:
            present = '<label><input  type="checkbox" class="js-switch" checked id="{}"/></label>'.format(
                'a' + str(obj_s.pk)),
        else:
            present = '<label><input  type="checkbox" class="js-switch" id="{}"/></label>'.format('a' + str(obj_s.pk)),

        student_dic = {
            'ID': obj_s.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.studentID.photo.thumbnail.url),
            'StudentName': obj_s.studentID.firstName + ' ' + obj_s.studentID.middleName + ' ' + obj_s.studentID.lastName,
            'Roll': obj_s.studentID.rollNumber,
            'Attendance': present,
            'Reason': '<div class=" form-group has-feedback"><input type="text" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                obj_s.reason, obj_s.pk),

            'Action': '<button type="button" class="btn btn-success" onclick="submitData({},{})">Submit</button>'.format(
                obj_s.pk, obj_s.pk)
        }

        assigned_sub_list.append(student_dic)
    return JsonResponse({'data': assigned_sub_list}, safe=False)


@csrf_exempt
def student_attendance_without_subject(request):
    if request.method == 'POST':
        attID = request.POST.get('attID')
        reason = request.POST.get('reason')
        atten = request.POST.get('atten')
        atten_stu = StudentAttendance.objects.get(pk=int(attID))
        atten_stu.reason = reason
        if atten == 'false':
            atten_stu.isAbsent = False
        if atten == 'true':
            atten_stu.isAbsent = True
        atten_stu.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_student_list_by_class_section_subject_by_date(request):
    date = request.GET.get('date')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    subjectID = request.GET.get('subjectID')

    if sectionID == "":
        sectionID = None
    student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(request))

    for obj in student_list:
        try:
            StudentAttendance.objects.get(studentID_id=obj.pk, standardID_id=classID, sectionID_id=sectionID,
                                          attendanceDate__icontains=date, subjectID_id=subjectID, sessionID=get_current_session(request))
        except:
            if int(get_current_session_year()) == int(get_current_session(request)):
                stu = StudentAttendance()
                stu.sectionID_id = sectionID
                stu.studentID_id = obj.pk
                stu.standardID_id = classID
                stu.subjectID_id = subjectID
                stu.attendanceDate = date
                stu.sessionID_id = get_current_session_year()
                stu.save()
            else:
                pass
    at_least = StudentAttendance.objects.filter(standardID_id=classID, sectionID_id=sectionID,
                                                attendanceDate__icontains=date, subjectID_id=subjectID, sessionID=get_current_session(request))

    assigned_sub_list = []
    for obj_s in at_least:
        # try:
        #     section = obj_s.sectionID.name
        # except:
        #     section = '-'
        if obj_s.isAbsent == True:
            present = '<label><input  type="checkbox" class="js-switch" checked id="{}"/></label>'.format(
                'a' + str(obj_s.pk)),
        else:
            present = '<label><input  type="checkbox" class="js-switch" id="{}"/></label>'.format('a' + str(obj_s.pk)),

        student_dic = {
            'ID': obj_s.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.studentID.photo.thumbnail.url),
            'StudentName': obj_s.studentID.firstName + ' ' + obj_s.studentID.middleName + ' ' + obj_s.studentID.lastName,
            'Roll': obj_s.studentID.rollNumber,
            'Attendance': present,
            'Reason': '<div class=" form-group has-feedback"><input type="text" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                obj_s.reason, obj_s.pk),

            'Action': '<button type="button" class="btn btn-success" onclick="submitData({},{})">Submit</button>'.format(
                obj_s.pk, obj_s.pk)
        }

        assigned_sub_list.append(student_dic)
    return JsonResponse({'data': assigned_sub_list}, safe=False)


@csrf_exempt
def student_attendance_with_subject(request):
    if request.method == 'POST':
        attID = request.POST.get('attID')
        reason = request.POST.get('reason')
        atten = request.POST.get('atten')
        subjectID = request.POST.get('subjectID')
        atten_stu = StudentAttendance.objects.get(pk=int(attID))
        atten_stu.reason = reason
        if atten == 'false':
            atten_stu.isAbsent = False
            atten_stu.subjectID_id = int(subjectID)
        if atten == 'true':
            atten_stu.isAbsent = True
            atten_stu.subjectID_id = int(subjectID)
        atten_stu.save()

        return JsonResponse({'response': 'ok'}, safe=False)


# ------------------ student attendance list--------------------------


def get_student_attendance_list_by_date_range(request):
    StartDate = request.GET.get('StartDate')
    EndDate = request.GET.get('EndDate')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    subjectID = request.GET.get('subjectID')
    student_list_data = []
    if sectionID == "":
        sectionID = None
    if subjectID == "":
        subjectID = None
    student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(request))

    for obj in student_list:
        present = StudentAttendance.objects.filter(studentID_id=obj.pk, isAbsent__exact=True, standardID_id=classID,
                                                   sectionID_id=sectionID,
                                                   attendanceDate__lte=EndDate, attendanceDate__gte=StartDate,
                                                   subjectID_id=subjectID,sessionID=get_current_session(request)).count()

        absent = StudentAttendance.objects.filter(studentID_id=obj.pk, isAbsent__exact=False, standardID_id=classID,
                                                  sectionID_id=sectionID,
                                                  attendanceDate__lte=EndDate, attendanceDate__gte=StartDate,
                                                  subjectID_id=subjectID ,sessionID=get_current_session(request)).count()

        if present == 0 and absent == 0:
            percent = 0
        else:
            percent = (float(present) / (float(present) + float(absent))) * 100

        student_dic = {
            'ID': obj.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj.photo.thumbnail.url),
            'StudentName': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Roll': obj.rollNumber,
            'Present': str(present) + '/' + str(present + absent),
            'Absent': absent,
            'Percentage': percent

        }

        student_list_data.append(student_dic)
    return JsonResponse({'data': student_list_data}, safe=False)


def get_student_list_with_class_and_section(request):
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    if sectionID == '':
        sectionID = None
    else:
        sectionID = int(sectionID)

    students = StudentDetail.objects.filter(isDeleted__exact=False, standardID_id=int(classID), sectionID_id=sectionID,sessionID=get_current_session(request))
    student_list = []
    for obj in students:
        student_dic = {
            'StudentID': obj.pk,
            'Name': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Roll': obj.rollNumber,
        }

        student_list.append(student_dic)
    return JsonResponse({'data': student_list}, safe=False)


def get_student_attendance_list_by_student(request):
    StartDate = request.GET.get('StartDate')
    EndDate = request.GET.get('EndDate')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    subjectID = request.GET.get('subjectID')
    StudentID = request.GET.get('StudentID')
    student_list_data = []
    if sectionID == "":
        sectionID = None
    if subjectID == "":
        subjectID = None
    stu = StudentDetail.objects.get(pk=int(StudentID))

    att = StudentAttendance.objects.filter(studentID_id=stu.pk, standardID_id=classID,
                                           sectionID_id=sectionID,
                                           attendanceDate__lte=EndDate,
                                           attendanceDate__gte=StartDate,
                                           subjectID_id=subjectID,sessionID=get_current_session(request)).order_by('attendanceDate')
    for obj in att:
        if obj.isAbsent == False:
            present = "No"
            absent = "Yes"
        else:
            present = "Yes"
            absent = "No"
        student_dic = {
            'ID': obj.pk,
            'Date': obj.attendanceDate.date(),
            'Present': present,
            'Absent': absent,
            'Reason': obj.reason,

        }

        student_list_data.append(student_dic)
    return JsonResponse({'data': student_list_data}, safe=False)


def get_teacher_attendance_list_by_date(request):
    date = request.GET.get('date')

    teacher_list = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True)

    for obj in teacher_list:
        try:
            TeacherAttendance.objects.get(teacherID_id=obj.pk,
                                          attendanceDate__icontains=date, sessionID=get_current_session(request))
        except:
            if int(get_current_session_year()) == int(get_current_session(request)):
                tea = TeacherAttendance()
                tea.teacherID_id = obj.pk
                tea.attendanceDate = date
                tea.sessionID_id = get_current_session_year()
                tea.save()
            else:
                pass
    at_least = TeacherAttendance.objects.filter(attendanceDate__icontains=date, sessionID=get_current_session(request))

    assigned_tea_list = []
    for obj_s in at_least:
        if obj_s.isAbsent == True:
            present = '<label><input  type="checkbox" class="js-switch" checked id="{}"/></label>'.format(
                'a' + str(obj_s.pk)),
        else:
            present = '<label><input  type="checkbox" class="js-switch" id="{}"/></label>'.format('a' + str(obj_s.pk)),

        teacher_dic = {
            'ID': obj_s.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.teacherID.photo.thumbnail.url),
            'TeacherName': obj_s.teacherID.firstName + ' ' + obj_s.teacherID.middleName + ' ' + obj_s.teacherID.lastName,
            'Attendance': present,
            'Reason': '<div class=" form-group has-feedback"><input type="text" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                obj_s.reason, obj_s.pk),

            'Action': '<button type="button" class="btn btn-success" onclick="submitData({},{})">Submit</button>'.format(
                obj_s.pk, obj_s.pk)
        }

        assigned_tea_list.append(teacher_dic)
    return JsonResponse({'data': assigned_tea_list}, safe=False)


@csrf_exempt
def add_teacher_attendance_by_date(request):
    if request.method == 'POST':
        attID = request.POST.get('attID')
        reason = request.POST.get('reason')
        atten = request.POST.get('atten')
        atten_stu = TeacherAttendance.objects.get(pk=int(attID))
        atten_stu.reason = reason
        if atten == 'false':
            atten_stu.isAbsent = False
        if atten == 'true':
            atten_stu.isAbsent = True
        atten_stu.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_teacher_attendance_list_by_date_range(request):
    StartDate = request.GET.get('StartDate')
    EndDate = request.GET.get('EndDate')

    teacher_list_data = []

    teacher_list = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True)

    for obj in teacher_list:
        present = TeacherAttendance.objects.filter(teacherID_id=obj.pk, isAbsent__exact=True,
                                                   attendanceDate__lte=EndDate, attendanceDate__gte=StartDate,
                                                   sessionID=get_current_session(request)).count()

        absent = TeacherAttendance.objects.filter(teacherID_id=obj.pk, isAbsent__exact=False,
                                                  attendanceDate__lte=EndDate, attendanceDate__gte=StartDate,
                                                  sessionID=get_current_session(request)).count()

        if present == 0 and absent == 0:
            percent = 0
        else:
            percent = (float(present) / (float(present) + float(absent))) * 100

        teacher_dic = {
            'ID': obj.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj.photo.thumbnail.url),
            'TeacherName': obj.firstName + ' ' + obj.middleName + ' ' + obj.lastName,
            'Present': str(present) + '/' + str(present + absent),
            'Absent': absent,
            'Percentage': percent

        }

        teacher_list_data.append(teacher_dic)
    return JsonResponse({'data': teacher_list_data}, safe=False)


def get_teacher_attendance_list_by_teacher(request):
    StartDate = request.GET.get('StartDate')
    EndDate = request.GET.get('EndDate')
    TeacherID = request.GET.get('TeacherID')
    teacher_list_data = []
    tea = TeacherDetail.objects.get(pk=int(TeacherID))

    att = TeacherAttendance.objects.filter(teacherID_id=tea.pk, attendanceDate__lte=EndDate,
                                           attendanceDate__gte=StartDate,sessionID=get_current_session(request) ).order_by('attendanceDate')
    for obj in att:
        if obj.isAbsent == False:
            present = "No"
            absent = "Yes"
        else:
            present = "Yes"
            absent = "No"
        teacher_dic = {
            'ID': obj.pk,
            'Date': obj.attendanceDate.date(),
            'Present': present,
            'Absent': absent,
            'Reason': obj.reason,

        }

        teacher_list_data.append(teacher_dic)
    return JsonResponse({'data': teacher_list_data}, safe=False)


# --------------------- Fee------------------------------------

def get_student_fee(request):
    studentID = request.GET.get('studentID')
    month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'
                  , 'September', 'October', 'November', 'December',)

    fee_list = []
    fees = StudentFee.objects.filter(studentID_id=int(studentID), isDeleted__exact=False, sessionID=get_current_session(request))
    if fees.count() == 0:
        for month in month_list:
            if int(get_current_session_year()) == int(get_current_session(request)):

                s_fee = StudentFee()
                s_fee.studentID_id = int(studentID)
                s_fee.month = month
                s_fee.sessionID_id = get_current_session_year()
                s_fee.save()
            else:
                pass
    for obj in fees:
        if obj.isPaid == True:
            paid = '<label><input  type="checkbox" class="js-switch" checked id="{}"/></label>'.format(
                'a' + str(obj.pk)),
        else:
            paid = '<label><input  type="checkbox" class="js-switch" id="{}"/></label>'.format('a' + str(obj.pk)),
        if obj.payDate is None:
            payDate = 'N/A'
        else:
            payDate = obj.payDate
        fee_dic = {
            'ID': obj.pk,
            'Month': obj.month,
            'IsPaid': paid,
            'PaidDate': payDate,
            'Remark': '<div class=" form-group has-feedback"><input type="text" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                obj.note, obj.pk),

            'Action': '<button type="button" class="btn btn-success" onclick="submitData({},{})">Submit</button>'.format(
                obj.pk, obj.pk)
        }
        fee_list.append(fee_dic)

    return JsonResponse({'data': fee_list}, safe=False)


@csrf_exempt
def add_fee_for_student(request):
    if request.method == 'POST':
        feeID = request.POST.get('feeID')
        reason = request.POST.get('reason')
        isPaid = request.POST.get('isPaid')
        fee_stu = StudentFee.objects.get(pk=int(feeID))
        fee_stu.note = reason

        if isPaid == 'false':
            fee_stu.isPaid = False
            fee_stu.payDate = None
        if isPaid == 'true':
            fee_stu.isPaid = True
            fee_stu.payDate = datetime.datetime.today().date()
        fee_stu.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_class_wise_student_fee(request):
    StandardID = request.GET.get('StandardID')
    SectionID = request.GET.get('SectionID')
    jan = ''
    feb = ''
    mar = ''
    apr = ''
    may = ''
    jun = ''
    jul = ''
    aug = ''
    sep = ''
    oct = ''
    nov = ''
    dec = ''
    if SectionID == "":
        SectionID = None
    else:
        SectionID = int(SectionID)

    students = StudentDetail.objects.filter(standardID_id=int(StandardID), sectionID_id=SectionID, sessionID=get_current_session(request))
    month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'
                  , 'September', 'October', 'November', 'December',)
    fee_list = []
    for stu in students:

        fees = StudentFee.objects.filter(studentID_id=int(stu.pk), sessionID=get_current_session(request))
        if fees.count() == 0:
            for month in month_list:
                if int(get_current_session_year()) == int(get_current_session(request)):

                    s_fee = StudentFee()
                    s_fee.studentID_id = int(stu.pk)
                    s_fee.month = month
                    s_fee.sessionID_id = get_current_session_year()
                    s_fee.save()
                else:
                    pass

        for obj in fees:
            if obj.month == 'January':
                if obj.isPaid == True:
                    jan = 'Paid'
                else:
                    jan = 'Due'
            if obj.month == 'February':
                if obj.isPaid == True:
                    feb = 'Paid'
                else:
                    feb = 'Due'
            if obj.month == 'March':
                if obj.isPaid == True:
                    mar = 'Paid'
                else:
                    mar = 'Due'
            if obj.month == 'April':
                if obj.isPaid == True:
                    apr = 'Paid'
                else:
                    apr = 'Due'
            if obj.month == 'May':
                if obj.isPaid == True:
                    may = 'Paid'
                else:
                    may = 'Due'
            if obj.month == 'June':
                if obj.isPaid == True:
                    jun = 'Paid'
                else:
                    jun = 'Due'
            if obj.month == 'July':
                if obj.isPaid == True:
                    jul = 'Paid'
                else:
                    jul = 'Due'
            if obj.month == 'August':
                if obj.isPaid == True:
                    aug = 'Paid'
                else:
                    aug = 'Due'
            if obj.month == 'September':
                if obj.isPaid == True:
                    sep = 'Paid'
                else:
                    sep = 'Due'
            if obj.month == 'October':
                if obj.isPaid == True:
                    oct = 'Paid'
                else:
                    oct = 'Due'
            if obj.month == 'November':
                if obj.isPaid == True:
                    nov = 'Paid'
                else:
                    nov = 'Due'
            if obj.month == 'December':
                if obj.isPaid == True:
                    dec = 'Paid'
                else:
                    dec = 'Due'

        stu_dic = {
            'ID': stu.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(stu.photo.thumbnail.url),
            'StudentName': stu.firstName + ' ' + stu.middleName + ' ' + stu.lastName,
            'Roll': stu.rollNumber,
            'jan': jan,
            'feb': feb,
            'mar': mar,
            'apr': apr,
            'may': may,
            'jun': jun,
            'jul': jul,
            'aug': aug,
            'sep': sep,
            'oct': oct,
            'nov': nov,
            'dec': dec,

        }
        fee_list.append(stu_dic)

    return JsonResponse({'data': fee_list}, safe=False)


def get_student_fee_detail(request):
    studentID = request.GET.get('studentID')
    month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'
                  , 'September', 'October', 'November', 'December',)

    fee_list = []
    fees = StudentFee.objects.filter(studentID_id=int(studentID), sessionID=get_current_session(request))
    if fees.count() == 0:
        for month in month_list:
            if int(get_current_session_year()) == int(get_current_session(request)):
                s_fee = StudentFee()
                s_fee.studentID_id = int(studentID)
                s_fee.month = month
                s_fee.sessionID_id = get_current_session_year()
                s_fee.save()
            else:
                pass
    for obj in fees:
        if obj.isPaid == True:
            paid = 'Paid'
        else:
            paid = 'Due'
        if obj.payDate is None:
            payDate = 'N/A'
        else:
            payDate = obj.payDate
        fee_dic = {
            'ID': obj.pk,
            'Month': obj.month,
            'IsPaid': paid,
            'PaidDate': payDate,
            'Remark': obj.note,
        }
        fee_list.append(fee_dic)

    return JsonResponse({'data': fee_list}, safe=False)


# ---------------------------Exam -----------------------------
@csrf_exempt
def add_exam(request):
    if request.method == 'POST':
        exam = request.POST.get('exam')

        try:
            try:
                ex = ExamList.objects.get(examName__iexact=exam)
                return JsonResponse({'response': 'Exam Name Already Exist.'}, safe=False)
            except:
                ex = ExamList()
                ex.examName = exam
                ex.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_exam_list(request):
    exams = ExamList.objects.filter(isDeleted__exact=False)
    exam_list = []
    i = 1
    for obj in exams:
        exam_dic = {
            'ID': obj.pk,
            'Count': i,
            'ExamName': obj.examName,
            'Action': ' <a onclick ="editExamDetail({},\'{}\')" data-toggle="modal" data-target="#myModalAssignEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.examName), str(obj.pk))
        }
        i = i + 1

        exam_list.append(exam_dic)
    return JsonResponse({'data': exam_list}, safe=False)


def edit_exam(request):
    if request.method == 'POST':
        exam = request.POST.get('exam')
        examID = request.POST.get('examID')

        try:
            try:
                ex = ExamList.objects.get(examName__iexact=exam)
                return JsonResponse({'response': 'Exam Name Already Exist.'}, safe=False)
            except:
                ex = ExamList.objects.get(pk=int(examID))
                ex.examName = exam
                ex.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def delete_exam(request):
    if request.method == 'POST':
        examID = request.POST.get('examID')
        try:
            ex = ExamList.objects.get(pk=int(examID))
            ex.isDeleted = True
            ex.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def assign_exam(request):
    if request.method == 'POST':
        standard = request.POST.get('standard')
        fullMark = request.POST.get('fullMark')
        passMark = request.POST.get('passMark')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        examList = request.POST.get('examList')
        try:
            for cls in str(standard).split(','):
                try:
                    exam = Exam.objects.get(classID_id=int(cls), isDeleted__exact=False, sessionID=get_current_session(request))

                except:
                    if int(get_current_session_year()) == int(get_current_session(request)):
                        exam = Exam()
                        exam.classID_id = int(cls)
                        exam.fullMark = fullMark
                        exam.passMark = passMark
                        exam.startExamDate = startDate
                        exam.endExamDate = endDate
                        exam.examID_id = int(examList)
                        exam.sessionID_id = get_current_session_year()
                        exam.save()

                    else:
                        pass

            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_assign_exam_list(request):
    # try:
        exams = Exam.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
        exam_list = []
        i = 1
        for obj in exams:
            exam_dic = {
                'ID': obj.pk,
                'Count': i,
                'ExamName': obj.examID.examName,
                'Standard': obj.classID.name,
                'StartDate': obj.startExamDate,
                'PassMark': obj.passMark,
                'FullMark': obj.fullMark,
                'EndDate': obj.endExamDate,
                'Action': ' <a onclick ="editExamDetail({},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')" data-toggle="modal" data-target="#myModalAssignEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(obj.pk), str(obj.examID.examName), obj.examID_id, obj.startExamDate, obj.endExamDate, obj.fullMark,
                    obj.passMark, str(obj.pk))
            }
            i = i + 1

            exam_list.append(exam_dic)
        return JsonResponse({'data': exam_list}, safe=False)
    # except:
    #     return JsonResponse({'data': []}, safe=False)

def update_assign_exam(request):
    if request.method == 'POST':
        EditID = request.POST.get('EditID')
        fullMark = request.POST.get('fullMark')
        passMark = request.POST.get('passMark')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        examList = request.POST.get('examList')
        try:

            exam = Exam.objects.get(pk=int(EditID))
            exam.fullMark = fullMark
            exam.passMark = passMark
            exam.startExamDate = startDate
            exam.endExamDate = endDate
            exam.examID_id = int(examList)
            exam.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def delete_assign_exam(request):
    if request.method == 'POST':
        examID = request.POST.get('examID')
        try:

            exam = Exam.objects.get(pk=int(examID))
            exam.isDeleted = True
            exam.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


# ----------------------------Marks----------------------------------------

def get_assign_exam_list_by_class(request, id=None):
    exam_list = []
    exams = Exam.objects.filter(isDeleted__exact=False, classID_id=int(id), sessionID=get_current_session(request))
    if exams.count() > 0:
        for obj in exams:
            exam_dic = {
                'ID': obj.pk,
                'ExamName': obj.examID.examName,
            }
            exam_list.append(exam_dic)

    else:
        exam_dic = {
            'ID': '',
            'ExamName': 'No Exam Available'
        }
        exam_list.append(exam_dic)
    return JsonResponse({'data': exam_list}, safe=False)


def get_student_list_by_class_section_subject_by_exam_for_marks(request):
    examID = request.GET.get('examID')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    subjectID = request.GET.get('subjectID')
    if sectionID == "":
        sectionID = None
    student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(request))

    for obj in student_list:
        try:
            MarkOfStudentsByExam.objects.get(studentID_id=obj.pk, standardID_id=classID, sectionID_id=sectionID,
                                             examID_id=examID, subjectID_id=subjectID, sessionID=get_current_session(request))
        except:
            if int(get_current_session_year()) == int(get_current_session(request)):

                stu = MarkOfStudentsByExam()
                if sectionID != None:
                    stu.sectionID_id = int(sectionID)
                stu.studentID_id = obj.pk
                stu.standardID_id = int(classID)
                stu.subjectID_id = int(subjectID)
                stu.examID_id = int(examID)
                stu.mark = '0'
                stu.sessionID_id = get_current_session_year()
                stu.save()
            else:
                pass
    at_least = MarkOfStudentsByExam.objects.filter(standardID_id=classID, sectionID_id=sectionID,
                                                   examID_id=examID, subjectID_id=subjectID, sessionID=get_current_session(request))

    assigned_sub_list = []
    for obj_s in at_least:
        student_dic = {
            'ID': obj_s.pk,
            'Image': '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.studentID.photo.thumbnail.url),
            'StudentName': obj_s.studentID.firstName + ' ' + obj_s.studentID.middleName + ' ' + obj_s.studentID.lastName,
            'Roll': obj_s.studentID.rollNumber,
            'FullMark': obj_s.examID.fullMark,
            'PassMark': obj_s.examID.passMark,
            'MarkObtain': '<div class=" form-group has-feedback"><input type="number" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                obj_s.mark, obj_s.pk),

            'Action': '<button type="button" class="btn btn-success" onclick="submitData({})">Submit</button>'.format(
                obj_s.pk)
        }

        assigned_sub_list.append(student_dic)
    return JsonResponse({'data': assigned_sub_list}, safe=False)


@csrf_exempt
def add_mark_of_student(request):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        mark = request.POST.get('mark')
        add_mark = MarkOfStudentsByExam.objects.get(pk=int(ID))
        add_mark.mark = mark

        add_mark.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_student_marks_by_class(request):
    examID = request.GET.get('examID')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    subjects = AssignClassSubject.objects.filter(classID_id=int(classID), isDeleted__exact=False, sessionID=get_current_session(request)).order_by('id')
    subjects_list = []
    for subs in subjects:
        subjects_list.append(subs.pk)
    if sectionID == "":
        sectionID = None
    student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(request))

    for obj in student_list:
        for sub in subjects:
            try:
                MarkOfStudentsByExam.objects.get(studentID_id=obj.pk, standardID_id=classID,
                                                 sectionID_id=sectionID,
                                                 examID_id=examID, subjectID_id=sub.pk, sessionID=get_current_session(request))
            except:
                if int(get_current_session_year()) == int(get_current_session(request)):

                    stu = MarkOfStudentsByExam()
                    stu.sectionID_id = sectionID
                    stu.studentID_id = obj.pk
                    stu.standardID_id = int(classID)
                    stu.subjectID_id = int(sub.pk)
                    stu.examID_id = int(examID)
                    stu.mark = '0'
                    stu.sessionID_id = get_current_session_year()
                    stu.save()
                else:
                    pass
    assigned_sub_list = []
    for obj_s in student_list:
        student_marks_list = [
            obj_s.pk,
            '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.photo.thumbnail.url),
            obj_s.firstName + ' ' + obj_s.middleName + ' ' + obj_s.lastName,
            obj_s.rollNumber,
        ]

        for s_mark in tuple(subjects_list):
            marks = MarkOfStudentsByExam.objects.get(studentID_id=obj_s.pk, standardID_id=classID,
                                                     sectionID_id=sectionID,
                                                     examID_id=examID, subjectID_id=s_mark, sessionID=get_current_session(request))

            student_marks_list.append(marks.mark)
        assigned_sub_list.append(student_marks_list)
    return JsonResponse({'data': assigned_sub_list}, safe=False)


# def get_student_marks_by_class(request):
#     examID = request.GET.get('examID')
#     classID = request.GET.get('classID')
#     sectionID = request.GET.get('sectionID')
#     subjects = AssignClassSubject.objects.filter(classID_id=int(classID), isDeleted__exact=False).order_by('id')
#     subjects_list = []
#     for subs in subjects:
#         subjects_list.append(subs.pk)
#     if sectionID == "":
#         sectionID = None
#     student_list = StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, isDeleted__exact=False)
#
#     for obj in student_list:
#         for sub in subjects:
#             try:
#                 MarkOfStudentsByExam.objects.get(studentID_id=obj.pk, standardID_id=classID,
#                                                  sectionID_id=sectionID,
#                                                  examID_id=examID, subjectID_id=sub.pk)
#             except:
#                 stu = MarkOfStudentsByExam()
#                 stu.sectionID_id = sectionID
#                 stu.studentID_id = obj.pk
#                 stu.standardID_id = int(classID)
#                 stu.subjectID_id = int(sub.pk)
#                 stu.examID_id = int(examID)
#                 stu.mark = '0'
#                 stu.save()
#     assigned_sub_list = []
#     for obj_s in student_list:
#         student_marks_list = [
#             obj_s.pk,
#             '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.photo.thumbnail.url),
#             obj_s.firstName + ' ' + obj_s.middleName + ' ' + obj_s.lastName,
#             obj_s.rollNumber,
#         ]
#
#         for s_mark in tuple(subjects_list):
#             marks = MarkOfStudentsByExam.objects.get(studentID_id=obj_s.pk, standardID_id=classID,
#                                                      sectionID_id=sectionID,
#                                                      examID_id=examID, subjectID_id=s_mark)
#
#             student_marks_list.append(marks.mark)
#         assigned_sub_list.append(student_marks_list)
#     return JsonResponse({'data': assigned_sub_list}, safe=False)


def get_student_marks_by_student(request):
    examID = request.GET.get('examID')
    classID = request.GET.get('classID')
    sectionID = request.GET.get('sectionID')
    studentID = request.GET.get('studentID')
    subjects = AssignClassSubject.objects.filter(classID_id=int(classID), isDeleted__exact=False, sessionID=get_current_session(request)).order_by('id')
    subjects_list = []
    for subs in subjects:
        subjects_list.append(subs.pk)
    if sectionID == "":
        sectionID = None
    student_list = StudentDetail.objects.get(pk=int(studentID), isDeleted__exact=False, sessionID=get_current_session(request))

    for sub in subjects:
        try:
            MarkOfStudentsByExam.objects.get(studentID_id=student_list.pk, standardID_id=classID,
                                             sectionID_id=sectionID,
                                             examID_id=examID, subjectID_id=sub.pk, sessionID=get_current_session(request))
        except:
            if int(get_current_session_year()) == int(get_current_session(request)):

                stu = MarkOfStudentsByExam()
                stu.sectionID_id = sectionID
                stu.studentID_id = student_list.pk
                stu.standardID_id = int(classID)
                stu.subjectID_id = int(sub.pk)
                stu.examID_id = int(examID)
                stu.mark = '0'
                stu.sessionID_id = get_current_session_year()
                stu.save()
            else:
                pass
    assigned_sub_list = []
    i = 1
    for sub in subjects:
        mark = MarkOfStudentsByExam.objects.get(studentID_id=student_list.pk, standardID_id=classID,
                                                sectionID_id=sectionID,
                                                examID_id=examID, subjectID_id=sub.pk, sessionID=get_current_session(request))

        sub_dic = {
            'SerialNo': i,
            'Subject': sub.subjectID.subjectName,
            'FullMark': mark.examID.fullMark,
            'PassMark': mark.examID.passMark,
            'MarkScored': mark.mark,
        }
        i = i + 1
        assigned_sub_list.append(sub_dic)

    return JsonResponse({'data': assigned_sub_list}, safe=False)


# ---------------------------Exam -----------------------------
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        datestart = request.POST.get('datestart')
        dateend = request.POST.get('dateend')

        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                ev = Event()
                ev.title = title
                ev.message = description
                ev.startDate = datestart
                ev.endDate = dateend
                ev.sessionID_id = get_current_session(request)
                ev.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please update the session to latest session. '}, safe=False)

        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_event_list(request):
    events = Event.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    event_list = []
    i = 1
    for obj in events:
        event_dic = {
            'ID': obj.pk,
            'Count': i,
            'StartDate': obj.startDate,
            'EndDate': obj.endDate,
            'Title': obj.title,
            'Description': obj.message,
            'Action': ' <a onclick ="editEventDetail({},\'{}\',\'{}\',\'{}\',\'{}\')" data-toggle="modal" data-target="#myModalStudentEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.startDate), obj.endDate, obj.title, obj.message,
                str(obj.pk))
        }
        i = i + 1

        event_list.append(event_dic)
    return JsonResponse({'data': event_list}, safe=False)


def edit_event(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        datestart = request.POST.get('datestart')
        dateend = request.POST.get('dateend')

        try:
            ev = Event.objects.get(pk=int(id))
            ev.title = title
            ev.message = description
            ev.startDate = datestart
            ev.endDate = dateend
            ev.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_event(request):
    if request.method == 'POST':
        eventID = request.POST.get('eventID')
        try:

            event = Event.objects.get(pk=int(eventID))
            event.isDeleted = True
            event.save()
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def update_session_by_admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        year = request.POST.get('year')
        try:
            request.session['CurrentSchoolSession'] = {'currentSessionYear':year,'Id':id }
            return JsonResponse({'response': 'ok'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)
# --------------------------------------------SMS ---------------------------------------
@csrf_exempt
def send_sms_to_school(request):
    if request.method == 'POST':
        msg = request.POST.get('msg')
        no_list = []
        if int(get_current_session_year()) == int(get_current_session(request)):
            try:
                students = StudentDetail.objects.filter(sessionID_id=get_current_session(request), isDeleted__exact=False)
                for obj in students:
                    parent = ParentDetail.objects.get(pk=obj.parentID_id)


                    no_list.append(parent.phoneNumber)
                teachers = TeacherDetail.objects.filter(isDeleted__exact=False, isActive__exact=True)
                for tea in teachers:
                    no_list.append(tea.phoneNumber)

                sms = SendSms()
                sms.sessionID_id = get_current_session_year()
                sms.message = msg
                sms.to = "Message sent to entire school."
                sms.save()
                return JsonResponse({'response': 'ok'}, safe=False)

            except:
                return JsonResponse({'response': 'error'}, safe=False)
        else:

            return JsonResponse({'response': 'Error. Please select the current session.'}, safe=False)


@csrf_exempt
def send_sms_to_class(request):
    if request.method == 'POST':
        msg = request.POST.get('msg')
        standard = request.POST.get('standard')
        section = request.POST.get('section')
        no_list = []
        if section == "":
            section = None

        if int(get_current_session_year()) == int(get_current_session(request)):
            try:
                students = StudentDetail.objects.filter(sessionID_id=get_current_session(request),
                                                        standardID_id=int(standard), sectionID_id= section ,isDeleted__exact=False)
                for obj in students:
                    parent = ParentDetail.objects.get(pk=obj.parentID_id)


                    no_list.append(parent.phoneNumber)

                sms = SendSms()
                sms.sessionID_id = get_current_session_year()
                sms.message = msg
                classID = Standard.objects.get(pk = int(standard))
                if section == None:
                    sms.to = "Message sent to entire {}.".format(classID.name)
                else:
                    sec = Section.objects.get(pk = int(section))
                    sms.to = "Message sent to {} of {} .".format(sec.name,classID.name)

                sms.save()
                return JsonResponse({'response': 'ok'}, safe=False)

            except:
                return JsonResponse({'response': 'error'}, safe=False)
        else:

            return JsonResponse({'response': 'Error. Please select the current session.'}, safe=False)


@csrf_exempt
def send_sms_to_student(request):
    if request.method == 'POST':
        msg = request.POST.get('msg')
        standard = request.POST.get('standard')
        section = request.POST.get('section')
        student = request.POST.get('student')
        no_list = []
        if section == "":
            section = None

        if int(get_current_session_year()) == int(get_current_session(request)):
            try:
                students = StudentDetail.objects.get(pk = int(student) ,sessionID_id=get_current_session(request),
                                                        standardID_id=int(standard), sectionID_id= section ,isDeleted__exact=False)

                parent = ParentDetail.objects.get(pk=students.parentID_id)


                no_list.append(parent.phoneNumber)

                sms = SendSms()
                sms.sessionID_id = get_current_session_year()
                sms.message = msg
                classID = Standard.objects.get(pk = int(standard))
                if section == None:
                    sms.to = "Message sent to {}({}) of {}.".format(students.firstName+' '+students.middleName+' '+students.lastName, students.rollNumber ,classID.name)
                else:
                    sec = Section.objects.get(pk = int(section))
                    sms.to = "Message sent to {}({}) of {}({}).".format(students.firstName+' '+students.middleName+' '+students.lastName, students.rollNumber ,classID.name, sec.name)

                sms.save()
                return JsonResponse({'response': 'ok'}, safe=False)

            except:
                return JsonResponse({'response': 'error'}, safe=False)
        else:

            return JsonResponse({'response': 'Error. Please select the current session.'}, safe=False)


def get_sms_list(request):
    sms = SendSms.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request)).order_by('-id')
    sms_list = []
    i = 1
    for obj in sms:
        sms_dic = {
            'ID': obj.pk,
            'Count': i,
            'SentOn': obj.datetime.strftime("%m/%d/%Y, %I:%M %p"),
            'To': obj.to,
            'Message': obj.message,

        }
        i = i + 1

        sms_list.append(sms_dic)
    return JsonResponse({'data': sms_list}, safe=False)



# -----------------------------------------------analytic ----------------------------------------------------
def get_student_count_by_class_and_section(request):
    class_list = Standard.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request)).order_by('datetime')
    std = []
    s_count = []



    for obj in class_list:
        if obj.hasSection == 'No':
            student_c = StudentDetail.objects.filter(standardID=obj.pk, isDeleted__exact=False).count()

            std.append(obj.name)
            s_count.append(student_c)

        if obj.hasSection == 'Yes':
            sec_list = Section.objects.filter(standardID=obj.pk, isDeleted__exact=False)
            for s_obj in sec_list:
                student_c_s = StudentDetail.objects.filter(standardID=obj.pk, isDeleted__exact=False, sectionID=s_obj.pk).count()
                std.append(obj.name +' - '+ s_obj.name)
                s_count.append(student_c_s)






    data = {
        'ClassList': std,
        'Counts':s_count
    }



    return JsonResponse({'data': data}, safe=False)