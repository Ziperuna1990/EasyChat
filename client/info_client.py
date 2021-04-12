
class Client :
    login = str()
    nick_name = str()
    sid = str()

    def SetLogin(self , login):
        self.login = login

    def SetName(self , name):
        self.nick_name = name

    def SetSid(self , sid):
        self.sid = sid

    def PrintClientInfo(self):
        print(self.nick_name , " # " , self.sid)


    def __init__(self , login=None , name=None , sid=None ):
        if sid != None :
            self.login = login
            self.sid = sid
            self.nick_name = name
        else :
            login = None
            name = None
            sid = None
