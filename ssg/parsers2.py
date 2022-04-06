from typing import List


class Parser:
    extensions: List[str] = []

    def __init__(self):
        pass

    def valid_extension(self, extension):
        return extension in self.extensions

    @classmethod
    def add(cls):
        cls.extensions.append('vjc')


class Parser2:

    def __init__(self):
        self.extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def add(self):
        self.extensions.append('vjc')



a = Parser()
b = Parser()

a.add()
print(a.extensions)
print(b.extensions)


class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}*i'

    def __add__(self, other):
        return Complex(self.a*other.a, self.b*other.b)




c1 = Complex(1,2)
c2 = Complex(2,4)

print(c1)
print(c2)

print(c1+c2)

