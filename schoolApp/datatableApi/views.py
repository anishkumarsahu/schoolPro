from django.db.models import Q
from django.utils.html import escape

from schoolApp.apiView import get_current_session, get_current_session_year
from schoolApp.models import *
# done
from django_datatables_view.base_datatable_view import BaseDatatableView


class getNonTeachingStaffListJson(BaseDatatableView):
    order_columns = ['id', 'photo', 'firstName', 'EmployeeCode',
                     'phoneNumber', 'DOB', 'joinDate', 'gender',
                     'isActive', 'Action', ]

    def get_initial_queryset(self):
        return NonTeachingStaff.objects.filter(isDeleted__exact=False)

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    EmployeeCode__icontains=search) | Q(DOB__icontains=search)
                | Q(joinDate__icontains=search)| Q(gender__icontains=search)
                | Q(isActive__icontains=search))

        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:
            if item.isActive == True:
                active = "Yes"
            else:
                active = "No"

            json_data.append([
                escape(item.pk),
                '<img src="{}" class="avatar" alt="Photo">'.format(item.photo.thumbnail.url),
                item.firstName + ' ' + item.middleName + ' ' + item.lastName,  # escape HTML for security reasons
                item.EmployeeCode,
                item.phoneNumber,
                item.DOB,
                item.joinDate,
                item.gender,
                active,
                '<a onclick ="userDetailId({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myViewModal"><i class="fa fa-eye"></i> View </a> <a onclick ="EditUserComputerOperator({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="getIdFordeletingComputerOperator({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(item.pk), str(item.pk), str(item.pk))
                ,

            ])
            i = i + 1
        return json_data


class getStudentListJson(BaseDatatableView):
    order_columns = ['StudentID', 'photo', 'firstName', 'standardID',
                     'sectionID', 'rollNumber', 'gender', 'parentID',
                     'phoneNumber',
                     'uniqueKey', 'Action', ]

    def get_initial_queryset(self):
        classID = self.request.GET.get('classID')
        sectionID = self.request.GET.get('sectionID')
        if sectionID == "":
            sectionID = None

        return StudentDetail.objects.filter(sessionID_id=get_current_session(self.request), isDeleted__exact=False,
                                            sectionID_id=sectionID, standardID_id=classID)

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    rollNumber__icontains=search) | Q(uniqueKey__icontains=search)
                | Q(gender__icontains=search))

        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:
            parent = ParentDetail.objects.get(pk=item.parentID_id)
            try:
                section = item.sectionID.name
            except:
                section = '-'

            json_data.append([
                escape(item.pk),

                '<img src="{}" class="avatar" alt="Photo">'.format(item.photo.thumbnail.url),
                item.firstName + ' ' + item.middleName + ' ' + item.lastName,  # escape HTML for security reasons
                item.standardID.name,
                section,
                item.rollNumber,
                item.gender,
                parent.fatherFirstName + ' ' + parent.fatherMiddleName + ' ' + parent.fatherLastName,
                parent.phoneNumber,  # escape HTML for security reasons
                item.uniqueKey,
                '<a onclick ="getStudentDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editStudentDetail({})" data-toggle="modal" data-target="#myModalStudentEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteStudentDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(item.pk), str(item.pk), str(item.pk))
                ,

            ])
            i = i + 1
        return json_data


class getTeacherListJson(BaseDatatableView):
    order_columns = ['teacherID', 'photo', 'firstName', 'phoneNumber',
                     'EmployeeCode', 'DOB', 'dateOfJoining', 'gender', 'isActive',
                     'Action', ]

    def get_initial_queryset(self):

        return TeacherDetail.objects.filter(isDeleted__exact=False)

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    EmployeeCode__icontains=search)
                | Q(gender__icontains=search) | Q(isActive__icontains=search))

        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:
            if item.isActive == True:
                active = "Yes"
            else:
                active = "No"

            json_data.append([
                escape(item.pk),
                '<img src="{}" class="avatar" alt="Photo">'.format(item.photo.thumbnail.url),
                item.firstName + ' ' + item.middleName + ' ' + item.lastName,  # escape HTML for security reasons
                item.phoneNumber,
                item.EmployeeCode,
                item.DOB,
                item.dateOfJoining,
                item.gender,
                active,
                '<a onclick ="getTeacherDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editTeacherDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteTeacherDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(item.pk), str(item.pk), str(item.pk))

            ])
            i = i + 1
        return json_data


