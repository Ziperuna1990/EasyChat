import tkinter as tk
import client

class Gui_Client:
    window = tk.Tk()
    client_is_connected = False
    #Buttons
    ConnectionButton = tk.Button(window, text="connect", heigh="2", width="10")
    DisconnectButton = tk.Button(window, text="disconnect", heigh="2", width="10")
    QuitButton = tk.Button(window, text="Quit", heigh="2", width="10" , command=quit)
    SendButton = tk.Button(window , text="Send" , heigh="2", width="10")

    EntryMsgPlace = tk.Entry(window, width="30")

    #function for button
    def ConnectionToServer(self):
        client.sio.connect("http://"+ client.HOST + client.PORT)
        self.ConnectionButton.config(state=tk.DISABLED)
        self.DisconnectButton.config(state=tk.NORMAL)

        self.client_is_connected = True
        print(client.sio.sid + " # SID # ")

    def DisconnectionServer(self):
        id_client = client.sio.sid
        client.sio.disconnect()
        self.ConnectionButton.config(state=tk.NORMAL)
        self.DisconnectButton.config(state=tk.DISABLED)

        self.client_is_connected = False
        print(id_client + " # is disconnected # ")
        #print("BUTTON is clicked!!!")

    def ClosedMainWindow(self):
        if self.client_is_connected :
           id_client = client.sio.sid
           client.sio.disconnect()
           print(id_client + " # is disconnected # ")

        self.window.quit()

    def SendMasseges(self):
        if self.client_is_connected == True:
           message_body = self.EntryMsgPlace.get()
           client.sio.emit('message' , message_body)

           self.EntryMsgPlace.delete(0 , 'end')
        else :
            print("### logs ###")
            print("error 404 # don't connect to the server")


    def __init__(self):
        self.window.geometry("300x300")
        self.window.title("Test of Client!!!")

        #Buttons positions
        self.ConnectionButton.config(command=lambda : self.ConnectionToServer())
        self.ConnectionButton.place(x = 100 , y = 30)

        self.DisconnectButton.place(x = 0 , y = 30)
        self.DisconnectButton.config(state=tk.DISABLED)
        self.DisconnectButton.config(command=lambda : self.DisconnectionServer())

        self.QuitButton.place(x = 0 , y = 70)
        self.QuitButton.config(command=lambda : self.ClosedMainWindow())

        self.SendButton.place(x = 100 , y = 70)
        self.SendButton.config(command = lambda : self.SendMasseges())
        #Entry
        self.EntryMsgPlace.place(x = 0 , y = 0 )
        self.window.mainloop()



