# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()##22/7
b = Rat(9)#9 / 7
c = Rat(5,  8)#5/8
d = Rat(dr1 = 9)#22/9
e = Rat(dr1 = 3 , nr1 = 2)#2/3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)#11 15
print('a  :  ' , a)#22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c)#5/8
print('d  :  ' , d)#22/9
print('e  :  ' , e)#2/3
print('f  :  ' , f)#11/15
c . _init_()
print('c  :  ' , c)#22/7
a . _init_(3.8  , 4.6)#3.8/4.6
print('a  :  ' , a)
g = Rat(nr1 = 9 , 5)#error
h = Rat(nr = 9 , dr = 5)#


# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)#15 , 8 , 1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_){dd1:15 , mm1:1,yy1:1947
print('b  :  ' , b . _dict_)#{yy1:1950 , mm1:1 , dd1:26}
print('c  :  ' , c . _dict_)#{mm1 : 7 , dd1 :19 , yy1:1985}
d = Date()#error
e = Date(dd = 30 , mm = 4 , yy = 2022)#error
f = Date(dd1 = 26 , mm1 = 8 , 2023)#error


'''
Object  'a'   --->  

Object  'b'   --->  

Object  'c'   --->  
'''


# Find  outputs (Home  work)
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
# End  of  class
a = c1()#error
b = c2()
print(b)#c2  class  constructor
print(b . _init_())#c2  class  constructor
c = c3()#c3  class  constructor
print(c . _init_())#error 


# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()#constructor


#  Difference  between  init()    and  _init_()   methods (Home  work)
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
a = c1()#constructor
print(a . _dict_){x:10,y:20}
b = c2()
print(b . _dict_)#{x:30,y:40}
b . init()#method
print(b . _dict_)#{}


'''
Object  'a'  --->  

Object  'b'  ---> 
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
print(x . _dict_)#{a:10}
x . m1()
print(x . _dict_)#{a:10,b:20}
f1()#error
print(x . _dict_)#error
x . d = 40
print(x . _dict_)#{a:10,b:20,d:40}
y = c2()
y . m3()
print(x . _dict_)#
z = c1()
print(z . _dict_)


'''
object  'x'  --->

object  'z'  --->

object  'y'  --->
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
print(a . _dict_)
print(b . _dict_)
del  a . x
del  b . y
print(a . _dict_)
print(b . _dict_)
print(a . x)
print(b . y)


'''
Object  'a'   --->  

Object  'b'   --->  
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
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()



#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#Two  argument  constructor : 10 20
b = c1(30)#Two  argument  constructor :30 20 
c = c1()#Two  argument  constructor :100 200



# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1()#constructor
print(a)#None

# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a)#Function none


# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()#error
b = c1(25)#Function : 25
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
How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a = c1()
b=prog9a.c1()



'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a=c1()
b=prog9a.c1()