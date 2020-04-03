x = [6, 3, 1]
g = (i**2 for i in x) #Generator Expression
print(next(g)) # -> 36
