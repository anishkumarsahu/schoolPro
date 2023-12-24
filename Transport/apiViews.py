import datetime
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse

from schoolApp.apiView import get_current_session_year, get_current_session
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string


# ------------------------- driver ----------------------------------------
def add_driver(request):
    if request.method == 'POST':
        Dname = request.POST.get('Dname')
        Daddress = request.POST.get('Daddress')
        Dphone = request.POST.get('Dphone')
        Dexperience = request.POST.get('Dexperience')

        image = request.FILES['Dimage']
        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                driver = Driver()
                driver.name = Dname
                driver.address = Daddress
                driver.phoneNumber = Dphone
                driver.experience = Dexperience
                driver.photo = image
                driver.sessionID_id = get_current_session_year()
                driver.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_driver_list(request):
    drivers = Driver.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    driver_list = []
    for obj in drivers:
        driver_dic = {
            'DriverID': obj.pk,
            'Name': obj.name,
            'Photo': '<img src="{}" class="avatar" alt="Photo">'.format(obj.photo.thumbnail.url),
            'Phone': obj.phoneNumber,
            'Experience': obj.experience,
            'Address': obj.address,
            'AddedOn': obj.datetime.date(),
            'Action': ' <a onclick ="editDriverDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteDriverDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        driver_list.append(driver_dic)
    return JsonResponse({'data': driver_list}, safe=False)


def get_driver_detail(request, id=None):
    obj = Driver.objects.get(pk=id, isDeleted__exact=False, sessionID=get_current_session(request))

    driver_dic = {
        'DriverID': obj.pk,
        'Name': obj.name,
        'Photo': obj.photo.thumbnail.url,
        'Phone': obj.phoneNumber,
        'Experience': obj.experience,
        'Address': obj.address,
        'AddedOn': obj.datetime.date(),
        'Action': ' <a onclick ="editDriverDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteDriverDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
            str(obj.pk), str(obj.pk), str(obj.pk))
    }

    return JsonResponse({'data': driver_dic}, safe=False)


@csrf_exempt
def edit_driver_photo(request):
    if request.method == 'POST':
        DriverID = request.POST.get('EDriverID')
        image = request.FILES['file']
        try:
            driver_data = Driver.objects.get(pk=int(DriverID))
            driver_data.photo = image
            driver_data.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'error'})


def edit_driver_detail(request):
    if request.method == 'POST':
        DID = request.POST.get('DID')
        Dname = request.POST.get('Dname')
        Daddress = request.POST.get('Daddress')
        Dphone = request.POST.get('Dphone')
        Dexperience = request.POST.get('Dexperience')
        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                driver = Driver.objects.get(pk=int(DID))
                driver.name = Dname
                driver.address = Daddress
                driver.phoneNumber = Dphone
                driver.experience = Dexperience
                driver.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_driver_detail(request):
    if request.method == 'POST':
        id = request.POST.get('deleteID')

        driver = Driver.objects.get(pk=int(id))
        driver.isDeleted = True
        driver.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_driver_list_for_vehicle(request):
    drivers = Driver.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    driver_list = []
    for obj in drivers:
        driver_dic = {
            'DriverID': obj.pk,
            'Name': obj.name,
            'Phone': obj.phoneNumber,
        }

        driver_list.append(driver_dic)
    return JsonResponse({'data': driver_list}, safe=False)


# ---------------------------------------------------------------------------------------------------





