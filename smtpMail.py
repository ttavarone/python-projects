import smtplib

smtpServer = 'smtp.gmail.com'
loginEmail = 'ttavarone@gmail.com'
password = 'hyrdetxanptsxrhg'

recipient = 'ttavarone@me.com'

subject = 'B=D'
body = 'Penis'

smtpObj = smtplib.SMTP(smtpServer, 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(loginEmail, password)
for x in range(1):
	smtpObj.sendmail(loginEmail, recipient, 'Subject: '+subject+str(x)+' \n'+body)
	body += body[1:]
	# for y in range(10**x):
	# 	body += "penis"
smtpObj.quit()