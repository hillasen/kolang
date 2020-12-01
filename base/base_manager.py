from base import If, variable, Function, Script, Return, For, Class

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
        if (name == "Script"):
            return Script.Script()
        if (name == "Return"):
            return Return.Return()
        if (name == "For"):
            return For.For()
        if (name == "Dot"):
            return Class.Dot()