#! python3

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn) # Checking if it worked
conn.ehlo() # Need this function to start the connection

# Logging in to your gmail to send emails from
conn.starttls() # Encrypts password
conn.login('yourEmailGoesHere@gmail.com', 'yourPasswordGoesHere') # Email and password go here
conn.sendmail('yourEmailGoesHere', 'yourTargetGoesHere', 'Subject: Subject goes here...\n\nWe are in the body now. You need the 2 new lines to be able to write in the body')
conn.quit()