import json

from entity import User
from feactures import object_to_json


class SqlMemory :
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    # @ObjectJson
    def find_user(cls, parms)->User:
        user = User()
        user.username = parms['username']
        user.password = parms['password']
        return object_to_json(user)
    
    @classmethod
    def register(cls)->None:
        pass
    
    @classmethod
    def refresh_token(cls)->None:
        pass
    
    @classmethod
    def reset_password(cls)->None:
        pass

