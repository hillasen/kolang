from base import  base_manager

class Function:
    def __init__(self):
        self.rule = ["contents", "(", "contents_2", ")"]
        self.info = {"name" : "Function", "keyword" : "함수"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        if( 'contents' in option.keys()):
            if('contents_2' in option.keys()):
                return "function "+ option['contents'] + "(" + option['contents_2'] + ")"
            else:
                return "function " + option['contents'] + "()"
        else:
            if ('contents_2' in option.keys()):
                return "function(" + option['contents_2'] + ")"
            else:
                return "function()"
        pass