import configparser
import hashlib
import json

# basic user construct
# * define name, password, and admin
class User:
    def __init__(self, name, password_utf8, admin = False, config_file = "account.cfg") -> None:
        self.config_file = config_file
        self.name = name
        hash = hashlib.md5()
        hash.update(password_utf8.encode()) # hash it
        self.password = hash.hexdigest()
        self.admin = admin
        
    def as_dict(self):
        return {
            "name": self.name,
            "password": self.password,
            "admin": self.admin
        }

    def as_json(self):
        return json.dumps(self.as_dict(), indent=5) # jsonify the dict

    def as_config(self):
        cfg = configparser.ConfigParser()
        cfg["USER"] = (self.as_dict())

        return cfg
