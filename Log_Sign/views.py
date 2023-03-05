
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'Log_Sign/index.html', context)

def staff_log_sign(request):
    context = {}
    return render(request, 'Log_Sign/staff_log_sign.html', context)

def student_log_sign(request):
    context = {}
    return render(request, 'Log_Sign/student_log_sign.html', context)
