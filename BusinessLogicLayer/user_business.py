# Create user business class
from DataAccessLayer.user_data_access import UserDataAccess
# Download passlib module for password Hashing
# pip install passlib with terminal
# import passlib
from passlib.hash import pbkdf2_sha256


class UserBusiness:
    def __init__(self):
        self.user_data_access = UserDataAccess()

        self.user = None

    # Sign-in in Application
    def sign_in(self, firstname, lastname, username, password):
        if len(firstname) < 3:
            return [None, "Length First Name should be least 3"]
        # Ensuring that there is no number in the First name
        if any(char.isdigit() for char in firstname):
            return [None, "The First Name does not have a number"]

        if len(lastname) < 4:
            return [None, "Length Last Name should be least 4"]
        # Ensuring that there is no number in the Last name
        if any(char.isdigit() for char in firstname):
            return [None, "The Last Name does not have a number"]

        if len(username) < 3:
            return [None, "Length Username should be least 3"]

        # Enter a strong password
        if len(password) < 6:
            return [None, "length Password should be at least 6"]

        hash_password = pbkdf2_sha256.hash(password)

        self.user_data_access.create_account(firstname, lastname, username, hash_password)
        return [f"You have successfully registered in the application.\n Go back to the previous page and login.", None]

    # Login in Application
    def login(self, username, password):
        passwords = self.user_data_access.return_all_password()

        if len(username) < 3 or len(password) < 3:
            return [None, "Invalid Request"]
        # We loop over the received passwords to check each one of them
        for item in passwords:
            # pbkdf2_sha256 class has verify method.
            # We have to give two things to this method.
            # The first input of this method is the password that the user is going to enter.
            # The second input of this method is something that has already been hashed.
            # If the password has already been hashed, it will show the True result and allow the user to enter the
            # application, otherwise it will give the user an incorrect username or password error
            if pbkdf2_sha256.verify(password, item):  # == True
                self.user = self.user_data_access.get_user(username, item)
                break

        if self.user:
            return [self.user, None]
        else:
            return [None, "Invalid Username or Password"]



