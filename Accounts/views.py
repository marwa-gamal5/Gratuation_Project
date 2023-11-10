from django.shortcuts import render
from django.shortcuts import render , redirect
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import *
from django.conf import settings
from django.core.mail import EmailMessage, get_connection
from django.contrib import messages
import re



def sign_up(request):
    if request.method == 'POST':
        fn=request.POST.get('first_name')
        ls=request.POST.get('last_name')
        un=request.POST.get('username')
        em=request.POST.get('email')
        pwd=request.POST.get('password')
        conP=request.POST.get('conP')
        
        
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        reg=r'\b[A-Za-z0-9._%+-].[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\.[A-Z|a-z]{2,7}\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, em) or re.fullmatch(reg, em)):
            new_user = User.objects.create_user(un,em,pwd)
            # new_user.first_name = fn
            # new_user.last_name = ls
            new_user.save()
            return redirect('login')
        else:
           messages.error(request,("email invalid"))
    return render(request,'sign_up.html',{})



def Login(request):
    if request.method=='POST':
         name=request.POST.get('uname')
         password=request.POST.get('pass')
         user=authenticate(request,username=name,password=password)
         if user is not None:
            login(request,user)
            return redirect('sign_up')
         else:
            messages.error(request,("username or password invalid"))
    return render(request, 'login.html')