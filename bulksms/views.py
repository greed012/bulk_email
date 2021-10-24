from django.http import HttpResponse
from django.shortcuts import render
from .models import Bulkmsg
import smtplib
import re

regexObject = re.compile(r'.*')

def index(request):
    if request.method == "POST":
        sender = request.POST.get('sender', '')
        password = request.POST.get('password', '')
        receiver = request.POST.get('receiver', '')
        msg = request.POST.get('msg', '')
        details = Bulkmsg(sender=sender, password=password, receiver=receiver, msg=msg)
        details.save()
        return render(request, "index.html")
        sendsms()
    else:
        return render(request, "index.html")




def sendsms():
    data = Bulkmsg.objects.values('sender', 'password','receiver','msg')
    length = len(data)
    actualdata = data[length-1]
    print(actualdata)
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    sender1 = actualdata['sender']
    password1 = actualdata['password']
    msg1 = actualdata['msg']
    receiver1= actualdata['receiver']
    mo = regexObject.findall(receiver1)
    smtpObj.login(sender1, password1)
    for j in mo:
        if j == "":
            mo.remove(j)
    print(len(mo))
    for i in range(0, len(mo)):
        receiver1 = mo[i]
        print(receiver1)
        smtpObj.sendmail(sender1, receiver1, msg1)




