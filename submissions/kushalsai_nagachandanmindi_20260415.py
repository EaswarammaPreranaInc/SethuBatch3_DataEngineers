'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 
																																							39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		# How  to  read  real  and  imag
		self . real  =  float(input('Enter  real  part :  '))
		self . imag  =  float(input('Enter  imag  part :  '))
	def    __str__(self):
		# How  to  return  string  representation  of  complex  number
		if self . imag >= 0:
			return str(self . real) + ' + ' + str(self . imag) + 'i'
		else:
			return str(self . real) + ' - ' + str(-self . imag) + 'i'
	def  __add__(a ,  b):
		# How  to  add  objects  a  and  b
		result= complex()
		result . real  =  a . real  +  b . real
		result . imag  =  a . imag  +  b . imag
		return  result
		
	def  __sub__(a ,  b):
		# How  to  subtract  objects  a  and  b
		result= complex()
		result . real  =  a . real  -  b . real
		result . imag  =  a . imag  -  b . imag
		return  result
	def  __mul__(a ,  b):
		#How  to  multiply  objects  a  and   b
		result= complex()
		result . real  =  a . real  *  b . real  -  a . imag  *  b . imag
		result . imag  =  a . real  *  b . imag  +  a . imag  *  b . real	
	def  __truediv__(a ,  b):
		# How  to  divide  objects   a  and  b
		result= complex()
		denominator  =  b . real  *  b . real  +  b . imag  *  b . imag
		result . real  =  (a . real  *  b . real  +  a . imag  *  b . imag) / denominator
		result . imag  =  (a . imag  *  b . real  -  a . real  *  b . imag) / denominator
		return  result
# # End  of  the  class
# How  to  create  two  complex  class  objects
a= complex()
b= complex()
# How  to  read   inputs  into  1st  object
# How  to  read   inputs  into  2nd  object
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' , a*b)
print('Division  : ' , a/b)


'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  ---> False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  ---> False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  ---> True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  --->  True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  __gt__()  method ?  ---> a > b   (or)  a . __gt__(b)
     What  is  the  method  call  to  __lt__()  method ?  ---> a < b  (or)  a . __lt__(b)
     What  is  the  method  call  to  __eq__()  method ?  --->  a == b   (or)  a . __eq__(b)
     What  is  the  method  call  to  __ge__()  method ?  --->  a >= b   (or) a . __ge__(b)
     What  is  the  method  call  to  __le__()  method ?  ---> a <= b  (or)  a . __le__(b)
     What  is  the  method  call  to  __ne__()  method ?  --->  a != b  (or)  a . __ne__(b)
'''
import  math
class  Rat:
	def  get(self):
			#  How  to  read  numerator  and  denominator  into  object
			self . num  =  int(input('Enter  numerator :  '))
			self . den  =  int(input('Enter  denominator :  '))
	def __gt__(self,b):
			c= self . num  *  b . den
			d= self . den  *  b . num
			return  c>d
	def __lt__(self,b):
			c= self . num  *  b . den
			d= self . den  *  b . num
			return  c<d
	def __eq__(self,b):
			c= self . num  *  b . den
			d= self . den  *  b . num
			return  c==d
	def __ge__(self,b):	
			c= self . num  *  b . de
			d= self . den  *  b . num	
			return  c>=d
	def __ne__(self,b):
			c= self . num  *  b . den
			d= self . den  *  b . num
			return  c!=d
#  End  of   the  class
# How  to  create  two  Rat   class  objects  'a'  and  'b'
a= Rat()
b= Rat()
# How  to  read  1st  rational   number  into  object  'a'
# How  to  read  2nd  rational   number  into  object  'b'
if  (a > b):
	print('>')
if  (a<b):
	print('<')
if  (a==b):
	print('==')
if  (a>=b):
	print('>=')
if  (b<=a):
	print('<=')
if  (a!=b):
	print('!=')
 
 
# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
# How  to  call  m1()  method  of  outer  class
a=outer()
# How  to  call  m1()  method  of  inner  class
a.m1()
# How  to  call  m1()  method  of  inner  class  in  another  way
i=outer().inner()
# How  to  call  m1()  method  of  inner  class  in  one  more  way
i.m1()
i = a.inner().m1()



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
  
		self . empno = 25
		self . ename = 'Rama Rao'
		self . sal = 10000.0
		# How  to  create  date  class  object
		self . dob = self . date()
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print(self . empno)
		print(self . ename)
		print(self . sal)
		# How  to  call  disp()  method  of  date  class
		self . dob . disp()	
	class   date:
		def    __init__(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self . dd = 15
			self . mm = 8
			self . yy = 1947
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print(self . dd)
			print(self . mm)
			print(self . yy)
# End  of  the  class
How  to  call  disp()  method  of  emp  class
a= emp()
a . disp()



# Object  'e'  --->

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		# How  to  initialize  variable  'x'  of  object  self  to  25
		self . x = 25
		# How  to  create  inner1  class  object
		self . i1 = self . inner1()
		# How  to  create  inner2  class  object
		self . i2 = self . inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
# How  to  call   disp()  method  of outer  class
a= outer()
a . disp()
# How  to  call   disp()  method  of inner1  class
a . i1 . disp()
# How  to  call   disp()  method  of inner2  class
a . i2 . disp()


# Object  'o'  --->


# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
How  to  create  c1  class  object
a= c1()
How  to  create  inner  c2  class  object
i=a.c2()
How  to  create  outer  c2  class  object
o=c2()




# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
# How  to  create  outer  c2  class  object
o=c2()
# How  to  create  inner  c2  class  object
i=o.c2()
# How  to  create  inner  c2  class  object  in  another  way
i=c2().c2()
# How  to  create  inner  c2  class  object  in  one  more  way
i=o.c2()
