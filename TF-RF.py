import math 

def calc(b, c):
    result = math.log(2+(b/max(1,c)))
    return result

print(calc(2,1))
