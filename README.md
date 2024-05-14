# *This project is a simple educational project in which I used `three-layer architecture (MVC)`.*
### *In this project, I taught you how to hash a password and store it in the database and still be able to log in to the application.*

#### *In the first step, we create the user registration section in the application. In this section, the user must enter the first name, last name, username and password. We store the entered information in the database..*

## But our work does not end at this stage, and the main problem is at the stage of entering the user into the application.

### *Because when the user enters his username and password in the application, this error is sent to the user that the username and password are wrong, and this problem is because the user entered the password: for example, 123 but The same password does not exist , In the database and hash this password.*

## *To solve this problem, in the data access layer, we extract all the passwords of the database and put them in a list, then in the logic layer, we loop the passwords we put in a list and do Verification .*

#### The verify method receives two parameters, the first parameter is the password that the user enters, and the second parameter is the hashes that we have stored in the database. Then we put it inside a condition, it returns true if it matches, false otherwise.

#### If it is correct, the user enters the application, but if it is incorrect, the error of the username and password will be shown to the user.
