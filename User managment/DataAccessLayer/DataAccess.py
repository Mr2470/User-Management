import sqlite3
from CommonLayer.user import User


class DataAccess:
    def get_user(self, username, password):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute(f"""SELECT id,
            f_name,
            l_name,
            Username,
            Password,
            is_Active,
            role
            FROM user
            where Username = ?
            and Password = ?;
    
            """, [username, password]).fetchone()
            user = User(data[0],data[1],data[2],data[3],None,data[5],data[6])
            print(user.firstName)
            return user
    def get_all_users(self):
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""SELECT id,
       f_name,
       l_name,
       Username,
       is_Active,
       role
  FROM user;
""").fetchall()
            return data
    def ActiveUser(self,id):
        print(id)
        for i in id:
            with sqlite3.connect("database.db") as connection:
                cursor = connection.cursor()
                data = cursor.execute(f"""UPDATE user
   SET is_Active = ?
 WHERE id = ?;""",[0,i])
                connection.commit()
                print("Activation compelite")

    def DeActiveUser(self,id):
        print(id)
        for i in id:
            with sqlite3.connect("database.db") as connection:
                cursor = connection.cursor()
                data = cursor.execute(f"""UPDATE user
           SET is_Active = ?
         WHERE id = ?;""", [1, i])
                connection.commit()
                print("DeActivation compelite")
    def Register(self,fname,lname,username,password):
        print(fname,lname,username,password)
        with sqlite3.connect("database.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO user (
                     f_name,
                     l_name,
                     Username,
                     Password                     
                     )
                 VALUES (
                     '{fname}',
                     '{lname}',
                     '{username}',
                     '{password}'
                 );""")
            connection.commit()