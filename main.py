import customtkinter as ct


from tkinter import ttk


screen = ct.CTk()
# screen.title("PASSWORD MANAGER")
screen.geometry("800x600")



button= ct.CTkButton(screen,text="My_Button",fg_color="red")
button.place(x=100,y=200)



screen.mainloop()

