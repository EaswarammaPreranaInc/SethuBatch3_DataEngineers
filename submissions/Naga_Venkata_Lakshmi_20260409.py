# Find  outputs
class  Rat:
	def   _init_(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   _str_(self):
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
print('a  :  ' , a) #22 7
print('b  :  ' , b) #9,7
print('c  :  ' , c) #5,8
print('d  :  ' , d) #22,9
print('e  :  ' , e) #2,3
print('f  :  ' , f) #11,15
c . _init_()
print('c  :  ' , c) #22,7
a . _init_(3.8  , 4.6) #3.8/4.6
print('a  :  ' , a)
g = Rat(nr1 = 9 , 5)
h = Rat(nr = 9 , dr = 5) #9/5
'''outputs
Enter numerator  :  11
Enter Denominator  :  15
a  :   <__main__.Rat object at 0x000001B6050E8980>
a  :   <__main__.Rat object at 0x000001B6050E8980>'''


# Find  outputs (Home  work)
class  Date:
        def   _init_(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . _dict_)
print('b  :  ' , b . _dict_)
print('c  :  ' , c . _dict_)
d = Date() #missing arguments
e = Date(dd = 30 , mm = 4 , yy = 2022) #wrong parameters
f = Date(dd1 = 26 , mm1 = 8 , 2023) #positional argument follows keyword argument
'''outputs
a : {'dd' : 15, 'mm' : 8, 'yy' : 1947}
b : {'dd' : 26, 'mm' : 1, 'yy' : 1950}
c : {'dd' : 19, 'mm' : 7, 'yy' : 1985}'''


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
a = c1()
b = c2()
print(b)
print(b . _init_())
c = c3()
print(c . _init_())
'''outputs
<__main__.c2 object at 0x000001747FB68AD0>
c2  class  constructor
None
c3  class  constructor
None'''


# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor')
		b = c1()
# End  of  class
a = c1()

'''outputs
constructor 
constructor
constructor
infinite times and leads to maximum recursion depth exceeded.'''


#  Difference  between  init()    and  _init_()   methods (Home  work)
'''__init__() : 1.special dunder method python recognizes it.
         2.Called automatically when you do class()
         3.Constructor used to initialize object.
init() : 1.Normal method-python treats it like any function you named.
         2.Never called automatically.You must do obj.init()
         3.just a regular method with no special role.'''

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
print(a . _dict_)
b = c2()
print(b . _dict_)
b . init()
print(b . _dict_)
'''outputs
Constructors
{'x' : 10, 'y' : 20}
{}
Method
{'x' : 30, 'y' : 40}'''


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
print(x . _dict_)
x . m1()
print(x . _dict_)
f1()
print(x . _dict_)
x . d = 40
print(x . _dict_)
y = c2()
y . m3()
print(x . _dict_)
z = c1()
print(z . _dict_)

'''outputs
{'a' : 10}
{'a' : 10, 'b' : 20}
{'a' : 10, 'b' : 20, 'c' : 30}
{'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
{'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40, 'e' : 50}
{'a' : 10}'''


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

'''outputs
{'x' : 10, 'y' : 20, 'z' : 30}
{'x' : 10, 'y' : 20, 'z' : 30}
{'y' : 20, 'z' : 30}
{'x' : 10, 'z' : 30}'''

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
'''outputs
3rd constructor'''


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
'''outputs
Two argument constructor : 10 20
Error because 1 required positional argument is missing.
Error because 2 required positional arguments are missing.'''




