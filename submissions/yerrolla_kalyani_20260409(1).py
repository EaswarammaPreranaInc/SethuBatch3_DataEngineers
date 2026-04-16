# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()
b = Rat(9)
c = Rat(5,  8) 
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)
# print('a  :  ' , a)#22/7
# print('b  :  ' , b)#9/7
# print('c  :  ' , c)#5/8
# print('d  :  ' , d)#22/9
# print('e  :  ' , e)#2/3
# print('f  :  ' , f)#3/2
c . __init__()
print('c  :  ' , c)##22/7
a . __init__(3.8  , 4.6)
print('a  :  ' , a)#3.8/4.6
g = Rat(nr1 = 9 , 5)#error PA is not accepted  after the ka
h = Rat(nr = 9 , dr = 5)


# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)#{'dd1':15,'mm1':8,'yy1':1947}
print('b  :  ' , b . __dict__)#{ 'dd1' : 26 ,  'mm1' : 1 , 'yy1' : 1950 }
print('c  :  ' , c . __dict__)#{'dd1' : 19 ,  'mm1' : 19 , 'yy1' : 1985}
d = Date()#error,missing 3 positional argument 
e = Date(dd = 30 , mm = 4 , yy = 2022)#{'dd1' = 30 ,  'mm1' = 4 , 'yy1' = 2023}
f = Date(dd1 = 26 , mm1 = 8 , 2023)#error PA is not accepted after KA


'''
Object  'a'   --->  dd1'=15,'mm1'=8,'yy1'=1947

Object  'b'   --->  'dd1' = 26 ,  'mm1' = 1 , 'yy1' = 1950 

Object  'c'   --->  'dd1' = 19 ,  'mm1' = 19 , 'yy1' = 1985
'''

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)#type and address of the object 
print(b . __init__())#c2  class  constructor<nxt>None
c = c3()
print(c . __init__())#c3  class  constructor<nxt>None


Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()


# Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  _init_(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()
print(a . __dict__)#{}
b = c2()
print(b . __dict__)#{}
b . init()#Method
print(b . __dict__)#{'x':30,'y':40}


'''
Object  'a'  --->  empty 

Object  'b'  ---> x=30,y=40
'''
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
print(x . __dict__)#{}
x . m1()
print(x . __dict__)#{'b':20}
f1()
print(x . __dict__)#{'b':20}
x . d = 40
print(x . __dict__)#{'b':20,'d':40}
y = c2()
y . m3()
print(x . __dict__)#{'b':20,'d':40,'e':50}
z = c1()
print(z . __dict__)#{'b':20}


'''
object  'x'  --->b=20,d=20,e=50

object  'z'  --->b=20

object  'y'  --->empty
'''
# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)#{}
print(b . __dict__)#{}
# del  a . x#error no object x in a to delete it 
# del  b . y#error no object y  in a to delete it
print(a . __dict__)#{}
print(b . __dict__)#{}
print(a . x)#error no object x in a to delete it
print(b . y)#error no object y  in a to delete it


'''
Object  'a'   ---> empty  

Object  'b'   --->  empty
'''
#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('1st  constructor')
	def  _init_(self):
		print('2nd  constructor')
	def  _init_(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()


#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)#error  excepted 2 got 1  arguments for __init__(self,x,y)
c = c1()#error excepted 2 got 0 arguments for __init__(self,x,y)



#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Two  argument  constructor :10 	20
b = c1(30)#Two  argument  constructor : 10	 200
c = c1()#Two  argument  constructor : 100 	200



#What  happens  when  function  and  class  have  same  name ?class is recognized and the function f1 () is discarded
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1() 
print(a)#type and address of the object a 




#Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)#Function



# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
# a = c1()#error excpect one argument got 0 for c1(x) function 
b = c1(25)#Function : 25 and <None> is returned
print(b)#None



 #  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')


#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()#c1  class  of  prog9b




#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1()#c1  class  of  prog9a



#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
from prog9a import c1  #How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a=c1()#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a##CANNOT create  c1  class  object  of  prog9a BECAUSE THE CURRENT MODULE AND PROG91 HAS SAME NAMES SO CURRENT MODULE HAS HIGH PRIORITY THAN IMPORTED ONE AND PROG9A IS DISCARDED AND CURRENT MODULE C1() OBJ IS RECOGNIGED 


'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
import prog9a How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()#How  to  create  c1  class  object  of  current  module
a=prog9a.c1()# How  to  create  c1  class  object  of  prog9a