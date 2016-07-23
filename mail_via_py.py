import smtplib
smtpObj=smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
usr_name_from=raw_input('enter ur gmail address:')
from_passwd=raw_input('enter passwd for this account:')
usr_name_to=raw_input('enter to gmail address:')
smtpObj.login(usr_name_from,from_passwd)
smtpObj.sendmail(usr_name_from,usr_name_to,'Hi, I am busy ryt now.\nThanks,\nSandesh')
smtpObj.quit()

