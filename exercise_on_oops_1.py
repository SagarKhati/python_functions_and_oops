import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
p1 = Point(4, 2, 9)
print(p1) # --> <__main__.Point object at 0x03A00950>

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return 'point : ({}, {}, {})'.format(self.x, self.y, self.z)
p1 = Point(4, 2, 9)
print(p1) # --> point : (4, 2, 9)

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return 'point : ({}, {}, {})'.format(self.x, self.y, self.z)
    def distance(p1, p2):
        return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2+(p1.z-p2.z)**2)
p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print(Point.distance(p2, p3)) # --> 8.717797887081348

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return 'point : ({}, {}, {})'.format(self.x, self.y, self.z)
    def __add__(p1, p2):
        return Point(p1.x+p2.x, p1.y+p2.y, p1.z+p2.z)
p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print(p2 + p3) # --> point : (2, 4, 10)


