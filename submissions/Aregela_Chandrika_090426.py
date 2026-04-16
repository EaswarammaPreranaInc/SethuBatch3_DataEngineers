# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('c1  class constructor') #  c1  class constructor
		return  25 # error
class  c2:
	def  _init_(self):
		print('c2  class  constructor') # c2  class  constructor
		return  None # None
class  c3:
	def  _init_(self):
		print('c3  class  constructor') # c3  class  constructor
# End  of  class
a = c1() 
b = c2()
print(b)
print(b . _init_()) # Type and address
c = c3()
print(c . _init_()) # Type and address








# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Constructor') # Constructor.....
		b = c1()
# End  of  class
a = c1()






#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  _init_(self):
        print('Constructor') # Constructor
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method') # Method
        self . x = 30
        self . y = 40
a = c1()
print(a . __dict__) # {'x': 10, 'y': 20}
b = c2()
print(b . __dict__) # {'x': 30, 'y': 40}
b . init()
print(b . __dict__) # {'x': 30, 'y': 40}


'''
Object  'a'  --->  

Object  'b'  ---> 
'''









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
print(x . _dict_) # {'a': 10}
x . m1()
print(x . _dict_)  # {'a': 10, 'b': 20}
f1() 
print(x . _dict_)   # {'a': 10, 'b': 20, 'c': 30}
x . d = 40
print(x . _dict_)   # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = c2()
y . m3()
print(x . _dict_)   # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
z = c1()
print(z . _dict_) # {'a': 10}


'''
object  'x'  --->  {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

object  'z'  ---> {'a': 10}

object  'y'  ---> {}
'''








# Find  outputs  (Home  work)
class   c1:
	def   _init_(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . _dict_) # {'x': 10, 'y': 20, 'z': 30}
print(b . _dict_) # {'x': 10, 'y': 20, 'z': 30}
del  a . x
del  b . y
print(a . _dict_)  # {'y': 20, 'z': 30}
print(b . _dict_) # {'x': 10, 'z': 30}
print(a . x)
print(b . y)


'''
Object  'a'   --->  {'y': 20, 'z': 30}

Object  'b'   --->  {'x': 10, 'z': 30}
'''








#  Find  outputs (Home  work)
class   c1:
	def  _init_(self): # discarded
		print('1st  constructor')
	def  _init_(self): # discarded
		print('2nd  constructor')
	def  _init_(self): # Recognised
		print('3rd  constructor') # 3rd  constructor
# End  of  the  class
a = c1()










#  Find  outputs  (Home  work)
class   c1:
	def  _init_(self): # 
		print('No  argument  constructor')
	def  _init_(self , x): # 
		print('single  argument  constructor : ' , x)
	def  _init_(self , x , y):
		print('Two  argument  constructor : ' , x , y)  # Two argument constructor :  10 20
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()








#  Find  outputs
class   c1:
	def  _init_(self):
		print('No  argument  constructor')
	def  _init_(self , x):
		print('single  argument  constructor : ' , x)  # Two argument constructor :  30 200
	def  _init_(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)  # Two argument constructor :  10 20
                                                           # Two argument constructor :  100 200
# End  of  the  class
a = c1(10 , 20)
b = c1(30)
c = c1()









# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  _init_(self):
		print('Constructor') # Constructor
# End  of  the  class
a = f1()
print(a) # Type and Address










# Find  outputs (Home  work)
class    c1:
	def   _init_(self):
		print('Constructor')
def  c1():
	print('Function') # Function
#end of the  class
a = c1()
print(a) # type and Address










# Find outputs  (Home  work)
class    c1:
        def  _init_(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x) # Function
# End  of  class  c1
a = c1()
b = c1(25)
print(b) # Type and address







#  Save  the  program  in  prog9a.py  file
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9a')






#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b') # c1 class of prog9b
a = c1()





#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c') # c1 class of prog9a
from  prog9a  import  c1
a = c1()






#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
How  to  import  class  c1  from  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9d')
a = c1()         #How  to  create  c1  class  object  of  current  module
b = c1_prog9a()                 #How  to  create  c1  class  object  of  prog9a







'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''
How  to  import  prog9a
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9e')
a = c1()#How  to  create  c1  class  object  of  current  module
b = prog9a.c1()#How  to  create  c1  class  object  of  prog9a
