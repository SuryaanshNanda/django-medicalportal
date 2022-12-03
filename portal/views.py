from django.shortcuts import render, redirect
from .models import Patient, Professional
from django.contrib import messages
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# from .models import Patient

# Create your views here.
# def home_view(request):
#     context ={}
#     context['form']= Patient()
#     return render(request, "login.html", context)
@csrf_exempt
def Patientregister(request):
    pass
    if request.method=='POST':
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
    # Username=request.POST.get('Username')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        ConfirmPassword=request.POST.get('ConfirmPassword')
        Phone=request.POST.get('Phone')
        City=request.POST.get('City')
        Bloodtype=request.POST.get('Blood')
        PatientidType=request.POST.get('PatientidType')
        Patientid=request.FILES.get('Patientid')
        if len(Password)<8:
            raise serializers.ValidationError({'error': 'password too short'})  
        if Password != ConfirmPassword:
            raise serializers.ValidationError({'error': 'password and password2 do not match'})
            #messages.success(request, 'Password does not match.')
        if Patient.objects.filter(Email=Email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
            #messages.success(request, 'Email already exists.')
  
        patient=Patient(Name=Name,Address=Address, Email=Email,Password=Password,ConfirmPassword=ConfirmPassword,Phone=Phone,City=City,PatientidType=PatientidType, Patientid= Patientid)
        patient.save()
        return redirect('/waithere')

    return render(request,'rpatient.html')
def adminwait(request):
     return render(request,'adminwait.html')

def logpatient(request):
    if request.method=='POST':
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        if Patient.objects.filter(Email=Email).exists():
            obj=Patient.objects.get(pk=Email)
            feild="Password"
            password=getattr(obj, feild)
            if(password==Password):
                if(getattr(obj,"Verified")==True):
                    return redirect('/patientdashboard')
                else:
                     return redirect('/noapproval')
            else:
                raise serializers.ValidationError({'error': 'Wrong Password or Email'})
        else:
             raise serializers.ValidationError({'error': 'Wrong Password or Email'})
    return render(request,'lpatient.html')

def loggedinpatient(request):
    return render(request,'pdashboard.html')

def nope(request):
    return render(request,'notapproved.html')

def professionalregister(request):
    pass
    if request.method=='POST':
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        ConfirmPassword=request.POST.get('ConfirmPassword')
        Phone=request.POST.get('Phone')
        Role=request.POST.get('Role')
        City=request.POST.get('City')
        Hospital_Name=request.POST.get('Hospital_Name')
        Professionalid=request.POST.get('Professionalid')
        if len(Password)<8:
            raise serializers.ValidationError({'error': 'password too short'})  
        if Password != ConfirmPassword:
            raise serializers.ValidationError({'error': 'password and password2 do not match'})
            #messages.success(request, 'Password does not match.')
        if Professional.objects.filter(Email=Email).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
            #messages.success(request, 'Email already exists.')
  
        professional=Professional(Name=Name,Address=Address, Email=Email,Password=Password,ConfirmPassword=ConfirmPassword,Phone=Phone,Role=Role, City=City,Hospital_Name=Hospital_Name,Professionalid=Professionalid)
        professional.save()
        return redirect('/waithere')
    return render(request,'rprofessional.html')

def logprof(request):
    if request.method=='POST':
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        if Professional.objects.filter(Email=Email).exists():
            obj=Professional.objects.get(pk=Email)
            feild="Password"
            password=getattr(obj, feild)
            if(password==Password):
                if(getattr(obj,"Verified")==True):
                    return redirect('/professionaldashboard')
                else:
                     return redirect('/noapproval')
            else:
                raise serializers.ValidationError({'error': 'Wrong Password or Email'})
        else:
             raise serializers.ValidationError({'error': 'Wrong Password or Email'})
    return render(request,'lprofessional.html')

def Home(request):
    return render(request,'home.html')

def prodash(request):
     return render(request,'dprofessional.html')

def patdash(request):
     return render(request,'dpatient.html')



