import os
from PIL import Image, ImageTk
import customtkinter as ctk

class Login(ctk.CTkFrame):
    width = 900
    height = 600
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        current_path = os.path.dirname(os.path.realpath(__file__))
       
        
        # Convert the image to a PhotoImage object
        self.img = ctk.CTkImage(Image.open(current_path + "/assets/image/bg_gradient.jpg"),size=(self.width, self.height))
        
        
        # Create a label to hold the image
        self.background = ctk.CTkLabel(self, image=self.img)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Add some widgets to the second screen
       # self.label2 = ctk.CTkLabel(self, text="Screen 2", font=("Arial", 24))
    #self.label2.pack(padx=50, pady=50)
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0)
        self.login_label = ctk.CTkLabel(self.login_frame, text="MTA Website Tools\nLogin Page",
                                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=150, pady=(15, 15))
        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.show_Dashboard, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
       
        self.login_frame.pack(padx=0, pady=150)
       
    
    def show_Dashboard(self):
        self.pack_forget()
        self.master.show_Dashboard()