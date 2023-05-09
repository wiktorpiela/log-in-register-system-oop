import json
import os

def read_json_file(path):
    with open(path, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object

def append_json_file(path, json_object, username, password):
    with open(path, mode='w', encoding='utf-8') as feedsjson:
        entry = {'username': username, 'password': password}
        json_object.append(entry)
        json.dump(json_object, feedsjson)

def check_username_taken(json_object, currentUsername):
    usernameTaken = False
    for x in range(len(json_object)):
        if currentUsername==json_object[x]["username"]:
            usernameTaken = True
            break
    return usernameTaken

