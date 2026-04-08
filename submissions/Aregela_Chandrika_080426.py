'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from prog5a import triangle   #How  to  call  get()  method  in  another  way
t = triangle()
triangle.get(t)
triangle.test(t)
print('Area : ',   triangle.area(t))
print('Perimeter: ',  triangle.peri(t))






# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)




'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
n = int(input('Enter number of students: '))     # How  to  store  'n'  student  class  objects   in  list  'a'
a = [] 
for i in range(n):
    s = student()
    s.get()
    s.compute()
    a.append(s)
    
for x in a:
    print(x.__dict__)




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
	def    __str__(self):
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





#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))





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
        
        
        
        
        
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
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




# mod1 . py
print('Hyd')
print('Sec')
print('Cyb')
x = 25
def  f1():
	print('Function')
class   c1:
	def   m1(self):
			print('Method')

'''
1) What  are  the  members  of  mod1 ?  --->  Object  'x' ,  function  f1()  and  class  c1

2) py  mod1.py
    What  are  the  outputs ?  --->  Hyd  <next line>  Sec  <next  line>  Cyb  <next  line>

3) Why  are  function  f1()  and  method  m1()  not  executed ?  --->  Since  they  are  not  called
'''






#  How  to  reuse  mod1  ?  (Home  work)
print('Hello')
How  to  import  mod1
print(How  to  print   variable  'x'   of  mod1)
How  to  call  function  f1()  of  mod1
How  to  call  method  m1()  of  class  c1  in  mod1
print('Bye')
import  mod4
print(x)
f1()






#  Find  outputs  (Home  work)
print('Before')
How  to  run  mod1
print(mod1 . x)
mod1 . f1()
a = mod1 . c1()
print('After')
run_module('mod1')
runpy . run_module(mod1)





# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
How  to  import  all  the  members  of  cal  module
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))
How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()





# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
print(How  to  print  variable  'x'  of  cal   module)
print(y)
print(cal . x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10 , 7))
How  to  call  m1()  method  of  class  c1  in  cal  module





# Module  alias
print('Begin')
How  to  import  cal  module  with   another  name  using  import  statement
print(How  to  print  variable  'x'  of  cal   module)
print(How  to  print  variable  'y'  of  cal   module)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(How  to  call  div()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *





# Member  alias
How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(How  to  print  variable  'x'  of  cal   module)
print(x)
print(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(How  to  call  mul()  function  of  cal  module  with  10  and  7)
How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()





# cal . py
x = 100
y = 200
def  add(a , b):
	return  a + b
def	 sub(a , b):
	return  a - b
def	 mul(a , b):
	return  a * b
def	 div(a , b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')

'''
1) What  is  the  module  name ?  --->  cal

2) What  are  the  members  of  cal  module ?  --->  Two  objects  x  and  y ,
																			      Four  functions  add() , sub() , mul()  and  div()  and
																				  class  c1

3) Is  m1()  a  member  of  cal  module ?  --->  No  becoz  it  is  a  method  of  class

4) How  many  statements  are  in  cal  module ?  --->  Two
																				     i.e.  x =  100   and  y = 200

5) py  cal . py
    What  are  the  outputs ?  --->  Nothing  becoz  there  are  no  print  statements  in  cal  module'''
    
    
    
    
    
    
# mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


'''
What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1
'''







# mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')'


'''
What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1
'''









# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x)
disp()
a = c1()
a . m1()







# Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x)
disp()
a = c1()
a . m1()







# How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(How  to  print  variable  'x'  of  mod2
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module







# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module






# How  to  use  members  of  all  the  three  modules  with  from  statement ?
How  to  import  members  of  mod1
How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
print(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2
print()
print()
print(How  to  print  variable  'x'  of  current  module)
How  to  call  disp()  function  of current  module
How  to  call  method  m1()  of  class   c1  in  current  module










# mod1.py  (Home  work)
# How  to  prevent  execution  the  middle  3  statements  when  mod1  is  imported  elsewhere
print('One')
print('Two')
print('Three')
print('Four')
print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')





# Find  outputs (Home  work)
print('Begining  of  mod2')
import   mod1
print('End  of  mod2')




#  Find  outputs
import  cal
print(cal . x)
print(cal . y)
print(cal . add(10 , 7))
print(cal . sub(10 , 7))
print(cal . mul(10 , 7))
print(cal . div(10 , 7))
a = cal . c1()
a . m1()





#  Find  outputs
from  cal  import   y , sub , mul
print(x)
print(y)
print(add(10 , 7))
print(sub(10 , 7))
print(mul(10 , 7))
print(div(10 , 7))
a = c1()