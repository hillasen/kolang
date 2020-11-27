from base import  base_manager

class For:
    def __init__(self):
        self.rule = ["(","contents", "text" ,"가", "contents_2", "text", "부터","contents_3", "text", "까지",")"]
        self.info = {"name" : "For", "keyword" : "반복하기"}
        pass
    def getInfo(self):
        return self.info

    def getRule(self):
        return self.rule

    def doRun(self, option):
        if(int(option['contents_2']) <= int(option['contents_3'])):
            return "for(var " + option['contents'] + "=" + option['contents_2'] + ";" + option['contents'] + "<=" + option['contents_3'] + ";" + option['contents'] + "++)"
        if(int(option['contents_2']) > int(option['contents_3'])):
            return "for(var " + option['contents'] + "=" + option['contents_2'] + ";" + option['contents'] + ">=" + option['contents_3'] + ";" + option['contents'] + "--)"
        pass