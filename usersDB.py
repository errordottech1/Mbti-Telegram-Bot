import sqlite3
class UsersDatabase:
    def create(self):       
        try:
            conn = sqlite3.connect('mbtiDataBase.db')
            query = """CREATE TABLE mbtiUsers(
                                                ID INTEGER NOT NULL,
                                                I INTEGER NOT NULL, 
                                                E INTEGER NOT NULL, 
                                                S INTEGER NOT NULL, 
                                                N INTEGER NOT NULL, 
                                                T INTEGER NOT NULL, 
                                                F INTEGER NOT NULL, 
                                                P INTEGER NOT NULL,
                                                J INTEGER NOT NULL, 
                                                LEVEL INTEGER NOT NULL )"""

            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:        
            if (conn):
                conn.close()
                print("sqlite connection is closed")

    def insert(self, i,e,s,n,t,f,p,j,lvl,user_id):
        conn = sqlite3.connect('mbtiDataBase.db')
        conn.execute("INSERT INTO mbtiUsers (ID,I,E,S,N,T,F,P,J,LEVEL) "
                    "VALUES (?,?, ?, ?, ?, ?, ?,?,?,?)",(user_id,i,e,s,n,t,f,p,j,lvl))
        conn.commit()
        conn.close()

    def levelById(self,userIDDD):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT LEVEL from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (userIDDD, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]
        

    def checkUser(self,userIID):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT * from mbtiUsers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            if row[0] == userIID:
                return 1
        return 0

    def increaseLevel(self, id, level):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set LEVEL = ? where ID = ?"""
        data = (level,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("level increased")
        cursor.close()

    def readScoreI(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT I from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]

    def readScoreE(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT E from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]
    
    def readScoreS(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT S from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]
    
    def readScoreN(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT N from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]

    def readScoreT(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT T from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]

    def readScoreF(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT F from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]

    def readScoreP(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT P from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]

    def readScoreJ(self, id):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT J from mbtiUsers where id = ?"""
        cursor.execute(sqlite_select_query, (id, ))
        record = cursor.fetchone()
        conn.close()
        return record[0]
    
    def increaseI(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set I = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()
        
    def increaseE(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set E = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseS(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set S = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseN(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set N = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseT(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set T = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseF(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set F = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseP(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set P = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()

    def increaseJ(self, id,newScore):
        conn = sqlite3.connect('mbtiDataBase.db')
        cursor = conn.cursor()
        sql_update_query = """Update mbtiUsers set J = ? where ID = ?"""
        data = (newScore,id)
        cursor.execute(sql_update_query, data)
        conn.commit()
        print("letter point increased")
        cursor.close()