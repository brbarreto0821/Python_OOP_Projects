Setup:

Open the command line and enter:

$ cd ..\MailListManager
$ python -m smtpd -n -c DebuggingServer localhost:1025

Open a second command line window and enter:

$ cd ..\MailListManager
$ python mailing.py
$ python send.py

The output will be in the first command line window.