from django.urls import path
from . import views

handler404 = 'course_app.views.error_404'
handler500 = 'course_app.views.error_500'


urlpatterns = [
    path ('' , views.index , name ='index'),
    path ('course_add' , views.course_add , name ='course_add'),
    path('confirm_delete/<int:id>/',views.confirm_delete,name='confirm_delete'),
    path('delete_course',views.delete_course ,name='delete_course'),
    path('addComment/<int:id>',views.add_comment,name='addComment'),
    path('comment/<int:id>',views.comment , name='comment'),



]