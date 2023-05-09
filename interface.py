from modules.classes import Register
import getpass

decision = input("").lower()

while decision != "x":

    email = input("Type email: ")
    password = getpass.getpass("Enter password: ")
    confirmPassword = getpass.getpass("Confirm password: ")

    if password==confirmPassword:
        newUser = Register(email, password)

        if newUser.validate_email():
            if not newUser.email_taken(email):
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
