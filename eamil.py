import smtplib

class MAIL():
    def send_eamil(cod,to):


        my_eamil = "priyanshuranjan7004@gmail.com"
        password = "wapcmcrqczzxymxn"

        connections = smtplib.SMTP("smtp.gmail.com")
        connections.starttls()
        connections.login(user=my_eamil, password=password)
        connections.sendmail(from_addr=my_eamil, to_addrs=to
                             , msg=cod)
        connections.close()
    def send_login_id(to,login_id_password):

        
        my_eamil = "priyanshuranjan7004@gmail.com"
        password = "wapcmcrqczzxymxn"

        connections = smtplib.SMTP("smtp.gmail.com")
        connections.starttls()
        connections.login(user=my_eamil,password=password)
        connections.sendmail(from_addr=my_eamil,to_addrs=to,msg=login_id_password)
        connections.close()

