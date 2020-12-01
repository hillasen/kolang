from base import  base_manager

class Dot:
    def __init__(self):
        self.rule = []
        self.info = {"name" : "dot", "keyword" : "의"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        return "."
        pass