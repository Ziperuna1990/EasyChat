
class Client :
    login = str()
    nick_name = str()
    sid = str()

    def __init__(self , login , name , sid ):
        self.login = login
        self.sid = sid
        self.nick_name = name


class ClientManager :
    array_clients = []

    def AddNewClient(self):
        self.array_clients.append(Client)

    def GetArrayClients(self):
        return self.array_clients