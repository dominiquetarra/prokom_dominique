from pathlib import Path
import json

def stored_user(path) :
    if path.exists() :
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else :
        return None

def new_user (path) :
    username = input("Username : ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user() :
    path = Path('exercise10_14.json')
    username = stored_user(path)
    if username :
        correct = input(f"Are you {username}? (y/n) : ")
        if correct == 'y' :
            print(f"Welcome back {username}")
        else :
            username = new_user(path)
            print(f"Hi, {username}! We'll remember you when you return")
    else :
        username = new_user(path)
        print(f"Hi, {username}! We'll remember you when you return")

greet_user()