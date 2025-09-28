from django.shortcuts import render
from .models import Task

# Create your views here.

def check(request):
    return render(request,'index.html')



def display_view(request):
    tasks=Task.objects.all()
    return render(request,'display.html',{'tasks':tasks})