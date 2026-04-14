#1
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # 5
print(sys . getrefcount(c1())) # 2
print(sys . getrefcount(352)) # 2
print(sys . getrefcount([10 , 20 , 15 , 18])) # 2
print(sys . getrefcount(10.8)) # 2
print(sys . getrefcount({10 , 20 , 15 , 18})) # 2
print(sys . getrefcount('Hyd')) # 2
print(sys . getrefcount({10 : 20 , 30 : 40})) # 2
print(sys . getrefcount((10 , 20 , 30 , 40))) # 2


#2
# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() #  Constructor  : 1000
print(t . __init__()) # Constructor  : 1000  /n None
print(sys . getrefcount(t)) # 2
print(t . __del__())  # Destructor  :  1000  /n 25
print(sys . getrefcount(t)) # 2
print('Bye') # Bye
#  # Destructor  :  1000


#3
# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a) # type and address of object
	print('Function  end')
	return   a
print('Program  Begin') 
b = f1()
print(b)
print('Program  End')

'''
Program Begin
Function Begin
Object is created
type and address of object
Function end
Object is created
type and address of object
Program End
Object is lost
'''


#4
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')

'''
Program Begin
Function begin
Object is created
Function end
Object is lost
Program End
'''



#5
#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

'''
Program Begin
Function begin
Object is created
Function end
Object is lost
None
Program End
'''

#6
# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

'''
Program begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
c2 class object is lost
c1 class object is lost
'''


#7
# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')


'''
Destructor
Hello
Destructor
'''

#8
'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects
'''
import math
class rat:
    def get(self):
        self.nr = int(input("First rational number :"))
        self.dr = int(input("Second rational number :"))
        self.test()
    def test(self):
        while self.dr == 0:
            self.dr = int(input("re enter denominator :"))
    def __str__(self):
        return f'{self.nr}/{self.dr}'
    
    def __add__(self, other):   # modified
        temp = rat()
        temp.nr = self.nr * other.dr + self.dr * other.nr
        temp.dr = self.dr * other.dr
        temp.simplify()
        return temp

    def __sub__(self, other):   # modified
        temp = rat()
        temp.nr = self.nr * other.dr - self.dr * other.nr
        temp.dr = self.dr * other.dr
        temp.simplify()
        return temp

    def __mul__(self, other):   # modified
        temp = rat()
        temp.nr = self.nr * other.nr
        temp.dr = self.dr * other.dr
        temp.simplify()
        return temp

    def __truediv__(self, other):   # modified
        temp = rat()
        temp.nr = self.nr * other.dr
        temp.dr = self.dr * other.nr
        temp.simplify()
        return temp

    def simplify(self):   # unchanged
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g


# object creation
a = rat()
b = rat()

a.get()
b.get()

# operator overloading use
c = a + b
d = a - b
e = a * b

print("Sum        :", c)
print("Difference :", d)
print("Product    :", e)

if b.nr != 0:
    f = a / b
    print("Division   :", f)
else:
    print("Division is not permitted.")       
        
        
       
#9
# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)

'''
30
None
'''

#10
# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # Recursion error



#11
# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b) # __gt__ method  : 10 20 /n None
print(a < b) # __gt__ method  : 20 10 /n None


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''

#12
# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)#
b = c1(20)
print(a >= b)#False
print(a <= b)  #  b >= a#True


'''
Object  'a'   --->#  xx= 10

Object  'b'   --->  #x = 20
'''

#13
# Find  outputs (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)#False
print(a != b)  # not (a == b)#	True
'''
Object  'a'   --->#  x= 10

Object  'b'   --->  #x = 20
'''


#14
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)#__eq__ method  : 25 25 None
print(a != b)#__eq__ method  : 25 25 True
#None → False
#not False → True
print(a . x !=  b . x)#False

#15
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method :  ' , m . x , n . x)
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b)#__ne__ method : 25 25 False
print(a == b)#__ne__ method :25 25  True
print(a  is  b)#True


#16
# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a# b points to class c1
print(a != b)#False
print(a == b)#True


#17
#  Is  10 > 20  a  recursion ?Yes
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)#recursion occurs here
a = c1()
b = c1()
print(a > b)

#18
# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  __gt__  method : ' , p . x , q . x)
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  __gt__  method : ' , p . x , q . x)
# End  of  the  class
a = c1(10)
b = c1(20)
a > b#c1  class  __gt__  method :10  20
a < b#c1  class  __gt__  method : 20 10
m = c2(30)
n = c2(40)
a < m#c2  class  __gt__  method :30 10
n < b#c2  class  __gt__  method : 20 40


#19
# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25#a.empno=25
		self . hr = 250#a.hr=250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return   x.hr * y.noh
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  x.hr * y.noh
# End of the class
a = c1()
b = c2()
print(a * b)#a--->c1()  b--->c2()  a
print(b * a)
#__mul__  method  of  class   c1	200
#'__mul__  method  of  class   c2'      200


#20
# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		
		return self.x + self.y
class c2:
	def __add__(m , n):
	
		return m.x + n.y

#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
print('a + 7 : ' , a + 7)
print(7 + a)
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ' , a + m)
print(m + a)


#21
# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  p.x+q.x
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)#Sum: 30  
print('Join : ' , m + n)#Join: 1020


'''
Object  a  --->x = 10

Object  b  --->x = 20

Object  m  --->x = "10"

Object  n  --->x ="20"
'''











