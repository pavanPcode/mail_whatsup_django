from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utilities import mail_send,send_whatsApp_message
from .models import Messagesdetails,Customers
import datetime
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')

    else:
        return render(request,'login.html')



def hello(request):
    return  HttpResponse('hello p3')


# Create your views here.

@login_required(login_url='/login/')
def send(request):

    mobile = request.POST.get("mobilenumber")
    gmail = request.POST.get("email")
    message = request.POST.get("subject")


    send_whatsApp_message(mobile, message)
    mail_send(gmail,message)
    foo_instance = Messagesdetails.objects.create(customername='not devloped',mobile = mobile,
                                                  email =gmail,message = message,sendingtime = datetime.datetime.now(tz=timezone.utc))

    return HttpResponse("""<h>message sended successfully </h> 
    <a href="/">Home page link</a>""")

@login_required(login_url='/login/')
def page_logout(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def mail(request):

    if request.POST.get("customername"):
        customername = request.POST.get("customername")
        customerDetails = Customers.objects.filter(customername=customername).only('mobile','email')

        for i in customerDetails:
            mobile,email = i.mobile,i.email

        custometList = Customers.objects.all()
        return render(request, "index.html", {'customername':customername,'custometList':custometList,'mobile':mobile,'email':email})
    custometList = Customers.objects.all()
    return render(request,"index.html",{'custometList':custometList})
