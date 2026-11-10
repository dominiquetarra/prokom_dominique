from pathlib import Path
import json

def stored_user(path) :
    if path.exists() :
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else :
        return None

def new_user (path) :
    username = input("Username : ")
    game = input("Game : ")

    user_data = {
        'username' : username , 
        'game' : game
    }
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def greet_user() :
    path = Path('exercise10_13.json')
    user_data = stored_user(path)
    if user_data :
        print(f"Welcome back {user_data['username']}")
        print(f"Hope you enjoy playing {user_data['game']}")
    else :
        user_data = new_user(path)
        print(f"Hi, {user_data['username']}! We'll remember you when you return")

greet_user()