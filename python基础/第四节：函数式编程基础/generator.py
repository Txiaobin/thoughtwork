def fib_yield(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

a = fib_yield(5)
for i in range(5):
    print(next(a))