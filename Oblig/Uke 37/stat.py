import numpy as np


def mean(x_list):
    """"
    A function that calculates the mean of the values in x_list
    """""
    return 1/len(x_list)*sum(x_list)

def test_mean():
    """"
    A test function that compares mean(x_list) with np.mean()
    """""
    test_x = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(test_x)
    computed = mean(test_x)
    tol = 1E-14
    assert abs(expected - computed) < tol, f'Mean computed {computed} != {expected}(expected)'


test_mean()


def standard_deviation(x_list):
    ''''
    A function that calculates the std of the values in x_list
    '''''
    return np.sqrt(1/len(x_list)*sum((x - np.mean(x_list))**2 for x in x_list))

def test_standard_deviation():
    """""
    A test for std that compares it to numpy.std
    """""
    test_x = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(test_x)
    computed = standard_deviation(test_x)
    tol = 1E-14
    assert abs(expected - computed) < tol, f'Std computed {computed} != {expected}(expected)'


test_standard_deviation()
