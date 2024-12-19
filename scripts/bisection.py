import math

tol = (10 ** -6)


def bisection(a, b, tol, nmax, i):
    c = (a + b) / 2.0
    fc = func(c)

    print(str(c) + " | " + str(fc) + " | " + str(i))

    if abs(fc) < tol or i >= nmax:
        print("Root is " + str(fc))
        return fc

    if func(c) * func(a) < 0:
        return bisection(a, c, tol, nmax, i + 1)
    else:
        return bisection(c, b, tol, nmax, i + 1)


def bisection_wrapper(a, b, tol, nmax=500, i=0):
    if func(a) * func(b) >= 0 or a >= b:
        print("Wrong input")
        return
    return bisection(a, b, tol, nmax, i)


def func(x):
    return math.exp(x) - x ** 2


print(bisection_wrapper(-2, 0, tol, 500, 0))
