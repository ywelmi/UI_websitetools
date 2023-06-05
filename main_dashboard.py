import os
import tkinter as tkinter
from PIL import Image, ImageTk
import customtkinter as ctk

class MainDashBoard(ctk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        
      
        self.winfo_height().as_integer_ratio
        
        # main top 
        self.main_top = ctk.CTkFrame(self,height=180,width=master.winfo_width(),fg_color='#2b2b2b')
        self.main_top.pack( fill=tkinter.X, expand=True, padx=5)
        #self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.main_top.grid_columnconfigure((0,1,2), weight=1)
        self.main_top.configure(border_width=2)
        self.main_top.configure(border_color='white')
# Set the relief style to 'ridge'
        #self.main_top.configure(relief="ridge")

        self.high_severity = ctk.CTkFrame(self.main_top, height=150, width=150, corner_radius=85, fg_color='red')
        self.high_severity.grid(column=0, row=0)

        self.inside = ctk.CTkFrame(self.main_top, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.inside.grid(row=0, column=0)

        self.high_severity_data = ctk.CTkLabel(self.main_top, text="5", font=ctk.CTkFont(size=40, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.high_severity_data.grid(row=0)

        self.high_severity_label = ctk.CTkLabel(self.main_top, text="High Severity Vulnerabilities", font=ctk.CTkFont(size=20, weight="bold"),text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.high_severity_label.grid(row=0, pady=(215,10), column=0)
        
        self.medium_severity = ctk.CTkFrame(self.main_top, height=150, width=150, corner_radius=85, fg_color='red')
        self.medium_severity.grid(column=1, row=0)

        self.medium_inside = ctk.CTkFrame(self.main_top, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.medium_inside.grid(row=0, column=1)
        
        self.medium_severity_data = ctk.CTkLabel(self.main_top, text="5", font=ctk.CTkFont(size=40, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.medium_severity_data.grid(row=0, column=1)

        self.medium_severity_label = ctk.CTkLabel(self.main_top, text="Medium Severity Vulnerabilities", font=ctk.CTkFont(size=20, weight="bold"),text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.medium_severity_label.grid(row=0, pady=(215,10), column=1)

        self.low_severity = ctk.CTkFrame(self.main_top, height=150, width=150, corner_radius=85, fg_color='red')
        self.low_severity.grid(column=2, row=0)

        self.low_inside = ctk.CTkFrame(self.main_top, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.low_inside.grid(row=0, column=2)
        
        self.low_severity_data = ctk.CTkLabel(self.main_top, text="5", font=ctk.CTkFont(size=40, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.low_severity_data.grid(row=0, column=2)

        self.low_severity_label = ctk.CTkLabel(self.main_top, text="Low Severity Vulnerabilities", font=ctk.CTkFont(size=20, weight="bold"),text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.low_severity_label.grid(row=0, pady=(215,10), column=2)
        
        #------------------------------------------------------

        # sacn information
        self.scan_information = ctk.CTkFrame(self,height=85, width=master.winfo_width(), fg_color="white", bg_color='black')
        self.scan_information.pack( fill=tkinter.X, expand=True, padx=5)
        self.scan_information.grid_columnconfigure((0,1,2,3), weight=1)
        #scan running
        self.scan_running_label = ctk.CTkLabel(self.scan_information, text="Scan running", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.scan_running_label.grid(row=0, pady=(25,5), padx=25, column=0)

        self.scan_running = ctk.CTkLabel(self.scan_information, text="5", font=ctk.CTkFont(size=28, weight="bold"),text_color='red', fg_color='white', bg_color='white')
        self.scan_running.grid(row=1, pady=(0,10), column=0)
        #scan waiting
        self.scan_waiting_label = ctk.CTkLabel(self.scan_information, text="Scan waiting", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.scan_waiting_label.grid(row=0, pady=(25,5), column=1)

        self.scan_waiting = ctk.CTkLabel(self.scan_information, text="5", font=ctk.CTkFont(size=28, weight="bold"),text_color='red', fg_color='white', bg_color='white')
        self.scan_waiting.grid(row=1, pady=(0,10), column=1)
        #total scan conducted
        self.scan_conducted_label = ctk.CTkLabel(self.scan_information, text="Total scan conducted", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.scan_conducted_label.grid(row=0, pady=(25,5), column=2)

        self.scan_conducted = ctk.CTkLabel(self.scan_information, text="5", font=ctk.CTkFont(size=28, weight="bold"),text_color='red', fg_color='white', bg_color='white')
        self.scan_conducted.grid(row=1, pady=(0,10), column=2)
        #total targets
        self.scan_targets_label = ctk.CTkLabel(self.scan_information, text="Total targets", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white')
        self.scan_targets_label.grid(row=0, pady=(25,5), column=3)

        self.scan_targets = ctk.CTkLabel(self.scan_information, text="5", font=ctk.CTkFont(size=28, weight="bold"),text_color='red', fg_color='white', bg_color='white')
        self.scan_targets.grid(row=1, pady=(0,10), column=3)
        
        #------------------------------------------------------
        self.main_center = ctk.CTkFrame(self,height=400, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_center.pack( fill=tkinter.X, expand=True, padx=5)
        self.main_center.grid_columnconfigure((0,1), weight=1)

        self.left_main_center = ctk.CTkFrame(self.main_center,height=300,width=650, fg_color="white")
        self.left_main_center.grid(row=0,sticky="nw",column=0)
        self.most_target_label = ctk.CTkLabel(self.left_main_center, text="Most Vulnerable Target", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white', width=560)
        self.most_target_label.grid(row=0, pady=(25,5),sticky="nw", padx=10, column=0)
        self.left_main_center.grid_columnconfigure((0,1), weight=1)

        self.right_main_center = ctk.CTkFrame(self.main_center,height=300,width=650,fg_color="white")
        self.right_main_center.grid(row=0,sticky="ne",column=1)
        self.most_vulnerabilities_label = ctk.CTkLabel(self.right_main_center, text="Top vulnerabilities", font=ctk.CTkFont(size=20, weight="bold"),text_color='black', fg_color='white', bg_color='white',width=560)
        self.most_vulnerabilities_label.grid(row=0, pady=(25,5), sticky="nw",padx=10, column=0)
        
        count = 4
        while count > 0:
            self.most_vulnerabilities_label = ctk.CTkLabel(self.right_main_center, text="Example " + str(count), font=ctk.CTkFont(size=15, weight="bold"),text_color='black', fg_color='white', bg_color='white')
            self.most_vulnerabilities_label.grid(row=count, pady=(15,5), sticky="nw",padx=(20,5), column=0)
            self.data_most_vulnerabilities_label = ctk.CTkLabel(self.right_main_center, text="Data " + str(count), font=ctk.CTkFont(size=15, weight="bold"),text_color='black', fg_color='white', bg_color='white', width=80)
            self.data_most_vulnerabilities_label.grid(row=count, pady=(15,5),padx=(10,0), sticky="nw", column=1)
            self.most_target_label = ctk.CTkLabel(self.left_main_center, text="Example " + str(count), font=ctk.CTkFont(size=15, weight="bold"),text_color='black', fg_color='white', bg_color='white')
            self.most_target_label.grid(row=count, pady=(15,5), sticky="nw",padx=10, column=0)
            self.data_most_target_label = ctk.CTkLabel(self.left_main_center, text="Data " + str(count), font=ctk.CTkFont(size=15, weight="bold"),text_color='black', fg_color='white', bg_color='white', width=80)
            self.data_most_target_label.grid(row=count, pady=(15,5),padx=(10,0), sticky="nw", column=1)
            count -= 1
        #
        self.slide = ctk.CTkFrame(self,height=100, width=master.winfo_width(), fg_color="white")
        self.slide.pack( fill=tkinter.X, expand=True, padx=15)

       

    #  self.right_dashboard   ----> dashboard widget  
