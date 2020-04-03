def fib_gen():
    yield 0
    yield 1
    a, b = 0, 1
    while True:
        yield a+b
        a, b = b, a+b

fs = fib_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