# ------------------------- conductor ----------------------------------------
def add_conductor(request):
    if request.method == 'POST':
        Dname = request.POST.get('Dname')
        Daddress = request.POST.get('Daddress')
        Dphone = request.POST.get('Dphone')
        Dexperience = request.POST.get('Dexperience')

        image = request.FILES['Dimage']
        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                driver = Conductor()
                driver.name = Dname
                driver.address = Daddress
                driver.phoneNumber = Dphone
                driver.experience = Dexperience
                driver.photo = image
                driver.sessionID_id = get_current_session_year()
                driver.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_conductor_list(request):
    drivers = Conductor.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    driver_list = []
    for obj in drivers:
        driver_dic = {
            'DriverID': obj.pk,
            'Name': obj.name,
            'Photo': '<img src="{}" class="avatar" alt="Photo">'.format(obj.photo.thumbnail.url),
            'Phone': obj.phoneNumber,
            'Experience': obj.experience,
            'Address': obj.address,
            'AddedOn': obj.datetime.date(),
            'Action': ' <a onclick ="editDriverDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteDriverDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        driver_list.append(driver_dic)
    return JsonResponse({'data': driver_list}, safe=False)


def get_conductor_detail(request, id=None):
    obj = Conductor.objects.get(pk=id, isDeleted__exact=False, sessionID=get_current_session(request))

    driver_dic = {
        'DriverID': obj.pk,
        'Name': obj.name,
        'Photo': obj.photo.thumbnail.url,
        'Phone': obj.phoneNumber,
        'Experience': obj.experience,
        'Address': obj.address,
        'AddedOn': obj.datetime.date(),
        'Action': ' <a onclick ="editDriverDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteDriverDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
            str(obj.pk), str(obj.pk), str(obj.pk))
    }

    return JsonResponse({'data': driver_dic}, safe=False)


@csrf_exempt
def edit_conductor_photo(request):
    if request.method == 'POST':
        DriverID = request.POST.get('EDriverID')
        image = request.FILES['file']
        try:
            driver_data = Conductor.objects.get(pk=int(DriverID))
            driver_data.photo = image
            driver_data.save()
            return JsonResponse({'response': 'ok'})
        except:
            return JsonResponse({'response': 'error'})


def edit_conductor_detail(request):
    if request.method == 'POST':
        DID = request.POST.get('DID')
        Dname = request.POST.get('Dname')
        Daddress = request.POST.get('Daddress')
        Dphone = request.POST.get('Dphone')
        Dexperience = request.POST.get('Dexperience')
        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                driver = Conductor.objects.get(pk=int(DID))
                driver.name = Dname
                driver.address = Daddress
                driver.phoneNumber = Dphone
                driver.experience = Dexperience
                driver.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_conductor_detail(request):
    if request.method == 'POST':
        id = request.POST.get('deleteID')

        driver = Conductor.objects.get(pk=int(id))
        driver.isDeleted = True
        driver.save()

        return JsonResponse({'response': 'ok'}, safe=False)


def get_conductor_list_for_vehicle(request):
    drivers = Conductor.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    driver_list = []
    for obj in drivers:
        driver_dic = {
            'DriverID': obj.pk,
            'Name': obj.name,
            'Phone': obj.phoneNumber,
        }

        driver_list.append(driver_dic)
    return JsonResponse({'data': driver_list}, safe=False)


# ---------------------------------------------------------------------------------------------------


# ------------------------- Vehicle ----------------------------------------
def add_vehicle(request):
    if request.method == 'POST':
        Vname = request.POST.get('Vname')
        Vnumber = request.POST.get('Vnumber')
        Vterminal = request.POST.get('Vterminal')
        Vcapacity = request.POST.get('Vcapacity')
        Vdriver = request.POST.get('Vdriver')
        Vconductor = request.POST.get('Vconductor')

        try:
            if Vdriver == '':
                Vdriver = None
            if Vconductor == '':
                Vconductor = None
            if int(get_current_session_year()) == int(get_current_session(request)):
                driver = VehicleDetail()
                driver.name = Vname
                driver.number = Vnumber
                driver.terminal = Vterminal
                driver.seatCapacity = Vcapacity
                driver.driverID_id = Vdriver
                driver.conductorID_id = Vconductor
                driver.sessionID_id = get_current_session_year()
                driver.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_vehicle_list(request):
    vehicles = VehicleDetail.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    vehicle_list = []
    for obj in vehicles:
        if obj.driverID_id == None:
            driver = 'N/A'
        else:
            driver = obj.driverID.name
        if obj.conductorID_id == None:
            conductor = 'N/A'
        else:
            conductor = obj.conductorID.name
        vehicle_dic = {
            'VehicleID': obj.pk,
            'Name': obj.name,
            'Number': obj.number,
            'Terminal': obj.terminal,
            'Seat': obj.seatCapacity,
            'Driver': driver,
            'Conductor': conductor,
            'AddedOn': obj.datetime.date(),
            'Action': ' <a onclick ="editVehicleDetail({})" class="btn btn-info btn-xs" data-toggle="modal" data-target="#myModalEdit"><i class="fa fa-pencil"></i> Edit </a> <a onclick ="deleteVehicleDetail({})" class="btn btn-danger btn-xs" data-toggle="modal" data-target="#myModalDelete"><i class="fa fa-trash-o"></i> Delete </a> '.format(
                str(obj.pk), str(obj.pk), str(obj.pk))
        }

        vehicle_list.append(vehicle_dic)
    return JsonResponse({'data': vehicle_list}, safe=False)


