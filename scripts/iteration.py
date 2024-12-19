def iteration(g, x0, tol, nmax, i):
    x1 = g(x0)

    print(f"Iteration ({i}):" + str(x1))

    if abs(x1 - x0) < tol or i >= nmax:
        return x1

    return iteration(g, x1, tol, nmax, i + 1)