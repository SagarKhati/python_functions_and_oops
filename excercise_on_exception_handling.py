x = int( input())
try:
  if x<=0 or x>=100:
    raise ValueError
except ValueError:
  print("Input integer value must be between 0 and 100.")
  

x = input()
try:
  if len(x) > 10:
    raise ValueError
except ValueError:
  print("Input String contains more than 10 characters.")
else:
  print(x)
  

try:
  fs = open('UnknownFile.txt', 'r')
except FileNotFoundError:
  print("File not found.")
  
  
class RadiusInputError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return self.value
class Circle:
  def __init__(self, r):
    if r.isdigit() == False:
      raise RadiusInputError("'{}' is not a number.".format(r))
    self.radius = r
try:
  c1 = Circle('hello')
except RadiusInputError as e:
  print(e)
