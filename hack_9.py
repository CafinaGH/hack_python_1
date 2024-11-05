"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    output = []
    for num in result:
       output.append(num)
       output.append('@')
    return output 

print(fn_hack_9())
