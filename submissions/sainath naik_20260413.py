1.#Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))
print(sys . getrefcount(c1()))
print(sys . getrefcount(352))
print(sys . getrefcount([10 , 20 , 15 , 18]))
print(sys . getrefcount(10.8))
print(sys . getrefcount({10 , 20 , 15 , 18}))
print(sys . getrefcount('Hyd'))
print(sys . getrefcount({10 : 20 , 30 : 40}))
print(sys . getrefcount((10 , 20 , 30 , 40)))

'''
5
2
2
2
2
2
2
2
2
'''



2.# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . _init_())
print(sys . getrefcount(t))
print(t . _del_())
print(sys . getrefcount(t))
print('Bye')

'''
Constructor  :   2458614532240
None
2
Destructor  :   2458614532240
25
2
Bye
'''



3.# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

'''
Program  Begin
Function  Begin
<__main__.c1 object at 0x000001C6EA008BD0>
Function  end
<__main__.c1 object at 0x000001C6EA008BD0>
Program  End
'''



4.#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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
program  Begin
function begin
function end
program  End
'''




5.#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
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
Program  Begin
Function  begin
Function  end
None
Program  End
'''



6.# Most  tricky  program  (Can  not  do  figure)
# Circular  reference (Home  work)
class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')
		self . a = c1(self)
		print('End  of  c2  class constructor')
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

'''
program begin
program end
'''



7.# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

'''
Hello
'''



'''
8.Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

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

4) Leave  get() ,  test() , _str_()  and  simplify()  methods  unchanged
'''
# # import math

# # class rat:
# #     def get(self):  # Do not modify
# #         self.nr = int(input('Enter  numerator : '))
# #         self.dr = int(input('Enter  denominator : '))
# #         self.test()

# #     def test(self):  # Do not modify
# #         while self.dr == 0:
# #             self.dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))

# #     def _str_(self):  # Do not modify
# #         return f'{self.nr} / {self.dr}'

# #     # -------- Operator Overloading Methods --------

# #     def __add__(self, other):
# #         res = rat()
# #         res.nr = self.nr * other.dr + self.dr * other.nr
# #         res.dr = self.dr * other.dr
# #         res.simplify()
# #         return res

# #     def __sub__(self, other):
# #         res = rat()
# #         res.nr = self.nr * other.dr - self.dr * other.nr
# #         res.dr = self.dr * other.dr
# #         res.simplify()
# #         return res

# #     def __mul__(self, other):
# #         res = rat()
# #         res.nr = self.nr * other.nr
# #         res.dr = self.dr * other.dr
# #         res.simplify()
# #         return res

# #     def __truediv__(self, other):
# #         if other.nr == 0:
# #             print('Division is not permitted.')
# #             return None
# #         res = rat()
# #         res.nr = self.nr * other.dr
# #         res.dr = self.dr * other.nr
# #         res.simplify()
# #         return res

# #     def __str__(self):
# #         return self._str_()

# #     # -------- Simplify (Do not modify) --------
# #     def simplify(self):
# #         if self.nr != 0:
# #             g = math.gcd(self.nr, self.dr)
# #             self.nr //= g
# #             self.dr //= g


# # # -------- Main Program --------

# # a = rat()
# # b = rat()

# # a.get()
# # b.get()

# # print('Sum : ', a + b)
# # print('Difference : ', a - b)
# # print('Product : ', a * b)

# # result = a / b
# # if result:
# #     print('Division : ', result)
# # else:
# #     print('Division is not permitted.')




9.# # Is  10 + 20  a  recursion ?
# # class   c1:
# # 	def  __add__(a , b):
# # 			print(10 + 20)
# # a = c1()
# # b = c1()
# # print(a + b)

'''
30
None
'''



10.# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
#		x = c1() # RecursionError: maximum recursion depth exceeded while calling a Python object
		y = c1()
#		print(x + y) # NameError: name 'x' is not defined
a = c1()
b = c1()
print(a + b)

'''
None
'''



11.# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10) # TypeError: c1() takes no arguments
b = c1(20) # TypeError: c1() takes no arguments
print(a > b)
print(a < b)

'''
__gt__ method  :   10 20
None
__gt__ method  :   20 10
None
'''



12.# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)  #  b >= a

'''
__ge__ method :   10 20
False
__ge__ method :   20 10
True
'''



13.# Find  outputs (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('__eq__ method  : ' , m . x , n . x)
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b)
print(a != b)  # not (a == b)

'''
__eq__ method  :  10 20
False
__eq__ method  :  10 20
True
'''



14.# Find  outputs  (Home  work)
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



15.# Find  outputs  (Home  work)
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



16.# Find  outputs  (Home  work)
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




17.#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)

'''
false
false
false
RecursionError: maximum recursion depth exceeded while calling a Python object
'''



18.# Find  outputs  (Home  work)
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



19.# Overload  *  operator  to  multiply  two  different  class  objects
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250

    def __mul__(self, other):
        print('__mul__ method of class c1')
        return 25 * 8


class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8

    def __mul__(self, other):
        print('__mul__ method of class c2')
        return 8 * 25


a = c1()
b = c2()

print(a * b)
print(b * a)

'''
__mul__ method of class c1
200
__mul__ method of class c2
200
'''



20.# Find  outputs  (Home  work)
class c1:
	def __add__(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
print('a + 7 : ' , a + 7)
#print(7 + a) # TypeError: unsupported operand type(s) for +: 'int' and 'c1'
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
# print(m + n) # TypeError: unsupported operand type(s) for +: 'c2' and 'c2'
print('a + m : ' , a + m)
print(m + a) # TypeError: unsupported operand type(s) for +: 'c2' and 'c1'

'''
a + b :  __add__ method  of  class   c1
a + 7 :  __add__ method  of  class   c1
7 + 8 :  15
a + m :  __add__ method  of  class   c1
'''



21.# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     _init_(self , y):
		self . x = y
	def __add__(p , q):
		if isinstance(p . x , int) and isinstance(q . x , int):
			return p . x + q . x
		else:
			return str(p . x) + str(q . x)
#end of the class
#a = c1(10) # TypeError: c1() takes no arguments
#b = c1(20) # TypeError: c1() takes no arguments
#m = c1('10') # TypeError: c1() takes no arguments
#n = c1('20') # TypeError: c1() takes no arguments
#print('Sum : ' , a + b) # NameError: name 'a' is not defined
# print('Join : ' , m + n) # NameError: name 'm' is not defined