from .models import Student
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    context={}
    return render(request, 'In_Out_student/register.html', context)