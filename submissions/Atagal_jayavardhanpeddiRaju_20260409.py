class Rat:
    def _init_(self, nr1 = 22, dr1 = 7):
        self.nr = nr1
        self.dr = dr1
    def _str_(self):
        return f'{self.nr} / {self.dr}'

a = Rat()               
b = Rat(9)                   
c = Rat(5, 8)                
d = Rat(dr1 = 9)             
e = Rat(dr1 = 3, nr1 = 2)   

x = eval(input('Enter numerator  :  '))     
y = eval(input('Enter Denominator  :  '))    
f = Rat(x, y)            

print('a  :  ', a)           #a  :   <__main__.Rat object at ...>
print('b  :  ', b)           #b  :   <__main__.Rat object at ...>
print('c  :  ', c)           #c  :   <__main__.Rat object at ...>
print('d  :  ', d)           #d  :   <__main__.Rat object at ...>
print('e  :  ', e)           #e  :   <__main__.Rat object at ...>
print('f  :  ', f)           #f  :   <__main__.Rat object at ...>

c._init_()                 
print('c  :  ', c)          c  :   <__main__.Rat object at ...>

a._init_(3.8, 4.6)          
print('a  :  ', a)          a  :   <__main__.Rat object at ...>

g = Rat(nr1 = 9, 5)         #Error
h = Rat(nr = 9, dr = 5)     #Error



class Date:
        def _init_(self , dd1 , mm1  , yy1):
                self.dd = dd1
                self.mm = mm1
                self.yy = yy1

a = Date(15 , 8 , 1947)                      
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)   
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)   

print('a  :  ' , a._dict_) #('Date' object has no attribute '_dict_')
print('b  :  ' , b._dict_)  #('Date' object has no attribute '_dict_')
print('c  :  ' , c._dict_)  #('Date' object has no attribute '_dict_')

d = Date()                                  #Error
e = Date(dd = 30 , mm = 4 , yy = 2022)      #Error
f = Date(dd1 = 26 , mm1 = 8 , 2023)         #Error


class  c1:
	def  _init_(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  _init_(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  _init_(self):
		print('c3  class  constructor')
a = c1()
b = c2()
print(b)  #<__main__.c2 object at 0x7cfbd608dca0>
print(b . _init_()) #c2  class  constructor
c = c3()
print(c . _init_())   c3  #class  constructor


# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor') #'Constructor'
		b = c1()
# End  of  class
a = c1()


class c1:
    def _init_(self):
        print('Constructor')
        self.x = 10
        self.y = 20

class c2:
    def init(self):
        print('Method')
        self.x = 30
        self.y = 40

a = c1()                      
print(a._dict_)     #Error       

b = c2()                      
print(b._dict_)     #Error          

b.init()                      
print(b._dict_)     #Error 


# Find  outputs (Home  work)
class   c1:
        def   _init_(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()
print(x.__dict__)
x . m1()
print(x.__dict__)
f1()
print(x.__dict__)
x . d = 40
print(x.__dict__)
y = c2()
y . m3()
print(x.__dict__)
z = c1()
print(z.__dict__)

{}
{'b': 20}
{'b': 20, 'c': 30}
{'b': 20, 'c': 30, 'd': 40}
{'b': 20, 'c': 30, 'd': 40, 'e': 50}
{}


# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a.__dict__)
print(b.__dict__)
del  a . x
del  b . y
print(a.__dict__) #{}
print(b.__dict__) #{}
print(a . x) #{}
print(b . y) #{}


#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #empty
b = c1(30) #empty
c = c1()


# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1()
print(a) #<__main__.f1 object at 0x7a3f8355db80>


# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a) #Function


# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()
b = c1(25)
print(b) #Function :  25

# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a) #Function

# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()
b = c1(25)
print(b) #Function :  25

from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b') #empty
a = c1()

class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c') #empty
from  prog9a  import  c1
a = c1()

How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
How  to  create  c1  class  object  of  current  module
How  to  create  c1  class  object  of  prog9a

import prog9a   

class c1:
    def __init__(self):
        print("c1 class of current module")

if __name__ == "__main__":

    obj1 = c1()           
    obj2 = prog9a.c1()     

    s = prog9a.student() 

