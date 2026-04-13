# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) # 5
print(sys . getrefcount(c1())) # 1
print(sys . getrefcount(352)) # ref count of an immutable object is high
print(sys . getrefcount([10 , 20 , 15 , 18])) # 1
print(sys . getrefcount(10.8)) # ref count of an immutable object is high
print(sys . getrefcount({10 , 20 , 15 , 18})) # 1
print(sys . getrefcount('Hyd')) # ref count of an immutable object is high
print(sys . getrefcount({10 : 20 , 30 : 40})) #1
print(sys . getrefcount((10 , 20 , 30 , 40))) # ref count of an immutable object is high


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
t = Test() # Constructor : Address of t
print(t . __init__()) # Constructor : Address of t # None
print(sys . getrefcount(t)) # 2
print(t . __del__()) # print('Destructor  :  ' , id(self)) # 25
print(sys . getrefcount(t)) # 2
print('Bye') # Bye


# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
	print('Function  Begin') # Function Begin
	a  =  c1() # Object is created
	print(a) # Type and address
	print('Function  end') # Function End
	return a 
print('Program  Begin') # Program Begin
b = f1() # Go to function call
print(b) # Type and address of object a
print('Program  End') # Program End


#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin') # Function Begin
        a  =  c1() # Object is created
        print('Function  end') # Function end
        return a # Object is lost
print('Program  Begin') # Program Begin
f1()
print('Program  End') # Program End


#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin') # Function begin
        a  =  c1() # Object is created
        print('Function  end') # Function end # Object is lost
print('Program  Begin') # Program Begin
b = f1() 
print(b) # None
print('Program  End') # Program End


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
		self . a = c1(self) # c1 class object is created
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin') # Program begin
x = c2() # c2 class object is created
print('program end')
'''
Program begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
'''


# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a # Destructor
print('Hello') # Hello


#1
'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
   What  is  the  difference  ?  --->  2 / 3 - 5 / 9 = (18 - 15) / 27 =  3 / 27 = 1 / 9
   What  is  the  product  ?  ---> 2 / 3 * 5 / 9 = 10 / 27 =  10 / 27
   What  is   the  division  ?  ---> 2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  2 / 3
   Second  rational  number ---> 0 / 9
   What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3
   What  is  the  product  ?  ---> 2 / 3 * 0 / 9 =  0 / 27 = 0 / 27  (simplification  is  not  required  becoz  numerator  is  0)
    What  is   the  division  ?  ---> 2 / 3 /  0 / 9 =  2 / 3 * 0 / 9  --->  Division  is  not  possible  becoz  b . nr  is  0

3) Modify  the  following  program  with  operator  overloding  methods

4) Leave  get() ,  test() , __str__()  and  simplify()  methods  unchanged
'''
import math

class rat:
    def get(self):   # Do not modify
        self.nr = int(input('Enter numerator : '))
        self.dr = int(input('Enter denominator : '))
        self.test()

    def test(self):  # Do not modify
        while self.dr == 0:
            self.dr = int(input('Denominator can not be zero and re-enter : '))

    def __str__(self):   # Do not modify
        return f'{self.nr} / {self.dr}'

    def __add__(a, b):
        c = rat()
        c.nr = a.nr * b.dr + a.dr * b.nr
        c.dr = a.dr * b.dr
        c.simplify()
        return c

    def __sub__(a, b):
        c = rat()
        c.nr = a.nr * b.dr - a.dr * b.nr
        c.dr = a.dr * b.dr
        c.simplify()
        return c

    def __mul__(a, b):
        c = rat()
        c.nr = a.nr * b.nr
        c.dr = a.dr * b.dr
        c.simplify()
        return c

    def __truediv__(a, b):
        c = rat()
        c.nr = a.nr * b.dr
        c.dr = a.dr * b.nr
        c.simplify()
        return c

    def simplify(self):   # Do not modify
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g
# End  of  the  class
#  Modify  the  following  statements
a = rat()
b = rat()

a.get()
b.get()

print('Sum : ', a + b)
print('Difference : ', a - b)
print('Product : ', a * b)

if b.nr != 0:
    print('Division : ', a / b)
else:
    print('Division is not permitted.')


# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) # 30 # None


# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # infinite recursion


# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b) # __gt__ method : 10 20 # None
print(a < b) # __gt__ method : 20 10 # None


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''


# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b) # __ge__ method : 10 20 # False
print(a <= b) # __ge__ method : 20 10 # True


'''
Object  'a'   --->  x = 10

Object  'b'   --->  x = 20
'''


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
print(a == b) # __eq__ method  : 10 20 # False
print(a != b)  # not (a == b) # __eq__ method  : 10 20 # True


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  :  ' , m . x , n . x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a . x !=  b . x)
'''
__eq__ method  :   25 25
None
__eq__ method  :   25 25
True
False
'''


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
print(a != b)
print(a == b)
print(a  is  b)
'''
__ne__ method :   25 25
False
False
False
'''

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('__ne__ method  :  ' , m . x , n . x)
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a
print(a != b)
print(a == b)
'''
__ne__ method  :   10 10
False
True
'''


#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b) # infinite recursion


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
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b
'''
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10
c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40
'''


# Overload  *  operator  to  multiply  two  different  class  objects
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 25   # hourly rate

    def __mul__(x, y):
        print("__mul__ method of class c1")
        return x.hr * y.noh


class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8   # number of hours

    def __mul__(x, y):
        print("__mul__ method of class c2")
        return x.noh * y.hr
a = c1()
b = c2()
print(a * b)
print(b * a)


# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # '__add__ method  of  class   c1'
print('a + 7 : ' , a + 7) # '__add__ method  of  class   c1'
print(7 + a) # error , cannot add int class object with c1 class
print('7 + 8 : ' , 7 + 8) # 7 + 8 = 15
m = c2()
n = c2()
print(m + n) # error
print('a + m : ' , a + m) # '__add__ method  of  class   c1'
print(m + a) # error



# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
        def __init__(self , y):
                self . x = y

        def __add__(p , q):
                op1 = p . x
                op2 = q . x
                try:
                        return op1 + int(op2)
                except:
                        try:
                                return op1 + float(op2)
                        except:
                                return str(op1) + str(op2)
#end of the class
a = c1(10)
b = c1(20)

m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)