class getParentListJson(BaseDatatableView):
    order_columns = ['ParentID', 'parentID.fatherFirstName', 'parentID.motherFirstName', 'parentID.occupation',
                     'parentID.phoneNumber', 'parentID.fatherMiddleName', 'Action', ]

    def get_initial_queryset(self):
        classID = self.request.GET.get('classID')
        sectionID = self.request.GET.get('sectionID')
        if sectionID == "":
            sectionID = None
        return StudentDetail.objects.filter(sessionID_id=get_current_session(self.request), isDeleted__exact=False,
                                            sectionID_id=sectionID, standardID_id=classID)

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    rollNumber__icontains=search) | Q(uniqueKey__icontains=search)
                | Q(gender__icontains=search) | Q(parentID__fatherFirstName__icontains=search)
                | Q(parentID__fatherMiddleName__icontains=search)| Q(parentID__fatherLastName__icontains=search)
                | Q(parentID__motherFirstName__icontains=search)| Q(parentID__motherMiddleName__icontains=search)
                | Q(parentID__motherLastName__icontains=search)| Q(parentID__phoneNumber__icontains=search)
                | Q(parentID__occupation__icontains=search)

            )
        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1

        for item in qs:
            json_data.append([
                item.pk,
                item.parentID.fatherFirstName + ' ' + item.parentID.fatherMiddleName + ' ' + item.parentID.fatherLastName,
                item.parentID.motherFirstName + ' ' + item.parentID.motherMiddleName + ' ' + item.parentID.motherLastName,
                item.parentID.occupation,
                item.parentID.phoneNumber,
                item.firstName + ' ' + item.middleName + ' ' + item.lastName +  '- Roll no:' + item.rollNumber,
                '<a onclick ="getParentDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editParentDetail({})" data-toggle="modal" data-target="#myModalEditParent" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteParentDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                    str(item.parentID.pk), str(item.parentID.pk), str(item.parentID.pk))
            ])
            i = i + 1
        return json_data


