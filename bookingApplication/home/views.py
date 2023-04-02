from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "home/homepage.html")



def aboutPage(request):
    return HttpResponse("About Page")