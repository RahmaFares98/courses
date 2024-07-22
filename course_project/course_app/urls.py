from django.urls import path
from . import views

urlpatterns = [
    path ('' , views.index , name ='index'),
    path ('course_add' , views.course_add , name ='course_add'),
    path('confirm_delete/<int:id>/',views.confirm_delete,name='confirm_delete'),
    path('delete_course',views.delete_course ,name='delete_course'),


]