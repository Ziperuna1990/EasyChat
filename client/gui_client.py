import tkinter as tk
from tkinter import messagebox
import socketio
import info_client

sio = socketio.Client()

HOST="localhost"
PORT=":8000"

class Gui_Client(tk.Frame):
    ChatTextPlace = None
    ListBoxUsers = None


    def ConnectionToServer(self): # Function Connection to the server
        if self.client_is_connected == True:
            print("LOGS # now is connected !!! ")
        else :
            sio.connect("http://" + HOST + PORT)
            self.ConnectionButton.config(state=tk.DISABLED)
            self.DisconnectButton.config(state=tk.NORMAL)

        self.client_is_connected = True

    def DisconnectionServer(self): # Function for Disconnection from server
        if self.client_is_connected != True:
            id_client = sio.sid
            sio.emit('logout', self.current_user.nick_name)
            sio.disconnect()
            self.ConnectionButton.config(state=tk.NORMAL)
            self.DisconnectButton.config(state=tk.DISABLED)
        else: print("LOGS # now is deisconnected !!! ")
        self.client_is_connected = False
        self.UserIsLogined = False

    def SendMasseges(self): # Function for recive message to server
        if self.client_is_connected == True:
           message_body = self.EntryMsgPlace.get()
           sio.emit('message' , [self.current_user.nick_name , message_body])

           self.EntryMsgPlace.delete(0 , 'end')
        else :
            print("### logs ###")
            print("error 404 # don't connect to the server")


    # events
    @sio.on('welkome_message')
    def GetWelkomeMessage(data):
        Gui_Client.ChatTextPlace.config(state=tk.NORMAL)
        Gui_Client.ChatTextPlace.insert(tk.END, data)
        Gui_Client.ChatTextPlace.insert(tk.END, '\n')
        Gui_Client.ChatTextPlace.config(state=tk.DISABLED)

        #print(data)

    @sio.on('disconnect_message')
    def GetDisconnectMessage(data):
        Gui_Client.ChatTextPlace.config(state=tk.NORMAL)
        Gui_Client.ChatTextPlace.insert(tk.END, data)
        Gui_Client.ChatTextPlace.insert(tk.END, '\n')
        Gui_Client.ChatTextPlace.config(state=tk.DISABLED)

    @sio.on('recive_message')
    def GetClientMessage(data):
        Gui_Client.ChatTextPlace.config(state=tk.NORMAL)
        Gui_Client.ChatTextPlace.insert(tk.END, data)
        Gui_Client.ChatTextPlace.insert(tk.END, '\n')
        Gui_Client.ChatTextPlace.config(state=tk.DISABLED)

    @sio.on('recive_login')
    def GetLoginInfo(data):
        Gui_Client.ListBoxUsers.insert(tk.END, data)

    @sio.on('recive_logout')
    def GetLogoutInfo(data):
        for i in range(Gui_Client.ListBoxUsers.size()):
           if Gui_Client.ListBoxUsers.get(i) == data:
               Gui_Client.ListBoxUsers.delete(i)


    def __init__(self , master=None , image=None , app=None , current_user=None):
        tk.Frame.__init__(self, master)

        self.current_user = current_user
        self.client_is_connected = False
        self.configure(bg='gray74')

        self.user_image = tk.PhotoImage(master=self, file=r'/Users/andrurevkah/PycharmProjects/GameChat/images/tima.png')
        self.send_button_image = tk.PhotoImage(master=self , file = r'/Users/andrurevkah/PycharmProjects/GameChat/images/send.png')

        # Frame
        self.frame_first = tk.Frame(self , height = 300, width = 300)
        self.frame_user = tk.Frame(self , height = 50, width = 300 )

        # label
        self.user_image_lb = tk.Label(self.frame_user, image=self.user_image)
        self.user_name_lb = tk.Label(self.frame_user , text = self.current_user.nick_name , font = "Arial 16 bold")

        # ListBox
        self.ListBoxUsers = tk.Listbox(self, height="25", width="20")

        # Buttons
        self.ConnectionButton = tk.Button(self, text="connect", height="2", width="15")
        self.DisconnectButton = tk.Button(self, text="disconnect", height="2", width="15")
        self.QuitButton = tk.Button(self, text="Quit", height="2", width="15", command=quit)
        self.SendButton = tk.Button(self.frame_first, text="Send" , image = self.send_button_image , border = "0", bg = "white")

        # Entry widgets
        self.EntryMsgPlace = tk.Text(self.frame_first, width="50" , height="3" , bg = "gray75")

        # Text widget
        self.ChatTextPlace = tk.Text(self.frame_first, width="40", height="33")
        self.ChatTextPlace.config(state=tk.DISABLED)

        #Buttons positions
        self.ConnectionButton.config(command=lambda : self.ConnectionToServer())

        self.DisconnectButton.config(state=tk.DISABLED)
        self.DisconnectButton.config(command=lambda : self.DisconnectionServer())
        self.SendButton.config(command = lambda : self.SendMasseges())

        #pack
        self.ChatTextPlace.pack(fill = 'x' , side = 'top')
        self.ListBoxUsers.pack(side = 'right' , fill = 'y')
        self.EntryMsgPlace.pack(side = 'left' , ipady = 5)
        self.SendButton.pack(side = 'left')

        self.user_image_lb.pack(side = 'left')
        self.user_name_lb.pack(side = 'left')

        self.frame_user.pack(fill = 'x' , side = 'top')
        self.frame_first.pack(fill = 'x' , side = 'top')






