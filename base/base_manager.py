from base import If, variable, Function

class Base_manager(object):
    def __init__(self):
        pass
    def getInstant(self, name):
        if(name == "If"):
            return If.If()
        if (name == "Variable"):
            return variable.Variable()
        if (name == "Function"):
            return Function.Function()