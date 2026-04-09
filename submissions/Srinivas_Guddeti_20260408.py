'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from prog5a import triangle
t = triangle() # How  to  create  triangle  object
triangle.get(t) # How  to  call  get()  method  in  another  way
triangle.test(t) # How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(t)) # Area : 6.0
print('Perimeter: ', triangle.peri(t)) # Perimeter: 12.0

# -----------------------------------------------------------------------------------------------------

 # What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__) # {}
s . get() # Input: 25, Rama Rao, male, 52, 48, 55
print(s . __dict__) # {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
s . compute()
print(s . __dict__) # {'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155.0, 'avg': 51.67, 'grade': 'Second class'}

# -----------------------------------------------------------------------------------------------------

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
n = int(input('Enter number of students: ')) # How  to  read  number  of  students  into   variable  'n'
a = []
for i in range(n):
    a.append(student()) # How  to  store  'n'  student  class  objects   in  list  'a'

for x in a:
    x.get() # How  to   read  each  student  data  into   the  object  held  by  the  list
    x.compute() # How  to   store  results  in   each  object  held  by  the  list
    print(x) # How  to   print  each  object  held  by  the  list

# -----------------------------------------------------------------------------------------------------

 '''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
'''
import  math
class  Rat:
	def  get(self):
		self.nr = int(input('Enter numerator: ')) # How  to  read  numerator  
		self.dr = int(input('Enter denominator: ')) # How  to  read  denominator 
		self.test() # How  to  call  test()  method
	def  test(self):
		while self.dr == 0:
			self.dr = int(input('Denominator is zero. Re-enter: ')) # Ask  user  to  reenter
	def    __str__(self):
			 return  F'{self.nr} / {self.dr}' # return values in '2 / 3' form
	def   add(self , a , b):
		self.nr = a.nr * b.dr + b.nr * a.dr # How  to  add  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object  
	def   sub(self , a , b):
		self.nr = a.nr * b.dr - b.nr * a.dr # How  to  subtract  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object  
	def   mul(self , a , b):
		self.nr = a.nr * b.nr # How  to  multiply  objects
		self.dr = a.dr * b.dr
		self.simplify() # How  to  simplify  object 
	def    div(self , a , b):
		self.nr = a.nr * b.dr # How  to  divide  objects
		self.dr = a.dr * b.nr
		self.simplify() # How  to  simplify  object 
	def   simplify(self):
		if self.nr != 0:
			common = math.gcd(self.nr, self.dr) # How  to  find  gcd
			self.nr //= common # How  to  simplify  rational  number
			self.dr //= common
# End  of the class

a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat() # How  to  create  6  objects
a.get(); b.get() # How  to  read  rational  numbers
c.add(a, b); d.sub(a, b); e.mul(a, b) # Perform operations
print('Sum: ', c) # How  to  print  object   'c'
print('Difference: ', d) # How  to  print  object   'd'
print('Product: ', e) # How  to  print  object   'e'
if b.nr != 0:
	f.div(a, b)
	print('Division: ', f) # How  to  print  object  'f
else:
	print('Division  is  not  permitted')

# -----------------------------------------------------------------------------------------------------

 #  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # List of attributes in Rat class
print(dir(a)) # List of attributes in object 'a' including nr, dr

# -----------------------------------------------------------------------------------------------------

 #  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # False
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False

# -----------------------------------------------------------------------------------------------------

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
		x . talk() # Meow Meow Meow .... / Mehar Mehar Mehar ....
	else:
		x . bark() # Bhow Bhow Bhow ....

# -----------------------------------------------------------------------------------------------------

 #  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume 'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume 20
setattr(a , varname , value)
print(a . __dict__) # {'x': 10, 'y': 20}
print(a . x) # 10
# Iteration 1: x -> 10, Iteration 2: y -> 20, Iteration 3: z -> Error
# print(getattr(a, 'z')) # Error because 'z' is not defined in object

# -----------------------------------------------------------------------------------------------------

# (Home  work)
# Write  a  program  to  convert  a  dictionary  to  Emp  class  object
class  Emp:
        pass
#End  of  the  class
dict_emp = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
for k, v in dict_emp.items(): setattr(e, k, v) # How  to  convert  dictionary  to  object  'e'
for k in dict_emp.keys(): print(getattr(e, k)) # How  to  print  object  'e' (25, Rama Rao, 10000.0)

