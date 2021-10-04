from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('hello home page')
def starting_page(request):
    return HttpResponse('this is the first page you are seing like khudra.com.np')