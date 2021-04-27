import tkinter as tk
import socketio
import postsql as db

sio = socketio.Client()

HOST="localhost"
PORT=":8000"

class Gui_Client(tk.Frame):
    ChatTextPlace = None
    controller_db = db.Postgres()


    def ConnectionToServer(self): # Function Connection to the server
            try:
               sio.connect("http://" + HOST + PORT)
            except Exception:
                print("error connection")
            finally:
                self.app.LoginPage()


    def DisconnectionServer(self): # Function for Disconnection from server
        if self.client_is_connected != True:
            id_client = sio.sid
            sio.emit('logout', self.current_user.nick_name)
            sio.disconnect()
        else: print("LOGS # now is deisconnected !!! ")
        self.client_is_connected = False
        self.UserIsLogined = False

    def SendMasseges(self): # Function for recive message to server
           message_body = self.EntryMsgPlace.get("1.0" , tk.END)
           sio.emit('message' , [self.current_user.nick_name , message_body])

           self.EntryMsgPlace.delete('1.0' , tk.END)


    def LoadAllUsers(self):
        self.ListBoxUsers.delete(0, tk.END)
        list_nicknames = self.controller_db.GetAllNameDB()
        for i in list_nicknames:
            print(i[0])
            self.ListBoxUsers.insert(tk.END , i[0])

    def ShowOnlineUsers(self):
        self.ListBoxUsers.delete(0 ,tk.END)
        list_all_sid = self.controller_db.GetAllSid()
        for i in list_all_sid:
            if i[0] != "None" :
                name = self.controller_db.GetNameFromSid(i[0])
                self.ListBoxUsers.insert(tk.END, name[0][0])

    def InitSid(self , sid):
        self.current_user.sid = sid
        self.controller_db.UpdateSid(sid , self.current_user.nick_name)

    def SendEnterMessage(self, key):
        self.SendMasseges()
        #self.EntryMsgPlace.insert(tk.END , '\n')
        self.EntryMsgPlace.delete(0 , tk.END)



    def __init__(self , master=None , image=None , app=None , current_user=None):
        tk.Frame.__init__(self, master)

        self.current_user = current_user
        self.client_is_connected = False
        self.configure(bg='gray74')
        self.app = app

        self.user_image = tk.PhotoImage(master=self, file=r'/Users/andrurevkah/PycharmProjects/GameChat/images/tima.png')
        self.send_button_image = tk.PhotoImage(master=self , file = r'/Users/andrurevkah/PycharmProjects/GameChat/images/send.png')

        # Frame
        self.frame_first = tk.Frame(self , height = 300, width = 300)
        self.frame_user = tk.Frame(self , height = 50, width = 300 )

        self.frame_list_user = tk.Frame(self , height = 300)
        self.frame_list_user_btn = tk.Frame(self.frame_list_user , bg = 'gray74')

        # label
        self.user_image_lb = tk.Label(self.frame_user, image=self.user_image)
        self.user_name_lb = tk.Label(self.frame_user , text = self.current_user.nick_name , font = "Arial 16 bold")

        self.scrollbar = tk.Scrollbar(self , orient=tk.VERTICAL, command=lambda :self.ChatTextPlace.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


        # ListBox
        self.ListBoxUsers = tk.Listbox(self.frame_list_user, height="35", width="20" , yscrollcommand=self.scrollbar.set , font = "Arial 16 bold")
        self.LoadAllUsers()

        # Buttons
        self.SendButton = tk.Button(self.frame_first, text="Send" , image = self.send_button_image , border = "0", bg = "white" ,command = lambda : self.SendMasseges())

        self.ShowOnlineUserBtn = tk.Button(self.frame_list_user_btn , text="online" , height="2", width="5" , command = lambda :self.ShowOnlineUsers())
        self.ShowAllUserBtn = tk.Button(self.frame_list_user_btn , text="all" , height="2", width="5" , command = lambda :self.LoadAllUsers())

        # Entry widgets
        self.EntryMsgPlace = tk.Text(self.frame_first, width="50" , height="3" , bg = "gray75" ,font=("Arial", 16, "bold"))

        # Text widget
        self.ChatTextPlace = tk.Text(self.frame_first, width="40", height="33" , font=("Arial", 16, "bold") , yscrollcommand=self.scrollbar.set ,bg = 'azure')
        self.ChatTextPlace.config(state=tk.DISABLED)

        #pack
        self.ChatTextPlace.pack(fill = 'x' , side = 'top')
        self.ListBoxUsers.pack(side = 'bottom' , fill = 'y')
        self.EntryMsgPlace.pack(fill = 'x' , side = 'left' , ipady = 5)
        self.SendButton.pack(fill = 'x' , side = 'left')
        self.ShowAllUserBtn.pack(side = 'left')
        self.ShowOnlineUserBtn.pack(side = 'left')

        self.user_image_lb.pack(side = 'left')
        self.user_name_lb.pack(side = 'left')

        self.frame_list_user.pack(fill = 'x' , side='right')
        self.frame_list_user_btn.pack(side = "top")
        self.frame_user.pack(fill = 'x' , side = 'top')
        self.frame_first.pack(fill = 'x' , side = 'top')

        #self.ConnectionToServer()
        self.EntryMsgPlace.bind('<Control-Return>' , self.SendEnterMessage)

        self.InitSid(sio.sid)

        @sio.on('welkome_message')
        def GetWelkomeMessage(data):
            self.ChatTextPlace.config(state=tk.NORMAL)
            self.ChatTextPlace.insert(tk.END, data)
            self.ChatTextPlace.insert(tk.END, '\n')
            self.ChatTextPlace.config(state=tk.DISABLED)

            # print(data)

        @sio.on('disconnect_message')
        def GetDisconnectMessage(data):
            self.ChatTextPlace.config(state=tk.NORMAL)
            self.ChatTextPlace.insert(tk.END, data)
            self.ChatTextPlace.insert(tk.END, '\n')
            self.ChatTextPlace.config(state=tk.DISABLED)

        @sio.on('recive_message')
        def GetClientMessage(data):
            self.ChatTextPlace.config(state=tk.NORMAL)
            self.ChatTextPlace.insert(tk.END,'\t' + data)
            self.ChatTextPlace.insert(tk.END, '\n')
            self.ChatTextPlace.config(state=tk.DISABLED)

        @sio.on('recive_login')
        def GetLoginInfo(data):
            self.ListBoxUsers.insert(tk.END, data)

        @sio.on('recive_logout')
        def GetLogoutInfo(data):
            for i in range(self.ListBoxUsers.size()):
                if self.ListBoxUsers.get(i) == data:
                    self.ListBoxUsers.delete(i)






