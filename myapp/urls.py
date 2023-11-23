from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('index/', views.Index, name='index.html'),
    path('home/', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('salarybasedattendance/', views.Salary_based_attendance, name='salary_based_attendance'),
    path('assigntask/', views.AssignTask, name='assigntask'),
    path('attendancemanage/', views.AttendanceManage, name='attendancemanage'),
    path('leavemanage/', views.LeaveManage, name='leavemanage'),
    path('contact/', views.contact_form, name='contact_form'),
    path('bookfree/', views.bookfree, name='bookfree'),
    path('congratsfree/', views.CongratsFree, name='congratsfree'),
    path('payment.html', views.Payment, name='payment'),
    path('payment/', views.Payment, name='payment'),
    path('success_page/', views.success_page, name='success_page'),
    path('login/', views.login_view, name='login'),
    path('freedemo/', views.Freedemo, name='freedemo'),
]