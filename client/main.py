
import autorization
from gui_client import socketio
import tkinter as tk

class ChatAppController:
    #app_chat = gui_client.Gui_Client()

    def OpenWindow(self):
        self.app_autorization = autorization.WindowManager()
        self.app_autorization.root.mainloop()





def main():
    app = ChatAppController()
    app.OpenWindow()

    # HOST = "localhost"
    # PORT = ":8000"
    #
    # sio = socketio.Client()
    #
    # sio.connect("http://" + HOST + PORT)


if __name__ == "__main__":
    main()