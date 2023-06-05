import os
import tkinter
from PIL import Image, ImageTk
from scan import Scan1
from main_dashboard import MainDashBoard
import customtkinter as ctk

class DashBoard(ctk.CTkFrame):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
       
        # Create two screens (frames) and add them to the window
        
        # Don't pack the second screen yet - we'll do it when we switch to it
        
        # Add some widgets to the first screen

        self.main_container = ctk.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = ctk.CTkFrame(self.main_container, width=200, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
        
        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3,4,5,6,7), weight=0)
        self.left_side_panel.grid_rowconfigure((8, 9, 10, 11,12), weight=1)
        
        
        # self.left_side_panel WIDGET
        self.logo_label = ctk.CTkLabel(self.left_side_panel, text="MTA Website Tools \n", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        
        #logo MTA
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.img = ctk.CTkImage(Image.open(current_path + "/assets/image/mta.png"),size=(70, 70))
        self.logo_label_img = ctk.CTkLabel(self.left_side_panel,image=self.img, text="")
        self.logo_label_img.grid(row=0, column=0, padx=20, pady=(30, 10))


       
       
        
        # button to select correct frame IN self.left_side_panel WIDGET
        self.bt_dashboard = ctk.CTkButton(self.left_side_panel, width=180, height=35, anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/home.png"),size=(30, 30)), text="    Dashboard", command=self.dashboard)
        self.bt_dashboard.grid(row=2, column=0, padx=20, pady=10)

        self.bt_scan = ctk.CTkButton(self.left_side_panel,width=180,height=35,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/search.png"),size=(30, 30)), text="    Scan", command=self.scan)
        self.bt_scan.grid(row=3, column=0, padx=20, pady=10)
        
        self.bt_exploit = ctk.CTkButton(self.left_side_panel,width=180,height=35,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/exploit.png"),size=(30, 30)), text="    Exploit", command=self.exploit)
        self.bt_exploit.grid(row=4, column=0, padx=20, pady=10)
        
        self.bt_history = ctk.CTkButton(self.left_side_panel,width=180,height=35,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/history.png"),size=(30, 30)), text="    History", command=self.history)
        self.bt_history.grid(row=5, column=0, padx=20, pady=10)

        self.bt_help = ctk.CTkButton(self.left_side_panel,width=180,height=35,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/help.png"),size=(30, 30)), text="    Help", command=self.help)
        self.bt_help.grid(row=6, column=0, padx=20, pady=10)

        self.bt_setting = ctk.CTkButton(self.left_side_panel,width=180,height=35,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/setting.png"),size=(30, 30)), text="    Settings", command=self.setting)
        self.bt_setting.grid(row=7, column=0, padx=20, pady=10)
        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = ctk.CTkFrame(self.main_container, corner_radius=10, fg_color="black", bg_color='black')
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
        
        self.right_dashboard= MainDashBoard(self.main_container)
        #self.right_dashboard = ctk.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        #self.clear_frame()
        #self.main_dashboard= MainDashBoard(self.right_dashboard)
        #self.main_dashboard.pack(in_=self.right_dashboard, side=tkinter.LEFT,fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        

    #  self.right_dashboard   ----> dashboard widget  
    def dashboard(self):
        
        self.clear_frame()
        # self.bt_from_frame4 = ctk.CTkButton(self.right_dashboard, text="help", command=lambda:print(self.right_dashboard.winfo_height()) )
        # self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))
       
        self.main_dashboard= MainDashBoard(self.right_dashboard)
        self.main_dashboard.pack(side=tkinter.LEFT,fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    #  self.right_dashboard   ----> statement widget
    def scan(self):
        self.clear_frame()
        self.main_dashboard= Scan1(self.right_dashboard)
        self.main_dashboard.pack(side=tkinter.LEFT,fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        
    #  self.right_dashboard   ----> categories widget
    def exploit(self):
        self.clear_frame()
        self.bt_from_frame4 = ctk.CTkButton(self.right_dashboard, text="exploit", command=lambda:print("test cats") )
        self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))

    def help(self):
        self.clear_frame()
        self.bt_from_frame4 = ctk.CTkButton(self.right_dashboard, text="help", command=lambda:print("test cats") )
        self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))

    def history(self):
        self.clear_frame()
        self.bt_from_frame4 = ctk.CTkButton(self.right_dashboard, text="history", command=lambda:print("test cats") )
        self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))    

    def setting(self):
        self.clear_frame()
        self.bt_from_frame4 = ctk.CTkButton(self.right_dashboard, text="settings", command=lambda:print("test cats") )
        self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))
    # Change scaling of all widget 80% to 120%
    
        
    
            
            
    # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page       
    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()
       
        
    def show_Login(self):
        self.clear_frame()
        self.master.show_Login()

        
