import AutorizationWindow

class ChatAppController:
    #app_chat = gui_client.Gui_Client()

    def OpenWindow(self):
        self.app_autorization = AutorizationWindow.WindowManager()
        self.app_autorization.root.mainloop()

def main():
    app = ChatAppController()
    app.OpenWindow()

if __name__ == "__main__":
    main()