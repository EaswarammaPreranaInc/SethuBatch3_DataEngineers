#1
'''
Repeat prog5a such that methods are called in a different way

1) What are the two ways to call a method ? --> object . method()  and  classname . method(object)

2) Reuse triangle class defined in prog5a but do not define triangle class again
'''
from prog5a import triangle
t = triangle()
triangle.get(t)
triangle.test(t)
print('Area : ', triangle.area(t))
print('Perimeter: ', triangle.peri(t))



#2
# What are the outputs if inputs are 25 , Rama Rao , male , 52 , 48 , 55 (Home work)
from prog9a import student
s = student()
print(s.__dict__) 
# {}
s.get() 
# (Input: 25, Rama Rao, male, 52, 48, 55)
print(s.__dict__) 
# {'roll': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
s.compute()
print(s.__dict__) 
# {'roll': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55, 'total': 155, 'avg': 51.66}



#3
'''
Repeat student program for 'n' students

1) import student class defined in prog9a but do not rewrite

2) Use list of objects
'''
from prog9a import student
n = int(input('Enter number of students: '))
a = [student() for i in range(n)]
for s in a:
    s.get()
for s in a:
    s.compute()
for s in a:
    print(s.__dict__)



#4
'''
Write a program to add, subtract, multiply and divide two rational numbers

1) 1st rational number ---> 2/3
   2nd rational number ---> 5/9
   What is the sum? ---> 2/3 + 5/9 = (18 + 15)/27 = 33/27 = 11/9
   What is the difference? ---> 2/3 - 5/9 = (18 - 15)/27 = 3/27 = 1/9
   What is the product? ---> 2/3 * 5/9 = 10/27 = 10/27
   What is the division? ---> 2/3 / 5/9 = 2/3 * 9/5 = 18/15 = 6/5 ---> Successful division

2) 1st rational number ---> 2/3
   2nd rational number ---> 0/9
   What is the sum? ---> 2/3 + 0/9 = (18 + 0)/27 = 18/27 = 2/3
   What is the difference? ---> 2/3 - 0/9 = (18 - 0)/27 = 18/27 = 2/3
   What is the product? ---> 2/3 * 0/9 = 0/27 = 0/27 ---> Simplification is not required because numerator is 0
   What is the division? ---> 2/3 / 0/9 = 2/3 * 9/0 = 18/0 ---> Division is not permitted

3) When is simplification needed? ---> When numerator is non-zero
'''
import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()
    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))
    def __str__(self):
        return f'{self.nr} / {self.dr}'
    def add(self, a, b):
        self.nr = (a.nr * b.dr) + (b.nr * a.dr)
        self.dr = a.dr * b.dr
        self.simplify()
    def sub(self, a, b):
        self.nr = (a.nr * b.dr) - (b.nr * a.dr)
        self.dr = a.dr * b.dr
        self.simplify()
    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()
    def div(self, a, b):
        self.nr = a.nr * b.dr
        self.dr = a.dr * b.nr
        self.simplify()
    def simplify(self):
        if self.nr != 0:
            common = math.gcd(self.nr, self.dr)
            self.nr //= common
            self.dr //= common

a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()
a.get()
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
print('Sum:', c)
print('Difference:', d)
print('Product:', e)
if b.nr != 0:
    f.div(a, b)
    print('Division:', f)
else:
    print('Division is not permitted')



#5
# dir() function demo program (Home work)
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat)) # Returns list of all class attributes and methods including add, div, get, mul, etc.
print(dir(a)) # Returns list of all class attributes plus instance attributes 'nr' and 'dr'



#6
#Find outputs (Home work)
class Rat:
    def m1():
        pass
#End of the class
a = Rat()
a.nr = 22
print(hasattr(a, 'nr')) # True
print(hasattr(a, 'dr')) # False
print(hasattr(a, 'm1')) # True
print(hasattr(a, 'm2')) # False
print(hasattr(Rat, 'm1')) # True
print(hasattr(Rat, 'm2')) # False
print(hasattr(Rat, 'nr')) # False (nr is an instance variable, not class variable)



#7
#Find outputs (Home work)
class Cat:
    def talk(self): print('Meow Meow Meow ....')
class Dog:
    def bark(self): print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self): print('Mehar Mehar Mehar ....')
#End of the classes
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x, 'talk'): x.talk()
    else: x.bark()
# Meow Meow Meow ....
# Bhow Bhow Bhow ....
# Mehar Mehar Mehar ....



#8
#Find outputs (Home work)
class c1:
    pass
#End of the class
a = c1()
a.x = 10
varname = 'y' 
value = 20    
setattr(a, varname, value)
print(a.__dict__) # {'x': 10, 'y': 20}
print(a.x) # 10
# Iteration 1 (x): 10
# Iteration 2 (y): 20
# Iteration 3 (z): Invalid variable name : z (getattr fails as 'z' doesn't exist)



#9
'''
(Home work)
Write a  program to convert a dictionary {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0} to Emp class object
i.e. object should contain empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint: Use setattr() and getattr() functions
'''
class Emp:
    pass
d = {'Empno' : 25, 'Ename' : 'Rama Rao', 'Sal' : 10000.0}
e = Emp()
for k, v in d.items():
    setattr(e, k, v)
for k in d.keys():
    print(f'{k} : {getattr(e, k)}')