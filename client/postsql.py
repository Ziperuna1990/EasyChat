import psycopg2
from psycopg2 import Error
import ClientClass as User
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Postgres():
    conn = None

    # INSERT
    def AddInfoToDB(self , user = User.Client()):
        self.ConnectionToDB()
        cursor = self.conn.cursor()
        user_info = (user.user_id, user.login, user.password, user.sid, user.nick_name)
        sql = """INSERT INTO "User" (user_id , login_user , password_user , sid_user , nickname_user) VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(sql , user_info)
        self.conn.commit()
        self.CloseConnectionDB(cursor)

    # GET########################################
    def GetSidFromLogin(self , login):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT sid_user FROM "User" WHERE login_user = %s"""
        cursor.execute(sql, (login,))
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetAllSid(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        cursor.execute("""SELECT sid_user FROM "User" """)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetAllPasswords(self): # все пароли с БД
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        cursor.execute("""SELECT password_user FROM "User" """)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetColUser(self): # количество юзеров в БД
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT * FROM "User" """
        cursor.execute(sql)
        all_result = cursor.fetchall()
        print(len(all_result))

        self.CloseConnectionDB(cursor)
        return len(all_result)

    def GetIdFromName(self , nick_name):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT user_id FROM "User" WHERE nickname_user = %s """
        cursor.execute(sql, (nick_name,))
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetNameFromLogin(self , login):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT nickname_user FROM "User" WHERE login_user = %s """
        cursor.execute(sql , (login , ))
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetIdUser(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT user_id FROM "User" """
        cursor.execute(sql)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetInfoDB(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM "User" """)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetAllNameDB(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        cursor.execute("""SELECT nickname_user FROM "User" """)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetAllLogins(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        cursor.execute("""SELECT login_user FROM "User" """)
        all_result = cursor.fetchall()
        print(all_result)

        self.CloseConnectionDB(cursor)
        return all_result

    def GetNameFromSid(self , sid):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """SELECT nickname_user FROM "User" WHERE sid_user = %s """
        cursor.execute(sql , (sid , ))
        all_result = cursor.fetchall()

        self.CloseConnectionDB(cursor)
        return all_result

    # UPDATE##########################################
    def UpdateSid(self , sid , name):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """UPDATE "User" SET sid_user = %s WHERE nickname_user = %s """
        cursor.execute(sql, (sid,name))
        self.conn.commit()

        self.CloseConnectionDB(cursor)

    def UpdateSidl(self , sid , current_sid):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """UPDATE "User" SET sid_user = %s WHERE sid_user = %s"""
        cursor.execute(sql, (sid,current_sid))
        self.conn.commit()

        self.CloseConnectionDB(cursor)

    # DELETE

    def DeleteDataFronUserName(self, nickname):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """DELETE FROM "User" WHERE nickname_user=%s """
        cursor.execute(sql, (nickname,))
        self.conn.commit()

        self.CloseConnectionDB(cursor)

    def DeleteAllDataDB(self):
        self.ConnectionToDB()

        cursor = self.conn.cursor()
        sql = """DELETE FROM "User" """
        cursor.execute(sql)
        self.conn.commit()

        self.CloseConnectionDB(cursor)


    def CloseConnectionDB(self , cursor):
        if self.conn:
            cursor.close()
            self.conn.close()
            print("Соединение с PostgreSQL закрыто")


    def ConnectionToDB(self):
        print("adada")
        try:
            self.conn = psycopg2.connect(user="root",
                                         # пароль, который указали при установке PostgreSQL

                                         password="root",
                                         host="127.0.0.1",
                                         database="chat" ,
                                         port="5432")
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            print("Информация о сервере PostgreSQL")
            print(self.conn.get_dsn_parameters(), "\n")
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)



def main():
    db = Postgres()
    db.ConnectionToDB()

    # info = User.Client("andru" , "root" , "root")
    # info.user_id = "2"
    # info.sid = "123124"
    #
    # db.AddInfoToDB(info)
    db.UpdateSidl("None" , "ab2242f")



if __name__ == "__main__":
    main()