class getClassListJson(BaseDatatableView):
    order_columns = ['name', 'parentID.fatherFirstName', 'parentID.motherFirstName', 'parentID.occupation',
                     'parentID.phoneNumber', 'parentID.fatherMiddleName', 'Action', ]

    def get_initial_queryset(self):
        query = self.request.GET.get('query')
        if query == 'all':
            class_list = Standard.objects.filter(isDeleted__exact=False,
                                                 sessionID=get_current_session(self.request)).order_by('datetime')
        else:
            class_list = Standard.objects.filter(isDeleted__exact=False, pk=int(query),
                                                 sessionID=get_current_session(self.request)).order_by('datetime')

        return class_list

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    rollNumber__icontains=search) | Q(uniqueKey__icontains=search)
                | Q(gender__icontains=search) | Q(parentID__fatherFirstName__icontains=search)
                | Q(parentID__fatherMiddleName__icontains=search)| Q(parentID__fatherLastName__icontains=search)
                | Q(parentID__motherFirstName__icontains=search)| Q(parentID__motherMiddleName__icontains=search)
                | Q(parentID__motherLastName__icontains=search)| Q(parentID__phoneNumber__icontains=search)
                | Q(parentID__occupation__icontains=search)

            )
        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1

        for item in qs:

            if item.hasSection == 'No':
                try:
                    teachers = AssignTeacherToClassOrSection.objects.get(standardID_id=item.pk,
                                                                         sessionID=get_current_session(self.request))
                except:

                    if int(get_current_session_year()) == int(get_current_session(self.request)):
                        assign_teacher = AssignTeacherToClassOrSection()
                        assign_teacher.standardID_id = item.pk
                        assign_teacher.sessionID_id = get_current_session_year()
                        assign_teacher.save()
                    else:
                        pass
                if teachers.classTeacher_id == None:
                    teacher = 'No Data'
                else:
                    teacher = teachers.classTeacher.firstName + ' ' + teachers.classTeacher.middleName + ' ' + teachers.classTeacher.lastName


                json_data.append([
                    item.name,
                    'NaN',
                    item.startingRoll,
                    item.endingRoll,
                    teacher,
                    '<a onclick ="getParentDetail({})" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-eye"></i> View </a> <a onclick ="editParentDetail({})" data-toggle="modal" data-target="#myModalEditParent" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteParentDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                        str(item.pk), str(item.pk), str(item.pk))
                ])


            if item.hasSection == 'Yes':
                sec = Section.objects.filter(standardID_id=item.pk, isDeleted__exact=False,
                                             sessionID=get_current_session(self.request))
                for objs in sec:
                    try:
                        teachers = AssignTeacherToClassOrSection.objects.get(sectionID_id=objs.pk,
                                                                             sessionID=get_current_session(self.request))
                    except:
                        if int(get_current_session_year()) == int(get_current_session(self.request)):

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

                    json_data.append([
                        objs.standardID.name,
                        objs.name,
                        objs.startingRoll,
                        objs.endingRoll,
                        teacher,
                        '<a href="#" class="btn btn-primary btn-xs" data-toggle="modal" data-target="#myModal"  onclick="getClassDetailWithSection({},{})"><i class="fa fa-eye"></i> View </a> <a href="#" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditClass"  onclick="editClassDetailWithSection({},{})"><i class="fa fa-pencil"></i> Edit </a> <a href="#" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete" onclick = "deleteClassSection({})"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                            str(objs.standardID_id), objs.pk, str(objs.standardID_id), objs.pk, objs.pk)
                    ])

        return json_data


