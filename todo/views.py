from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import AddTask

# Create your views here.

def check(request):
    return render(request,'index.html')



def display_view(request):
    tasks=Task.objects.all()
    return render(request,'display.html',{'tasks':tasks})



def add_view(request):
    if request.method=='POST':
        form=AddTask(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    form=AddTask()
    return render(request,'add.html',{'form':form})



def edit_view(request,pk):
    task=get_object_or_404(Task,pk=pk)

    if request.method=='POST':
        form=AddTask(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect('home')
    

    form=AddTask(instance=task)
    return render(request,'edit.html',{'form':form})



def delete_view(request,pk):
    task=get_object_or_404(Task,pk=pk)

    if request.method=='POST':
        task.delete()
        return redirect('home')
    
    return render(request,'delete.html',{'task':task})



def complete_view(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.complete=not task.complete
    task.save()
    return redirect ('home')




def completed_view(request):
    tasks=Task.objects.filter(complete=True)
    return render(request,'completed.html',{'tasks':tasks})