def get_vehicle_detail(request, id=None):
    obj = VehicleDetail.objects.get(pk=id, isDeleted__exact=False, sessionID=get_current_session(request))

    vehicle_dic = {
        'VehicleID': obj.pk,
        'Name': obj.name,
        'Number': obj.number,
        'Terminal': obj.terminal,
        'Seat': obj.seatCapacity,
        'Driver': obj.driverID_id,
        'Conductor': obj.conductorID_id,
        'AddedOn': obj.datetime.date(),
    }

    return JsonResponse({'data': vehicle_dic}, safe=False)


def edit_vehicle_detail(request):
    if request.method == 'POST':
        EVID = request.POST.get('EVID')
        EVname = request.POST.get('EVname')
        EVnumber = request.POST.get('EVnumber')
        EVterminal = request.POST.get('EVterminal')
        EVseat = request.POST.get('EVseat')
        EVdriver = request.POST.get('EVdriver')
        EVconductor = request.POST.get('EVconductor')
        try:
            if int(get_current_session_year()) == int(get_current_session(request)):

                vehicle = VehicleDetail.objects.get(pk=int(EVID))
                vehicle.name = EVname
                vehicle.number = EVnumber
                vehicle.terminal = EVterminal
                vehicle.seatCapacity = EVseat
                vehicle.driverID_id = EVdriver
                vehicle.conductorID_id = EVconductor
                vehicle.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


@csrf_exempt
def delete_vehicle_detail(request):
    if request.method == 'POST':
        id = request.POST.get('deleteID')

        driver = VehicleDetail.objects.get(pk=int(id))
        driver.isDeleted = True
        driver.save()

        return JsonResponse({'response': 'ok'}, safe=False)


# ------------------------------------Expenses----------------------------------------------
def add_vehicle_expenses(request):
    if request.method == 'POST':
        Evehicle = request.POST.get('Evehicle')
        Etype = request.POST.get('Etype')
        Ecost = request.POST.get('Ecost')
        Edes = request.POST.get('Edes')
        EDate = request.POST.get('EDate')

        try:
            if int(get_current_session_year()) == int(get_current_session(request)):
                expense = VehicleExpenses()
                expense.vehicleID_id = int(Evehicle)
                expense.expenseType = Etype
                expense.cost = Ecost
                expense.description = Edes
                expense.expenseDate = EDate
                expense.sessionID_id = get_current_session_year()
                expense.save()
                return JsonResponse({'response': 'ok'}, safe=False)
            else:
                return JsonResponse({'response': 'Error. Please select current session to enter detail.'}, safe=False)
        except:
            return JsonResponse({'response': 'error'}, safe=False)


def get_vehicle_expenses_list(request):
    vehicles = VehicleExpenses.objects.filter(isDeleted__exact=False, sessionID=get_current_session(request))
    vehicle_list = []
    for obj in vehicles:
        vehicle_dic = {
            'ID':obj.pk,
            'VehicleName': obj.vehicleID.name,
            'VehicleNumber': obj.vehicleID.number,
            'Cost': obj.cost,
            'Type': obj.expenseType,
            'Description': obj.description,
            'ExpenseDate': obj.expenseDate,
            'AddedOn': obj.datetime.date(),
        }

        vehicle_list.append(vehicle_dic)
    return JsonResponse({'data': vehicle_list}, safe=False)
