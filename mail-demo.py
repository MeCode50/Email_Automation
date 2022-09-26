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
## create a variable for the email receieving the message
email_receiever = [ 'victorycollins31@gmail.com'] 
# crewte variale for the title of the email

# instantiate EmailMessage.
# em stands for the object we'll use to write the email
em = EmailMessage()
# define some elements of the email
em['from'] = email_sender
em['to'] = email_receiever
em['subject'] = 'check this out'


# use set_content method to define the body of the mail
em.set_content('This is a plain text email')

em.add_alternative("""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testing</title>
</head>
<body>
    <h1 style="color:blue;">This is a testing email</h1>
</body>
</html>
""", subtype='html')

# add a layer of security using ssl
context = ssl.create_default_context()

#send email using smtplib
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)


