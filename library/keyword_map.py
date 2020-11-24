from base import variable
from base import If
from base import variable
from base import Function

instant_if = If.If()
instant_variable = variable.Variable()
instant_function = Function.Function()

class Keyword_map(object):
    def __init__(self):
        self.maps = [instant_if.getInfo()['keyword'], instant_variable.getInfo()['keyword'], instant_function.getInfo()['keyword']]
        self.names = [instant_if.getInfo()['name'], instant_variable.getInfo()['name'], instant_function.getInfo()['name']]
        pass
    def getMaps(self):
        return self.maps
    def getName(self):
        return self.names