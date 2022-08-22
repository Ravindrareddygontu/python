import smtplib
import pandas as pd
from datetime import datetime
import os

currentpath = os.getcwd()
print(currentpath)
os.chdir(currentpath)
email_id = input("Enter emailid:")
password = input("enter password:")

def my_function(to, sub, msg):
    print(f"Email to {to} sent: \nSubject: {sub} ,\nMessage: {msg}")
    try:
        s = smtplib.SMTP("smtp.gmail.com:587")
        s.starttls()
        s.login(email_id, password)
        s.sendmail(email_id, to, f"subject:{sub}/n/n{msg}")
        print('success')
    except smtplib.SMTPAuthenticationError:
        print('login failed')
    s.quit()

file = pd.read_excel("data.xlsx")

today = datetime.now().strftime("%d-%m")
year_now = datetime.now().strftime("%y")
for row,column in file.iterrows():
    bday = column["birthday"]
    print(column)
   
    bday = bday.strftime("%d-%m")
  
    birthyear = []
    print(column['email'])
    if bday==today and year_now not in str(column["lastBirthyear"]):
        print(column['email'])
        my_function(column["email"],"Happy Birthday",column["dialogue"])
        birthyear.append(row)
        print(birthyear)
if birthyear != None:
        for i in birthyear:
            oldyear = file.loc[i,"lastBirthyear"]
            file.loc[i,"lastBirthyear"] = (str(oldyear)+" "+str(year_now))
file.to_excel('data.xlsx', index = False)
            
