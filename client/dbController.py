import sqlite3
import tkinter as tk
import ClientClass as User

#path = r'/Users/andrurevkah/PycharmProjects/GameChat/sqlDB/UsersChats.db'

class ClientsDB :
    conn = None

    def ConnectToDB(self):
        try:
            self.conn = sqlite3.connect(r'/Users/andrurevkah/PycharmProjects/GameChat/sqlDB/UsersChats.db')
        except:
            print("error")

        self.cursor = self.conn.cursor()

    #GET########################################
    def GetSidFromLogin(self , login):
        cursor = self.conn.cursor()
        sql = "SELECT sid_user FROM User WHERE login_user = ?"
        cursor.execute(sql, (login,))
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetAllSid(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT sid_user FROM User")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetAllPasswords(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT password_user FROM User")
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

    def GetInfoDB(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM User;")
        all_result = cursor.fetchall()
        print(all_result)
        return all_result

    def GetAllNameDB(self):
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

    def GetNameFromSid(self , sid):
        cursor = self.conn.cursor()
        sql = "SELECT nickname_user FROM User WHERE sid_user = ?"
        cursor.execute(sql , (sid , ))
        all_result = cursor.fetchall()
        return all_result

    #UPDATE##########################################
    def UpdateSid(self , sid , name):
        cursor = self.conn.cursor()
        sql = "UPDATE User SET sid_user = ? WHERE nickname_user = ?"
        cursor.execute(sql, (sid,name))
        self.conn.commit()

    def UpdateSidl(self , sid , current_sid):
        cursor = self.conn.cursor()
        sql = "UPDATE User SET sid_user = ? WHERE sid_user = ?"
        cursor.execute(sql, (sid,current_sid))
        self.conn.commit()

    #INSERT
    def AddInfoToDB(self , user = User.Client()):
        cursor = self.conn.cursor()
        user_info = (user.user_id , user.login , user.password , user.sid , user.nick_name)
        cursor.execute("INSERT INTO User VALUES(?,?,?,?,?);" , user_info)
        self.conn.commit()

    #DELETE

    def DeleteDataFronUserName(self , nickname):
        cursor = self.conn.cursor()
        sql = 'DELETE FROM User WHERE nickname_user=?'
        cursor.execute(sql , (nickname,))
        self.conn.commit()

    def DeleteAllDataDB(self):
        cursor = self.conn.cursor()
        sql = 'DELETE FROM User'
        cursor.execute(sql)
        self.conn.commit()


    def __init__(self):
        self.ConnectToDB()
        #self.GetInfoDB()
