from modules.classes import Register, Login
import getpass

notification = """
    Type 'register' to create new account.
    Type 'login' to sing in.
    Type 'exit' to quit.'
"""

print(notification)
decision = input("What do you wanna do? ").lower()

while decision != "exit":

    if decision == "register":
        email = input("Type email: ")
        password = getpass.getpass("Enter password: ")
        confirmPassword = getpass.getpass("Confirm password: ")

        if password==confirmPassword:
            if Register.validate_email(email):
                if not Register.email_taken(email)[0]:
                    newUser = Register(email, password)
                    newUser.save_new_user()
                    print("Your account has been successfully created!")
                    decision = input("Type 'login' to sing in: ").lower()
                else:
                    print("This email is already taken. Please ry again!")
                    break
            else:
                print("Your email is not valid. Try again!")
                break
        else:
            print("Both passwords are not the same. Try again!")
            break

    elif decision=="login":
        email = input("Type email: ")
        if Login.email_taken(email):
            password = getpass.getpass("Enter password: ")
            newLogin = Login(email, password)
            if newLogin.check_password_for_user(email, password):
                print("You have been successfully logged in!")
                decision = input("What do you wanna do next? ").lower()
            else:
                print("Wrong password. Try again!")
                decision = input("What do you wanna do next? ").lower()
        else:
            print("This email doesn't exist. Registration required!")
            break
    else:
        print(f"Command {decision} not found. Try again!")
        decision = input("What do you wanna do next? ").lower()

print("Bye!")