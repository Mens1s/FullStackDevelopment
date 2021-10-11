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
        print(1)
        id=request.POST["id"]
        password=request.POST["password"]
        response = bank.user(request,id,password)
        return response
    else:
        currency,value = bank.currency()
        context = {'test': currency,
                    'value' : value}
        return render(request, 'pages/atmproject.html', context)

def atmproject2(request):
    print(1)
    return render(request, 'pages/atmproject2.html')

def atmprojectuser(request):
    return render(request, "pages/atmprojectuser.html")

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
            return redirect('atmproject2')
        else:
            return redirect('atmproject')
    def register(request,id,password,name,surname):
        test = password,name,surname 
        if User.objects.filter(username = id).exists():
            return redirect('atmprojectregister')
        else:           
            user = User.objects.create(username=id,password=password,first_name=name,last_name=surname)
            user.save()
            return redirect('atmprojectuser')
