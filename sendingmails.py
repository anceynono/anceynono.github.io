import smtplib
content='this is a test email fron l&d services'
body='\r\n'.join(['to:%s'%'lancedsilva2000@gmail.com','from:%s'%'broxxxxxxon@gmail.com','subject:%s'%'test email',content])
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.starttls()
mail.login("broxxxxxxxxon@gmail.com","brothers123")
try:
    mail.sendmail('brxxxxxxxx@gmail.com','lanxxxxxxx0@gmail.com',content)
    print('message send')
except:
    print('error occured')
mail.close()
