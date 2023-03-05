from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', include('In_Out_student.urls')),
    path('staff/', include('In_Out_staff.urls')),
    path('student_log_sign/', views.student_log_sign, name='student_log_sign'),
    path('staff_log_sign/', views.staff_log_sign, name='staff_log_sign'),
] 