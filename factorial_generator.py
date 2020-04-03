def factorial_gen():
    'Generates the Factorial of Natural Numbers'
    yield 1
    yield 1
    i = 1
    while True:
        i = i * (i+1)
        yield i

fs = factorial_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
