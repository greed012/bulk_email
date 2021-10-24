from django.test import TestCase

# Create your tests here.
# to do
# take user input for email and password
#take to whom they want toi send
# see if there is any error and send things accordingly
# take input for ehat one want to send

import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
sender = input('Enter your password = ')
password = input('Enter your password = ')
to = input("enter the mailing address = ")
msg = input("enter your msg here = ")
smtpObj.login(sender,password)
smtpObj.sendmail(sender,to,msg)


