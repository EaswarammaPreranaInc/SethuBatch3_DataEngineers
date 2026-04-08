# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
'''s = student()
print(s . __dict__) #{}
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)'''
'''{'rol': 31, 'name': 'shankar', 'gender': 'male', 'm': [100, 50, 90]}
{'rol': 31, 'name': 'shankar', 'gender': 'male', 'm': [100, 50, 90], 'tm': 240, 'am': 80.0, 'grade': 'distinction with first class'}'''
a=[]

'''n=int(input("enter the number of students"))
for i in range(n):
    print(f"enter details for students {i+1}")
    sts=student()
    sts.get()
    sts.compute()
    a.append(sts)
for  i in a:
    print(i)'''

class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # False
print(hasattr(a , 'm2')) #false
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2')) # false
print(hasattr(Rat , 'nr')) # false


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
Mehar  Mehar  Mehar  ....
Bhow Bhow Bhow ....
Meow Meow Meow ....
'''

class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) #{x:10,y:20}
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
	invalid variable name : z
	'''

	#Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
#i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

#Hint:  Use  setattr()  and  getattr()  functions
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}

e=Emp()
for i in dict:
	setattr(e,i,dict[i])
for i in dict:
	print(f"{i}={getattr(e,i)}")




import mod1
print(mod1.x)
print(mod1.f1())
s=mod1.c1()
print('Bye')

import runpy
print('Before')
print(mod1 . x) #25
mod1 . f1()     #function
a = mod1 . c1()
print('After') 
#run_module('mod1') error
#runpy . run_module(mod1) error

'''print(x) #10
print(y) #20
#print(cal . x) error
print(add(10,7))
print(sub(10,7) )
print(mul(10,7))
print(div(10,7))
#print(cal . add(x , y)) error

b =c1()
'''

'''
cal.py
__all__=['x','mul','sub']
x=10
y=20
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
class c1:
    pass
'''
 
print('Begin')
from cal import *
print(x)
#print(y) error
#print(cal . x)error
print(add(10,7))
#print(sub(10 , 7))
print(mul(10,7) )
#print(div(10 , 7)) # error
e=c1()
e.m1()
  