import json, re

class Register:
    """
    This class creates new user object with email and password attributes.
    Additionally: 
        -checking email format correctness, doesn't allow to register 
        -it doesn't allow to register more then one user with the same email addess
        -saving new user object to json file if requirements are satisfied
    """
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    @staticmethod
    def validate_email(email:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True
        else:
            return False
    
    @staticmethod
    def email_taken(currentEmail:str):
        with open("userdb.json", 'r') as openfile:
            json_object = json.load(openfile)

        usersCount = len(json_object)
        emailTaken = False

        for x in range(usersCount):
            if currentEmail==json_object[x]["email"]:
                emailTaken = True
                break
        return emailTaken
    
    def save_new_user(self):
        with open("userdb.json", 'r') as openfile:
            json_object = json.load(openfile)

        with open("userdb.json", mode='w', encoding='utf-8') as feedsjson:
            entry = {'email': self.__email, 'password': self.__password}
            json_object.append(entry)
            json.dump(json_object, feedsjson)

class Login(Register):
    """
    Register class but extended by method check_password_for_user for checking if 
    user provided correct password.
    """
    def check_password_for_user(self, currentMail:str, inputPassword:str):

        with open("userdb.json", 'r') as openfile:
            json_object = json.load(openfile)

        usersCount = len(json_object)

        for x in range(usersCount):
            if currentMail==json_object[x]["email"]:
                whichUser = x
                break

        if json_object[whichUser]["password"] == inputPassword:
            return True
        else:
            return False

