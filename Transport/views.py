from django.shortcuts import render

# Create your views here.
def TransportVehicle(request):
    return render(request, 'TransportVehicle.html')

def TransportDriver(request):
    return render(request, 'TransportDriver.html')

def TransportConductor(request):
    return render(request, 'TransportConductor.html')

def TransportVehicleExpenses(request):
    return render(request, 'TransportVehicleExpenses.html')

def TransportAssignStudent(request):
    return render(request, 'TransportAssignStudent.html')


def TransportAddFees(request):
    return render(request, 'TransportAddFees.html')

def TransportFeesDetail(request):
    return render(request, 'TransportFeesDetail.html')