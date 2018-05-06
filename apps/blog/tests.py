from django.test import TestCase

# Create your tests here.
from sys import getrefcount
a = ['x']
print(getrefcount(a))
def p(x):
    print(getrefcount(a))
    b = x
    print(getrefcount(a))
    # del a
    # del b
    # del x
    return b
p(a)
print(getrefcount(a))
p(a)
print(getrefcount(a))
b = a
print(getrefcount(a))
del a

