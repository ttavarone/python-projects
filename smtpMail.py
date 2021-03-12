import smtplib

smtpServer = 'smtp.gmail.com'
loginEmail = 'ttavarone@gmail.com'
password = 'hyrdetxanptsxrhg'

recipient = 'ttavarone@me.com'

subject = ''
body = ''

smtpObj = smtplib.SMTP(smtpServer, 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(loginEmail, password)
smtpObj.sendmail(loginEmail, recipient, 'Subject: '+subject+' \n'+body)
smtpObj.quit()