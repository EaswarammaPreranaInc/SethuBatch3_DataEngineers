'''
Repeat prog5a such that methods are called in a different way

1) What are the two ways to call a method ? --> object . method()  and  classname . method(object)

2) Reuse triangle class defined in prog5a but do not define triangle class again
'''

from Navaneeth_Reddy_20260407 import triangle

k = triangle()
triangle.get(k)
triangle.test(k)
print('Area : ', triangle.area(k))
print('Perimeter: ', triangle.peri(k))

'''
Output :
Enter the 1st side : 4
Enter the 2nd side : 5
Enter the 3rd side : 6
Area :  9.921567416492215
Perimeter:  15
'''


from Navaneeth_Reddy_20260407 import Student


s = Student()

print(s.__dict__) 
s.get() 
print(s.__dict__) 
s.compute()
print(s.__dict__) 

'''
Output :
{}
Enter roll no : 25
Enter Name: Rama Rao
Enter gender(m/f) : m
Enter marks of subject 1: 52
Enter marks of subject 2: 48
Enter marks of subject 3: 55
{'rno': 25, 'name': 'Rama Rao', 'gender': 'm', 'marks': [52, 48, 55]}
{'rno': 25, 'name': 'Rama Rao', 'gender': 'm', 'marks': [52, 48, 55], 'tol': 155, 'avg': 51.666666666666664, 'grade': 'Third  class'}
'''

'''
Repeat student program for 'n' students

1) import student class defined in prog9a but do not rewrite

2) Use list of objects
'''

from Navaneeth_Reddy_20260407 import Student

n = int(input("Enter the number of Students : "))

lt = []

for i in range(n) :
    lt.append(Student())
    
for x in lt :
    x.get()

for y in lt :
    y.compute()

for j in lt :
    print(j.__dict__)

'''
Output :
Enter the number of Students : 3 
Enter roll no : 45
Enter Name: Rama Rao
Enter gender(m/f) : M
Enter marks of subject 1: 45
Enter marks of subject 2: 56
Enter marks of subject 3: 67
Enter roll no : 46
Enter Name: Sreya
Enter gender(m/f) : F
Enter marks of subject 1: 56
Enter marks of subject 2: 65
Enter marks of subject 3: 54
Enter roll no : 47
Enter Name: Nava
Enter gender(m/f) : M
Enter marks of subject 1: 67
Enter marks of subject 2: 75
Enter marks of subject 3: 76
{'rno': 45, 'name': 'Rama Rao', 'gender': 'M', 'marks': [45, 56, 67], 'tol': 168, 'avg': 56.0, 'grade': 'Third  class'}
{'rno': 46, 'name': 'Sreya', 'gender': 'F', 'marks': [56, 65, 54], 'tol': 175, 'avg': 58.333333333333336, 'grade': 'Third  class'}
{'rno': 47, 'name': 'Nava', 'gender': 'M', 'marks': [67, 75, 76], 'tol': 218, 'avg': 72.66666666666667, 'grade': 'DIstinction'}

'''

import math


class Rat:
    
    def get(self) :
        self.n = int(input("Enter the numerator : "))
        self.d = int(input("Enter the denominator : "))
        self.test()
        
    def test(self):
        while self.d == 0:
            self.d = int(input("Re-Enter the denominator : "))
            
    def __str__(self) :
        return f'{self.n}/{self.d}'
    
    
    def add(self, a, b) :
        self.n = (a.n * b.d) + (b.n * a.d)
        self.d = a.d * b.d
        self.simplify()
        
        
        
    def sub(self, a, b) :
        self.n = (a.n*b.d) - (b.n * a.d)
        self.d = a.d * b.d
        self.simplify()
        
    def mul(self,a,b) :
        self.n = a.n * b.n
        self.d = a.d * b.d
        self.simplify()
        
    def div(self , a, b) :
        self.n = a.n * b.d
        self.d = b.n * a.d
        self.simplify()
        
    def simplify(self) :
        g = math.gcd(self.n , self.d)
        self.n = (self.n)/g
        self.d = (self.d)/g

a = Rat()

b = Rat()

c = Rat()

d = Rat()

e = Rat()

f = Rat()

a.get()

b.get()


c.add(a,b)

print('Addition :', c)

d.sub(a,b)

print('Subtraction :', d)

e.mul(a,b)

print('Multiplication :' ,e)

if b.n != 0:
    f.div(a, b)
    print('Division:', f)
else:
    print('Division is not permitted')

'''
Output :
Enter the numerator : 2
Enter the denominator : 3
Enter the numerator : 5
Enter the denominator : 9
Addition : 11.0/9.0
Subtraction : 1.0/9.0
Multiplication : 10.0/27.0
Division: 6.0/5.0

Enter the numerator : 2
Enter the denominator : 3
Enter the numerator : 0
Enter the denominator : 9
Addition : 2.0/3.0
Subtraction : 2.0/3.0
Multiplication : 0.0/1.0
Division is not permitted
'''

# dir() function demo program (Home work)
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat)) # It will return list of all class attributes and methods including add, div, get, mul, etc.
print(dir(a)) # It will return list of all class attributes and instance variable values of 'nr' and 'dr'


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
print(hasattr(Rat, 'nr')) # False


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
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
#1st iteration a.x = 10
#2nd iteration a.y = 20
#3rd Iteration a.z = Error, because there is no instance variable z in object a , so you can not print the unknown  instance variable


'''
(Home work)
Write a  program to convert a dictionary {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0} to Emp class object
i.e. object should contain empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint: Use setattr() and getattr() functions
'''

class Emp :
    pass
e = Emp
dict = {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0}

for k , v in dict.items() :
    setattr(e, k, v)

for x in dict :
    print(f'{x} : {getattr(e, x)}') 

'''
Output :
Empno : 25
Ename : Rama Rao
Sal : 10000.0
'''

    
    
        
    