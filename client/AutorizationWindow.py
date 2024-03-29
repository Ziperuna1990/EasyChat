import tkinter as tk
from tkinter import messagebox
import ChatWindow
import ClientClass as user
import postsql as db
import socketio.exceptions


path = r"/Users/andrurevkah/PycharmProjects/GameChat/images/login.png"

class WindowManager():
    root = tk.Tk()
    image_reg = tk.PhotoImage(master = root, file = path)
    controller_db = db.Postgres()
    if_connect = False


    def CheakAlredyLogin(self , login):
        sid = self.controller_db.GetSidFromLogin(login)[0][0]
        if sid == "None":
            return True
        else: return False

    def GiveAuthorizationUser(self , login , password):
        print(login , password)
        nickname = self.controller_db.GetNameFromLogin(login)
        new_user = user.Client(nickname[0][0],login , password)
        return new_user

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

    def DestroyWindow(self):
        new_frame = RegistrationWindow(master=self.root, image=self.image_reg, app=self)
        self.root.destroy()

    def ChatWindow(self , new_user):
        self.root.geometry("750x700")
        self.root.resizable(0,0)
        new_frame = ChatWindow.Gui_Client(master=self.root, image=self.image_reg, app=self , current_user=new_user)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH, expand=1)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            sid = ChatWindow.sio.sid
            print(sid)
            self.controller_db.UpdateSidl("None" , sid)

            ChatWindow.sio.disconnect()
            self.root.destroy()


    def __init__(self):
        self.root.geometry("300x520")
        self.root.resizable(0, 0)
        self.root.title("AlweysChat")
        self._frame = None

        #self.frames = {}

        auth_wind = AutorizetionWindow(master=self.root , image=self.image_reg , app=self)
        reg_wind = RegistrationWindow(master=self.root , image=self.image_reg , app=self)


        self.LoginPage()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #self.root.mainloop()

class AutorizetionWindow(tk.Frame):
    # auto_window = tk.Tk()
    # image_login = ImageTk.PhotoImage(Image.open(r"/Users/andrurevkah/PycharmProjects/GameChat/images/login.png"))
    current_login = None
    current_password = None

    def GoLogin(self):
        if self.mangerDB.GetColUser() == 0:
           msg = messagebox.showinfo("NonAutorizate" , "dont correct data")

        login = self.login_space.get()
        password = self.password_space.get()
        ip = self.ip_space.get()
        self.login_space.delete(0 , tk.END)
        self.password_space.delete(0 , tk.END)

        buff_logins = []
        buff_passwords = []
        all_logins = self.mangerDB.GetAllLogins()
        all_passwords = self.mangerDB.GetAllPasswords()

        for i in all_logins:
            buff_logins.append(i[0])
        for i in all_passwords:
            buff_passwords.append(i[0])


        login_access = False
        password_access = False

        for i in buff_logins:
            if i == login:
                login_access = True

        for i in buff_passwords:
            if i == password:
                password_access = True

        if login_access == True:
            if password_access == True :
                self.current_login = login
                self.current_password = password

                msg = messagebox.showinfo("Autorizated!!!" , "correct access!!!")
                new_user = self.app.GiveAuthorizationUser(self.current_login , self.current_password)
                # self.app.ChatWindow(new_user)

                if self.app.CheakAlredyLogin(self.current_login):

                   try:
                       ChatWindow.sio.connect("http://" + ip + ":8000")
                   except socketio.exceptions.ConnectionError as err:
                       msg = messagebox.showinfo("error!!!", err)
                       self.app.LoginPage()
                   else:
                       self.app.ChatWindow(new_user)
                else:
                    msg = messagebox.showinfo("error!!!", "User already logined!!!")
                    self.app.LoginPage()
            else:
                msg = messagebox.showinfo("Autorizated!!!", "incorrect access!!!")
        else:
            msg = messagebox.showinfo("Autorizated!!!", "incorrect access!!!")


    def GoRegistration(self):
        self.pack_forget()
        self.app.RegistrationPage()

    def __init__(self , master=None , image=None , app=None):
        tk.Frame.__init__(self, master)

        self.image = image
        self.app =app

        self.mangerDB = db.Postgres()

        image_label = tk.Label(self , image=self.image).pack()

        ip_label = tk.Label(self , text = "IP" , font = 'Helvetica 18 bold')
        ip_label.place(x=135, y=210)

        self.ip_space = tk.Entry(self)
        self.ip_space.place(x=50, y=240)

        login_label = tk.Label(self , text = "Login" , font = 'Helvetica 18 bold')
        login_label.place(x = 120 , y = 270)

        self.login_space = tk.Entry(self)
        self.login_space.place(x = 50 , y = 295)

        password_label = tk.Label(self , text="Password" , font = 'Helvetica 18 bold' )
        password_label.place(x = 100 ,y = 330)

        self.password_space = tk.Entry(self)
        self.password_space.place(x = 50 , y = 360)

        self.login_button = tk.Button(self, text="Login", height="2", width="15" , command = lambda : self.GoLogin())
        self.registration_button = tk.Button(self, text="Registration", height="2", width="15" , command =lambda : self.GoRegistration())

        self.login_button.place(x = 80 , y = 420)
        self.registration_button.place(x = 80 , y = 470)

        #self.pack(fill=tk.BOTH, expand=1)



class RegistrationWindow(tk.Frame):
    #Function for checking
    def GetNewIdForClient(self):
        all_ids = self.mangerDB.GetIdUser()

        buff = []
        for i in all_ids:
            buff.append(i[0])

        max_id = 0
        for i in buff:
            if max_id < int(i):
                max_id = int(i)
        new_id = max_id + 1
        return str(new_id)

    def GoLogin(self):
        print(self.GetNewIdForClient())
        self.pack_forget()
        self.app.LoginPage()

    def Registrate(self):
        info = [self.nickname_entry.get() , self.login_entry.get() , self.password_entry.get()]

        new_client = user.Client(info[0] , info[1] , info[2])
        new_client.user_id = self.GetNewIdForClient()
        new_client.sid = "None"

        self.mangerDB.AddInfoToDB(new_client)

        self.pack_forget()
        self.app.LoginPage()

    def __init__(self , master = None , image = None , app = None ):
        tk.Frame.__init__(self , master)
        self.image = image
        self.app = app

        self.mangerDB = db.Postgres()

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
        registrate_button = tk.Button(self , text="Registrate", height="2", width="10" , command = lambda : self.Registrate())
        cancel_button = tk.Button(self , text="Cancel", height="2", width="10" , command = lambda : self.GoLogin())

        registrate_button.place(x = 50 , y = 470)
        cancel_button.place(x = 150 , y = 470)


        #self.pack(fill=tk.BOTH, expand=1)







