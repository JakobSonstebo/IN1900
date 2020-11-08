class Quadratic(object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        s = 0
        for i, coefficient in enumerate(self.coefficients):
            s += coefficient*x**i
        return s

    def __str__(self):
        s = ''
        for i, coefficient in enumerate(self.coefficients):
            if i == len(self.coefficients) - 1:
                s += f'{coefficient}x^{i}'
            else:
                s += f'{coefficient}x^{i} + '
        return f'{s}'


class Cubic(Quadratic):
    def __init__(self, coefficients):
        super().__init__(coefficients)

    def derivative(self):
        del self.coefficients[0]
        new_coefficients = []
        for i, coefficient in enumerate(self.coefficients):
            new_coefficients.append((i + 1) * coefficient)
        return Quadratic(new_coefficients)


# Oppgave a
q = Quadratic([1, 3, 2])
print(q)
print(f'q(1) = {q(1)}, q(2) = {q(2)}')

# Oppgave b
c = Cubic([1, 3, 2, 4])
print(c)
print(f'c(1) = {c(1)}, c(2) = {c(2)}')
print(c.derivative())

"""
Terminal>>python polynomial.py
1x^0 + 3x^1 + 2x^2
q(1) = 6, q(2) = 15
1x^0 + 3x^1 + 2x^2 + 4x^3
c(1) = 10, c(2) = 47
3x^0 + 4x^1 + 12x^2
"""