from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
#create page

def index(request):
    return render(request, 'pages/index.html')
    
def cv(request):
    return render(request,'pages/cv.html')

def projects(request):
    return render(request,'pages/projects.html')