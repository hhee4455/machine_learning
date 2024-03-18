from LSJ import calculator

while True:
    expression = input("Input: ")
    if expression == '0 0 0':
        break
    print(calculator(expression))