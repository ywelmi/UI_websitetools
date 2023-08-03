import json
import os
import tkinter as tkinter
from PIL import Image, ImageTk
from scan_detail import Scan_Detail
import customtkinter as ctk
import array as arr
import os
from wapitiCore.controller.wapiti import Wapiti
from wapitiCore.main.wapiti import parse_args


class Scan1(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.winfo_height().as_integer_ratio
        self.scan = ScanAction(self)
        # self.scan_detail = Scan_Detail(self)
        self.scan.pack(fill=tkinter.X, expand=True, padx=5)

    def back_to_scan(self):

        self.scan = ScanAction(self)
        self.scan.pack(fill=tkinter.X, expand=True, padx=5)

    #  self.right_dashboard   ----> statement widget
    def show_detail(self, data):

        self.scan_detail = Scan_Detail(self, data)
        self.scan_detail.pack(fill=tkinter.X, expand=True, padx=5)


class ScanAction(ctk.CTkFrame):
    data = {}

    def __init__(self, master=None):
        super().__init__(master)

        showResult = False
        self.winfo_height().as_integer_ratio

        # main top
        self.main_top = ctk.CTkFrame(
            self, height=180, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_top.pack(fill=tkinter.X, expand=True, padx=5, pady=(5, 45))
        # self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.main_top.grid_columnconfigure((1), weight=1)
        self.main_top.configure(border_width=2)
        self.main_top.configure(border_color='white')
        # Set the relief style to 'ridge'
        # self.main_top.configure(relief="ridge")
        self.scan_running_label = ctk.CTkLabel(self.main_top, text="SCAN", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='White')
        self.scan_running_label.grid(row=0, pady=10, padx=25, column=0)
        button_new_scan = ctk.CTkButton(self.main_top, text="New scan", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                        corner_radius=10,
                                        command=lambda: print("Button clicked!"))
        button_new_scan.grid(column=2, row=0,  padx=20, pady=10,)
        button_stop_scan = ctk.CTkButton(self.main_top, text="Stop scan", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                         corner_radius=10,
                                         command=lambda: print("Button clicked!"))
        button_stop_scan.grid(column=3, row=0,  padx=20, pady=10,)
        button_delete_scan = ctk.CTkButton(self.main_top, text="Rescan", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                           corner_radius=10,
                                           command=lambda: print("Button clicked!"))
        button_delete_scan.grid(column=4, row=0,  padx=20, pady=10,)
        button_generate_report = ctk.CTkButton(self.main_top, text="Generate HTML report", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                               corner_radius=10,
                                               command=lambda: print("Button clicked!"))
        button_generate_report.grid(column=5, row=0,  padx=20, pady=10,)

        # ------------------------------------------------------
        self.main_center = ctk.CTkFrame(
            self, height=700, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_center.pack(fill=tkinter.X, expand=True,
                              padx=5, pady=(5, 25))
        self.main_center.grid_columnconfigure((1, 2), weight=1)
        self.main_center.grid_rowconfigure(1, weight=1)
        self.entry = ctk.CTkFrame(
            self.main_center, height=400, width=master.winfo_width(), fg_color='#2b2b2b')
        self.entry.grid_columnconfigure((1), weight=1)
        self.entry.grid_rowconfigure((1, 2, 3), weight=1)
        self.entry.grid(row=0, sticky="nw", column=0, padx=30, pady=(15, 15))

        self.target_entry = ctk.CTkEntry(
            self.entry, width=800, placeholder_text="Target URL. Example: https://google.com")
        self.target_entry.grid(
            row=0, column=0, sticky="nw", padx=25, pady=(15, 15))

        self.recently_label = ctk.CTkLabel(self.entry, text="Recently: ", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='White', fg_color='#2b2b2b')
        self.recently_label.grid(
            row=1, pady=10, padx=25, sticky="nw", column=0)

        # data
        count = 4
        while count > 1:
            self.recently_label = ctk.CTkLabel(self.entry, text="www.website" + str(
                count) + ".com", font=ctk.CTkFont(size=20, weight="bold"), text_color='White', fg_color='#2b2b2b')
            self.recently_label.grid(
                row=count, pady=5, padx=25, sticky="nw", column=0)
            count -= 1

        # select module to scan
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_center, label_text="Select module to scan", height=100)
        self.scrollable_frame.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []

        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        self.switch = []
        for i in range(len(options)):
            self.switch.insert(i, ctk.CTkSwitch)
            self.switch[i] = ctk.CTkSwitch(
                master=self.scrollable_frame, text=options[i])

            self.switch[i].grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(self.switch[i])

        button_start_scan = ctk.CTkButton(self.main_center, text="Start scan", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                          corner_radius=10,
                                          command=self.printData)
        button_start_scan.grid(column=3, row=0,  padx=20, pady=10,)

        self.status = ctk.CTkFrame(
            self, height=100, width=master.winfo_width(), fg_color="#2b2b2b")

        self.status.grid_columnconfigure((0, 1), weight=1)
        self.result_label = ctk.CTkLabel(self.status, text="Status: ", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='White', fg_color='#2b2b2b')
        self.result_label.grid(row=0, pady=10, padx=5, sticky="nw")
        self.result_label = ctk.CTkLabel(self.status, text="Scan https://www.google.com completed",
                                         font=ctk.CTkFont(size=20, weight="bold"), text_color='green')
        self.result_label.grid(row=0, pady=10, padx=(285, 5), column=0)
        button_view_detail = ctk.CTkButton(self.status, text="View details report", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                           corner_radius=10,
                                           command=self.show_detail)
        button_view_detail.grid(row=1,  padx=(280, 5), pady=10,)

        self.slide = ctk.CTkFrame(
            self, height=300, width=master.winfo_width(), fg_color="#2b2b2b")

        self.slide.grid_columnconfigure((0, 1, 2), weight=1)
        self.slide.configure(border_width=2)
        self.slide.configure(border_color='white')
        self.result_label = ctk.CTkLabel(self.slide, text="Scan result: ", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='red', fg_color='#2b2b2b')
        self.result_label.grid(row=0, pady=10, padx=15, sticky="nw")
        self.high_severity = ctk.CTkFrame(
            self.slide, height=150, width=150, corner_radius=85, fg_color='red')
        self.high_severity.grid(column=0, row=0)

        self.inside = ctk.CTkFrame(
            self.slide, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.inside.grid(row=0, column=0)

        self.high_severity_data = ctk.CTkLabel(self.slide, text="5", font=ctk.CTkFont(
            size=40, weight="bold"), text_color='black', fg_color='white', bg_color='white')
        self.high_severity_data.grid(row=0)

        self.high_severity_label = ctk.CTkLabel(self.slide, text="High Severity Vulnerabilities", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.high_severity_label.grid(row=0, pady=(215, 10), column=0)

        self.medium_severity = ctk.CTkFrame(
            self.slide, height=150, width=150, corner_radius=85, fg_color='red')
        self.medium_severity.grid(column=1, row=0)

        self.medium_inside = ctk.CTkFrame(
            self.slide, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.medium_inside.grid(row=0, column=1)

        self.medium_severity_data = ctk.CTkLabel(self.slide, text="5", font=ctk.CTkFont(
            size=40, weight="bold"), text_color='black', fg_color='white', bg_color='white')
        self.medium_severity_data.grid(row=0, column=1)

        self.medium_severity_label = ctk.CTkLabel(self.slide, text="Medium Severity Vulnerabilities", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.medium_severity_label.grid(row=0, pady=(215, 10), column=1)

        self.low_severity = ctk.CTkFrame(
            self.slide, height=150, width=150, corner_radius=85, fg_color='red')
        self.low_severity.grid(column=2, row=0)

        self.low_inside = ctk.CTkFrame(
            self.slide, height=85, width=85, corner_radius=85, fg_color='white', bg_color='red')
        self.low_inside.grid(row=0, column=2)

        self.low_severity_data = ctk.CTkLabel(self.slide, text="5", font=ctk.CTkFont(
            size=40, weight="bold"), text_color='black', fg_color='white', bg_color='white')
        self.low_severity_data.grid(row=0, column=2)

        self.low_severity_label = ctk.CTkLabel(self.slide, text="Low Severity Vulnerabilities", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='white', fg_color='#2b2b2b', bg_color='#000811')
        self.low_severity_label.grid(row=0, pady=(215, 10), column=2)

    def show_detail(self):
        self.destroy()
        self.master.show_detail(self.data)

    def printData(self):
        print(self.target_entry.get())
        for i in self.switch:
            if (i.get()):
                print(i.cget('text'))
        os.system("wapiti -u " + self.target_entry.get() + "-m all")
        file_path = os.path.expanduser("~/Desktop/data.json")

        with open(file_path, "r") as file:
            read_data = json.load(file)

        self.data = read_data
        print(read_data[0]['target'])

        print("Scan done!")
        self.status.pack(fill=tkinter.X, expand=True, padx=15, pady=(5, 25))
        self.slide.pack(fill=tkinter.X, expand=True, padx=15)
