1) What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   
from  prog9a  import  student
s = student()
print(s . _dict_)#{}
s . get()
print(s . _dict_)#{'rno':25, 'name':'Rama Rao', 'gender':'male',
 'm1':52, 'm2':48, 'm3':55}
s . compute()
print(s . _dict_)
#{
 'rno':25,
 'name':'Rama Rao',
 'gender':'male',
 'm1':52, 'm2':48, 'm3':55,
 'total':155,
 'avg':51.67,
 'result':'Pass'
}

2) Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
n = int(input('Enter number of students: ')) #How  to  read  number  of  students  into   variable  'n'
a = [] #How  to  store  'n'  student  class  objects   in  list  'a'
for i in range(n): #How  to   read  each  student  data  into   the  object  held  by  the  list
s = student()
    s.get()
    s.compute()
    a.append(s) #How  to   store  results  in   each  object  held  by  the  list
for s in a:
    print(s.__dict__) #How  to   print  each  object  held  by  the  list

3) Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

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
		self.nr = int(input("Enter numerator: ")) #How  to  read  numerator  
		self.dr = int(input("Enter denominator: ")) #How  to  read  denominator 
		self.test() #How  to  call  test()  method
	def  test(self):
		while self.dr == 0:
                    print("Denominator cannot be zero. Re-enter:") #Ask  user  to  reenter  denom  when  denom  is  zero
	            self.dr = int(input("Enter denominator: "))
	def    _str_(self):
		 return f"{self.nr} / {self.dr}" # return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.nr = a.nr*b.dr + b.nr*a.dr
                self.dr = a.dr*b.dr #How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		self.simplify() #How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr = a.nr*b.dr - b.nr*a.dr
                self.dr = a.dr*b.dr #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		self.simplify() #How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		 self.nr = a.nr*b.nr
        	 self.dr = a.dr*b.dr #How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		self.simplify() #How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		if b.nr == 0:
            	   self.dr = 0
                   return
                self.nr = a.nr*b.dr
                self.dr = a.dr*b.nr #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		self.simplify() #How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		 if self.nr != 0: #How  to  find  gcd  of  numerator  and   denominator
			 g = math.gcd(self.nr, self.dr)
           		 self.nr //= g
          	         self.dr //= g #How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat() #How  to  create  6  objects  a , b , c , d , e , f
a.get() #How  to  read  rational  number  into  object  'a'
b.get() #How to  read  rational  number  into  object  'b'
c.add(a,b) #How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b) #How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b) #How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b) #How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print("c=",c) #How  to  print  object   'c'
print("d =", d) #How  to  print  object   'd'
print("e =", e) #How  to  print  object   'e'
if f.dr! = 0:
	 print("f =", f)
else:
    print("Division is not permitted")

4) dir()  function  demo  program  
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

5) outputs  
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False

# Object  'a'  ---> nr = 22

6) outputs  
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')#Meow Meow Meow ....
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')#Bhow Bhow Bhow ....
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')#Mehar  Mehar  Mehar  ....
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

7) outputs  
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_)#{x : 10, y : 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))#20
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break


8) Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp() # How  to  convert  dictionary  to  object  'e'  with  for  loop
for k,v in d.items():
    setattr(e, k, v)
for k in d:
    print(k, "=", getattr(e, k)) #How  to  print  object  'e'  with  for  loop

9) How  to  reuse  mod1  ?  
print('Hello')
import mod1 #How  to  import  mod1
print(mod1.x) #print(How  to  print   variable  'x'   of  mod1)
mod1.f1() #How  to  call  function  f1()  of  mod1
a= mod1.c1()
a.m1() #How  to  call  method m1() of mod1
print('Bye')
import mod4
print(x)
f1()

10) outputs 
print('Before')#Before
import mod1 #How  to  run  mod1
print(mod1 . x)#10
mod1 . f1()
a = mod1 . c1()
print('After')#After
run_module('mod1')
runpy . run_module(mod1)

