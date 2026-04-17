#1
'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
import triangle as t

#How  to  create  triangle  object
sides = t . triangle()

#How  to  call  get()  method  in  another  way
t . triangle . get(sides)
#How  to  call  test()  method  in  another  way
t . triangle . test(sides)

print('Area : ', t . triangle . area(sides))
print('Perimeter: ', t . triangle . peri(sides))


# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  sdetails  import  student
s = student()
print(s . __dict__) # {}
s . get()
print(s . __dict__) # {'rno' : 25, 'sname' : 'Rama Rao', 'gender' : 'm', 'm' : [52, 48, 55]}
s . compute()
print(s . __dict__) # {'rno' : 25, 'sname' : 'Rama Rao', 'gender' : 'm', 'm' : [52, 48, 55], 'tot' : 155, 'avg' : 51.6, 'grade' : 'Second  class'}

#2
import math

class Rat:

    def get(self):
        self.n = int(input('Enter the numerator:'))
        self.d = int(input('Enter the denominator:'))
        self.test()

    def test(self):
        while self.d == 0:
            self.d = int(input('Denominator cannot be 0 please enter another number:'))

    def __str__(self):
        return f'{self.n}/{self.d}'  # values of object in the form of rational number such as '2 / 3'

    def add(self, a, b):
        self.a = a.n / a.d
        self.b = b.n / b.d
        self.n = (a.n * b.d) + (b.n * a.d)
        self.d = (a.d * b.d)
        return f'{self.n} / {self.d}'

        #How to add objects 'a' and 'b' and store results in object
        '''
        c.add(a , b)
        object a ---> 2 / 3
        object b ---> 5 / 9
        object c ---> 2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
        '''

    def sub(self, a, b):
        #How to subtract objects 'a' and 'b' and store results in object
        self.a = a.n / a.d
        self.b = b.n / b.d
        self.n = (a.n * b.d) - (b.n * a.d)
        self.d = (a.d * b.d)
        return f'{self.n} / {self.d}'

        '''
        d.sub(a , b)
        object a ---> 2 / 3
        object b ---> 5 / 9
        object d ---> 2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
        '''

    def mul(self, a, b):
        self.a = a.n / a.d
        self.b = b.n / b.d
        self.n = (a.n * b.n)
        self.d = (a.d * b.d)
        return f'{self.n} / {self.d}'

        #How to multiply objects 'a' and 'b' and store results in object
        '''
        e.mul(a , b)
        object a ---> 2 / 3
        object b ---> 5 / 9
        object e ---> 2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
        '''

    def div(self, a, b):
        self.a = a.n / a.d
        self.b = b.n / b.d

        if b.n == 0:
            return 'Division is not permitted'

        self.n = (a.n * b.d)
        self.d = (a.d * b.n)
        return f'{self.n} / {self.d}'

        '''
        f.div(a , b)
        object a ---> 2 / 3
        object b ---> 5 / 9
        object f ---> 2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
        '''

    def simplify(self):
        s = math.gcd(self.n, self.d)

        if self.n == 0:
            return f'{self.n}/{self.d}'
        else:
            try:
                return f'{self.n // s}/{self.d // s}'
            except ZeroDivisionError:
                return 'Division with Zero not permitted.'

        #How to simplify object
        '''
        c.simplify()
        1) 12 / 15 ---> 4 / 5
        2) 10 / 27 ---> 10 / 27
        3) 0 / 27 ---> 0 / 27
        '''

# End of the class


#3
'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''

# How to create 6 objects a , b , c , d , e , f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# How to read rational number into object 'a'
a.get()

# How to read rational number into object 'b'
b.get()

# How to add rational numbers
add = c.add(a, b)

# How to subtract rational numbers
sub = d.sub(a, b)

# How to multiply rational numbers
mul = e.mul(a, b)

# How to divide rational numbers
div = f.div(a, b)

print('Add:', add)
print('Sub:', sub)
print('Mul:', mul)
print('Div:', div)

# 1) import student class defined in prog9a but do not rewrite
from sdetails import student

# How to read number of students into variable 'n'
n = int(input('Enter number of students: '))

# How to store 'n' student class objects in list 'a'
a = []   # empty list

for i in range(n):
    s = student()   # create object
    a.append(s)     # store object in list

# How to read each student data into the object held by the list
for i in range(n):
    print(f'Enter details of student {i+1}')
    a[i].get()

# How to store results in each object held by the list
for i in range(n):
    a[i].compute()

# How to print each object held by the list
print('Student Details:')
for i in range(n):
    print(a[i])


#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # objects and methods of Rat class
print()
print()
print(dir(a)) # objects and methods of Rat class


#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False



# Object  'a'  --->


# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()
'''
Meow Meow Meow....
Bhow Bhow Bhow....
Mehar Mehar Meher....
'''


#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) # {x : 10 , y : 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''
10
20
Invalid variable name : z
'''


#4
'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
'''
(Home work)
Write a program to convert a dictionary {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0} to Emp class object
i.e. object should contain empno = 25 , ename = 'Rama Rao' , Sal = 10000.0

Hint: Use setattr() and getattr() functions
'''

class Emp:
    pass
# End of the class

dict = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# How to convert dictionary to object 'e' with for loop
e = Emp()

for k, v in dict.items():
    setattr(e, k, v)

# How to print object 'e' with for loop
for k in dict.keys():
    print(k, '=', getattr(e, k))