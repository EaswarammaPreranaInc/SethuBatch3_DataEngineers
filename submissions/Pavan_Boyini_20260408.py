from prog5a import triangle   # import class

# How to create triangle object       # t = triangle()

# How to call get() method in another way    # triangle.get(t)

# How to call test() method in another way   # triangle.test(t)

# print('Area : ',  How to call area() method in another way)   # print('Area : ', triangle.area(t))

# print('Perimeter : ',  How to call peri() method in another way)   # print('Perimeter : ', triangle.peri(t))




# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)

from  prog9a  import  student

from prog9a import student

s = student()

print(s.__dict__)   # {}

s.get()   # reads: 25, Rama Rao, male, 52, 48, 55

print(s.__dict__)   # {'rno':25, 'name':'Rama Rao', 'gender':'male', 'm1':52, 'm2':48, 'm3':55}

s.compute()   # calculates total and avg

print(s.__dict__)   # {'rno':25, 'name':'Rama Rao', 'gender':'male', 'm1':52, 'm2':48, 'm3':55, 'total':155, 'avg':51.67}

Repeat  student  program  for  'n'  students

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list


from prog9a import student

n = int(input("How many students ? : "))     # How to read number of students into variable 'n'

a = []                                       # How to store 'n' student class objects in list 'a'

for i in range(n):
    print("Student", i+1)
    
    s = student()                            # How to read each student data into the object held by the list
    s.get()
    
    s.compute()                              # How to store results in each object held by the list
    
    a.append(s)                              # How to store each object into list

for i in a:
    i.display()                              # How to print each object held by the list

'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  
		How  to  read  denominator 
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')


'''
Object  'a'  --->  

Object  'b'  --->  

Object  'c'  --->  

Object  'd'  --->  

Object  'e'  --->  

Object  'f'  --->  
'''

import math

class Rat:
    
    def get(self):
        self.num = int(input("Enter numerator : "))        # How to read numerator
        self.den = int(input("Enter denominator : "))      # How to read denominator
        self.test()                                        # How to call test() method

    def test(self):
        while self.den == 0:                               # Ask user to reenter denom when denom is zero
            print("Denominator cannot be zero")
            self.den = int(input("Re-enter denominator : "))

    def __str__(self):
        return f"{self.num} / {self.den}"                  # return rational number like '2 / 3'

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den           # add numerators
        self.den = a.den * b.den                           # common denominator
        self.simplify()                                    # How to simplify object

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den           # subtract numerators
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num                           # multiply numerators
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:                                     # division not permitted condition
            self.den = 0
            return
        self.num = a.num * b.den                           # multiply by reciprocal
        self.den = a.den * b.num
        self.simplify()

    def simplify(self):
        if self.num == 0:                                  # no need simplify when numerator is zero
            return
        g = math.gcd(self.num, self.den)                   # find gcd
        self.num //= g                                     # simplify numerator
        self.den //= g                                     # simplify denominator


# How to create 6 objects a, b, c, d, e, f
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

# How to add rational numbers in objects a and b and store results in object 'c'
c.add(a, b)

# How to subtract rational numbers in objects a and b and store results in object 'd'
d.sub(a, b)

# How to multiply rational numbers in objects a and b and store results in object 'e'
e.mul(a, b)

# How to divide rational numbers in objects a and b and store results in object 'f'
f.div(a, b)

# How to print object 'c'
print("Sum :", c)

# How to print object 'd'
print("Difference :", d)

# How to print object 'e'
print("Product :", e)

# if ???
if f.den != 0:                                             # check division valid
    print("Division :", f)                                 # How to print object 'f'
else:
    print("Division is not permitted")import math

class Rat:
    
    def get(self):
        self.num = int(input("Enter numerator : "))        # How to read numerator
        self.den = int(input("Enter denominator : "))      # How to read denominator
        self.test()                                        # How to call test() method

    def test(self):
        while self.den == 0:                               # Ask user to reenter denom when denom is zero
            print("Denominator cannot be zero")
            self.den = int(input("Re-enter denominator : "))

    def __str__(self):
        return f"{self.num} / {self.den}"                  # return rational number like '2 / 3'

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den           # add numerators
        self.den = a.den * b.den                           # common denominator
        self.simplify()                                    # How to simplify object

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den           # subtract numerators
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num                           # multiply numerators
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:                                     # division not permitted condition
            self.den = 0
            return
        self.num = a.num * b.den                           # multiply by reciprocal
        self.den = a.den * b.num
        self.simplify()

    def simplify(self):
        if self.num == 0:                                  # no need simplify when numerator is zero
            return
        g = math.gcd(self.num, self.den)                   # find gcd
        self.num //= g                                     # simplify numerator
        self.den //= g                                     # simplify denominator


# How to create 6 objects a, b, c, d, e, f
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

# How to add rational numbers in objects a and b and store results in object 'c'
c.add(a, b)

# How to subtract rational numbers in objects a and b and store results in object 'd'
d.sub(a, b)

# How to multiply rational numbers in objects a and b and store results in object 'e'
e.mul(a, b)

# How to divide rational numbers in objects a and b and store results in object 'f'
f.div(a, b)

# How to print object 'c'
print("Sum :", c)

# How to print object 'd'
print("Difference :", d)

# How to print object 'e'
print("Product :", e)

# if ???
if f.den != 0:                                             # check division valid
    print("Division :", f)                                 # How to print object 'f'
else:
    print("Division is not permitted")





#  dir()  function  demo  program  (Home  work)
from prog10a import Rat

a = Rat()
a.nr = 22
a.dr = 7

print(dir(Rat))    # list of class attributes (methods + default attributes)

print()
print()

print(dir(a))      # list of object attributes (includes 'nr', 'dr' + class attributes)


#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))   # True
print(hasattr(a , 'dr'))   # False
print(hasattr(a , 'm1'))   # True
print(hasattr(a , 'm2'))   # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False






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
		x . talk()          # cat and goat
	else:
		x . bark()     # Dog


output:
        Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....




#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)
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

class c1:
    pass

a = c1()
a.x = 10

varname = 'y'        # input assumed
value = 20           # input assumed

setattr(a , varname , value)

print(a.__dict__)    # {'x':10, 'y':20}
print(a.x)           # 10

# loop inputs: x, y, z

print(getattr(a , 'x'))   # 10
print(getattr(a , 'y'))   # 20

# for 'z'
# Invalid variable name : z


'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop
'''

class Emp:
    pass

dict = {'Empno':25 , 'Ename':'Rama Rao' , 'Sal':10000.0}

e = Emp()

# How to convert dictionary to object 'e' with for loop
for k, v in dict.items():
    setattr(e, k, v)

# How to print object 'e' with for loop
for k in dict:
    print(k, "=", getattr(e, k))