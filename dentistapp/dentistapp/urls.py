"""dentistapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

from dentistapp.views.createPatient import  patient_endpoint
from dentistapp.views.createEmployee import  employee_endpoint
from dentistapp.views.showDentistsInBranch import  dentist_in_branch_endpoint
from dentistapp.views.setAppointment import  appointment_endpoint
from dentistapp.views.checkAppointments import  check_appointment_endpoint
from dentistapp.views.index import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('patient', patient_endpoint),
    path('employee', employee_endpoint),
    path('dentist_in_branch', dentist_in_branch_endpoint),
    path('appointment', appointment_endpoint),
    path('check_appointment_endpoint', check_appointment_endpoint)
]
