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
        errors = Course.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
    # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
    # redirect the user back to the form to fix the errors
        name=request.POST['name']
        description=request.POST['description']
        desc=create_description(description)
        course=addcourse(name,desc)
    return redirect('/')


def delete_course(request):
    if request.method == 'POST':
        id = request.POST.get("cid")
        course=get_object_or_404(Course,id=id)
        course.delete()
    return redirect('/')  # Redirect to home 

def confirm_delete(request, id):
    course = get_object_or_404(Course, id=id)
    print(course)
    return render(request, 'confirm_delete.html', {'course': course})


def comment(request,id):
    context={'Comment':getallcomment() ,
            'course':get_data_course(id)
    }    
    return render (request,'comment.html',context  )


def add_comment(request,id):
    if request.method =='POST':
        name=get_data_course(id)
        comment=request.POST['comment']
        create_comment(comment,name)
    return redirect('comment',id=id)
# else:
#   return render(request, 'comment.html')
