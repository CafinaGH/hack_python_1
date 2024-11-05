"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    result = result.translate(str.maketrans({'O': '0', 'I': '1', 'A':'@'}))
    result = list(result)
    return result  
print(fn_hack_10())