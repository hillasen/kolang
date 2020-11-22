from base import variable
from base import If
from base import base_manager
from library import  keyword_map

class Builder(object):
    def __init__(self):
        self.instant_if = If.If()
        self.instant_Base_manager = base_manager.Base_manager()
        self.instant_Keyword_map = keyword_map.Keyword_map()
        pass
    def startRun(self, parsed_code):
        is_rule = False
        now_instant = None
        now_rule = []
        now_option = {}
        final_code = ""
        for cmd in parsed_code:
            if(is_rule == True and len(now_rule) == 0):
                is_rule = False
                print(now_instant.doRun(now_option))
                final_code += now_instant.doRun(now_option)
                now_rule = []
                now_option = []
            if(is_rule == True):
                if (now_rule[0] == "(" and cmd == "("):
                    now_option['('] = "("
                    now_rule.pop(0)
                    continue
                if (now_rule[0] == ")" and cmd == ")"):
                    now_option['('] = ")"
                    now_rule.pop(0)
                    continue
                if (cmd == "("):
                    now_option['('] = "("
                    now_option.pop(0)
                    now_rule.pop(0)
                    continue
                if (cmd == ")"):
                    now_option['('] = ")"
                    now_rule.pop(0)
                    now_rule.pop(0)
                    continue
                if (now_rule[0] == "contents"):
                    if 'contents' in now_option.keys():
                        now_option['contents'] += cmd
                    else:
                        now_option['contents'] = cmd
                    continue
                pass

            if cmd in self.instant_Keyword_map.getMaps():
                is_rule = True
                key_idx = self.instant_Keyword_map.getMaps().index(cmd)
                cmd_instant = self.instant_Base_manager.getInstant(self.instant_Keyword_map.getName()[key_idx])
                now_instant = cmd_instant
                now_rule = cmd_instant.getRule()
                continue

            else:
                final_code += cmd
                pass
            pass
        return final_code