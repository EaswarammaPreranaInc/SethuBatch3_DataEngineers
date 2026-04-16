
# Find  outputs
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
output
5
2
2
2
2
2
2
2
2




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
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')


output
Constructor : <id1>
Constructor : <id1>
None
2
Destructor : <id1>
25
2
Bye
Destructor : <id1>


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
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

output
Program Begin
Function Begin
Object is    created
<__main__.c1 object at 0x...>
Function end
<__main__.c1 object at 0x...>
Program End
Object is  lost




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

output
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End




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

output
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
None
Program  End



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

output
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end


c1  class  object  is  lost   
c2  class  object  is  lost   




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
output
Destructor
Hello



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
import  math
class  rat:
	def  get(self):  #  Do  not  modify  the  method
		self . nr = int(input('Enter  numerator : '))
		self . dr = int(input('Enter  denominator : '))
		self . test()
	def  test(self): #  Do  not  modify  the  method
		while  self . dr == 0:
			self . dr = int(input('Denominator  can  not  be  zero  and  re-enter :  '))
	def    __str__(self):  #  Do  not  modify  the  method
		return  F'{self . nr} / {self . dr}'
	def  add(self, a , b):  #  Modify  the  method
		self . nr = a . nr * b . dr + a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  sub(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr - a . dr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  mul(self ,  a , b):   #  Modify  the  method
		self . nr = a . nr * b . nr
		self . dr = a . dr * b . dr
		self . simplify()
	def  div(self, a , b):   #  Modify  the  method
		self . nr = a . nr * b . dr
		self . dr = a . dr * b . nr
		self . simplify()
	def   simplify(self):   #  Do  not  modify  the  method
		if self . nr != 0:
			g = math . gcd(self . nr, self . dr)
			self . nr = self . nr // g
			self . dr = self . dr // g
# End  of  the  class
#  Modify  the  following  statements
a = rat()
b = rat()
c = rat()
d = rat()
e = rat()
f = rat()
a . get()
b . get()
c . add(a , b)
d . sub(a , b)
e .  mul(a , b)
print('Sum :  ' , c)
print('Difference :  ' , d)
print('Product :  ' ,  e)
if b . nr != 0:
	f . div(a , b)
	print('Division  : ' , f)
else:
	print('Division is not permitted.')



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

    #  Operator Overloading

    def __add__(self, other):
        res = rat()
        res.nr = self.nr * other.dr + self.dr * other.nr
        res.dr = self.dr * other.dr
        res.simplify()
        return res

    def __sub__(self, other):
        res = rat()
        res.nr = self.nr * other.dr - self.dr * other.nr
        res.dr = self.dr * other.dr
        res.simplify()
        return res

    def __mul__(self, other):
        res = rat()
        res.nr = self.nr * other.nr
        res.dr = self.dr * other.dr
        res.simplify()
        return res

    def __truediv__(self, other):
        if other.nr == 0:
            print("Division is not permitted.")
            return None
        res = rat()
        res.nr = self.nr * other.dr
        res.dr = self.dr * other.nr
        res.simplify()
        return res

    def simplify(self):   # Do not modify
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g

# ---------------- MAIN ----------------

a = rat()
b = rat()

a.get()
b.get()

c = a + b
d = a - b
e = a * b

print('Sum : ', c)
print('Difference : ', d)
print('Product : ', e)

f = a / b
if f:
    print('Division : ', f)


input
2/3 and 5/9

output
Sum :  11 / 9
Difference :  1 / 9
Product :  10 / 27
Division :  6 / 5




# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)

output
30
None




# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)
print(a < b)


output
__gt__ method  :   10 20 None
__gt__ method  :   20 10 None

'''
Object  'a'   --->  10

Object  'b'   --->  20
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
print(a >= b)
print(a <= b)  #  b >= a

output
__ge__ method :   10 20 False
__ge__ method :   20 10 True


'''
Object  'a'   --->  10

Object  'b'   --->  20
'''




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

output
__eq__ method  :   25 25
 None
__eq__ method  :   25 25 
True 
False



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
output
__ne__ method  :   10 10
False
True


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

output
c1  class  __gt__  method :  10 20
c1  class  __gt__  method :  20 10
c2  class  __gt__  method :  30 10
c1  class  __gt__  method :  20 40



# Overload  *  operator  to  multiply  two  different  class  objects
class  c1:
	def  __init__(self):
		self . empno = 25
		self . hr = 250
	def __mul__(x , y):
		print('__mul__  method  of  class   c1')
		return  hourly-rate(i.e.  25) *  number-of-hours (i.e.  8)
class c2:
	def __init__(self):
		self . empno = 25
		self . noh = 8
	def __mul__(x , y):
		print('__mul__  method  of  class   c2')
		return  number-of-hours (i.e.  8) *  hourly-rate(i.e.  25)
# End of the class
a = c1()
b = c2()
print(a * b)
print(b * a)



output

__mul__ method of class c1
2000
__mul__ method of class c2
2000



# Find  outputs  (Home  work)
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
print(7 + a)
print('7 + 8 : ' , 7 + 8)
m = c2()
n = c2()
print(m + n)
print('a + m : ' , a + m)
print(m + a)



output
a + b :  __add__ method  of  class   c1
a + 7 :  __add__ method  of  class   c1
TypeError
7 + 8 :  15
TypeError
a + m :  __add__ method  of  class   c1
TypeError



# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class  c1:
	def     __init__(self , y):
		self . x = y
	def __add__(p , q):
		return  sum  of  numbers  (or)  join  of  strings
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ' , a + b)
print('Join : ' , m + n)

output
Sum :  30
Join :  1020

'''
Object a ---> 10 
 
Object b ---> 20  

Object m ---> '10'  

Object n ---> '20'
'''






