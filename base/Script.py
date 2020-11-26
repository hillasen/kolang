from base import  base_manager

class Script:
    def __init__(self):
        self.rule = ["contents", "text", "를" , "contents_2", "text", "에서"]
        self.info = {"name" : "Script", "keyword" : "스크립트"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        return "import " + option['contents'] + " from " + option['contents_2'] + ";"
        pass