'Sample Exception Handling'
try:
    a = pow(2, 4)
    print("Value of 'a' :", a)
    b = pow(2, 'hello')   # results in exception
    print("Value of 'b' :", b)
except TypeError as e:
    print('oops!!!')
print('Out of try ... except.')

'Raising Exceptions'
try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise TypeError('Two inputs must be integers.')
    c = a**b
except TypeError as e:
    print(e)

'User Defined Functions'
class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
try:
    a = 2; b = 'hello'
    if not (isinstance(a, int)
            and isinstance(b, int)):
        raise CustomError('Two inputs must be integers.')
    c = a**b
except CustomError as e:
    print(e)

'Using finally clause'
def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Dividing by Zero.")
    finally:
        print("In finally clause.")
print('First call')
print(divide(14, 7))
print('Second call')
print(divide(14, 0))

# Using 'else' clause
try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE')
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')


