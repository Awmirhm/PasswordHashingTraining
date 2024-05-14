# *This project is a simple educational project in which I used `three-layer architecture (MVC)`.*
### *In this project, I taught you how to hash a password and store it in the database and still be able to log in to the application.*

## We use the `passlib` library and the `pbkdf2_sha256` class to do this

#### *In the first step, we create the user registration section in the application. In this section, the user must enter the first name, last name, username and password. We store the entered information in the database.*

## But our work does not end at this stage, and the main problem is at the stage of entering the user into the application.

### *When the user enters his username and password in the application, this error is sent to the user that the username and password are wrong!!*
### *This problem is because the user entered a password: for example 123, but the same password does not exist in the database, there is a hash of this password in the database.*

## *To solve this problem, in the Data Access layer, we extract all the passwords stored in the database and put them in a list, then in the Business Logic layer, we process the passwords that are in a list and loop over them.*

#### The pbkdf2_sha256 class has a verify method that receives two parameters, the first parameter is the password that the user enters, and the second parameter is the hashes that we have stored in the database. Then we put it inside a condition (if), if the entered password matches the hash we entered, it will return true, otherwise it will return false.

#### If it is correct, the user enters the application, but if it is wrong, the error of the username and password is shown to the user.
