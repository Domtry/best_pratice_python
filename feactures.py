import json

class ObjectJson:
    
    def __init__(self, func):
        self.__func = func

    def __call__(self, **arg):
        rsult = self.__func(self, arg[1])
        return json.dumps(rsult.__dict__) 
    
    
def object_to_json(obj:object):
    return json.dumps(obj.__dict__) 