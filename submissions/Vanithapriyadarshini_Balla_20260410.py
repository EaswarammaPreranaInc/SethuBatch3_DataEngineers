# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.y=20
	def  m1(self):
		print('m1  method')
		print(t.x)
		print(t.y)
		t.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(t.x)
		print(t.y)
# End  of  the  class
t = Test()
print('Outside')# Outside
print(t.x)
print(t.y)
#print(t . __y)# Error, cant access private var directly outside the class
print(t . __dict__)# {'x':10 ,'y': 20}
t.m1()# m1 method    10    20     __m2 method     10    20    Back to m1 method 
t._Test__m2()
#t . __m2()# Error, cant access directly outside class 
print('End')# End


# Object  't'  --->x=10 y=20
 
#Find  outputs

#Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively

class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1()# Object is created at address : 1000
a = None# Object  at  address  1000  is  lost
b = c1()# Object is created at address : 2000
del    b# #Object  at  address  2000  is  lost
c = c1()# Object is created at address : 3000     # Object  at  address  3000  is  lost
c = c1()# Object is created at address : 3000
d = c1()# Object is created at address : 4000
e = c1()# Object is created at address : 5000
# Object  at  address  3000  is  lost
# Object  at  address  4000  is  lost
# Object  at  address  5000  is  lost


# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()# obj is created
a . __del__(25)# desstructor : 25   here conn are alive 
#when program terminates again its executed

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()# obj created
a . __del__(25)# destructor : 25    after program tarminetion  destructor : 35

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() # infinite 

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()# constructor     after prog terminates   destructor constructor destructor infinite recursion 


#  Find  outputs( Home  work)
class   c1:
	def __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()# #rd destructor    


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self), type(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()# Object  is  created  at  address  :  1000
del   a  # obj at address 1000 is lost
print('Hello')# Hello
del   b 
print('Hi')# Hi
del   c # # obj at address 3000 is lost
print('Bye')# Bye
d = c1()# 
print('End') # End 


# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]# Object  is  created  at  address  : ist obj addr , Object  is  created  at  address  :2nd obj addrs, Object  is  created  at  address  :3rd obj addrss

# after program termination ,,,obj at addrs 3rd     obj at addrs 32nd lost    obj at addrs 1st  lost
