from base import If, variable

class Base_manager(object):
    def __init__(self):
        pass
    def getInstant(self, name):
        if(name == "If"):
            return If.If()