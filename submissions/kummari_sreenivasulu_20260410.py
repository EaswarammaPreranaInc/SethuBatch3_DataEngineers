1.
# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		#print(self.x) #How  to  print   variable  'x'
		#print(self.__y) # How  to  print  private  variable  'y'
		print(self.__m2()) # How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		#print(self.x) # How  to  print   variable  'x'
		#print(self.__y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
#print(t.x) # How  to  print  variable  'x'
#print(t._Test__y) # How  to  print   variable  'y'
print(t . __dict__)
t.m1() # How  to  call  method  m1()
#t._Test.__m2() # How  to  call   method  m2()
#t . __m2()
print('End')
'''
{}
m1  method
__m2  method
None
Back to m1 method
End
'''



2.
#  Find  outputs
class  c1:
	def _init_(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self.__z__ = 30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a.__x__) # How  to  print  public  dunder  variable  'x'
print(a.__x) # How  to  print   private  variable  'x'
print(a._c1__x)
a.m1() # How  to  call  public  method  m1()
a.__m1__() # How  to  call  public  dunder  method  m1()
a._c1.__m1() # How  to  call  private  method  m1()
a .__m1()



3.
'''  
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()
'''
Object  is  created  at  address  :   2835150767952
Object  at  address  2835150767952  is  lost
Object  is  created  at  address  :   2835150767952
Object  at  address  2835150767952  is  lost
Object  is  created  at  address  :   2835150767952
Object  is  created  at  address  :   2835150768080
Object  at  address  2835150767952  is  lost
Object  is  created  at  address  :   2835150767952
Object  is  created  at  address  :   2835150768208
Object  at  address  2835150768080  is  lost
Object  at  address  2835150767952  is  lost
Object  at  address  2835150768208  is  lost
'''



4.
# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)
'''
Error  :  destructor  takes  exactly  one  argument  (the  object  itself)  but  two  were  given
'''


5.
# # Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)
'''
destructor :  25
destructor :  35
'''


6.
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
'''
destructor
destructor
destructor
destructor
destructor
destructor
destructor
infinite  loop  of  destructor  calls
'''



7.
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
destructor
constructor
destructor
constructor
destructor
constructor
destructor
constructor
destructor
constructor
destructor
infinite loop of destructor and constructor calls
'''



8.
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor') # 3rd destructor
# End  of  the  class
a = c1()



9.
#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')

'''
Hello
Hi
Bye
End
'''


10.
# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list

'''
Object  is  created  at  address  :   2685737682960
Object  is  created  at  address  :   2685737683024
Object  is  created  at  address  :   2685737683152
Object  at  address  2685737683152  is  lost 
Object  at  address  2685737683024  is  lost 
Object  at  address  2685737682960  is  lost 
'''


11.
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a

'''
destructor
25
Hello
destructor
'''