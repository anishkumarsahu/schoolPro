from django.urls import re_path
from .apiViews import *

urlpatterns = [
    # driver
    re_path(r'^addDriver/$', add_driver, name='add_driver'),
    re_path(r'^getDriverList/$', get_driver_list, name='get_driver_list'),
    re_path(r'^getDriverDetail/(?P<id>\d+)/$', get_driver_detail, name='get_driver_detail'),
    re_path(r'^editDriverPhoto/$', edit_driver_photo, name='edit_driver_photo'),
    re_path(r'^editDriverDetail/$', edit_driver_detail, name='edit_driver_detail'),
    re_path(r'^deleteDriverDetail/$', delete_driver_detail, name='delete_driver_detail'),
    re_path(r'^getDriverListForVehicle/$', get_driver_list_for_vehicle, name='get_driver_list_for_vehicle'),

    # conductor
    re_path(r'^addConductor/$', add_conductor, name='add_conductor'),
    re_path(r'^getConductorList/$', get_conductor_list, name='get_conductor_list'),
    re_path(r'^getConductorDetail/(?P<id>\d+)/$', get_conductor_detail, name='get_conductor_detail'),
    re_path(r'^editConductorPhoto/$', edit_conductor_photo, name='edit_conductor_photo'),
    re_path(r'^editConductorDetail/$', edit_conductor_detail, name='edit_conductor_detail'),
    re_path(r'^deleteConductorDetail/$', delete_conductor_detail, name='delete_conductor_detail'),
    re_path(r'^getConductorListForVehicle/$', get_conductor_list_for_vehicle, name='get_conductor_list_for_vehicle'),

    # vehicle
    re_path(r'^addVehicle/$', add_vehicle, name='add_vehicle'),
    re_path(r'^getVehicleList/$', get_vehicle_list, name='get_vehicle_list'),
    re_path(r'^getVehicleDetail/(?P<id>\d+)/$', get_vehicle_detail, name='get_vehicle_detail'),
    re_path(r'^editVehicleDetail/$', edit_vehicle_detail, name='edit_vehicle_detail'),
    re_path(r'^deleteVehicleDetail/$', delete_vehicle_detail, name='delete_vehicle_detail'),

    # expense
    re_path(r'^addVehicleExpenses/$', add_vehicle_expenses, name='add_vehicle_expenses'),
    re_path(r'^getVehicleExpensesList/$', get_vehicle_expenses_list, name='get_vehicle_expenses_list'),

]