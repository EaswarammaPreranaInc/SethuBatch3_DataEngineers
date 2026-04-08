from Vanithapriyadarshini_Balla_20260407 import triangle
a=triangle()
triangle.get(a)
triangle.test(a)
print("Area : ", triangle.area(a))
print("Perimeter : " ,triangle.peri(a))

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  Vanithapriyadarshini_Balla_20260407  import  Student
s = Student()
print(s . _dict_)# {}
s . get()
print(s . _dict_)#{'rno':25, 'sname':'Rama rao', 'gender': 'm', m=[52,48,55]}
s . compute()
print(s . _dict_)#{'rno':25, 'sname':'Rama rao', 'gender': 'm', m=[52,48,55], 'tot':155, 'avg'=51.67, 'grade': 'Second class'}

# Repeat  student  program  for  'n'  students
from  Vanithapriyadarshini_Balla_20260407  import  Student
n=int(input("Enter no.of students : "))
studs=[]
for i in range(n):
    s=Student()
    s.get()
    s.compute()
    studs.append(s)
for i in range(n):
    studs[i].disp()

#Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers
import  math
class  Rat:
	def  get(self):
		self.nr=int(input("Enter nr : "))  
		self.dr=int(input("Enter dr : "))  
		self.test()
	def  test(self):
		if self.dr != 0:
			pass
		else:
			print("Denominator cannot be 0, re-enter.")
	def    __str__(self):
			return  F'{self.nr}/{self.dr}'
	def   add(self , a , b):
		self.nr=a.nr * b.dr + b.nr * a.dr
		self.dr=a.dr * b.dr
		self.simplify()  
	def   sub(self , a , b):
		self.nr=a.nr * b.dr - b.nr * a.dr
		self.dr=a.dr * b.dr
		self.simplify() 
	def   mul(self , a , b):
		self.nr=a.nr * b.nr
		self.dr=a.dr * b.dr
		self.simplify()
	def    div(self , a , b):
		if b.nr==0:
			print("Zero Division Error")
			return
		self.nr=a.nr * b.dr 
		self.dr=a.dr * b.nr
		self.test()
		self.simplify()
	def   simplify(self):
			g=math.gcd(self.nr ,self.dr)
			self.nr=self.nr//g
			self.dr=self.dr//g

a=Rat()
b=Rat()
res=Rat()
print("Enter 1st rational number:")
a.get()
print("Enter 2nd rational number:")
b.get()
print("first rational number", a)
print("second rational number",b)
res.add(a,b)
print("Addition of two RN",res)
res.sub(a,b)
print("Substraction of two RN", res)
res.mul(a,b)
print("Product of two RN",res)
res.div(a,b)
print("Division of two RN",res)

#  dir()  function  demo  program  (Home  work)
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))# ['get','test','simplify','add','sub','mul','div','a','b','res']
print()
print()
print(dir(a))#['nr',dr',...]

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
		x . talk() # 'moew moew' 'Meher meher' 
	else:
		x . bark()# 'bhow bhow
		
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)# {'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))# 10 20 Invalid variable name : 'z'
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

#(Home  work)
#Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
#i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
for k,v in dict.items():
      setattr(e,k,v)
for attr,val in e.__dict__.items():
       print(f'{attr}: {getattr(e,attr)}')
    

