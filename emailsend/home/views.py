from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail
def index(request):
    return render(request,'index.html')
def home(request):
    subject = request.POST['sub']
    message = request.POST['msg']
    to=request.POST['to']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to, ]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'home.html')
