# the pythonApps username and password saved in our enviroment variable
import os
from email.message import EmailMessage 
# ssl a standard tech for keeping internet connection secure, and safeguarding sensitive data 
# sent between two systems.
import ssl
# we use smtplib to send email 
import smtplib
# create a variable for email sending the message
email_sender = 'emailtesting437@gmail.com'
#get python app password saved on our enviroment variable. 
email_password = os.environ.get('PYTHON_PASS')
# create a variable for the email receieving the message
email_receiever = [ 'victorycollins31@gmail.com'] 
# crewte variale for the title of the email
subject = 'testing the email'

# create the body/content of the mail
body = """"
Hello Max, you receieved this mail becuase my email automation with python just worked. 
I am so xcited. 
"""



# instantiate EmailMessage.
# em stands for the object we'll use to write the email
em = EmailMessage()
# define some elements of the email
em['from'] = email_sender
em['to'] = email_receiever
em['subject'] = subject
# use set_content method to define the body of the mail
em.set_content(body)

# add a layer of security using ssl
context = ssl.create_default_context()

#send email using smtplib
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)


