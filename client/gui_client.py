import tkinter as tk
import socketio
import info_client

sio = socketio.Client()

HOST="localhost"
PORT=":8000"

class Gui_Client:
    window = tk.Tk()
    current_user = info_client.Client()

    client_is_connected = False
    UserIsLogined = False

    #ListBox
    ListBoxUsers = tk.Listbox(window , height = "25" ,  width = "20")

    #Buttons
    ConnectionButton = tk.Button(window, text="connect", height="2", width="15")
    DisconnectButton = tk.Button(window, text="disconnect", height="2", width="15")
    QuitButton = tk.Button(window, text="Quit", height="2", width="15" , command=quit)
    SendButton = tk.Button(window , text="Send" , height="2", width="15")

    #Entry widgets
    EntryMsgPlace = tk.Entry(window, width = "30")

    #Text widget
    ChatTextPlace = tk.Text(window , width = "40" , height="33")

    #Menu
    MenuWidget = tk.Menu(window)
    SubMenuWidget = tk.Menu(MenuWidget)
    CloseSubMenuWidget = tk.Menu(MenuWidget)
    LoginSubMenuWidget =tk.Menu(MenuWidget)

    #function for button
    def LoginUser(self):
        sid_buf = sio.sid
        login_window = tk.Toplevel(self.window)
        login_window.geometry("300x300")


        if self.UserIsLogined == False :
            self.current_user.SetName("Andru")
            self.current_user.SetLogin("peoly")
            self.current_user.SetSid(sid_buf)
            self.UserIsLogined = True

            #Send User Name for added in ListBox for all clients
            sio.emit('login' , self.current_user.nick_name)

        message = str("User is Logined # " + self.current_user.sid)

        Gui_Client.ChatTextPlace.config(state=tk.NORMAL)
        self.ChatTextPlace.insert(tk.END, message)
        self.ChatTextPlace.insert(tk.END, '\n')
        Gui_Client.ChatTextPlace.config(state=tk.DISABLED)

    def ConnectionToServer(self):
        if self.client_is_connected == True:
            print("LOGS # now is connected !!! ")
        else :
            sio.connect("http://" + HOST + PORT)
            self.ConnectionButton.config(state=tk.DISABLED)
            self.DisconnectButton.config(state=tk.NORMAL)
            self.LoginUser()

        self.client_is_connected = True
        #print(sio.sid + " # SID # ")

    def DisconnectionServer(self):
        if self.client_is_connected != True:
            id_client = sio.sid
            sio.emit('logout', self.current_user.nick_name)
            sio.disconnect()
            self.ConnectionButton.config(state=tk.NORMAL)
            self.DisconnectButton.config(state=tk.DISABLED)
        else: print("LOGS # now is deisconnected !!! ")
        self.client_is_connected = False
        self.UserIsLogined = False
       # print(id_client + " # is disconnected # ")
        #print("BUTTON is clicked!!!")

    def ClosedMainWindow(self):
        if self.client_is_connected :
           id_client = sio.sid
           sio.disconnect()
           print(id_client + " # is disconnected # ")

        self.window.quit()

    def SendMasseges(self):
        if self.client_is_connected == True:
           message_body = self.EntryMsgPlace.get()
           sio.emit('message' , [self.current_user.nick_name , message_body])

           self.EntryMsgPlace.delete(0 , 'end')
        else :
            print("### logs ###")
            print("error 404 # don't connect to the server")

    def WirteMessageToText(self , data):
        self.ChatTextPlace.config(state=tk.NORMAL)
        self.ChatTextPlace.insert(tk.END, data)
        self.ChatTextPlace.insert(tk.END, '\n')
        self.ChatTextPlace.config(state=tk.DISABLED)


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


    def __init__(self):
        self.window.geometry("600x600")
        self.window.resizable(0 , 0)
        self.window.configure(bg='gray74')
        self.window.title("Test of Client!!!")

        Gui_Client.ChatTextPlace.config(state=tk.DISABLED)

        #Buttons positions
        self.ConnectionButton.config(command=lambda : self.ConnectionToServer())
        self.ConnectionButton.place(x = 150 , y = 500)

        self.DisconnectButton.place(x = 0 , y = 500)
        self.DisconnectButton.config(state=tk.DISABLED)
        self.DisconnectButton.config(command=lambda : self.DisconnectionServer())

        self.QuitButton.place(x = 0 , y = 540)
        self.QuitButton.config(command=lambda : self.ClosedMainWindow())

        self.SendButton.place(x = 150 , y = 540)
        self.SendButton.config(command = lambda : self.SendMasseges())
        #Entry
        self.EntryMsgPlace.place(x = 0 , y = 465 )

        #Text
        self.ChatTextPlace.place(x = 10 , y = 10)
       # self.ChatTextPlace.insert(tk.INSERT , "HELLO")
        #self.ChatTextPlace.config(state = tk.DISABLED)

        #ListBox
        self.ListBoxUsers.place(x = 300 , y = 10)

        #Menu
        self.SubMenuWidget.add_command(label="Connection", command=lambda: self.ConnectionToServer())
        self.SubMenuWidget.add_command(label = "disconnect" , command = lambda : self.DisconnectionServer())

        self.CloseSubMenuWidget.add_command(label = "Close" , command = lambda : self.ClosedMainWindow())

        self.LoginSubMenuWidget.add_command(label = "Login" , command = lambda : self.LoginUser())

        self.MenuWidget.add_cascade(label = "Connection" , menu = self.SubMenuWidget)
        self.MenuWidget.add_cascade(label = "Close Chat" , menu = self.CloseSubMenuWidget)
        self.MenuWidget.add_cascade(label = "Logins" , menu = self.LoginSubMenuWidget)

        self.window.config(menu = self.MenuWidget)
        self.window.mainloop()



