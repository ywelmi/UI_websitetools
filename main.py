import customtkinter as ctk
from dashboard import DashBoard
from login import Login
ctk.set_appearance_mode("dark")
class Main(ctk.CTk):
    width = 900
    height = 600
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Main")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # Create two screens (frames) and add them to the window
        self.Dashboard = DashBoard(self)
        self.Login = Login(self)
        
        self.Login.pack(fill="both", expand=True)
        
        # Don't pack the second screen yet - we'll do it when we switch to it
        
        # Add some widgets to the first screen
   
        
    def show_Login(self):
        self.Dashboard.pack_forget()
        self.Login = Login(self)
        self.Login.pack(fill="both", expand=True)

        
    def show_Dashboard(self):
        self.Login.pack_forget()
        self.Dashboard = DashBoard(self)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.Dashboard.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = Main()
    app.mainloop()
