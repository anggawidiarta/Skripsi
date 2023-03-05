# import math

# def calc(b, c):
#     result = math.log(2+(b/max(1,c)))
#     print(result)

# calc(1,1)


x = 0.69314


def crossRF(number):
    return number * x


result = list(map(crossRF, (1/20,0,1/16,1/8)))

print(result)
