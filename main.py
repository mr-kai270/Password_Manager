import customtkinter as ct
import csv 
import pandas as pd
from random_numbers import Numbers
from eamil import MAIL

number = Numbers()
code = number.generator() # the code to be send on the email

screen = ct.CTk()
screen.title("PASSWORD MANAGER")
screen.geometry("800x600")
screen.configure(fg_color = "#000000")

my_loginentry = ct.CTkEntry(screen,placeholder_text="User_id",)
my_loginentry.place(x=350,y=300)

Main_data_file = pd.DataFrame({'Login_Id':["fsdsdf","sf"],'Password':["sddfs","fds"]})
Main_data_file.to_csv('data.csv',index=False)

Main_data_file = pd.read_csv('data.csv')

my_passwordentry = ct.CTkEntry(screen,placeholder_text="User_password")
my_passwordentry.place(x=350,y=350)



def get_userid_password():
    global Main_data_file
    o_login = my_loginentry.get()
    o_pass = my_passwordentry.get()
# retrives data 0f user id
#  and password from the widget and sends to the database for checking the data
    data_to_append = {'Login_Id':[o_login],'Password':[o_pass]}
    data_to_append_df = pd.DataFrame(data_to_append)
    Main_data_file = pd.concat([Main_data_file,data_to_append_df],ignore_index=True)

    Main_data_file.to_csv('data.csv',index= False)

button_login= ct.CTkButton(screen,text="Login",fg_color="yellow",width=150,
                     height=50,command=get_userid_password, hover_color="darkgreen")
button_login.place(x=350,y=400)


# Takes entry of te email
my_signupentry = ct.CTkEntry(screen,placeholder_text="Enter Email id")

def  send_mail_from_signupentry_mail():
    email = my_signupentry.get()
    MAIL.send_eamil(cod=code,to=email)       
#  Function sends mail from the given mail in the signup entry, takes code from random_numbers 
    




# button to send code to the user input email
button_send_code = ct.CTkButton(screen,text="Send Code",fg_color="red",command=send_mail_from_signupentry_mail)                                                                                                           
button_send_code.place(x=450,y=400)


User_code = ct.CTkEntry(screen,placeholder_text="Enter code",fg_color="white",placeholder_text_color="red")


def show_button_signup():
    my_passwordentry.place_forget()
# sign up button function closes the passwoed and login entry widget and also pop ups the 
# email dialog and send email code 
    my_loginentry.place_forget()
    button_login.place_forget()
    button_send_code.place(x=350,y=400)
    my_signupentry.place(relx=0.5,rely=0.5,anchor=ct.CENTER)
    User_code.place(x=370,y=350)
    button_to_verify.place(x=180,y=300)


# widget to take user input
def verify_code():
    user_given_code = User_code.get()    
    if user_given_code == code:
        print("sucess")
        # MAIL.send_login_id(to=my_signupentry.get(),login_id_password=)


button_to_verify = ct.CTkButton(screen,text="veifynow",fg_color="red",width=150,height=50,
                                command=verify_code)



button_signup = ct.CTkButton(screen,text="Sign_UP",fg_color="yellow",width=150,
                             height=50,command=show_button_signup)
button_signup.place(x=350,y=455)  
#  sign up -------- Button


screen.mainloop()

