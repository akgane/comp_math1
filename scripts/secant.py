import math

tol = (10 ** -6)


def func(x):
    return x**3 - x - 1


def secant(func, a, b, tol, nmax = 500, i = 0):
    fa = func(a)
    fb = func(b)

    #print(a, fa, b, fb)

    approx = b - fb*((b - a) / (fb - fa))

    print(f"Approximation ({i}):", approx)

    if abs(approx - b) > tol:
        return secant(func, b, approx, tol, nmax, i + 1)
    return approx


def secant_wrapper(func, a, b, tol, nmax = 500, i = 0):
    if a > b or func(a) * func(b) >= 0:
        return 0
    return secant(func, a, b, tol, nmax, i)

# print(secant_wrapper(1, 2, tol))