11) How  to  use  members  of  cal  module  with  from  statement ?  
print('Begin')
from cal import * #How  to  import  all  the  members  of  cal  module
print(x) # (How  to  print  variable  'x'  of  cal   module)
print(y) #(How  to  print  variable  'y'  of  cal   module)
print(cal . x)
print(add(10,7)) #(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(sub(10,7)) #(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print(mul(10,7)) #(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print(div(10, 7)) #(How  to  call  div()  function  of  cal  module  with  10  and  7)
print(cal . add(x , y))
b= c1()
b.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
b = cal . c1()

12) How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  
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

13) Module  alias
print('Begin')
import cal as c # How  to  import  cal  module  with   another  name  using  import  statement
print(c.x) #(How  to  print  variable  'x'  of  cal   module)
print(c.y) #(How  to  print  variable  'y'  of  cal   module)
print(c.add(10,7)) #(How  to  call  add()  function  of  cal  module  with  10  and  7)
print#(c.sub(10,7)) #(How  to  call  sub()  function  of  cal  module  with  10  and  7)
print#(c.mul(10,7)) #(How  to  call  mul()  function  of  cal  module  with  10  and  7)
print#(c.div(10,7)) #(How  to  call  div()  function  of  cal  module  with  10  and  7)
a=c.c1() 
a.m1() #How  to  call  m1()  method  of  c1  class  in  cal  module
print(cal . x)
from  math  as   m  import  *

14) Member  alias
from cal import x as a, add as ad, mul as ml, c1 as c #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a) #(How  to  print  variable  'x'  of  cal   module)
print(x)
print(ad(10,7)) #(How  to  call  add()  function  of  cal  module  with  10  and  7)
print(ml(10,)) #(How  to  call  mul()  function  of  cal  module  with  10  and  7)
b = c() 
b.m1() #How  to  call  m1()  method  of  class  c1  in  cal  module
print(add(10 , 7))
b = c1()

15) cal . py
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
    What  are  the  outputs ?  --->  Nothing  becoz  there  are  no  print  statements  in  cal  module

16) mod1.py
x = 10
def  disp():
	print('disp  function  of  mod1')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  mod1')


'''
What  are  the  members  of  mod1 ?   ---> Object  'x' , function  disp()  and  class  c1
'''

17) mod2.py
x = 20
def   disp():
	print('disp  function  of  mod2')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  mod2')


'''
What  are  the  members  of  mod2 ? --->  Object  'x' ,  function  disp()  and  class  c1
'''

18) outputs 
x = 30
def   disp():
		print('disp  function  of  same  module ')#'disp  function  of  same  module
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')#m1  method of  class  c1  in  same  module
from  mod2  import   *
from  mod1  import   *
print(x)#10
disp()
a = c1()
a . m1()

19) outputs  
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')#disp  function  of  same  module
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')#m1  method of  class  c1  in  same  module
print(x)#30
disp()
a = c1()
a . m1()

20) How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
import mod1, mod2 #How  to  import  mod1  and  mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #(How  to  print  variable  'x'  of  mod1
mod1.disp() #How  to  call  disp()  function  of  mod1
a=mod1.c1() #
a.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x) #(How  to  print  variable  'x'  of  mod2
mod2.disp() #How  to  call  disp()  function  of  mod2
b=mod2.c1() 
b.m1() #How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x) #(How  to  print  variable  'x'  of  current  module)
disp()How  to  call  disp()  function  of current  module
c = c1()
c.m1() #How  to  call  method  m1()  of  class   c1  in  current  module

21) How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import * #How  to  import  members  of  mod1
form mod2 import * # How  to  import  members  of  mod2
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

22) mod1.py 
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

23) outputs 
print('Begining  of  mod2')#Begining of mod2
import   mod1
print('End  of  mod2')#End of mod2

24) outputs
import  cal
print(cal . x)#100
print(cal . y)#200
print(cal . add(10 , 7))#17
print(cal . sub(10 , 7))#3
print(cal . mul(10 , 7))#70
print(cal . div(10 , 7))#1.42
a = cal . c1()
a . m1()

25) outputs
from  cal  import   y , sub , mul
print(x)#Error not defined
print(y)#200
print(add(10 , 7))#Error not defined
print(sub(10 , 7))#3
print(mul(10 , 7))#70
print(div(10 , 7))#Error not defined
a = c1()#Error not defined


