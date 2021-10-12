from django.http.request import UnreadablePostError
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def projects(request):
    return render(request, 'pages/projects.html')

def atmproject(request):
    if request.POST:
        id=request.POST["id"]
        password=request.POST["password"]
        response = bank.user(request,id,password)
        return response
    else:
        currency,value = bank.currency()
        context = {'test': currency,
                    'value' : value}
        return render(request, 'pages/atmproject.html', context)

def atmprojectuser(request):
    name = request.user.first_name
    surname = request.user.last_name
    money = request.user.money
    context = {'name':name,
                'surname':surname,
                'money':money,}
    return render(request, "pages/atmprojectuser.html",context)

def atmprojectregister(request):
    if request.POST:
        id=request.POST["id"]
        password=request.POST["password"]
        name=request.POST["name"]
        surname=request.POST["surname"]
        response = bank.register(request,id,password,name,surname)
        return response
    else:
        currency,value = bank.currency()
        context = {'test': currency,
                    'value' : value}
        return render(request, "pages/atmprojectregister.html", context)
class bank():

    def currency():
        rates = requests.get("https://v1.nocodeapi.com/test123213/cx/ERFlVAPtciohTySe/rates").json()
        rates = rates['rates']

        unit = []
        value = []
        for a in rates:
            unit.append(a)
            value.append(rates[a])
        return unit,value
    def user(request,id,password):
        user = auth.authenticate(username=id,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('atmprojectuser')
        else:
            return redirect('atmproject')
    def register(request,id,password,name,surname):
        if User.objects.filter(username = id).exists():
            return redirect('atmprojectregister')
        else:           
            user = User.objects.create(username=id,password=password,first_name=name,last_name=surname)
            user.save()
            return redirect('atmprojectuser')
