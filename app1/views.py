from django.shortcuts import render
from django.http import HttpResponse
from .utilities import mail_send,send_whatsApp_message
from .models import Messagesdetails,Customers
import datetime
from django.utils import timezone


def hello(request):
    return  HttpResponse('hello p3')

# Create your views here.
def send(request):
    # mobile = request.GET['mobilenumber']
    # gmail=request.GET['email']
    # message = request.GET['subject']

    mobile = request.POST.get("mobilenumber")
    gmail = request.POST.get("email")
    message = request.POST.get("subject")


    send_whatsApp_message(mobile, message)
    mail_send(gmail,message)
    foo_instance = Messagesdetails.objects.create(customername='not devloped',mobile = mobile,
                                                  email =gmail,message = message,sendingtime = datetime.datetime.now(tz=timezone.utc))

    return HttpResponse("""<h>message sended successfully </h> 
    <a href="/sendMessages/index">Home page link</a>""")



def mail(request):

    if request.POST.get("customername"):
        customername = request.POST.get("customername")
        customerDetails = Customers.objects.filter(customername=customername).only('mobile','email')

        for i in customerDetails:
            mobile,email = i.mobile,i.email
        print(mobile,email)
        custometList = Customers.objects.all()
        return render(request, "index.html", {'customername':customername,'custometList':custometList,'mobile':mobile,'email':email})
    custometList = Customers.objects.all()
    return render(request,"index.html",{'custometList':custometList})
