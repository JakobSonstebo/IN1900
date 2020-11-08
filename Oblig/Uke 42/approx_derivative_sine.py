from math import sin, cos, pi

def f(x):
    return sin(x)


def df_approx(f, x, delta_x):
    return (f(x + delta_x) - f(x)) / delta_x


x = pi / 3
for n in range(1, 20):
    delta_x = 10 ** (-n)
    calculated = df_approx(f, x, delta_x)
    exact = cos(x)
    rel_err = abs(calculated - exact) / abs(exact)
    abs_err = abs(calculated - exact)

    print("delta_x: %e, df_approx: %13.10e, df_exact: %13.10e, abs_error: %e, \n"
          "rel_error: %e, n=%d" % (delta_x, calculated, exact, abs_err, rel_err, n))
