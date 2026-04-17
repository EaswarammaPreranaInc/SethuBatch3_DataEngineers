# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))	#5
print(sys . getrefcount(c1()))	#2
print(sys . getrefcount(352))	#2
print(sys . getrefcount([10 , 20 , 15 , 18]))	#2
print(sys . getrefcount(10.8))	#2
print(sys . getrefcount({10 , 20 , 15 , 18}))	#2
print(sys . getrefcount('Hyd'))		#2
print(sys . getrefcount({10 : 20 , 30 : 40}))	#2
print(sys . getrefcount((10 , 20 , 30 , 40)))	#2





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
t = Test()	#constructor : <id1>
print(t . __init__())		#constructor : <id1> <next> None
print(sys . getrefcount(t))	#2
print(t . __del__())		#destructor : <id1>  <next> 25
print(sys . getrefcount(t))	#2
print('Bye')			#Bye
#Destructor : <id1>






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
print('Program  Begin')		#program begin
b = f1()	#Functon begin <next> object is created <next> c1 object at address of the object <next> function end 
print(b)	#c1 object at address of the object
print('Program  End')	#program end
#object is lost




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
print('Program  Begin')		#program begin
f1()				#function begin <next> object is created <next> function end <next> object is lost
print('Program  End')		#program end





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
print('Program  Begin')		#program begin
b = f1()			#object is created <next> c1 object at address of the object <next> function end
print(b)			#c1 object at address of the object
print('Program  End')		#program end
#object is lost






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
print('Program  begin')		#program begin
x = c2()	#c2  class  object  is  created <next> c1 class object is created <next> end of c1 class constructor <next> end of c2 class constructor 
print('program end')	#program end




# Lucky  object
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()	#object is created
del  a		#destructor
print('Hello')	#hello
#destructor




import math

class rat:
    def get(self):
        self.nr = int(input("Enter numerator: "))
        self.dr = int(input("Enter denominator: "))
        while self.dr == 0:
            self.dr = int(input("Denominator cannot be zero, re-enter: "))

    def __str__(self):
        return f"{self.nr} / {self.dr}"

    def simplify(self):
        if self.nr != 0:
            g = math.gcd(self.nr, self.dr)
            self.nr //= g
            self.dr //= g

    def make(self, n, d):
        r = rat()
        r.nr, r.dr = n, d
        r.simplify()
        return r

    def __add__(a, b):
        return a.make(a.nr*b.dr + a.dr*b.nr, a.dr*b.dr)

    def __sub__(a, b):
        return a.make(a.nr*b.dr - a.dr*b.nr, a.dr*b.dr)

    def __mul__(a, b):
        return a.make(a.nr*b.nr, a.dr*b.dr)

    def __truediv__(a, b):
        if b.nr == 0:
            print("Division not permitted")
            return None
        return a.make(a.nr*b.dr, a.dr*b.nr)


# Main
a = rat()
b = rat()

print("First number")
a.get()
print("Second number")
b.get()

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

d = a / b
if d:
    print("Division:", d)






# Is  10 + 20  a  recursion ?
class   c1:
	def  __add__(a , b):
			print(10 + 20)
a = c1()
b = c1()
print(a + b)	#30 <next> None


# Is  x + y  a  recursion  ?  (Home  work)
class   c1:
	def  __add__(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)	#recursion error



# Find  outputs
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __gt__(m , n):
		print('__gt__ method  :  ' , m . x , n . x)
# End  of  the  class
a = c1(10)
b = c1(20)
print(a > b)	#__gt__ method : 10 20 <next> None
print(a < b)	#__gt__ method : 20 10 <next> None



# Find  outputs  (Home work)
class   c1:
	def   __init__(self , y):
		self . x = y
	def    __ge__(m , n):
		print('__ge__ method :  ' , m . x , n . x)
		return  m . x > n . x
# End  of  the  class
a = c1(10)	#__ge__ method : 10 20 <next> 
b = c1(20)	#__ge__ method : 20 10
print(a >= b)	#False
print(a <= b)  #  b >= a	#True








