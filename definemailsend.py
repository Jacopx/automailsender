import smtplib
import datetime
import time

hs = 0 # SELECT THE HOUR
ts = 0 
ss = 0

print 'The message will be sent at: %s:%s.%s' % (hs,ts,ss)

# Account for send
username = 'example@gmail.com'
password = 'password'

# Destination, Subject and Text
TO = 'dest@gmail.com'
SUBJECT = 'Subject example'
TEXT = 'Text example'
# Merging message
MSG = """From: %s\nTo: %s\nSubject: %s\n\n%s """ % (username, TO, SUBJECT, TEXT)

force=False

# Start countdown
while True:
    isnow = datetime.datetime.now() #get time
    if isnow.hour == hs and isnow.minute == ts and isnow.second == ss or force == True:
        hold = datetime.datetime.now()
        try: # try to send
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(FROM, TO, MSG)
            server.quit()
            issent = datetime.datetime.now()
            delay = issent - hold
            print '-------------------------------------------------------------------'
            print 'Successfully sent the mail at %s:%s.%s with %s of delay' % (isnow.hour, isnow.minute, isnow.second, delay)
            print '-------------------------------------------------------------------\n'
            break
        except: # force mode in case of fail to send
            print 'Failed to send mail from %s at %s:%s.%s\n FORCE SEND ACTIVATED!' % (username, isnow.hour, isnow.minute, isnow.second)
            force=True
    else: # waiting for the right time
        print 'Not yet sended, is %s:%s.%s' % (isnow.hour, isnow.minute, isnow.second)
        time.sleep(0.05)
