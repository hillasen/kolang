from base import variable
from base import If
from base import variable

instant_if = If.If()
instant_variable = variable.Variable()

class Keyword_map(object):
    def __init__(self):
        self.maps = [instant_if.getInfo()['keyword'], instant_variable.getInfo()['keyword']]
        self.names = [instant_if.getInfo()['name'], instant_variable.getInfo()['name']]
        pass
    def getMaps(self):
        return self.maps
    def getName(self):
        return self.names