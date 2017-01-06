import smtplib
import datetime
import time

hs = 0 # SELECT THE HOUR
ts = 0
ss = 0

# Account for send
username = 'sender@gmail.com'
password = 'password'

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    print ('CORRECT LOGIN!')
except:
    print ('Wrong login, change parameters!')
    raise SystemExit

print ('The message will be sent at: %s:%s.%s' % (hs,ts,ss))

# Destination, Subject and Text
TO = 'dest.example@gmail.com'
SUBJECT = 'Subject example'
TEXT = 'Text example'
# Merging message
MSG = ("""From: {0}\nTo: {1}\nSubject: {2}\n\n{3} """.format(username, TO, SUBJECT, TEXT))

force=False

# Start countdown
while True:
    isnow = datetime.datetime.now() #get time
    if isnow.hour == hs and isnow.minute == ts and isnow.second == ss or force == True:
        hold = datetime.datetime.now()
        try: # try to send
            server.sendmail(username, TO, MSG)
            server.quit()
            issent = datetime.datetime.now()
            delay = issent - hold
            print ('*--------------------------------------------------------------------*')
            print ('| Successfully sent the mail at {0}:{1}.{2} with {3} s of delay |'.format(isnow.hour, isnow.minute, isnow.second, delay))
            print ('*--------------------------------------------------------------------*\n')
            break
        except: # force mode in case of fail to send
            print ('Failed to send mail from {0} at {1}:{2}.{3}\n FORCE SEND ACTIVATED!'.format(username, isnow.hour, isnow.minute, isnow.second))
            force=True
    else: # waiting for the right time
        print ('Not yet sended, is {0}:{1}.{2}'.format(isnow.hour, isnow.minute, isnow.second))
        time.sleep(0.05)
