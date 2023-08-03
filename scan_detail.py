import os
import tkinter as tkinter
from PIL import Image, ImageTk
import customtkinter as ctk
from wapitiCore.controller import wapiti
import json


class Scan_Detail(ctk.CTkFrame):

    def __init__(self, master, data):
        super().__init__(master)

        self.data1 = {
            "Backup file": [],
            "Weak credentials": [],
            "CRLF Injection": [],
            "Content Security Policy Configuration": [
                {
                    "method": "GET",
                    "path": "/",
                    "info": "CSP is not set",
                    "level": 1,
                    "parameter": "",
                    "referer": "",
                    "module": "csp",
                    "http_request": "GET / HTTP/1.1\nhost: www.google.com\nconnection: keep-alive\nuser-agent: Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0\naccept-language: en-US\naccept-encoding: gzip, deflate, br\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "curl_command": "curl \"https://google.com/\"",
                    "wstg": ["WSTG-CONF-12", "OSHP-Content-Security-Policy"]
                }
            ],
            "Cross Site Request Forgery": [],
            "Potentially dangerous file": [],
            "Command execution": [],
            "Path Traversal": [],
            "Fingerprint web application framework": [],
            "Fingerprint web server": [],
            "Htaccess Bypass": [],
            "HTTP Secure Headers": [
                {
                    "method": "GET",
                    "path": "/",
                    "info": "X-Content-Type-Options is not set",
                    "level": 1,
                    "parameter": "",
                    "referer": "",
                    "module": "http_headers",
                    "http_request": "GET / HTTP/1.1\nhost: google.com\nconnection: keep-alive\nuser-agent: Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0\naccept-language: en-US\naccept-encoding: gzip, deflate, br\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\ncookie: 1P_JAR=2023-02-17-15; AEC=ARSKqsKMHBg_vtBjTvKk9lpb6x-BXoyRIlaiVoI2jqhiqJOQB8QJdoBh_v0; NID=511=gj5LFftje-eIcNOx4eUdUWrrjrju9UH8-70zUEDR_06i4pFeTVCJK867xq_WhIUKwhirrWOCGApuG4jlSjiNdGDvauNqn-5uS-P23oDTX4vv_6X6gtGT_MNvtxAQn0DkHUeqW94iOdbOOx9JvxhZ9Vyoe3RwNUrhGF7hgyUsId0",
                    "curl_command": "curl \"https://google.com/\"",
                    "wstg": ["OSHP-X-Content-Type-Options"]
                },
                {
                    "method": "GET",
                    "path": "/",
                    "info": "Strict-Transport-Security is not set",
                    "level": 1,
                    "parameter": "",
                    "referer": "",
                    "module": "http_headers",
                    "http_request": "GET / HTTP/1.1\nhost: google.com\nconnection: keep-alive\nuser-agent: Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0\naccept-language: en-US\naccept-encoding: gzip, deflate, br\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\ncookie: 1P_JAR=2023-02-17-15; AEC=ARSKqsKMHBg_vtBjTvKk9lpb6x-BXoyRIlaiVoI2jqhiqJOQB8QJdoBh_v0; NID=511=gj5LFftje-eIcNOx4eUdUWrrjrju9UH8-70zUEDR_06i4pFeTVCJK867xq_WhIUKwhirrWOCGApuG4jlSjiNdGDvauNqn-5uS-P23oDTX4vv_6X6gtGT_MNvtxAQn0DkHUeqW94iOdbOOx9JvxhZ9Vyoe3RwNUrhGF7hgyUsId0",
                    "curl_command": "curl \"https://google.com/\"",
                    "wstg": ["WSTG-CONF-07", "OSHP-HTTP-Strict-Transport-Security"]
                }
            ],
            "HttpOnly Flag cookie": [
                {
                    "method": "GET",
                    "path": "/",
                    "info": "HttpOnly flag is not set in the cookie : 1P_JAR",
                    "level": 1,
                    "parameter": "",
                    "referer": "",
                    "module": "cookieflags",
                    "http_request": "GET / HTTP/1.1\nhost: google.com\nconnection: keep-alive\nuser-agent: Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0\naccept-language: en-US\naccept-encoding: gzip, deflate, br\naccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "curl_command": "curl \"https://google.com/\"",
                    "wstg": ["WSTG-SESS-02"]
                }
            ],
            "Log4Shell": [],
            "Open Redirect": [],
            "Reflected Cross Site Scripting": [],
            "Secure Flag cookie": [],
            "SQL Injection": [],
            "TLS/SSL misconfigurations": [],
            "Server Side Request Forgery": [],
            "Stored Cross Site Scripting": [],
            "Subdomain takeover": [],
            "Blind SQL Injection": [],
            "XML External Entity": []
        }
        self.winfo_height().as_integer_ratio

        # main top
        self.main_top = ctk.CTkFrame(
            self, height=180, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_top.pack(fill=tkinter.X, expand=True, padx=5)
        # self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        self.main_top.grid_columnconfigure((2), weight=2)
        self.main_top.configure(border_width=2)
        self.main_top.configure(border_color='white')
        # Set the relief style to 'ridge'
        # self.main_top.configure(relief="ridge")
        target = data[0]['target']
        self.scan_result_label = ctk.CTkLabel(self.main_top, text="SCAN RESULT: ", font=ctk.CTkFont(
            size=20, weight="bold"), text_color='White')
        self.scan_result_label.grid(row=0, pady=10, padx=25, column=0)
        self.scan_target_label = ctk.CTkLabel(self.main_top, text=target, font=ctk.CTkFont(
            size=20, weight="bold"), text_color='red')
        self.scan_target_label.grid(row=0, pady=10, padx=(25, 5), column=1)
        button_back_to_scan = ctk.CTkButton(self.main_top, text="< Back to scan", text_color="black",  fg_color="red", font=('Arial', 15, 'bold'),
                                            corner_radius=10,
                                            command=self.back_to_scan)
        button_back_to_scan.grid(column=3, row=0,  padx=20, pady=10,)

        # ------------------------------------------------------
        # scan_search
        # search bar + total result
        self.main_entry = ctk.CTkFrame(
            self, height=180, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_entry.pack(fill=tkinter.X, expand=True, padx=5)
        self.target_entry = ctk.CTkEntry(
            self.main_entry, width=600, placeholder_text="Search Vunerabilities",)
        self.target_entry.grid(row=0, column=0, sticky="nw", pady=(15, 15))
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bt_search = ctk.CTkButton(self.main_entry, width=80, height=25, anchor="w", image=ctk.CTkImage(Image.open(
            current_path + "/assets/icons/search.png"), size=(15, 15)), text=" Search", text_color='white', fg_color='red', command=lambda: print(data[1][0]))
        self.bt_search.grid(row=0, column=1, padx=10, pady=10)
        total_vul = 85

        self.total_vul_label = ctk.CTkLabel(self.main_entry, text=str(
            total_vul) + " vulnerabilities", font=ctk.CTkFont(size=15, weight="bold"), text_color='red')
        self.total_vul_label.grid(row=0, pady=10, padx=(25, 5), column=2)

        self.main_center = ctk.CTkFrame(
            self, height=700, width=master.winfo_width(), fg_color='#2b2b2b')
        self.main_center.pack(fill=tkinter.X, expand=True, padx=5)
        self.main_center.grid_columnconfigure((0, 1), weight=1)
        self.data_vulnerabilities = ctk.CTkFrame(
            self.main_center, height=40, width=750)
        self.data_vulnerabilities.grid(row=0, column=0, sticky="nw")
        # self.main_center.grid_rowconfigure((), weight=2)

        self.header = ctk.CTkFrame(
            self.data_vulnerabilities, height=40, width=750, fg_color='gray')
        self.header.grid(row=0, column=0, sticky="nw")
        self.header.configure(border_width=1)
        self.header.configure(border_color='red')
        self.header.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        # header detail
        # id label
        self.id_label_frame = ctk.CTkFrame(
            self.header, width=50, fg_color='gray', corner_radius=0)
        self.id_label_frame.grid(row=0, column=0, sticky="nw")
        self.id_label_frame.configure(border_width=1)
        self.id_label_frame.configure(border_color='red')
        self.id_label = ctk.CTkLabel(self.id_label_frame, text="Id", font=ctk.CTkFont(
            size=15, weight="bold"), text_color='White', fg_color='gray', width=50)
        self.id_label.grid(row=0, column=0, pady=10, padx=5, sticky="nw")
        # sev label
        self.sev_label_frame = ctk.CTkFrame(
            self.header, width=100, fg_color='gray', corner_radius=0)
        self.sev_label_frame.grid(row=0, column=1, sticky="nw")
        self.sev_label_frame.configure(border_width=1)
        self.sev_label_frame.configure(border_color='red')
        self.sev_label = ctk.CTkLabel(self.sev_label_frame, text="Sev", font=ctk.CTkFont(
            size=15, weight="bold"), text_color='White', fg_color='gray', width=100)
        self.sev_label.grid(row=0, column=1, pady=10, padx=5, sticky="nw")

        # name label
        self.name_label_frame = ctk.CTkFrame(
            self.header, width=300, fg_color='gray', corner_radius=0)
        self.name_label_frame.grid(row=0, column=2, sticky="nw")
        self.name_label_frame.configure(border_width=1)
        self.name_label_frame.configure(border_color='red')
        self.name_label = ctk.CTkLabel(self.name_label_frame, text="Name", font=ctk.CTkFont(
            size=15, weight="bold"), text_color='White', fg_color='gray', width=300)
        self.name_label.grid(row=0, column=2, pady=10, padx=5, sticky="nw")

        # des label
        self.des_label_frame = ctk.CTkFrame(
            self.header, width=500, fg_color='gray', corner_radius=0)
        self.des_label_frame.grid(row=0, column=3, sticky="nw")
        self.des_label_frame.configure(border_width=1)
        self.des_label_frame.configure(border_color='red')
        self.des_label = ctk.CTkLabel(self.des_label_frame, text="Description", font=ctk.CTkFont(
            size=15, weight="bold"), text_color='White', fg_color='gray', width=450)
        self.des_label.grid(row=0, column=3, pady=10, padx=5, sticky="nw")

        # count label
        self.count_label_frame = ctk.CTkFrame(
            self.header, width=50, fg_color='gray', corner_radius=0)
        self.count_label_frame.grid(row=0, column=4, sticky="nw")
        self.count_label_frame.configure(border_width=1)
        self.count_label_frame.configure(border_color='red')
        self.count_label = ctk.CTkLabel(self.count_label_frame, text="Count", font=ctk.CTkFont(
            size=15, weight="bold"), text_color='White', fg_color='gray', width=50)
        self.count_label.grid(row=0, column=4, pady=10, padx=5, sticky="nw")

        # data in table
        options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        i = 0
        for key, value in data[1].items():
            self.data = ctk.CTkFrame(
                self.data_vulnerabilities, height=40, width=950, fg_color='#d0caca')
            self.data.grid(row=i+1, column=0, sticky="nw", pady=4)
            self.data.configure(border_width=1)
            self.data.configure(border_color='white')
            if (value != []):
                self.id_data = ctk.CTkLabel(self.data, text=str(i+1), font=ctk.CTkFont(
                    size=15, weight="bold"), text_color='Black', fg_color='#d0caca', width=50)
                self.id_data.grid(row=0, column=0, pady=10,
                                  padx=5, sticky="nw")
                if (value[0]['level'] == 0):
                    self.sev_data = ctk.CTkLabel(self.data, text="Info", font=ctk.CTkFont(
                        size=15), text_color='Black', fg_color='#d0caca', width=100)
                if (value[0]['level'] == 1):
                    self.sev_data = ctk.CTkLabel(self.data, text="Low level", font=ctk.CTkFont(
                        size=15), text_color='Black', fg_color='#d0caca', width=100)
                if (value[0]['level'] == 2):
                    self.sev_data = ctk.CTkLabel(self.data, text="Medium level", font=ctk.CTkFont(
                        size=15), text_color='Black', fg_color='#d0caca', width=100)
                if (value[0]['level'] == 3):
                    self.sev_data = ctk.CTkLabel(self.data, text="High level", font=ctk.CTkFont(
                        size=15), text_color='Black', fg_color='#d0caca', width=100)
                if (value[0]['level'] == 4):
                    self.sev_data = ctk.CTkLabel(self.data, text="Critical level", font=ctk.CTkFont(
                        size=15), text_color='Black', fg_color='#d0caca', width=100)
                self.sev_data.grid(row=0, column=1, pady=10,
                                   padx=5, sticky="nw")
                self.name_data = ctk.CTkLabel(self.data, text=key, font=ctk.CTkFont(
                    size=15), text_color='Black', fg_color='#d0caca', width=300)
                self.name_data.grid(
                    row=0, column=2, pady=10, padx=5, sticky="nw")
                self.des_data = ctk.CTkLabel(self.data, text=value[0]['info'], font=ctk.CTkFont(
                    size=15), text_color='Black', fg_color='#d0caca', width=450)
                self.des_data.grid(row=0, column=3, pady=10,
                                   padx=5, sticky="nw")
                self.count_data = ctk.CTkLabel(self.data, text="1", font=ctk.CTkFont(
                    size=15), text_color='Black', fg_color='#d0caca', width=50)
                self.count_data.grid(
                    row=0, column=4, pady=10, padx=5, sticky="nw")
                i += 1

        # info vulnerabilities
        self.info_vulnerabilities = ctk.CTkFrame(
            self.main_center, height=600, width=350, fg_color='#dc4c4c', bg_color='#dc4c4c')
        self.info_vulnerabilities.grid(row=0, column=2, padx=15)
        self.info_vulnerabilities.grid_columnconfigure((0), weight=1)
        self.scan_detail_label = ctk.CTkLabel(self.info_vulnerabilities, text="Scan details", font=ctk.CTkFont(
            size=20, weight="bold"), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.scan_detail_label.grid(
            row=0, column=0, pady=5, padx=5, sticky="nw")

        self.horizontal_line_label = ctk.CTkLabel(self.info_vulnerabilities, text="----------------------------------------------------",
                                                  anchor="nw", font=ctk.CTkFont(size=20, weight="bold"), text_color='Black', fg_color='#dc4c4c', width=350)
        self.horizontal_line_label.grid(
            row=1, column=0, pady=5, padx=5, sticky="nw")

        policy_scan = "Basic Network Scan"
        status = "Completed"
        start = "10:30 AM - 30/5/2023"
        end = "10:35 AM - 30/5/2023"
        elapsed = "5 minutes"
        self.policy_label = ctk.CTkLabel(self.info_vulnerabilities, text="Policy:      " + policy_scan,
                                         font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.policy_label.grid(row=2, column=0, pady=5, padx=5, sticky="nw")

        self.status_label = ctk.CTkLabel(self.info_vulnerabilities, text="Status:     " + status,
                                         font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.status_label.grid(row=3, column=0, pady=5, padx=5, sticky="nw")

        self.start_label = ctk.CTkLabel(self.info_vulnerabilities, text="Start:        " + start,
                                        font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.start_label.grid(row=4, column=0, pady=5, padx=5, sticky="nw")

        self.end_label = ctk.CTkLabel(self.info_vulnerabilities, text="End:          " + end, font=ctk.CTkFont(
            size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.end_label.grid(row=5, column=0, pady=5, padx=5, sticky="nw")

        self.elapsed_label = ctk.CTkLabel(self.info_vulnerabilities, text="Elapsed:   " + elapsed,
                                          font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.elapsed_label.grid(row=6, column=0, pady=5, padx=5, sticky="nw")

        self.vul_detail_label = ctk.CTkLabel(self.info_vulnerabilities, text="Vulnerabilities", font=ctk.CTkFont(
            size=20, weight="bold"), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.vul_detail_label.grid(
            row=7, column=0, pady=5, padx=5, sticky="nw")

        self.horizontal_line_label_1 = ctk.CTkLabel(self.info_vulnerabilities, text="----------------------------------------------------",
                                                    anchor="nw", font=ctk.CTkFont(size=20, weight="bold"), text_color='Black', fg_color='#dc4c4c', width=350)
        self.horizontal_line_label_1.grid(
            row=8, column=0, pady=5, padx=5, sticky="nw")

        high_severity = 1
        medium_severity = 2
        low_severity = 3
        # self.high_color = ctk.CTkButton(self.info_vulnerabilities, width=35, height=35, anchor="w", image=ctk.CTkImage(Image.open(current_path + "/assets/icons/round_red.jpg"),size=(30, 30)), text="High :      "+ str(high_severity), fg_color='#dc4c4c')
        self.critical_color = ctk.CTkLabel(self.info_vulnerabilities,  text="🔥 Critical :      " + str(
            high_severity), fg_color='#dc4c4c', compound="left", padx=5, anchor="w")
        self.critical_color.grid(row=9, column=0, padx=5, pady=5, sticky="nw")

        self.high_color = ctk.CTkLabel(self.info_vulnerabilities,  text="🔴 High :      " + str(
            high_severity), fg_color='#dc4c4c', compound="left", padx=5, anchor="w")
        self.high_color.grid(row=10, column=0, padx=5, pady=5, sticky="nw")

        self.medium_severity_label = ctk.CTkLabel(self.info_vulnerabilities, text="🟠 Medium :      " + str(
            medium_severity), fg_color='#dc4c4c', text_color='blue', compound="left", padx=5, anchor="w")

        self.medium_severity_label.grid(
            row=11, column=0, pady=5, padx=5, sticky="nw")

        self.low_severity_label = ctk.CTkLabel(self.info_vulnerabilities, text="🟡 Low :      " + str(
            low_severity), font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.low_severity_label.grid(
            row=12, column=0, pady=5, padx=5, sticky="nw")

        self.info_severity_label = ctk.CTkLabel(self.info_vulnerabilities, text="🕵️ Info :      " + str(
            low_severity), font=ctk.CTkFont(size=15), anchor="nw", text_color='Black', fg_color='#dc4c4c', width=350)
        self.info_severity_label.grid(
            row=13, column=0, pady=5, padx=5, sticky="nw")

        self.slide = ctk.CTkFrame(
            self, height=200, width=master.winfo_width(), fg_color="#2b2b2b")
        self.slide.pack(fill=tkinter.X, expand=True, padx=15, pady=10)
        self.slide.grid_columnconfigure((0, 1, 2), weight=1)
        self.slide.configure(border_width=2)
        self.slide.configure(border_color='white')

    def back_to_scan(self):
        self.destroy()
        self.master.back_to_scan()

    def get_data():
        print("event come hereeee")
    #  self.right_dashboard   ----> dashboard widget
