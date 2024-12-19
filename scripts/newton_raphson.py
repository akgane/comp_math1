import math
from scipy.misc import derivative


def func(x):
    return x**3 - x - 1


def dfunc(func, x):
    return derivative(func, x)


def newton_raphson(func, x, tol, nmax, i):
    fx = func(x)
    dfx = dfunc(func, x)

    print(f"Newton-Raphson ({i}):", x)

    if abs(fx) < tol or i >= nmax:
        return x

    x_new = x - fx / dfx
    return newton_raphson(func, x_new, tol, nmax, i + 1)

# print(newton_raphson())