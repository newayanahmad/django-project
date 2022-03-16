from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib import messages

# Create your views here.

def account(request,slug):
    if request.method=='POST':
        try:
            name=request.POST['name'].title()
            email=request.POST['email'].lower()
            password=request.POST['password']
            email_count=CustomUser.objects.filter(username=email).count()
            if email_count!=0:
                message= messages.error(request, 'Email already registered! Try using another email')
                return render(request, 'login.html', {'height':360, 'margin_back':147, 'margin_form':-306, 'messages': message})
            else:
                newuser=CustomUser.objects.create_user(email=email, name=name, password=password, username=name)
                newuser.save()
                user=authenticate(email=email, password=password)
                login(request, user)
                return redirect('/')
        except:
            email=request.POST['loginemail']
            password=request.POST['loginpassword']
            user=authenticate(email=email, password=password)
            if user==None:
                mes=messages.error(request, "Invalid credentials!")
                print(mes)
                return render(request, 'login.html', {'height':263, 'margin_back':37, 'margin_form':0, 'messages':mes})
            else:
                login(request, user)
                return redirect('/')
    
    if slug.lower()=='register':                
        return render(request, 'login.html', {'height':470, 'margin_back':147, 'margin_form':-306})
    elif slug.lower()=='login':
        return render(request, 'login.html', {'height':300, 'margin_back':37, 'margin_form':0})
    else:
        api(request, slug)
    
def logout_user(request):
    logout(request)
    return redirect('/')

def api(request, name):

    return JsonResponse({'name':name,'query':'request'})


def home(request):
    return render(request, 'home.html')
