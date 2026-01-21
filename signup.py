import customtkinter as ct
from customtkinter import CTkEntry

class SIGNUP(CTkEntry):
    def __init__(self,label1,label2):
        # super().__init__()
        label1.place_forget()
        label2.place_forget()
        self.place(relx=0.5, rely=0.5,x=350,y=400)