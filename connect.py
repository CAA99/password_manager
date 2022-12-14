import os 
import sqlite3

db_name = 'password_manager.db'

class Create_DB:
    def __init__(self,db_name):
        self.db_name = db_name
        if os.path.exists(db_name):
            print(f'{db_name} ya existe')
        else:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            try:
                self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS password_manager(
                    "id"	INTEGER NOT NULL,
                    "site_name"	TEXT NOT NULL ,
                    "site_url"	TEXT,
                    "email"	TEXT NOT NULL,
                    "username"	TEXT,
                    "password"	TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT)
                    );
                """)
                self.conn.commit()
                print('BASE DE DATOS HA SIDO CREADA')
            except:
                print('Se ha producido un error')


class PasswordManager:
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    
    def create_user(self, site_name, site_url, email, username, password):
        self.site_name = site_name
        self.site_url = site_url
        self.email = email
        self.username = username
        self.password = password
        print(self.site_name, self.site_url, self.email, self.password)
        try:
            sql = self.cursor.execute(f"""
            INSERT INTO {self.db_name.replace('.db','')} (
                site_name,
                site_url,
                email,
                username,
                password
            )
            VALUES(?,?,?,?,?)""", 
            (self.site_name, self.site_url, self.email, self.username, self.password))
            self.conn.commit()

            return sql.fetchall()
        except sqlite3.Error as e:
            print(e)


    def read_password(self, site_name): 
        self.site_name = site_name

        try:
            sql = self.cursor.execute(f"""
            SELECT site_name, email, username, password 
            FROM password_manager
            WHERE  site_name = ?
            """, (self.site_name,))
            return sql.fetchall()
        except sqlite3.Error as e:
            print(e)


    def update_password(self, site_name, password):
        self.site_name = site_name
        self.password = password

        try:
            self.cursor.execute(f"""
            UPDATE {self.db_name.replace('.db','')} 
            SET password =? 
            WHERE site_name =?""", 
            (self.password, self.site_name))

            self.conn.commit()
        
            return self.cursor.execute(f"""SELECT * FROM {self.db_name.replace('.db','')} WHERE site_name =?""",(self.site_name,)).fetchall()

        except sqlite3.Error as e:
            print(e)

    
    def delete(self, site_name):
        self.site_name = site_name
        self.cursor.execute(f"""DELETE FROM {self.db_name.replace('.db','')} WHERE site_name=?""", (self.site_name,))
        self.conn.commit()
        return 'REGISTRO ELIMINADO'

    def __del__(self):
        self.conn.close()

