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

    def GetNameDB(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nickname_user FROM User")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetAllLogins(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT login_user FROM User")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def DeleteAllDataDB(self):
        cursor = self.conn.cursor()
        sql = 'DELETE FROM User'
        cursor.execute(sql)
        self.conn.commit()

    def GetIdFromName(self , nick_name):
        cursor = self.conn.cursor()
        sql = "SELECT user_id FROM User WHERE nickname_user = ?"
        cursor.execute(sql, (nick_name,))
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetNameFromLogin(self , login):
        cursor = self.conn.cursor()
        sql = "SELECT nickname_user FROM User WHERE login_user = ?"
        cursor.execute(sql , (login , ))
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetIdUser(self):
        cursor = self.conn.cursor()
        sql = "SELECT user_id FROM User"
        cursor.execute(sql)
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetColUser(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM USER"
        cursor.execute(sql)
        all_result = cursor.fetchall()
        print(len(all_result))
        return len(all_result)

    def GetAllPasswords(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password_user FROM User")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def __init__(self):
        self.ConnectToDB()
        #self.GetInfoDB()



def main():
    db = ClientsDB()
    va = db.GetNameFromLogin("admin")
    print(va[0][0])

if __name__ == "__main__":
    main()