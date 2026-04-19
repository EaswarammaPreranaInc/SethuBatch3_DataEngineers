# 1) What are k, l, x, y, z, m, n, p, q, s?
# x -> class variable
# y -> instance variable
# z -> local variable
# m -> class variable
# p -> instance variable
# q -> class variable
# s -> local variable
# k -> global variable
# l -> class variable
# n -> instance variable

class c1:
    x = 10  # class variable

    def m1(self):
        self.y = 20   # instance variable
        z = 30        # local variable
        c1.m = 40     # class variable

def f1():
    a = c1()          # local variable
    a.p = 50          # instance variable
    c1.q = 60         # class variable
    s = 70            # local variable

k = 80                # global variable
c1.l = 90             # class variable
b = c1()              # global variable
b.n = 100             # instance variable


# 2) Find outputs (Person class)
# Note: _init_ and _del_ should be __init__ and __del__

class Person:
    def __init__(self):
        self.name = ''

    @property
    def name(self):
        print('getter method')
        return self._name

    @name.setter
    def name(self, value):
        print('Setter Method')
        self._name = value

    @name.deleter
    def name(self):
        print('Deleter method')
        del self._name

    def __del__(self):
        print('Destructor')

p = Person()
print(p.name)
p.name = 'Vamsi'
print(p.name)
del p.name
print(p.name)
del p

# Output:
# Setter Method
# getter method
#
# Setter Method
# getter method
# Vamsi
# Deleter method
# getter method
# Error: AttributeError (because _name is deleted)


# 3) Find outputs (enumerate on list)
import time
list = [25, 10.8, 'Hyd', True]
e = enumerate(list, start=5)
while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break
print(list[5])

# Output:
# (5, 25)
# (6, 10.8)
# (7, 'Hyd')
# (8, True)
# Error: IndexError: list index out of range


# 4) Can string be enumerated?
import time
a = input('Enter any string : ')  # Assume input is 'Hyd'
e = enumerate(a)
while True:
    try:
        print(next(e))
        time.sleep(1)
    except StopIteration:
        break

# Output for 'Hyd':
# (0, 'H')
# (1, 'y')
# (2, 'd')


# 5) Can set be enumerated?
import time
a = {25, 10.8, 'Hyd', True, 3+4j}
print(a)
b = enumerate(a)
while True:
    try:
        print(next(b))
        time.sleep(1)
    except StopIteration:
        break

# Output: order may vary
# (0, ...)
# (1, ...)
# (2, ...)
# (3, ...)
# (4, ...)


# 6) Can dictionary be enumerated?
import time
def disp(e):
    while True:
        try:
            print(next(e))
            time.sleep(1)
        except StopIteration:
            break
    print()

dict = {'Empno': 25, 'Emp Name': 'Rama Rao', 'Sal': 10000.0}
e1 = enumerate(dict.keys())
disp(e1)
e2 = enumerate(dict.values())
disp(e2)
e3 = enumerate(dict.items())
disp(e3)
e4 = enumerate(dict, start=5)
disp(e4)

# Output:
# (0, 'Empno')
# (1, 'Emp Name')
# (2, 'Sal')
#
# (0, 25)
# (1, 'Rama Rao')
# (2, 10000.0)
#
# (0, ('Empno', 25))
# (1, ('Emp Name', 'Rama Rao'))
# (2, ('Sal', 10000.0))
#
# (5, 'Empno')
# (6, 'Emp Name')
# (7, 'Sal')


# 7) Find outputs
import time
a = ['Telangana', 'Andhra Pradesh', 'Karnataka', 'TamilNadu', 'Maharastra']
b = ['Hyderabad', 'Amaravathi', 'Bangalore', 'Chennai', 'Mumbai']
e = enumerate(a)
for index, element in e:
    print(f'{element:20}  ...  {b[index]}')
    time.sleep(1)

# Output:
# Telangana            ... Hyderabad
# Andhra Pradesh       ... Amaravathi
# Karnataka            ... Bangalore
# TamilNadu            ... Chennai
# Maharastra           ... Mumbai