from base import  base_manager

class If:
    def __init__(self):
        self.rule = ["(", "contents", ")"]
        self.info = {"name" : "If", "keyword" : "만약"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        return "if(" + option['contents'] + ")"
        pass