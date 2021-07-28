from django.shortcuts import render
from django.http import  HttpResponse

def DocsPage(request):
    return render(request, "OnlineHelp/docs.html")

def Cover(request):
    return render(request, "Cover.html")

def MainPage(request):
    return render(request, "OnlineHelp/index.html")
# Create your views here.
