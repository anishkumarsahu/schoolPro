from django.db import models

# Create your models here.
from schoolApp.models import *


class Driver(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    photo = StdImageField(upload_to="StudentImage", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)


class Conductor(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    photo = StdImageField(upload_to="StudentImage", blank=True, null=True,
                          variations={'thumbnail': {'width': 250, 'height': 250}})
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)



class VehicleDetail(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    terminal = models.CharField(max_length=200, blank=True, null=True)
    seatCapacity = models.CharField(max_length=100, blank=True, null=True)
    driverID = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.CASCADE)
    conductorID = models.ForeignKey(Conductor, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)


class VehicleExpenses(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    vehicleID = models.ForeignKey(VehicleDetail, blank=True, null=True, on_delete=models.CASCADE)
    cost = models.CharField(max_length=100, blank=True, null=True)
    expenseType = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    expenseDate = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)



class StudentVehicleAssign(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    vehicleID = models.ForeignKey(VehicleDetail, blank=True, null=True, on_delete=models.CASCADE)
    studentID = models.ForeignKey(StudentDetail, blank=True, null=True, on_delete=models.CASCADE)
    fee = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)


class StudentVehicleFee(models.Model):
    schoolID = models.ForeignKey(SchoolDetail, blank=True, null=True, on_delete=models.CASCADE)
    sessionID = models.ForeignKey(SchoolSession, blank=True, null=True, on_delete=models.CASCADE)
    studentVehicleAssignID = models.ForeignKey(StudentVehicleAssign, blank=True, null=True, on_delete=models.CASCADE)
    studentID = models.ForeignKey(StudentDetail, blank=True, null=True, on_delete=models.CASCADE)
    month = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    payDate = models.DateField(blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)
    lastUpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    isDeleted = models.BooleanField(default=False)