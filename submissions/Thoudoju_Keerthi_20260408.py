'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

import Thoudoju_Keerthi_20260407 m

obj = m.triangle()

m.triangle.get(obj)
m.triangle.test(obj)
print(m.triangle.area(obj))
print(m.triangle.peri(obj))

or

from  Thoudoju_Keerthi_20260407 import triangle
obj = triangle()
triangle.get(obj)
triangle.test(obj)
print(triangle.area(obj))
print(triangle.peri(obj))

 # What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_) #{}
s . get()
print(s . _dict_) # {rno : 25, sname : radha, gender : male, m :[52, 48, 55]}
s . compute()
print(s . _dict_) # {rno : 25, sname : radha, gender : male, m :[52, 48, 55], tot : 155, avg :51.33, grade : 'Second  class'}

'''
class   student:
	def   get(self):  #  self  is  object  's'
		self . rno = int(input('Enter  roll  number : ')) #  Adds  variable  rno  to  object  's'  with  user  input
		self . sname = input('Enter  student  name :  ')  #  Adds  variable  sname  to  object  's'  with  user  input
		self . gender = input(('Enter  gender (m/f) : '))   #  Adds  variable  gender  to  object  's'  with  user  input
		self . m = []  #  Adds  empty  list   'm'   to  object  's'
		for  i  in  range(3):  #  Marks  of  3  subjects
			marks = int(input(F'Enter  marks  of  subject  {i + 1}  :  '))  #  Reads  input  to  local  variable
			self . m . append(marks)  #  Appends  value  of  Lv  to  list  s . m
	def   compute(self):  #  self  is  object  's'
		self . tot = sum(self . m)  #  Adds  variable  tot  to  object  's'  with  sum  of  marks
		self . avg = self . tot / 3  #  Adds  variable  avg  to  object  's'  with  average  marks
		if  min(self . m) < 40:   #  At  least  one  subject  is  below  40  marks
				self . grade = 'Fail'  #  Adds  variable  grade  to  object  's'  with  'Fail'
		elif  self . avg >= 70:
				self . grade = 'Distinction'  #  Adds  variable  grade  to  object  's'  with  'Distinction'
		elif  self . avg >= 60:
				self . grade = 'First  class'  #  Adds  variable  grade  to  object  's'  with  'First  class'
		elif  self . avg  >= 50:
				self . grade = 'Second  class'   #  Adds  variable  grade  to  object  's'  with  'Second  class'
		else:
				self . grade = 'Third  class'   #  Adds  variable  grade  to  object  's'  with  'Third  class'
	def  disp(self):  #  self  is  object  's'
		print('Roll  Number  :  ' ,  self . rno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' ,  self . gender)
		print('Total  Marks  :  ' , self . tot)
		print(F'Average  :  {self . avg:.2f}')
		print('Grade  :  ' , self . grade)
	def   __str__(self):
		return  F'{self . rno}  \t {self . sname}  \t  {self . gender}  \t  {self . tot}  \t  {self . avg:.2f}  \t  {self . grade}'
'''

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
'''

from prog9a import student s
n = int(input('Enter number of students'))
res =[]
for i in range(1, n+1):
	print(f'Student {i}')
	chr(96 +i) = s()
	res.append(chr(96 +i)]
for i in res:
	i.get()
for i in res:
	i.compute()
for i in res:
	i.__str__()
	
	
	

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

import  math
class  Rat:
	def  get(self):
		self.n = int(input('Enter numerator')) 
		self.d = int(input('Enter denominator')) 
		self.test()
	def  test(self):
		while self.d == 0:
			print('Please non -zero denominator')
			self.d =  float(input('Enter denominator'))
	def    _str_(self):
			 return  f'({self.n / self.d})
	def   add(self , a , b):
		 
 
	def add(self, a, b):
        	self.n = a.n * b.d + b.n * a.d
        	self.d = a.d * b.d
        	self.simplify()

    	def sub(self, a, b):
        	self.n = a.n * b.d - b.n * a.d
        	self.d = a.d * b.d
        	self.simplify()

    	def mul(self, a, b):
        	self.n = a.n * b.n
        	self.d = a.d * b.d
        	self.simplify()

    	def div(self, a, b):
        	if b.n == 0:
            		return False
        	self.n = a.n * b.d
        	self.d = a.d * b.n
        	self.simplify()
        	return True

	def simplify(self):
        	if self.n == 0:
            		self.d = 1
            		return
        	gcd = math.gcd(int(self.n), int(self.d))
        	self.n = int(self.n // gcd)
        	self.d = int(self.d // gcd)

a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

print("Enter rational number a:")
a.get()

print("Enter rational number b:")
b.get()

c.add(a, b)     
d.sub(a, b)     
e.mul(a, b)     
valid = f.div(a, b)   
# Print results
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)

if valid:
    print("Division:", f)
else:
    print("Division is not permitted")


 #  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

#Returns  all  the  methods  of  the  class  in  the  form  of  list  of  strings


#Returns  all  the  instance  variables  of  the  object  and   methods  of  the  class in  the  form  of  list  of  strings

 #  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))

#True
#False
#False
#False
#True
#False
#False

# Object  'a'  ---> nr

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

#'Meow Meow Meow ....'
#'Bhow Bhow Bhow ....'
#'Mehar  Mehar  Mehar  ....'

 #  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class

a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_) #{ x : 10, y : 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

#10
#20
#'Invalid  variable   name   : z

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class emp:
	def emp_m(self):
		pass

d = eval(input(enter dictionary : '))
obj = emp()
for k,v in d.items():
	setattr(obj,k,v)
for k in d:
	print(getattr(obj,k))
		

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop


d = eval(input(enter dictionary : '))
e = Emp()
for k,v in d.items():
	setattr(e,k,v)
for k in d:
print(getattr(e,k))
