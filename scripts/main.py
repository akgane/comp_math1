import math
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from scripts.iteration import iteration
from scripts.newton_raphson import newton_raphson
from scripts.secant import secant_wrapper


def g1(x):
    return (x + 1) ** (1 / 3)


def g2(x):
    return math.cos(x)


def g3(x):
    return math.exp(-x)


def g4(x):
    return -((x**2 + x + 7) ** (1/3))


def g5(x):
    return (-4 * math.sin(x)) ** 1/2


def g6(x):
    return math.cos(x) / math.exp(x)


def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 500)
    y = [func(val) for val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.title("graph")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


tol = (10 ** -6)
x0 = 0.5
nmax = 100


def func(x):
    return math.cos(x) - x * math.exp(x)

iteration_ans = iteration(g6, x0, tol, nmax, 0)
secant_ans = secant_wrapper(func, 0, 1, tol, nmax, 0)
newton_raphson_ans = newton_raphson(func, x0, tol, nmax, 0)

print(f"{iteration_ans:.3f}")
print(f"{secant_ans:.3f}")
print(f"{newton_raphson_ans:.3f}")

plot_function(func, (-2, 2))
