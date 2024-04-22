from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.

# Create your views here.
def home(request):
     return render(request,"index.html")
def contact(request):
     if request.method=="POST":
          contact=Contact()
          name=request.POST.get("name")
          email=request.POST.get("email")
          message=request.POST.get("message") 
          contact.name=name 
          contact.email=email
          contact.message=message
          contact.save()
          context={}
          context['success']="Thank For Contact Me !!"
     return render(request,'index.html',context)