"""
Basic template to set up logging and mailsending for errorhandling in a system.

"""
import logging
from logging.handlers import RotatingFileHandler
import logging.handlers as handlers
import smtplib
from datetime import date
from datetime import timedelta

#Setting up logging using rotation.
log_file = 'c:\\scripts\\example.log' 
logging.basicConfig(
        handlers=[RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)],
        level=logging.INFO,
        format='%(asctime)s, %(message)s ',
        datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()  # get the root logger


#Checking for last success entry in reversed example.log and setting up email sending with last successdate if error occurs.
today = date.today()
yesterday = today - timedelta(days=1)
success = []
for line in reversed(list(open(log_file))):
    if "Success" in line:
        success.append(line)
        break
if len(success) < 9:
    last_date = yesterday
else:
    last_date = success[0][:10]


#Mailsetup.
sender = 'Name <example@sender.com>'
receiver = 'reciever@example.com'
host ='smtp server'
server = smtplib.SMTP(host)                      

subject = 'Error in system'
body = f'An error has occured in examplesystem.Last successful date: Date: {last_date}. Check log: example.log \n\n Regards systemadmin examplesystem.'

msg = 'Subject: ' + subject + ' \n\n' + body

#Remaining logic kept out due to company spesifics. Adjust as needed.