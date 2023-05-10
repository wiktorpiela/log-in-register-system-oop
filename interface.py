from modules.classes import Register
import getpass

decision = input("").lower()

while decision != "x":

    email = input("Type email: ")
    password = getpass.getpass("Enter password: ")
    confirmPassword = getpass.getpass("Confirm password: ")

    if password==confirmPassword:
        if Register.validate_email(email):
            if not Register.email_taken(email):
                newUser = Register(email, password)
                newUser.save_new_user()
            else:
                print("This email is already taken. Please ry again!")
                break
        else:
            print("Your email is not valid. Try again!")
            break
    else:
        print("Both passwords are not the same. Try again!")
        break
