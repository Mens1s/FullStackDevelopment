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

def atmproject2(request):
    print(1)
    return render(request, 'pages/atmproject2.html')

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
            messages.add_message(request,messages.SUCCESS,"Loged In")
            return redirect('atmproject2')
        else:
            messages.add_message(request,messages.ERROR,"Wrong Id or Password")
            return redirect('atmproject')
    def login():
        pass
