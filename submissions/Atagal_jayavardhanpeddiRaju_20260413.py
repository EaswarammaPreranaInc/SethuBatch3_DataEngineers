# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b)) #5
print(sys . getrefcount(c1())) #1
print(sys . getrefcount(352)) #3
print(sys . getrefcount([10 , 20 , 15 , 18])) #1
print(sys . getrefcount(10.8)) #3
print(sys . getrefcount({10 , 20 , 15 , 18})) #1
print(sys . getrefcount('Hyd')) #3
print(sys . getrefcount({10 : 20 , 30 : 40})) #1
print(sys . getrefcount((10 , 20 , 30 , 40))) #2


# Find  outputs  (Home  work)
import  sys
class  Test:
	def  _init_(self):
		print('Constructor  :  ' , id(self)) #Constructor  :   1980605695712
		return    None
	def  _del_(self):
		print('Destructor  :  ' , id(self)) #Destructor  :   1980605695712
		return  25 #25
# End  of  the  class
t = Test()
print(t . _init_()) #none
print(sys . getrefcount(t)) #2
print(t . _del_())
print(sys . getrefcount(t)) #2
print('Bye') #Bye


# Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created') #Object  is    created
	def  _del_(self):
		print('Object  is  lost')  #Object  is  lost
# End  of  the  class
def    f1():
	print('Function  Begin') #Function  Begin
	a  =  c1()
	print(a) #<__main__.c1 object at 0x7e21d6871bb0>
	print('Function  end') #Function  end
	return   a #<__main__.c1 object at 0x7e21d6871bb0>
print('Program  Begin') #Program  Begin
b = f1()
print(b)
print('Program  End') #Program  End

#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin') #Function  begin
        a  =  c1()
        print('Function  end') #Function  end
        return   a
print('Program  Begin') #Program  Begin
f1()
print('Program  End') #Program  End


#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
# End  of  the  class
def    f1():
        print('Function  begin') #Function  begin
        a  =  c1()
        print('Function  end') #Function  end
print('Program  Begin') #Program  Begin
b = f1()
print(b) #None
print('Program  End') #Program  End


# Most  tricky  program  (Can  not  do  figure)
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
print('Program  begin') #Program  begin
x = c2()
print('program end') #program end



# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello') #Hello



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

4) Leave  get() ,  test() , _str_()  and  simplify()  methods  unchanged
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
	def    _str_(self):  #  Do  not  modify  the  method
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
	print('Division is not permitted.'


import math

class rat:
    def get(self):
        self.nr = int(input('Enter numerator : '))
        self.dr = int(input('Enter denominator : '))
        self.test()

    def test(self): 
        while self.dr == 0:
            self.dr = int(input('Denominator can not be zero and re-enter : '))

    def __str__(self): 
        return f'{self.nr} / {self.dr}'

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
            return None
        res = rat()
        res.nr = self.nr * other.dr
        res.dr = self.dr * other.nr
        res.simplify()
        return res

    def simplify(self): 
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr = self.nr // g
            self.dr = self.dr // g

a = rat()
b = rat()

a.get()
b.get()

c = a + b
d = a - b
e = a * b

print('Sum :', c)
print('Difference :', d)
print('Product :', e)

f = a / b
if f is not None:
    print('Division :', f)
else:
    print('Division is not permitted.')


# Is  10 + 20  a  recursion ?
class   c1:
	def  _add_(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b) #error unsupported operand 


# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) #error unsupported operand


# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    _gt_(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b) #error
print(a < b) #error


# Find  outputs (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('_eq_ method  : ' , m . x , n . x) # _eq_ method  :  10 20
			return  m . x == n . x
# End  of  the  class
a = c1(10)
b = c1(20)
print(a == b) #False
print(a != b)  # not (a == b) #True


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
			self . x = y
	def    __eq__(m , n):
			print('_eq_ method  :  ' , m . x , n . x) #_eq_ method  :   25 25
#end of the class
a = c1(25)
b = c1(25)
print(a == b) #True
print(a != b) #False
print(a . x !=  b . x)


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('_ne_ method :  ' , m . x , n . x) #_ne_ method :   25 25
		return  m . x != n . x
#end of the class
a = c1(25)
b = c1(25)
print(a != b) #False
print(a == b) #False
print(a  is  b) #False


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ne__(m , n):
		print('_ne_ method  :  ' , m . x , n . x)  #_ne_ method  :   10 10
		return  m . x != n . x
# End  of  the  class
a = c1(10)
b = a
print(a != b) #False
print(a == b) #True


#  Is  10 > 20  a  recursion ?
class  c1:
	def   __gt__(a , b):
		print(10 > 20) #False
		print(a > b) #False
a = c1()
b = c1()
print(a > b) #False

# Find  outputs  (Home  work)
class  c1:
	def __init__(self , y):
		self . x = y
	def  __gt__(p , q):
		print('c1  class  _gt_  method : ' , p . x , q . x) 
class  c2:
	def __init__(self , y):
		self . x = y
	def __gt__(p , q):
		print('c2  class  _gt_  method : ' , p . x , q . x) 
# End  of  the  class
a = c1(10) #c1  class  _gt_  method :  10 20
b = c1(20) #c1  class  _gt_  method :  20 10
a > b
a < b
m = c2(30) #c2  class  _gt_  method :  30 10
n = c2(40) #c1  class  _gt_  method :  20 40
a < m
n < b

class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250  

    def __mul__(self, other):
        print('__mul__ method of class c1') #__mul__ method of class c2
2000
        return self.hr * other.noh  


class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8   

    def __mul__(self, other):
        print('__mul__ method of class c2') #__mul__ method of class c2
2000
        return self.noh * other.hr  


# Find  outputs  (Home  work)
class c1:
	def _add_(x , y):
		return '__add__ method  of  class   c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) #error
print('a + 7 : ' , a + 7) #error
print(7 + a) #error
print('7 + 8 : ' , 7 + 8) #7 + 8 :  15
m = c2()
n = c2()
print(m + n) #error
print('a + m : ' , a + m) #error
print(m + a) #error


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
print('Sum : ' , a + b) Sum :30
print('Join : ' , m + n) Join : 1020




