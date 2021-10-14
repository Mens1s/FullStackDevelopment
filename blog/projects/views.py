from django.http.request import UnreadablePostError
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Customer
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

# Create nnew page
def atmprojectuser(request):
    name = Customer.first_name
    surname = Customer.last_name
    money = Customer.balance
    context = {'name':name,
                'surname':surname,
                'balance':money,}
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
            messages.add_message(request, messages.ERROR, "Id or Password is wrong!")
            return redirect('atmproject')
    def register(request,id,password,name,surname):
        if Customer.objects.filter(username = id).exists():
            messages.add_message(request, messages.ERROR, "Id is still using!")
            return redirect('atmprojectregister')
        else:   
            user = Customer.objects.create(username=id,password=password,first_name=name,last_name=surname,balance="0")   
            userAdmin = User.objects.create(username=id,password=password)    
            userAdmin.save()
            user.save()
            return redirect('atmprojectuser')
