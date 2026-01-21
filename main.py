import customtkinter as ct
import csv 
import pandas as pd

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


# retrives data 0f user id and password from the widget and sends to the database for checking the data
def get_userid_password():
    global Main_data_file
    o_login = my_loginentry.get()
    o_pass = my_passwordentry.get()

    data_to_append = {'Login_Id':[o_login],'Password':[o_pass]}
    data_to_append_df = pd.DataFrame(data_to_append)
    Main_data_file = pd.concat([Main_data_file,data_to_append_df],ignore_index=True)

    Main_data_file.to_csv('data.csv',index= False)










button_login= ct.CTkButton(screen,text="Login",fg_color="yellow",width=150,
                     height=50,command=get_userid_password, hover_color="darkgreen")
button_login.place(x=350,y=400)


# button_signup = ct.CTkButton(screen,text="Sign_UP",fg_color="yellow",width=150,
#                              height=50,command=)


screen.mainloop()




# def show_label1():
#     # Hide others (if they were shown) and show Label 1
#     label2.place_forget() # Removes it from the layout
#     label3.place_forget()
#     label1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER) # Show label


# btn1 = ctk.CTkButton(app, text="Show Label 1", command=show_label1)
# btn1.pack(pady=10)