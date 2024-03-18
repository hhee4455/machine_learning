def calculator(expr):
    n, o, m = expr.split()
    n, m = float(n), float(m)
    result = 0

    if o == '+':
        result = n + m
    elif o == '-':
        result = n - m
    elif o == '*':
        result = n * m
    elif o == '/':
        result = n / m
    
    return result