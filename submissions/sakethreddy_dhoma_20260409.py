class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()   # nr=22 , dr =7
b = Rat(9)  #  nr=9  ,dr=7
c = Rat(5,  8) # nr=5 , dr=7
d = Rat(dr1 = 9) # nr=22 ,dr=7
e = Rat(dr1 = 3 , nr1 = 2)  #  dr=3 , nr=2
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # x=11, y=15
print('a  :  ' , a)  # a:  22/7
print('b  :  ' , b)  # b:  9/7
print('c  :  ' , c)  # c:  5/7
print('d  :  ' , d)  # d:  22/7   
print('e  :  ' , e)  # e:  2/3
print('f  :  ' , f)  # f:  11/15
c . __init__()  # nr=22 , dr=7
print('c  :  ' , c)  #  c:  22/7
a . __init__(3.8  , 4.6)  # nr=3.8, dr=4.6
print('a  :  ' , a)  # a: 3.8/4.6
g = Rat(nr1 = 9 , 5)  # error  keyword arguments are followed by positional arguments
h = Rat(nr = 9 , dr = 5) # error  nr and dr are not found


# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947) # dd=15, mm=8, yy=1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26) #  dd=26, mm=1, yy=1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985) #  dd=19, mm=7, yy=1985
print('a  :  ' , a . __dict__) # a: {'dd':15, 'mm':8, 'yy'=1947}
print('b  :  ' , b . __dict__)  #b: { 'dd':26,'mm':1,'yy'=1950}
print('c  :  ' , c . __dict__) # c: {'dd'=19, 'mm'=7, 'yy'=1985}
d = Date() # error arguments should pass
e = Date(dd = 30 , mm = 4 , yy = 2022)  # Error arguments are not found / defined
f = Date(dd1 = 26 , mm1 = 8 , 2023)     # Error keyword arguments are followed by key word arguments


'''
Object  'a'   --->  dd=15, mm=8, yy=1947

Object  'b'   --->  dd=26, mm=1, yy=1950

Object  'c'   --->  dd=19, mm=7, yy=1985

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
a = c1() # c1 class constructor
         # error constructor returns only none not any value
b = c2() # c2 class constructor
print(b) # type and address of object
print(b . __init__()) # c2 class constructor 
                            None
c = c3()  # c3 class constructor
print(c . __init__()) # c3 class constructor 
                            None 
 


# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1() 
# End  of  class
a = c1() 

# outputs
  Infinite loop of constructor 
 

#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40

a = c1() # constructor
         
print(a . __dict__) # {'x':10, 'y':20}

b = c2() 
print(b . __dict__){}

b . init()          # Method 
print(b . __dict__) # {x:30 ,y:40} 

'''
Object  'a'  --->  x=10,y=20

Object  'b'  ---> x:30 ,y:40

'''



# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
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
print(x . __dict__) # {'a'=10}
x . m1()
print(x . __dict__) # {'a'=10,'b'=20}
f1() 
print(x . __dict__) # {'a'=10,'b'=20,'c'=50}
x . d = 40
print(x . __dict__) # {'a'=10,'b'=20,'c'=50,'d'=40}

y = c2() 
y . m3() 
print(x . __dict__) # {'a'=10,'b'=20,'c'=50,'d'=40,'e'=50,}
z = c1()
print(z . __dict__) # {'a'=10}


'''
object  'x'  ---> {'a'=10,'b'=20,'c'=50,'d'=40,'e'=50,}

object  'z'  ---> {'a'=10}

object  'y'  ---> {}
'''




# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__) # {'x'=10,'y'=20,'z'=30}
print(b . __dict__) # {'x'=10,'y'=20,'z'=30}
del  a . x 
del  b . y
print(a . __dict__) # {'y'=20,'z'=30}
print(b . __dict__) # {'x'=10,'z'=30}
print(a . x) # error
print(b . y) # erroe


'''
Object  'a'   ---> y=20,z=30

Object  'b'   --->  x=10,y=20,z=30
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

# output
  3rd constructor


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

#output
 Two argument constructor: 10 20



# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor')
# End  of  the  class
a = f1() 
print(a)  

#output : type and address of object


# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function')
#end of the  class
a = c1()
print(a) #Function
         #None



# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
a = c1()  # error
b = c1(25) 
print(b) # function :  25
         # None



class c1:
    def _init_(self):
        print('c1 class of prog9a')


from prog9a import c1

class c1:
    def _init_(self):
        print('c1 class of prog9b')

a = c1() # nothing is printed


class c1:
    def _init_(self):
        print('c1 class of prog9c')

from prog9a import c1

a = c1() # nothing is printed



from prog9a import c1 as c1_prog9a

class c1:
    def __init__(self):
        print('c1 class of prog9d')

# current class object
a = c1()

# prog9a class object
b = c1_prog9a()


import prog9a

class c1:
    def __init__(self):
        print('c1 class of prog9e')

# current class
a = c1()

# prog9a class
b = prog9a.c1()


