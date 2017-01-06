# Automatic Python Mail Sender

A little script for send in a choose time (with less than 1s of delay) the mail that you want. There is a brute force mode in case of failing after the first try. Useful for automatic Jobs, you can run it in FreeBSD or with Automator in macOS for example.
The script is now compatible with Python 3.x.

## Getting Started

This software works with all version of Python above 3.6.x

### Prerequisites

To run this script you need to have Python installed.

```
brew install python
```

### From ask to pre-defined

If you'll use this script with the same message, destination address, or something else... You prefer the predefined version of the software. When you choose the second one (definemailsend.py) you need to change all the part of the code properly.

```
from:
  username = 'example@gmail.com'
to:
  username = 'jacopo.nasi@gmail.com'
```

## Running the tests

To run the system run simply:
```
python mailsend.py
```
or
```
python definemailsend.py
```

# How it works?

This script use the SMTP library, datetime and time library.
### mailsend.py
  This Python ask the user input (with the classic UNIX encryption view for the passoword) of the of the sender account and check if it's work, if not re-ask the data. After that the time camps are verified, the minutes can't be higher than 59, ecc... While the cycle wait until the right send time print the 'Not yet send...' message, when it start if everything is okay will print a confirmation output in case of fail it will active the force mode that try to send the message until it works (20 times for second).
### definemailsend.py
  This Python don't ask anything to the user and it will not verify the input of the user a part from the account information and if they are wrong stop the execution.
  While the cycle wait until the right send time print the 'Not yet send...' message, when it start if everything is okay will print a confirmation output in case of fail it will active the force mode that try to send the message until it works (20 times for second).
### Output Example
```
Choose the send time
Hours: 10
Minute: 14
Second: 10
The message will be sent at: 10:13.59
Sender mail (omit @gmail.com): jacopo.nasi
Password for jacopo.nasi@gmail.com: [encrypt simbol]
*---------------*
| Correct login |
*---------------*
Destinator: jacopo.nasi@gmail.com
Subject: prova
Text: prova
Not yet sended, is 10:14.7
Not yet sended, is 10:14.7
Not yet sended, is 10:14.8
...
*-----------------------------------------------------------------*
| Successfully sent the mail at 10:14.10 with 0.102677 s of delay |
*-----------------------------------------------------------------*
```
## Dependencies

* [smtplib] - For SMTP framework
* [datetime] - Date time Library
* [time] - Time library
* [getpass] - Getting encrypted password

## Built With

* [Python](http://pythoncentral.io) - The programming language


## Authors

* **Jacopo Nasi** - *Initial work* - [Jacopx](https://github.com/Jacopx)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Use at your own risk
* I'm not responsible of your use of this code
