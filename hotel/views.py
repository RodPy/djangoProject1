from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (resquest):
    return HttpResponse("Esto es home de hotel")
