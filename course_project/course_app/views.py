from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import*
from . import models
from django.conf import settings
# Create your views here.


def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '505.html', status=500)

def index(request):
    context={'courses':getallcourse() ,
            "descriptions" :getalldescription()}
    
    return render (request,'index.html',context  )



def course_add(request):
    if request.method == 'POST':
        try:
            errors = Course.objects.basic_validator(request.POST)
            
            if len(errors)> 0:
                for key, value in errors.items():
                    messages.error(request, value)
            else:
                name = request.POST.get('name', '')
                description = request.POST.get('description', '')
                desc = create_description(description)
                course = addcourse(name, desc)
                messages.success(request, "Course successfully added.")
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            # Log the exception for further investigation if necessary
    
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
