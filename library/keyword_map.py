from base import variable
from base import If
from base import variable
from base import Function
from base import Script
from base import Return
from base import For
from base import Class

instant_if = If.If()
instant_variable = variable.Variable()
instant_function = Function.Function()
instant_script = Script.Script()
instant_return = Return.Return()
instant_for = For.For()
instant_dot = Class.Dot()

class Keyword_map(object):
    def __init__(self):
        self.maps = [instant_if.getInfo()['keyword'], instant_variable.getInfo()['keyword'], instant_function.getInfo()['keyword'], instant_script.getInfo()['keyword'], instant_return.getInfo()['keyword'], instant_for.getInfo()['keyword']]
        self.names = [instant_if.getInfo()['name'], instant_variable.getInfo()['name'], instant_function.getInfo()['name'], instant_script.getInfo()['name'], instant_return.getInfo()['name'], instant_for.getInfo()['name']]
        pass
    def getMaps(self):
        return self.maps
    def getName(self):
        return self.names