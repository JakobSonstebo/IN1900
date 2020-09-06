s = 0
M = 3

for k in range(1, M):           # k and not i in the for loop expression and range(1, M + 1) for [1, 2, 3]
    s += 1/(2*k)**2             # Parenthesis

print(s)
