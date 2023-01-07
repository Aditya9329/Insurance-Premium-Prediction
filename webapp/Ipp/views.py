from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    res = render(request,"index.html")
    return res 