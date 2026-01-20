import customtkinter as ct
from tkinter import ttk

screen = ct.CTk()
# screen.title("PASSWORD MANAGER")
screen.geometry("800x600")
screen.configure(fg_color = "#000000")

my_loginentry = ct.CTkEntry(screen,placeholder_text="User_id")
my_loginentry.place(x=350,y=300)

# my_entry.get() "Gets the input "

my_passwordentry = ct.CTkEntry(screen,placeholder_text="User_password")
my_passwordentry.place(x=350,y=350)


button= ct.CTkButton(screen,text="My_Button",fg_color="white",width=150,
                     height=50,command=my_loginentry.get())
button.place(x=350,y=400)



screen.mainloop()

