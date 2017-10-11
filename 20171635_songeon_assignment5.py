import timeit

kfib_limit= 10001
fib_memorization = [0 for i in range(kfib_limit)]

def fib_memorization(n):
    if n == 1 or n == 2:
        return 1
    else:
        if not n < kfib_limit:
            return fib_memorization(n-1) + fib_recursive(n-2)

        if fib_memorization[n]:
            return fib_memorization[n]
        else:
            fib_memorization[n] = fib_memorization(n-1) + fib_recursive(n-2)
            return fib_memorization[n]

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_loop(n):
    if n == 1 or n == 2:
        return 1
    cn = 0
    nb = 1
    nbb = 1
    for i in range(2, n):
        cn = nb + nbb
        nb, nbb = cn, nb
    return cn

if __name__ == "__main__":
    st = timeit.default_timer()
    print(fib_recursive(20))
    print("recursive elapsed", timeit.default_timer() - st)

    st = timeit.default_timer()
    print(fib_memorization(20))
    print("memorization elapsed", timeit.default_timer() - st)

    st = timeit.default_timer()
    print(fib_loop(20))
    print("loop elapsed", timeit.default_timer() - st)
