import timeit

kfib_limit= 10001
lfib_memorization = [0 for i in range(kfib_limit)]

def fib_memorization(n):
    if n < 1:
        return n
    if n == 1 or n == 2:
        return 1
    else:
        if not n < kfib_limit:
            return fib_memorization(n-1) + fib_memorization(n-2)

        if lfib_memorization[n]:
            return lfib_memorization[n]
        else:
            lfib_memorization[n] = fib_memorization(n-1) + fib_memorization(n-2)
            return lfib_memorization[n]

def fib_recursive(n):
    if n < 1:
        return n
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
    while True:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
            break
        st1 = timeit.default_timer()
        print(fib_recursive(nbr))
        print("recursive elapsed %.6f"% round(timeit.default_timer() - st1, 6))

        st2 = timeit.default_timer()
        print(fib_memorization(nbr))
        print("memorization elapsed %.6f" % round(timeit.default_timer() - st2, 6))

        st3 = timeit.default_timer()
        print(fib_loop(nbr))
        print("loop elapsed %.6f" % round(timeit.default_timer() - st3, 6))

        #for fill zero in memorization list
        lfib_memorization = list(map(lambda x: 0, lfib_memorization))
