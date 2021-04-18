
class Client :
    login = str()
    password = str()
    nick_name = str()
    sid = str()
    user_id = str()

    def SetLogin(self , login):
        self.login = login

    def SetName(self , name):
        self.nick_name = name

    def SetSid(self , sid):
        self.sid = sid

    def SetId(self , id):
        self.user_id = id

    def SetPassword(self , password):
        self.password = password

    def PrintClientInfo(self):
        print(self.nick_name , " # " , self.sid)


    def __init__(self , name=None , login=None , password = None):
        self.nick_name = name
        self.login = login
        self.password = password
