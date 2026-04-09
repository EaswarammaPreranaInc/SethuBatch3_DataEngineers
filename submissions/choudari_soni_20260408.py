# '''
# Repeat  prog5a  such  that  methods  are  called  in  a  different  way

# 1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

# 2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
# '''
from choudari_soni_20260407 import triangle
t=triangle()
t.get() 
t.test()
print('Area : ',    t.area()  )
print('Perimeter: ',  t.peri()  )

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  choudari_soni_20260407  import  Student
s = Student()
print(s . __dict__)#{}
s . get()
print(s . __dict__)#{'Roll Number':25,'Name':'Rama Rao','Gender':'male',m1:52,m2:48,m3:55}
s . compute()
print(s . __dict__)#{'total':155,'Avg':51.66}

# #  dir()  function  demo  program  (Home  work)
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
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False



# Object  'a'  --->

# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')#Meow Meow Meow
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')#Bhow Bhow Bhow.....
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')#Mehar Mehar Mehat....
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
print(a . __dict__)#{'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))#10<\n>20
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  choudari_soni_20260407  import  Student
n=int(input('Enter a number ='))
a=[]
for i in range(n):
    s=Student()
    s.get()
    s.compute()
    a.append(s)
print("\nStudent Details:\n")   
for s in a:
    s.disp()
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
		self.nr=int(input("Enter numerator:"))#How  to  read  numerator  
		self.dr=int(input("Enter denomirator:"))#How  to  read  denominator 
		self.text()#How  to  call  test()  method
	def  test(self):
		if self.dr==0#Ask  user  to  reenter  denom  when  denom  is  zero
            print("Division is not permitted.")
	def    __str__(self):
			 return f"{self.nr} / {self.dr}" # values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self.nr=a.nr*b.dr+b.nr*a.ndr#How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		self.dr = a.dr * b.dr
        self.simplify()#How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-b.nr*a#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		self.b=a.dr * b.dr#How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.nr=a.nr * b.dr//a.dr * b.nr#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		self.dr = a.dr * b.dr
        self.simplify()#How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.nr = a.nr * b.dr#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		self.dr = a.dr * b.nr#
      self.simplify()#How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		    if self.nr!=0# simplification only when numerator is non-zero
                g=math.gcd(self.nr,self.dr)#How  to  find  gcd  of  numerator  and   denominator
			#  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat()#How  to  create  6  objects  a , b , c , d , e , f
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
a.get()#How  to  read  rational  number  into  object  'a'
b.get()#How to  read  rational  number  into  object  'b'
c.add(a,b)#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a, b)#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a, b)#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b)#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print(a)#How  to  print  object   'c'
print(b) #How  to  print  object   'd'
print(e)#How  to  print  object   'e'
if  f.div(a,b):
	print(f)#How  to  print  object  'f
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



