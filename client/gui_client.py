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


    def __init__(self , master=None , image=None , app=None):
        tk.Frame.__init__(self, master)

        self.current_user = info_client.Client()
        self.client_is_connected = False
        self.configure(bg='gray74')

        # ListBox
        self.ListBoxUsers = tk.Listbox(self, height="25", width="20")

        # Buttons
        self.ConnectionButton = tk.Button(self, text="connect", height="2", width="15")
        self.DisconnectButton = tk.Button(self, text="disconnect", height="2", width="15")
        self.QuitButton = tk.Button(self, text="Quit", height="2", width="15", command=quit)
        self.SendButton = tk.Button(self, text="Send", height="2", width="15")

        # Entry widgets
        self.EntryMsgPlace = tk.Entry(self, width="30")

        # Text widget
        self.ChatTextPlace = tk.Text(self, width="40", height="33")
        self.ChatTextPlace.config(state=tk.DISABLED)

        #Buttons positions
        self.ConnectionButton.config(command=lambda : self.ConnectionToServer())
        self.ConnectionButton.place(x = 150 , y = 500)

        self.DisconnectButton.place(x = 0 , y = 500)
        self.DisconnectButton.config(state=tk.DISABLED)
        self.DisconnectButton.config(command=lambda : self.DisconnectionServer())

        self.QuitButton.place(x = 0 , y = 540)

        self.SendButton.place(x = 150 , y = 540)
        self.SendButton.config(command = lambda : self.SendMasseges())
        #Entry
        self.EntryMsgPlace.place(x = 0 , y = 465 )

        #Text
        self.ChatTextPlace.place(x = 10 , y = 10)

        #ListBox
        self.ListBoxUsers.place(x = 300 , y = 10)





