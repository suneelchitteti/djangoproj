from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return render(request,"suneel.html",{"suneel":"8190904730"})
def welcome1(request):
    return HttpResponse("<html><body><h1><marquee><center>Are you looking for python developer job</center></h1></body></html></marquee>")
# Create your views here.
