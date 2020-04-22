def fib_gen(n):
    fn = 1
    for i in range(0, n):
        fn = fn * (i + 1)
        yield fn


n1 = 18
test = 1
for itm in fib_gen(n1):
    print(itm)
    if test > 15 or test == n1:
        break
    test += 1
