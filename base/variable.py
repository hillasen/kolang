from base import  base_manager

class Variable:
    def __init__(self):
        self.rule = []
        self.info = {"name" : "Variable", "keyword" : "변수"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        return "var "
        pass