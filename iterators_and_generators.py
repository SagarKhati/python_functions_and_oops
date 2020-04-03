lst1 = [1,2,3,4]
for i in lst1:
    print(i)

iter1 = iter([1,2,3])
print(type(iter1))
for i in iter1:
    print(i)

iter1 = iter([1,2,3])
print(next(iter1))
print(next(iter1))
print(next(iter1))
#print(next(iter1)) #StopIteration

iter1 = iter([1,2,3])
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break


###### Generators

def sum_func(a,b):
    return a+b

def generator_123():
    yield 1
    yield 2
    yield 3
print(type(generator_123()))
gen1 = generator_123()
print(next(gen1))
print(next(gen1))
print(next(gen1))
#print(next(gen1)) #StopIteration

gen1 = generator_123()
for i in gen1:
    print(i)
