import customtkinter as ct
import csv 
import pandas as pd

screen = ct.CTk()
screen.title("PASSWORD MANAGER")
screen.geometry("800x600")
screen.configure(fg_color = "#000000")

my_loginentry = ct.CTkEntry(screen,placeholder_text="User_id",)
my_loginentry.place(x=350,y=300)

df = pd.read_csv('data.csv')

my_passwordentry = ct.CTkEntry(screen,placeholder_text="User_password")
my_passwordentry.place(x=350,y=350)


def get_userid_password():
    o_login = my_loginentry.get()
    o_pass = my_passwordentry.get()
    # with open ('data.csv' , 'w') as csvfile:
        # fieldnames = ['LOGIN_ID','PASSWORD']
        # writer = csv.DictWriter(csvfile,fieldnames=fieldnames)



        # writer.writeheader()
        # writer.writerow({'LOGIN_ID': o_login,
                        #  'PASSWORD':o_pass})
    df[o_login] = [o_pass]
    df.to_csv('data.csv', index= False)                    







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