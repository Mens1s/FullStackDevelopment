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
        with open("log.txt", "w") as log:
            log.write(id)
            log.close()
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
    with open("log.txt","r") as log:
        id = log.read()
    customer = Customer.objects.get(username=id)
    if request.POST:
        money = request.POST["money"]
        type = request.POST["type"]
        confirm = request.POST["confirm"]

        if str(type).lower() == "withdraw":
            if int(money) > int(customer.balance):
                messages.add_message(request, messages.ERROR, "Your money doesn't enough!")
            else:
                if str(confirm).lower() == "confirm":
                    customer.balance -= int(money)
                    customer.save()
                    messages.add_message(request, messages.SUCCESS, "Your order have done succesfuly.")
                else:
                    messages.add_message(request, messages.ERROR, "Please control 'confirm'. ")
        else:
            if str(confirm).lower() == "confirm":
                customer.balance += int(money) 
                customer.save()  
                messages.add_message(request, messages.SUCCESS, "Your order have done succesfuly.")

            else:
                messages.add_message(request, messages.ERROR, "Please control 'confirm' .")
    
    name = customer.first_name
    surname = customer.last_name
    money = str(customer.balance)
    context = {'name':name,
                'surname':surname,
                'balance':money,}
    return render(request, "pages/atmprojectuser.html",context)

def atmprojectregister(request):
    if request.POST:
        id=request.POST["id"]
        with open("log.txt","w") as log:
            log.write(id)
            log.close()
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