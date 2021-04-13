import sqlite3
import client.info_client as User

#path = r'/Users/andrurevkah/PycharmProjects/GameChat/sqlDB/UsersChats.db'

class ClientsDB :
    conn = None

    def ConnectToDB(self):
        try:
            self.conn = sqlite3.connect(r'/Users/andrurevkah/PycharmProjects/GameChat/sqlDB/UsersChats.db')
        except:
            print("error")

        self.cursor = self.conn.cursor()

    def AddInfoToDB(self , user = User.Client()):
        cursor = self.conn.cursor()
        user_info = (user.user_id , user.login , user.password , user.sid , user.nick_name)
        cursor.execute("INSERT INTO User VALUES(?,?,?,?,?);" , user_info)
        self.conn.commit()

    def DeleteDataFronUserName(self , nickname):
        cursor = self.conn.cursor()
        sql = 'DELETE FROM User WHERE nickname_user=?'
        cursor.execute(sql , (nickname,))
        self.conn.commit()

    def GetInfoDB(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM User;")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def DeleteAllDataDB(self):
        cursor = self.conn.cursor()
        sql = 'DELETE FROM User'
        cursor.execute(sql)
        self.conn.commit()


    def __init__(self):
        self.ConnectToDB()
        #self.GetInfoDB()




def main():
    db = ClientsDB()
    #db.ConnectToDB()

    user = User.Client()
    user.sid = "12345"
    user.nick_name = "MAx"
    user.login = "login"
    user.password = "pass"
    user.user_id = "16"

    #db.AddInfoToDB(user)
    #db.GetInfoDB()
    #db.DeleteAllDataDB()
    #db.GetInfoDB()


if __name__ == "__main__":
    main()