# from django.contrib import admin
from django.urls import path
from .views import Patientregister,adminwait, logpatient,loggedinpatient, nope,logprof,professionalregister, Home,prodash, patdash

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , Home,name="Home"),
    path('register-patient' , Patientregister,name="Patientregister"),
    path('waithere',adminwait,name="adminwait"),
    path('loginpatient',logpatient,name="logpatient"),
    path('patientdashboard',loggedinpatient,name="loggedinpatient"),
    path('noapproval',nope,name="nope"),
    path('loginprof',logprof,name="loginproffesional"),
    path('profsignup',professionalregister,name="professionalregister"),
    path('professionaldashboard',prodash,name="prodash"),
    path('patientdashboard',patdash,name="patdash")


]