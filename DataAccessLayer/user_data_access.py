# Import Sqlite3
import sqlite3
from CommonLayer.user import User


# Create user data access class

class UserDataAccess:
    def __init__(self):
        self.data_base_name = "PasswordHashingTraining.db"

    # Account creation by the user
    def create_account(self, firstname, lastname, username, password):
        # Insert User information into database with query
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO User (
                         first_name,
                         last_name,
                         username,
                         password
                     )
                     VALUES (
                         ?,
                         ?,
                         ?,
                         ?
                     )""", [firstname, lastname, username, password])
            connection.commit()

    # Getting user account information and user login in the application when the entered information is correct
    def get_user(self, username, password):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username
                FROM User
                WHERE  username = ?
                AND    password = ?""", [username, password]).fetchone()

            if data:
                user = User.create_with_tuple(data)
                return user
            else:
                return None

    # Returning all the hashed passwords stored in the database to make sure they are correct.
    def return_all_password(self):
        passwords = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                SELECT id,
                       first_name,
                       last_name,
                       username,
                       password
                FROM User""").fetchall()

            for item in data:
                passwords.append(item[4])
            return passwords


