import tkinter
import smtplib


from tkinter import ttk

my_eamil = "priyanshuranjan7004@gmail.com"
password = "wapcmcrqczzxymxn"


connections = smtplib.SMTP("smtp.gmail.com")
connections.starttls()
connections.login(user=my_eamil, password=password)
connections.sendmail(from_addr=my_eamil,to_addrs="priyanshuranjan2700@gmail.com"
                     ,msg="Hello")
connections.close()