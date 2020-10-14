def fibonacci(x0, x1, N):
    """Function that prints out the first N fibonacci numbers"""
    # Initial conditions
    initial = [x0, x1]
    for n in range(len(initial)):
        print(f'x_{n}: {initial[n]}')

    # Printing out the rest
    xnm2 = x0
    xnm1 = x1
    for n in range(2, N):
        xn = xnm1 + xnm2
        print(f"x_{n}: {xn}")
        xnm2 = xnm1; xnm1 = xn

fibonacci(1, 1, 15)

"""
Terminal>>python fibonacci.py
x_0: 1
x_1: 1
x_2: 2
x_3: 3
x_4: 5
x_5: 8
x_6: 13
x_7: 21
x_8: 34
x_9: 55
x_10: 89
x_11: 144
x_12: 233
x_13: 377
x_14: 610
"""
