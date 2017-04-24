def decompose(n, sum_=None):
    if sum_ is None:
        sum_ = n ** 2
    for i in range(1, n):
        if sum_ - (n - i) ** 2 == 0:
            return [n-i]
        if sum_ < (n - i - 1) ** 2:
            continue
        solution = decompose(n-i, sum_ - (n - i) ** 2)
        if solution is None:
            continue
        else:
            return solution + [n - i]
    return


print(decompose(50))
