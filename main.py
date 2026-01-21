import customtkinter as ct
import csv 
import pandas as pd

screen = ct.CTk()
screen.title("PASSWORD MANAGER")
screen.geometry("800x600")
screen.configure(fg_color = "#000000")

my_loginentry = ct.CTkEntry(screen,placeholder_text="User_id",)
my_loginentry.place(x=350,y=300)

df = pd.DataFrame({'Login_Id':["fsdsdf","sf"],'Password':["sddfs","fds"]})
df.to_csv('data.csv',index=False)

df = pd.read_csv('data.csv')

my_passwordentry = ct.CTkEntry(screen,placeholder_text="User_password")
my_passwordentry.place(x=350,y=350)


def get_userid_password():
    global df
    o_login = my_loginentry.get()
    o_pass = my_passwordentry.get()

    data_to_append = {'Login_Id':[o_login],'Password':[o_pass]}
    data_to_append_df = pd.DataFrame(data_to_append)
    df = pd.concat([df,data_to_append_df],ignore_index=True)

    df.to_csv('data.csv',index= False)


button= ct.CTkButton(screen,text="My_Button",fg_color="blue",width=150,
                     height=50,command=get_userid_password, hover_color="darkgreen")
button.place(x=350,y=400)




screen.mainloop()




# def show_label1():
#     # Hide others (if they were shown) and show Label 1
#     label2.place_forget() # Removes it from the layout
#     label3.place_forget()
#     label1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER) # Show label


# btn1 = ctk.CTkButton(app, text="Show Label 1", command=show_label1)
# btn1.pack(pady=10)