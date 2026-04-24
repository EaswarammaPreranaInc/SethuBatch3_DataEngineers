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
o=c1()
i=o.c2()
o2=c2()


class   emp:
	def __init__(self):
		self.empno=int(input("enter the number "))
		self.name=input("enter name ")
		self.sal=float(input("enter sal : "))
		self.date=self.date()
	def   disp(self):
		print(f"{self.empno}\t{self.name}\t{self.sal}")
		self.date.disp()
	class   date:
		def    __init__(self):
			self.day=11
			self.mm=10
			self.yy=2002
		def disp(self):
			print(f"{self.day}-{self.mm}-{self.yy}")
# End  of  the  classs
s=emp()
s.disp()

class  outer:
	def  __init__(self):
		self.x=25
		self.in1=self.inner1()
		self.in2=self.inner2()
		
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
s=outer()
s.disp()
s.in1.disp()
s.in2.disp()


import  math
class  complex:
	def  get(self):
		self.x=eval(input("enter the value real "))
		self.y=eval(input("enter the value img"))
		
	#def    _str_(self):
		
	def  __add__(a,b):
		r=a.x+b.x
		i=a.y+b.y
		return f"{r}+{i}j"
	def __sub__(a,b):
		r=a.x-b.x
		i=a.y-b.y
		return  
a=complex()
b=complex()
a.get()
b.get()
print('Sum :  ' , a+b)
#print('Difference :  ' , ???)
#print('Product :  ' ,  ??)
#print('Division  : ' , ???)

''


class  Rat:
	def  get(self):
		self.num=eval(input("enter numerator value  : "))
		self.den=eval(input("enter denominator value : "))
			 
	def __gt__(a,b):
			return a.num*b.den>b.num*a.den
	def __lt__(a,b):
			return a.num*b.den<b.num*a.den
	def __eq__(a,b):
			return a.num*b.den==b.num*a.den
	def __ge__(a,b):
			return a.num*b.den>=b.num*a.den
	def __le__(a,b):
			return a.num*b.den<=b.num*a.den
	def __ne__(self,b):
			return a.num*b.den!=b.num*a.den
#  End  of   the  class
a=Rat()
b=Rat()
a.get()
b.get()
if    a  >  b:
	print('>')
elif  a  <  b:
	print('<')
elif a  ==  b:
	print('==')
elif  a  >=  b:
	print('>=')
elif a  <=  b:
	print('<=')
elif a  !=  b:
	print('!=')
	

class   outer:
	def  _init_(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def _init_(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
c=outer()
c.m1()
i=c.inner()
i.m1()
i2=outer.inner()
i2.m1()

#i = inner() #error



