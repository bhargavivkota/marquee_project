from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse('<h1><marquee><font color=red><i><b>Hi hello srujana</b></i></font></marquee></h1>')