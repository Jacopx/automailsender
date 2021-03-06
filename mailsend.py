import smtplib
import datetime
import time
import getpass

hs=-1
ts=-1
ss=-1
print ('Choose the send time')

# Choose the send time
while hs>23 or hs<0:
    hs = int(input('Hours: '))
while ts>59 or ts<0:
    ts = int(input('Minute: '))
while ss>59 or ss<0:
    ss = int(input('Second: '))

print ('The message will be sent at: {0}:{1}.{2}'.format(hs,ts,ss))

while True:
    username = input('Sender mail (omit @gmail.com): ')
    username = ('%s@gmail.com' % username)
    password = getpass.getpass('Password for ' + username +  ': ')
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        break
    except:
        print ('Wrong login, retry:')

print ('*---------------*')
print ('| Correct login |')
print ('*---------------*')

# Destination, Subject and Text
TO = input('Destinator: ')
SUBJECT = input('Subject: ')
TEXT = input('Text: ')
# Merging message
MSG = ("""From: {0}\nTo: {1}\nSubject: {2}\n\n{3}""".format(username, TO, SUBJECT, TEXT))

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
            print ('*----------------------------------------------------------------------*')
            print ('| Successfully sent the mail at {0}:{1}.{2} with {3} s of delay |'.format(isnow.hour, isnow.minute, isnow.second, delay))
            print ('*----------------------------------------------------------------------*\n')
            break
        except: # force mode in case of fail to send
            print ('Failed to send mail from {0} at {1}:{2}.{3}\n FORCE SEND ACTIVATED!'.format(username, isnow.hour, isnow.minute, isnow.second))
            force=True
    else: # waiting for the right time
        print ('Not yet sended, is {0}:{1}.{2}'.format(isnow.hour, isnow.minute, isnow.second))
        time.sleep(0.05)
