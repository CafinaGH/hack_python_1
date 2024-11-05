"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.translate(str.maketrans({'o': '0', 'i': '1', 'a':'@'}))
    return result  
print(fn_hack_5())