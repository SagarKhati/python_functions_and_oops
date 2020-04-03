class Person:
    pass

p1 = Person() #Creating the object 'p1'
print(p1) # <__main__.Person object at 0x03EE3070>

'Setting Attributes'
p1.fname = 'Jack'
p1.lname = 'Simmons'
print(p1.fname,'-',p1.lname) # 'Jack - Simmons'


class Person:
    'Represents a person.'
    def __init__(self, fname, lname):
        'Initialises two attributes of a person.'
        self.fname = fname
        self.lname = lname
p1 = Person('George', 'Smith')
print(p1.fname,'-',p1.lname) # -> 'George - Smith'
