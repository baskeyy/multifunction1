from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def max(request):
    return HttpResponse('<marquee><h1>justise legue</h1></marquee>')