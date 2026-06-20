from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.
def appointment(request):
    if request.method == "POST":
         form = AppointmentForm(request.POST) #to get the data from the form
         if form.is_valid(): # check if the form is valid
             form.save()    # save the data to the database
             return redirect('/book') # redirect to the same page after saving the data
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')  

def faq(request):
    return render(request, 'faq.html')  

def services(request):
    return render(request, 'services.html')

def allappointments(request):
    if request.method == "GET": #to get the data from the database
        appnts = Appointment.objects.all() # get all the appointments from the database
    return render(request, 'allappointments.html', {'appointment': appnts}) #get the data from the database and pass it to the frontend

def delete_appnt(request,id):
    appnts = Appointment.objects.get(id=id) # get the appointment with the given id from the database
    appnts.delete() # delete the appointment from the database
    return redirect('/allappointments') 

def update_appnt(request,id):
    appnts = Appointment.objects.get(id=id)
    if request.method == "POST": 
        form = AppointmentForm(request.POST, instance=appnts) # get the data from the form and update the appointment with the given id
        if form.is_valid(): 
             form.save()     
             return redirect('/allappointments') 
    else:
        form = AppointmentForm(instance=appnts)
    return render(request, 'update_appnt.html',{'form': form})