class getStudentListForAttendanceJson(BaseDatatableView):
    order_columns = ['id', 'photo', 'firstName', 'rollNumber',
                     'middleName', 'lastName', 'Action', ]

    def get_initial_queryset(self):
        classID = self.request.GET.get('classID')
        sectionID = self.request.GET.get('sectionID')
        # if sectionID == "":
        #     sectionID = None
        if classID =='' and sectionID == '':
            return StudentDetail.objects.filter(standardID_id=None, sectionID_id=None, sessionID=get_current_session(self.request))
        else:
            if sectionID == "":
                sectionID = None
            return StudentDetail.objects.filter(standardID_id=classID, sectionID_id=sectionID, sessionID=get_current_session(self.request))



    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(firstName__icontains=search) | Q(middleName__icontains=search) | Q(lastName__icontains=search) | Q(
                    phoneNumber__icontains=search) | Q(
                    rollNumber__icontains=search) | Q(uniqueKey__icontains=search)
                | Q(gender__icontains=search) | Q(parentID__fatherFirstName__icontains=search)
                | Q(parentID__fatherMiddleName__icontains=search)| Q(parentID__fatherLastName__icontains=search)
                | Q(parentID__motherFirstName__icontains=search)| Q(parentID__motherMiddleName__icontains=search)
                | Q(parentID__motherLastName__icontains=search)| Q(parentID__phoneNumber__icontains=search)
                | Q(parentID__occupation__icontains=search)

            )
        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        date = self.request.GET.get('date')
        classID = self.request.GET.get('classID')
        sectionID = self.request.GET.get('sectionID')
        subjectID = self.request.GET.get('subjectID')
        if date == '' and classID == '' and sectionID == '' and subjectID == '':
            return json_data
        else:
            if sectionID == "":
                sectionID = None

            if subjectID == "" or subjectID == 'null':
                subjectID = None
            for item in qs:

                try:
                    StudentAttendance.objects.get(studentID_id=item.pk, standardID_id=classID, sectionID_id=sectionID,
                                                  attendanceDate__icontains=date, subjectID_id=subjectID,
                                                  sessionID=get_current_session(self.request))
                except:
                    if int(get_current_session_year()) == int(get_current_session(self.request)):
                        stu = StudentAttendance()
                        stu.sectionID_id = sectionID
                        stu.studentID_id = item.pk
                        stu.standardID_id = classID
                        stu.subjectID_id = subjectID
                        stu.attendanceDate = date
                        stu.sessionID_id = get_current_session_year()
                        stu.save()
                    else:
                        pass
            at_least = StudentAttendance.objects.filter(standardID_id=classID, sectionID_id=sectionID,
                                                        attendanceDate__icontains=date, subjectID_id=subjectID,
                                                        sessionID=get_current_session(self.request))


            for obj_s in at_least:
                # try:
                #     section = obj_s.sectionID.name
                # except:
                #     section = '-'
                if obj_s.isAbsent == True:
                    present = '<label><input  type="checkbox" class="js-switch" checked id="{}"/></label>'.format(
                        'a' + str(obj_s.pk)),
                else:
                    present = '<label><input  type="checkbox" class="js-switch" id="{}"/></label>'.format(
                        'a' + str(obj_s.pk)),
                json_data.append([
                    obj_s.pk,
                    '<img src="{}" class="avatar" alt="Avatar">'.format(obj_s.studentID.photo.thumbnail.url),
                    obj_s.studentID.firstName + ' ' + obj_s.studentID.middleName + ' ' + obj_s.studentID.lastName,
                    obj_s.studentID.rollNumber,
                    present,
                    '<div class=" form-group has-feedback"><input type="text" value ="{}" class="form-control  removeWidth" id="{}" placeholder=""></div>'.format(
                        obj_s.reason, obj_s.pk),
                    '<button type="button" class="btn btn-success" onclick="submitData({},{})">Submit</button>'.format(
                        obj_s.pk, obj_s.pk)

                ])
            return json_data


class getEventsListJson(BaseDatatableView):
    order_columns = ['id','count', 'startDate', 'endDate', 'title',
                     'message','Action', ]

    def get_initial_queryset(self):
        return Event.objects.filter(isDeleted__exact=False, sessionID=get_current_session(self.request))

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(startDate__icontains=search) | Q(endDate__icontains=search) | Q(title__icontains=search) | Q(
                    message__icontains=search))

        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:

            json_data.append([
                escape(item.pk),
                i,
                item.startDate,
                item.endDate,
                item.title,
                item.message,
                ' <a onclick ="editEventDetail({},\'{}\',\'{}\',\'{}\',\'{}\')" data-toggle="modal" data-target="#myModalStudentEdit" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEditTeacher"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(item.pk), str(item.startDate), item.endDate, item.title, item.message,str(item.pk))

            ])
            i = i + 1
        return json_data



class getClassAssignedSubjectsJson(BaseDatatableView):
    order_columns = ['id','classID', 'subjectID','Action', ]

    def get_initial_queryset(self):
        classID = self.request.GET.get('classID')
        return AssignClassSubject.objects.filter(isDeleted__exact=False, sessionID=get_current_session(self.request), classID_id = int(classID))

    def filter_queryset(self, qs):

        search = self.request.GET.get('search[value]', None)

        if search:
            qs = qs.filter(
                Q(classID__name__icontains=search) | Q(subjectID__subjectName__icontains=search))

        return qs

    def prepare_results(self, qs):
        json_data = []
        i = 1
        for item in qs:

            json_data.append([
                i,
                item.classID.name,
                item.subjectID.subjectName,
                '  <a onclick ="deleteAssignDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(item.pk))

            ])
            i = i + 1
        return json_data

