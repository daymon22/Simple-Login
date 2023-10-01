Welcome to my journey!

This Python program is a basic user authentication system that uses a MySQL database to store login information. It provides the following functionalities:

1. **Database Connection:**
   - The `conectar_bd()` function is used to establish a connection to a local MySQL database. It returns a successful connection or displays an error message in case of connection failure.

2. **Password Hashing:**
   - The `calcular_hash(password)` function takes a password as input and calculates the SHA-256 hash of the password. The hash is stored in the database for security, rather than the plain text password.

3. **User Registration:**
   - The `registar()` function allows a new user to register in the system.
   - It checks if the username already exists in the database.
   - It prompts for a password, calculates the hash of the password, and stores the username and password hash in the database.

4. **Login Verification:**
   - The `verificar_login()` function allows a user to log in to the system.
   - It prompts for the username and password, calculates the hash of the password, and checks if the combination of username and password exists in the database.

5. **Password Reset:**
   - The `redefinir_senha()` function allows a user to reset their password.
   - It checks if the username exists in the database and if the current password is correct.
   - If the current password is correct, it allows the user to set a new password.

6. **Interactive Menu:**
   - The program enters an infinite loop that displays an interactive menu to the user.
   - The user can choose between options to register, verify login, reset the password, or exit.
   - Based on the user's choice, the appropriate function (registar, verificar_login, redefinir_senha) is called.

7. **Program Termination:**
   - The "0 - Sair" option allows the user to exit the program, ending the loop.

Overall, this program provides basic user authentication functionalities, but in a production environment, it is important to enhance security, store passwords more securely (e.g., using salting techniques), and implement additional security measures to protect against security threats like SQL injection.
