from library import keyword_map

key_map = keyword_map.Keyword_map()
non_k_map = ["{", "}", "(", ")"]
def code_parser(code):
    k_map = key_map.getMaps()
    for rpl in non_k_map:
        code = code.replace(rpl, " " + rpl + " ")
        pass
    for rpl in k_map:
        code = code.replace(rpl + " ", rpl + " ")
        pass
    for rpl in k_map:
        code = code.replace('\n'," " + "___nextline___" + " ")
        pass
    parsed_code = code.split()
    #print(parsed_code)
    return parsed_code