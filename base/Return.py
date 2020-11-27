from base import  base_manager

class Return:
    def __init__(self):
        self.rule = []
        self.info = {"name" : "Return", "keyword" : "돌려주기"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        return "return "
        pass