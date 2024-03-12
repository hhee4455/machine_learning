result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 = result1 + num
    return result1

def add2(num2):
    global result2
    result2 = result2 + num2
    return result2

print(add1(4))
print(add1(6))

print(add2(4))
print(add2(6))