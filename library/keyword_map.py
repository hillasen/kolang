from base import variable
from base import If

instant_if = If.If()

class Keyword_map(object):
    def __init__(self):
        self.maps = [instant_if.getInfo()['keyword']]
        self.names = [instant_if.getInfo()['name']]
        pass
    def getMaps(self):
        return self.maps
    def getName(self):
        return self.names