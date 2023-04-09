from User import User
from Send import stringify
from Codes import response_failed, response_ok, response_slept

from getpass import getpass
from time import sleep

import readline
import hashlib
import json
import base64

def start_pass_prompt():

    ### Account prompt
    
    print("----- ACCOUNT CREATION -----")
    username = input("enter a username: ")
    
    sleep(1) # prevent quick bot access

    password = getpass("enter a password: ")

    sleep(1)
    
    admin = input("Should this user be admin? (y-n) ")

    ### quick solution to parse y/n
    if (admin == "y"): admin = True
    else: admin = False

    ### construct a user

    construct = User(name=username, password_utf8=password,
                    admin=admin)
    cfg = construct.as_json()
    asbase64 = base64.b64encode(bytes(cfg, 'utf-8')).decode("utf-8")


    # print(base64.b64decode(asbase64).decode("utf-8"))

    with open("account.json", "w") as f:
        f.write(asbase64)

    print("account created. restart.")
    
    return response_ok

def login_prompt() -> int:
    u = input("username: ")
    p = getpass("password: ")
    
    hash = hashlib.md5()
    hash.update(p.encode()) # hash it

    js = None
    
    with open("account.json") as f:
        asstring = base64.b64decode(f.read()).decode("utf-8")
        js = json.loads(asstring)

    if (hash.hexdigest() == js["password"]):
        print("login successful")
        return response_ok
    else:
        print("login failed")
        return response_failed

import pathlib

def check_and_ask():
    if not (pathlib.Path("account.json").exists()):
        return start_pass_prompt()
    else:
        return login_prompt()