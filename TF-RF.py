# import math

# def calc(b, c):
#     result = math.log(2+(b/max(1,c)))
#     print(result)

# calc(1,1)


x = 1.09861


def crossRF(number):
    return number * x


result = list(map(crossRF, (1/8,0,0,0)))
print(result)
