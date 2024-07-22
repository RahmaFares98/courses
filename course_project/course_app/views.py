from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import*
from . import models

# Create your views here.
def index(request):
    context={'courses':getallcourse() ,
            "descriptions" :getalldescription()}
    
    return render (request,'index.html',context  )

def course_add (request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        desc=create_description(description)
        course=addcourse(name,desc)
    return redirect('/')


def delete_course(request):
    if request.method == 'POST':
        id = request.POST.get("cid")
        show=get_object_or_404(models.Course,id=id)
        show.delete()
    return redirect('/')  # Redirect to home 

def confirm_delete(request, id):
    course = get_object_or_404(models.Course, id=id)
    print(course)
    return render(request, 'confirm_delete.html', {'course': course})
