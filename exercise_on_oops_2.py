import unittest

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven1(self):
        self.assertEqual(isEven(5), False)
    def test_isEven2(self):
        self.assertEqual(isEven(10), True)
    def test_isEven3(self):
        self.assertEqual(isEven('hello'), TypeError)

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False
print(isEven(43)) # --> False

unittest.main()


