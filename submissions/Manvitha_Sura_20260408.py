'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
import prog5a
t=prog5a.triangle() #How  to  create  triangle  object
prog5a.triangle.get(t) #How  to  call  get()  method  in  another  way
prog5a.triangle.test(t) #How  to  call  test()  method  in  another  way
print('Area : ',  prog5a.triangle.area(t))
print('Perimeter: ',  prog5a.triangle.peri(t))

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)  #{}
s . get()
print(s . __dict__)  #{'rno':25 , 'sname':Rama  Rao ,  'gender':male ,'m':[52,48,55]}
s . compute()
print(s . __dict__)  #{'rno':25 , 'sname':Rama  Rao ,  'gender':male ,'m':[52,48,55],'tot': 155 ,'avg': 51.67 , 'grade':Second class }


'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
n=int(input('Enter number of students'))
a=[i for i in range(n)]
for i in range(n):
	print(F'Student {i+1}')
	a[i]=Student()
	a[i].get()
	a[i].compute()
for i in range(n):
	print(a[i].__str__())


import  math
class  Rat:
	def  get(self):
		self.nr=int(input('Enter numerator '))
		self.dr=int(input('Enter denominator ')) 
		self.test()
	def  test(self):
		if self.dr==0:
			self.dr=int(input('Enter denominator'))
		#Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return  F'{self.nr} / {self.dr}'
	def  add(self , a , b):
		self.nr=a.nr*b.dr+b.nr*a.dr# How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		self.dr=a.dr*b.dr
		self.simplify()# How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-b.nr*a.dr
		self.dr=a.dr*b.dr
		self.simplify()
		# How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		# How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.nr=a.nr*b.nr
		self.dr=a.dr*b.dr
		self.simplify()
		# How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		# How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.nr=a.nr*b.dr
		self.dr=a.dr*b.nr
		self.simplify()
		# How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		# How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if self.nr==0:
			return
		g=math.gcd(self.nr,self.dr)
		self.nr=self.nr//g
		self.dr=self.dr//g
		# How  to  find  gcd  of  numerator  and   denominator
		# How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
a.get()
b.get()
c.add(a,b)
d.sub(a,b)
e.mul(a,b)
f.div(a,b)
print(c.__str__())
print(d.__str__())
print(e.__str__())
if  f.dr!=0:
	print(f.__str__())
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
print(dir(Rat))  #list of strings of all methods 
print()
print()
print(dir(a))  #list of strings of all methods along with 'nr' and 'dr'



#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))  #True
print(hasattr(a , 'dr'))  #False
print(hasattr(a , 'm1'))  #True
print(hasattr(a , 'm2'))  #False
print(hasattr(Rat , 'm1'))  #True
print(hasattr(Rat , 'm2'))  #False
print(hasattr(Rat , 'nr'))  #False



# Object  'a'  --->nr==22


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
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''


#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)  #adds variable y with value 20 to object a
print(a . __dict__)  #{'x':10,'y':20}
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
Invalid  variable   name   :  z
'''


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
for x in dict:
        e=Emp()
        setattr(e,'x',dict[x])# How  to  convert  dictionary  to  object  'e'  with  for  loop
        print(getattr(e,'x'))# How  to  print  object  'e'  with  for  loop


