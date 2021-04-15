import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import Image, ImageTk

import info_client as user
import sqlDB.db_work as db


class WindowManager():
    root = tk.Tk()
    image_reg = ImageTk.PhotoImage(Image.open(r"/Users/andrurevkah/PycharmProjects/GameChat/images/login.png"))

    def LoginPage(self):
        new_frame = AutorizetionWindow(master=self.root, image=self.image_reg , app=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    def RegistrationPage(self):
        new_frame = RegistrationWindow(master=self.root, image=self.image_reg, app=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    def __init__(self):
        self.root.geometry("300x520")
        self.root.resizable(0, 0)
        self.root.title("AlweysChat")
        self._frame = None

        #self.frames = {}

        auth_wind = AutorizetionWindow(master=self.root , image=self.image_reg , app=self)
        reg_wind = RegistrationWindow(master=self.root , image=self.image_reg , app=self)


        self.RegistrationPage()

class AutorizetionWindow(tk.Frame):
    # auto_window = tk.Tk()
    # image_login = ImageTk.PhotoImage(Image.open(r"/Users/andrurevkah/PycharmProjects/GameChat/images/login.png"))
    controller = None
    buffer = None
    def SaveBuffer(self , name_widget):
        self.buffer = name_widget

    def GoRegistration(self):
        self.pack_forget()
        self.app.RegistrationPage()

    def __init__(self , master=None , image=None , app=None):
        tk.Frame.__init__(self, master)

        self.image = image
        self.app =app

        image_label = tk.Label(self , image=self.image).pack()

        login_label = tk.Label(self , text = "Login" , font = 'Helvetica 18 bold')
        login_label.place(x = 120 , y = 250)

        login_space = tk.Entry(self)
        login_space.place(x = 50 , y = 280)

        password_label = tk.Label(self , text="Password" , font = 'Helvetica 18 bold' )
        password_label.place(x = 100 ,y = 320)

        password_space = tk.Entry(self)
        password_space.place(x = 50 , y = 350)

        login_button = tk.Button(self, text="Login", height="2", width="15")
        registration_button = tk.Button(self, text="Registration", height="2", width="15" , command =lambda : self.GoRegistration())

        login_button.place(x = 80 , y = 400)
        registration_button.place(x = 80 , y = 450)

        #self.pack(fill=tk.BOTH, expand=1)



class RegistrationWindow(tk.Frame):

    def GoLogin(self):
        self.pack_forget()
        self.app.LoginPage()

    def Registrate(self):
        self.pack_forget()
        self.app.LoginPage()

        info = [self.nickname_entry.get() , self.login_entry.get() , self.password_entry.get()]

        new_client = user(info[0])

    def __init__(self , master = None , image = None , app = None ):
        tk.Frame.__init__(self , master)
        self.image = image
        self.app = app

        self.mangerDB = db.ClientsDB()

        image_label = tk.Label(self , image = self.image)
        image_label.pack()

        info_label = tk.Label(self , text = "Registration" , font = 'Helvetica 18 bold underline')
        info_label.place(x = 90  , y = 210 )

        nickname_label = tk.Label(self , text = "Nickname" , font = 'Helvetica 18 bold')
        nickname_label.place(x = 100 , y = 260)

        login_label = tk.Label(self , text = "Login" , font = 'Helvetica 18 bold')
        login_label.place(x = 120 , y = 330)

        self.password_label = tk.Label(self , text = "Password" , font = 'Helvetica 18 bold')
        self.password_label.place(x = 100 , y = 400)

        #Entry
        self.nickname_entry = tk.Entry(self)
        self.nickname_entry.place(x = 50 , y = 290)

        self.login_entry = tk.Entry(self)
        self.login_entry.place(x = 50 , y = 360)

        self.password_entry = tk.Entry(self)
        self.password_entry.place(x = 50 , y = 430)

        #Button
        registrate_button = tk.Button(self , text="Registrate", height="2", width="10")
        cancel_button = tk.Button(self , text="Cancel", height="2", width="10" , command = lambda : self.GoLogin())

        registrate_button.place(x = 50 , y = 470)
        cancel_button.place(x = 150 , y = 470)


        #self.pack(fill=tk.BOTH, expand=1)







