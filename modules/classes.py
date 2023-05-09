import json, re

class Register:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def validate_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.__email):
            return True
        else:
            return False
        
    def email_taken(self, currentEmail):
        with open("userDB.json", 'r') as openfile:
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
    def __init__(self, email, password):
        super().__init__(email, password)
