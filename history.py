import os
import tkinter as tkinter
from PIL import Image, ImageTk
import customtkinter as ctk

class History(ctk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        
      
        self.winfo_height().as_integer_ratio
        current_path = os.path.dirname(os.path.realpath(__file__))
        # main top 
        self.main_top = ctk.CTkFrame(self,height=180,width=master.winfo_width(),fg_color='#2b2b2b')
        self.main_top.pack( fill=tkinter.X, expand=True, padx=5)
        #self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.main_top.grid_columnconfigure((2), weight=2)
        self.main_top.configure(border_width=2)
        self.main_top.configure(border_color='white')
        # Set the relief style to 'ridge'
        #self.main_top.configure(relief="ridge")
        
        self.history_label = ctk.CTkLabel(self.main_top, text="HISTORY " , font=ctk.CTkFont(size=18, weight="bold"),text_color='White')
        self.history_label.grid(row=0, pady=10, padx=25, column=0)
        
        button_refresh_history = ctk.CTkButton(self.main_top, text="Refresh history", text_color="black",  fg_color="red", font=('Arial',15, 'bold'),
                       corner_radius=10,
                       command=self.refresh_exploit)
        button_refresh_history.grid(column=3, row=0,  padx=20, pady=10,)
       
        #------------------------------------------------------
        #scan_search
        #Dropdown menu + search bar + button send
        
        
        
        
        self.main_center = ctk.CTkFrame(self,height=600, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_center.pack( fill=tkinter.X, expand=True, padx=5)
        self.main_center.grid_columnconfigure(0, weight=1)
        self.tabview = ctk.CTkTabview(self.main_center, height=400, width=master.winfo_width(),segmented_button_selected_hover_color="red", segmented_button_selected_color="red", border_color="white", border_width=1)
        self.tabview.grid(row=0, column=0, sticky="nw")
        self.tabview.add("Scan")
        self.tabview.add("Exploit")
        self.tabview.add("Both scan and exploit")
      
        self.tabview.tab("Scan").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Exploit").grid_columnconfigure(0, weight=1)
        
        # Tab Params
        self.query_params_label = ctk.CTkLabel(self.tabview.tab("Scan"), text="History scan" , font=ctk.CTkFont(size=20, weight="bold"),text_color='White')
        self.query_params_label.grid(row=0, pady=10, column=0,sticky="nw")
        
        self.query_params_table = ctk.CTkFrame(self.tabview.tab("Scan"), height = 40,width=1350)
        self.query_params_table.grid(row =1, column =0, sticky="nw");
        #self.main_center.grid_rowconfigure((), weight=2)
        self.header_scan = ctk.CTkFrame(self.tabview.tab("Scan"), height = 40,width=1350, fg_color='gray')
        self.header_scan.grid(row = 0, column =0, sticky="nw");
        self.header_scan.configure(border_width=1)
        self.header_scan.configure(border_color='red')
        self.header_scan.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        
        #header_scan detail
        #id label
        self.id_label_frame = ctk.CTkFrame(self.header_scan,width=50, fg_color='gray', corner_radius=0)
        self.id_label_frame.grid(row=0, column=0,sticky="nw")
        self.id_label_frame.configure(border_width=1)
        self.id_label_frame.configure(border_color='red')
        self.id_label = ctk.CTkLabel(self.id_label_frame, text="ID Scan", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray', width=50)
        self.id_label.grid(row=0, column=0, pady=10, padx=5,sticky="nw")
        #sev label
        self.id_module_label_frame = ctk.CTkFrame(self.header_scan,width=100, fg_color='gray', corner_radius=0)
        self.id_module_label_frame.grid(row=0, column=1,sticky="nw")
        self.id_module_label_frame.configure(border_width=1)
        self.id_module_label_frame.configure(border_color='red')
        self.sev_label = ctk.CTkLabel(self.id_module_label_frame, text="ID module", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray', width=100)
        self.sev_label.grid(row=0, column=1, pady=10, padx=5,sticky="nw")
        
        #name label
        self.name_label_frame = ctk.CTkFrame(self.header_scan,width=300, fg_color='gray', corner_radius=0)
        self.name_label_frame.grid(row=0, column=2,sticky="nw")
        self.name_label_frame.configure(border_width=1)
        self.name_label_frame.configure(border_color='red')
        self.name_label = ctk.CTkLabel(self.name_label_frame, text="Target", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray', width=300)
        self.name_label.grid(row=0, column=2, pady=10, padx=5,sticky="nw")
        
        #des label
        self.des_label_frame = ctk.CTkFrame(self.header_scan,width=530, fg_color='gray', corner_radius=0)
        self.des_label_frame.grid(row=0, column=3,sticky="nw")
        self.des_label_frame.configure(border_width=1)
        self.des_label_frame.configure(border_color='red')
        self.des_label = ctk.CTkLabel(self.des_label_frame, text="Description", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray', width=530)
        self.des_label.grid(row=0, column=3, pady=10, padx=5,sticky="nw")
        
        #result label
        self.result_label_frame = ctk.CTkFrame(self.header_scan,width=300, fg_color='gray', corner_radius=0)
        self.result_label_frame.grid(row=0, column=4,sticky="nw")
        self.result_label_frame.configure(border_width=1)
        self.result_label_frame.configure(border_color='red')
        self.result_label = ctk.CTkLabel(self.result_label_frame, text="Result", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray', width=300)
        self.result_label.grid(row=0, column=4, pady=10, padx=5,sticky="nw")
        
        #Action label
        self.action_label_frame = ctk.CTkFrame(self.header_scan,width=50, fg_color='gray', corner_radius=0)
        self.action_label_frame.grid(row=0, column=5,sticky="nw")
        self.action_label_frame.configure(border_width=1)
        self.action_label_frame.configure(border_color='red')
        self.action_label = ctk.CTkLabel(self.action_label_frame, text="Action", font=ctk.CTkFont(size=15, weight="bold"),text_color='White',fg_color='gray',width=50)
        self.action_label.grid(row=0, column=5, pady=10, padx=5,sticky="nw")
        
       
        # data in table
        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        for i in range(len(options)):
            self.data = ctk.CTkFrame(self.tabview.tab("Scan"), height = 40, width=1350, fg_color='#d0caca')
            self.data.grid(row = i+1, column =0, sticky="nw", pady=4)
            self.data.configure(border_width=1)
            self.data.configure(border_color='white')
            self.id_data = ctk.CTkLabel(self.data, text=str(i+1), font=ctk.CTkFont(size=15, weight="bold"),text_color='Black',fg_color='#d0caca', width=50)
            self.id_data.grid(row=0, column=0, pady=10, padx=5,sticky="nw")
            self.sev_data = ctk.CTkLabel(self.data, text="Module" +str(i+1), font=ctk.CTkFont(size=15),text_color='Black',fg_color='#d0caca', width=100)
            self.sev_data.grid(row=0, column=1, pady=10, padx=5,sticky="nw")
            self.name_data = ctk.CTkLabel(self.data, text="Name" + options[i], font=ctk.CTkFont(size=15),text_color='Black',fg_color='#d0caca', width=300)
            self.name_data.grid(row=0, column=2, pady=10, padx=5,sticky="nw")
            self.des_data = ctk.CTkLabel(self.data, text="Description" + options[i], font=ctk.CTkFont(size=15),text_color='Black',fg_color='#d0caca', width=530)
            self.des_data.grid(row=0, column=3, pady=10, padx=5,sticky="nw")
            self.result_data = ctk.CTkLabel(self.data, text="Result" + options[i], font=ctk.CTkFont(size=15),text_color='Black',fg_color='#d0caca', width=300)
            self.result_data.grid(row=0, column=4, pady=10, padx=5,sticky="nw")
            self.count_data = ctk.CTkButton(self.data,width=50,height=25,anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/search.png"),size=(10, 10)), text=  "View", font=ctk.CTkFont(size=10))
            self.count_data.grid(row=0, column=5, pady=10, padx=5,sticky="nw")
        
        
        
       
        
        
        self.main_bottom = ctk.CTkFrame(self,height=500, width=master.winfo_width(), fg_color="#2b2b2b")
        self.main_bottom.pack( fill=tkinter.X, expand=True, padx=5, pady=10)
        self.main_bottom.grid_columnconfigure((0,1,2), weight=1)
        self.main_bottom.configure(border_width=2)
        self.main_bottom.configure(border_color='white')
        # label
        self.detail_label = ctk.CTkLabel(self.main_bottom, text="SCAN DETAILS" , font=ctk.CTkFont(size=15, weight="bold"),text_color='White')
        self.detail_label.grid(row=0, pady=10, padx=25, column=1)
        
        
        self.info_module = ctk.CTkFrame(self.main_bottom, height = 400,width=250, fg_color='#dc4c4c', bg_color='#dc4c4c')
        self.info_module.grid(row = 1, column =0, padx=15);
        self.info_module.grid_columnconfigure((0), weight=1)
        self.module_detail_label = ctk.CTkLabel(self.info_module, text="Module details", font=ctk.CTkFont(size=20, weight="bold"),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.module_detail_label.grid(row=0, column=0, pady=5, padx=5,sticky="nw")
        
        self.horizontal_line_label = ctk.CTkLabel(self.info_module, text="----------------------------------------------------",anchor="nw", font=ctk.CTkFont(size=20, weight="bold"),text_color='Black',fg_color='#dc4c4c',width=250)
        self.horizontal_line_label.grid(row=1, column=0, pady=5, padx=5,sticky="nw")
        
        self.vul_detail_label = ctk.CTkLabel(self.info_module, text="Vulnerabilities", font=ctk.CTkFont(size=20, weight="bold"),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.vul_detail_label.grid(row=7, column=0, pady=5, padx=5,sticky="nw")
        
        self.horizontal_line_label_1 = ctk.CTkLabel(self.info_module, text="----------------------------------------------------",anchor="nw", font=ctk.CTkFont(size=20, weight="bold"),text_color='Black',fg_color='#dc4c4c',width=250)
        self.horizontal_line_label_1.grid(row=8, column=0, pady=5, padx=5,sticky="nw")
        
        high_severity=1
        medium_severity=2
        low_severity=3
        #self.high_color = ctk.CTkButton(self.info_vulnerabilities, width=35, height=35, anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/round_red.jpg"),size=(30, 30)), text="High :      "+ str(high_severity), fg_color='#dc4c4c')
        self.high_color = ctk.CTkLabel(self.info_module, image=ctk.CTkImage(Image.open(current_path + "/assets/icons/round_red.jpg"),size=(30, 30)), text="High :      "+ str(high_severity), fg_color='#dc4c4c', compound="left", padx=5, anchor="w")
        self.high_color.grid(row=9, column=0, padx=5, pady=5, sticky="nw")
       
        
        self.medium_severity_label = ctk.CTkLabel(self.info_module, image=ctk.CTkImage(Image.open(current_path + "/assets/icons/round_blue.png"),size=(20, 20)), text="Medium :      "+ str(medium_severity), fg_color='#dc4c4c',text_color='blue', compound="left", padx=5, anchor="w")
        
        self.medium_severity_label.grid(row=10, column=0, pady=5, padx=5,sticky="nw")
        
        self.low_severity_label = ctk.CTkLabel(self.info_module, text="Low :      "+ str(low_severity), font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=350)
        self.low_severity_label.grid(row=11, column=0, pady=5, padx=5,sticky="nw")
        # main bottom with specific data
        self.data_vulnerabilities = ctk.CTkFrame(self.main_bottom, height = 40,width=750)
        self.data_vulnerabilities.grid(row = 1, column =1, sticky="nw");
        #self.main_center.grid_rowconfigure((), weight=2)
       
        self.header = ctk.CTkFrame(self.data_vulnerabilities, height = 40,width=450, fg_color='gray')
        self.header.grid(row = 0, column =0, sticky="nw");
        self.header.configure(border_width=1)
        self.header.configure(border_color='red')
        self.header.grid_columnconfigure((0,1,2,3,4), weight=1)
        
        #header detail
        #id label
        self.id_label_frame = ctk.CTkFrame(self.header,width=50, fg_color='gray', corner_radius=0)
        self.id_label_frame.grid(row=0, column=0,sticky="nw")
        self.id_label_frame.configure(border_width=1)
        self.id_label_frame.configure(border_color='red')
        self.id_label = ctk.CTkLabel(self.id_label_frame, text="Id", font=ctk.CTkFont(size=10, weight="bold"),text_color='White',fg_color='gray', width=50)
        self.id_label.grid(row=0, column=0, pady=10, padx=5,sticky="nw")
        #sev label
        self.sev_label_frame = ctk.CTkFrame(self.header,width=100, fg_color='gray', corner_radius=0)
        self.sev_label_frame.grid(row=0, column=1,sticky="nw")
        self.sev_label_frame.configure(border_width=1)
        self.sev_label_frame.configure(border_color='red')
        self.sev_label = ctk.CTkLabel(self.sev_label_frame, text="Sev", font=ctk.CTkFont(size=10, weight="bold"),text_color='White',fg_color='gray', width=100)
        self.sev_label.grid(row=0, column=1, pady=10, padx=5,sticky="nw")
        
        #name label
        self.name_label_frame = ctk.CTkFrame(self.header,width=100, fg_color='gray', corner_radius=0)
        self.name_label_frame.grid(row=0, column=2,sticky="nw")
        self.name_label_frame.configure(border_width=1)
        self.name_label_frame.configure(border_color='red')
        self.name_label = ctk.CTkLabel(self.name_label_frame, text="Name", font=ctk.CTkFont(size=10, weight="bold"),text_color='White',fg_color='gray', width=100)
        self.name_label.grid(row=0, column=2, pady=10, padx=5,sticky="nw")
        
        #des label
        self.des_label_frame = ctk.CTkFrame(self.header,width=200, fg_color='gray', corner_radius=0)
        self.des_label_frame.grid(row=0, column=3,sticky="nw")
        self.des_label_frame.configure(border_width=1)
        self.des_label_frame.configure(border_color='red')
        self.des_label = ctk.CTkLabel(self.des_label_frame, text="Description", font=ctk.CTkFont(size=10, weight="bold"),text_color='White',fg_color='gray', width=200)
        self.des_label.grid(row=0, column=3, pady=10, padx=5,sticky="nw")
        
      
       
        # data in table
        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
        for i in range(len(options)):
            self.data = ctk.CTkFrame(self.data_vulnerabilities, height = 40, width=450, fg_color='#d0caca')
            self.data.grid(row = i+1, column =0, sticky="nw", pady=4)
            self.data.configure(border_width=1)
            self.data.configure(border_color='white')
            self.id_data = ctk.CTkLabel(self.data, text=str(i+1), font=ctk.CTkFont(size=10, weight="bold"),text_color='Black',fg_color='#d0caca', width=50)
            self.id_data.grid(row=0, column=0, pady=10, padx=5,sticky="nw")
            self.sev_data = ctk.CTkLabel(self.data, text="Sev" + options[i], font=ctk.CTkFont(size=10),text_color='Black',fg_color='#d0caca', width=100)
            self.sev_data.grid(row=0, column=1, pady=10, padx=5,sticky="nw")
            self.name_data = ctk.CTkLabel(self.data, text="Name" + options[i], font=ctk.CTkFont(size=10),text_color='Black',fg_color='#d0caca', width=100)
            self.name_data.grid(row=0, column=2, pady=10, padx=5,sticky="nw")
            self.des_data = ctk.CTkLabel(self.data, text="Description" + options[i], font=ctk.CTkFont(size=10),text_color='Black',fg_color='#d0caca', width=200)
            self.des_data.grid(row=0, column=3, pady=10, padx=5,sticky="nw")
            
        
        
        # info vulnerabilities  
        self.info_vulnerabilities = ctk.CTkFrame(self.main_bottom, height = 400,width=250, fg_color='#dc4c4c', bg_color='#dc4c4c')
        self.info_vulnerabilities.grid(row = 1, column =2, padx=15);
        self.info_vulnerabilities.grid_columnconfigure((0), weight=1)
        self.scan_detail_label = ctk.CTkLabel(self.info_vulnerabilities, text="Scan details", font=ctk.CTkFont(size=20, weight="bold"),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.scan_detail_label.grid(row=0, column=0, pady=5, padx=5,sticky="nw")
        
        self.horizontal_line_label = ctk.CTkLabel(self.info_vulnerabilities, text="----------------------------------------------------",anchor="nw", font=ctk.CTkFont(size=20, weight="bold"),text_color='Black',fg_color='#dc4c4c',width=250)
        self.horizontal_line_label.grid(row=1, column=0, pady=5, padx=5,sticky="nw")
        
        policy_scan="Basic Network Scan"
        status = "Completed"
        start = "10:30 AM - 30/5/2023"
        end = "10:35 AM - 30/5/2023"
        elapsed="5 minutes"
        self.policy_label = ctk.CTkLabel(self.info_vulnerabilities, text="Policy:      "+ policy_scan, font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.policy_label.grid(row=2, column=0, pady=5, padx=5,sticky="nw")
        
        self.status_label = ctk.CTkLabel(self.info_vulnerabilities, text="Status:     "+ status, font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.status_label.grid(row=3, column=0, pady=5, padx=5,sticky="nw")
        
        self.start_label = ctk.CTkLabel(self.info_vulnerabilities, text="Start:        "+ start, font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.start_label.grid(row=4, column=0, pady=5, padx=5,sticky="nw")
        
        self.end_label = ctk.CTkLabel(self.info_vulnerabilities, text="End:          "+ end, font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.end_label.grid(row=5, column=0, pady=5, padx=5,sticky="nw")
        
        self.elapsed_label = ctk.CTkLabel(self.info_vulnerabilities, text="Elapsed:   "+ elapsed, font=ctk.CTkFont(size=15),anchor="nw",text_color='Black',fg_color='#dc4c4c',width=250)
        self.elapsed_label.grid(row=6, column=0, pady=5, padx=5,sticky="nw")
        
        self.main_x = ctk.CTkFrame(self.main_bottom,height=10, fg_color="#2b2b2b")
        self.main_x.grid(row=2, column=0, pady=5, padx=5,sticky="nw")
      
    def refresh_exploit(self):
        self.destroy()
        self.master.refresh_exploit()
        
    #  self.right_dashboard   ----> dashboard widget  
