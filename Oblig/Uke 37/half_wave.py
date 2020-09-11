from math import sin


def f(x):
    """Half wave rectifier."""
    if sin(x) > 0:
        return sin(x)
    else:
        return 0


def test_f_x():
    """Test for half wave rectifier with two values."""
    x_test = [0, 1]
    expected = [0, sin(1)]
    tol = 1E-14
    for x, exp in zip(x_test, expected):
        assert abs(f(x) - exp) < tol, f"Function does not return correctly rectified values"
    return


test_f_x()

"""
Terminal >> half_wave.py

"""
