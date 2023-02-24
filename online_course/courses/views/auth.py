from django.shortcuts import render
from courses.models import Course , Video
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from courses.forms import RegistrationForm

def signup(request):
    if(request.method == "GET"):

       form =RegistrationForm() 
       return render(request, template_name="courses/signup.html" , context = {'form':form})
    

    form =RegistrationForm(request.POST) 
    if(form.is_valid()):
        pass;   
    return render(request, template_name="courses/signup.html" , context = {'form':form})

def login(request):
       
     
    return render(request, template_name="courses/login.html")