# Multilevel  inheritance  demo  program
class  A:
	def    m1(self):
		print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		print('class   D   method')
		C.m1(d)       #How  to  call  method  m1()  of  class  C  without  creating  another  object
		How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() 
		super(C) . m1()   
		super(D , D) . m1()  
# End  of  the  class
d = D()         #How  to  call  method  m1()  of  class  D


----------------------------------------------------------------------------


# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')  # Father Height
class  mother:
        def  color(self):
                print('Mother  Color') # Mother Color
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification') # Child Qualification
# End  of  the  class
c  =  child()
c . qualification()
c . color()
c . height()
c . m1()

-----------------------------------------------------------------------------


#  Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
        def  m1(self):
                print('Child  Method') # Child Method
# End  of  the  class
c = child()
c . m1()

------------------------------------------------------------------------------

# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method') 
class  father:
        def  m1(self):
                print('Father  Method') # Father Method
class  child(father , mother , uncle):
	pass
# End  of  the  class
c = child()
c . m1()




# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method') # Mother Method
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()



# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method') # Uncle Method
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()



# Find  outputs
class  uncle:
        pass
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1() # error



# Identify  Error
class  c1(c1): ## 'c1' is not defined
	     pass
         
         
         
         
# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()



# Identify  Error
class   c1(c2): # 'c2' is not defined
	pass
class  c2(c1):
	pass
    
    
    
    
# Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')
class   c1(c2):
	def  m1(self):
			super() . m1()
			print('Child  Method')
class  c2(c1):
	def  m1(self):
			super() . m1()
			print('Grand  Child  Method')
a = c2()
a . m1()





# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')




# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		print('child   constructor')
	def   __del__(self):
		print('child  destructor')
# End of the class
c = child()
print('Bye')




# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')





# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')





# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()




# Find outputs  (Home  work)
class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
		How  to  print  static  variable  'x'
		How  to  print  static  variable  'x'   in  another  way
		How  to  print  static  variable  'x'   in  one  more  way
		How  to  print  variable  'x'  of  object  'c'
		How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
How  to  call  disp()  method  of   child  class





# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20
class   child(parent):
	def  __init__(self):
		self . x = 30
		print(self . x)   
		super() . __init__()
	def  disp(self):
		print(self . x)    
		print(super() . x) 
# End of the class
c = child()
c . disp()


'''
static   variable  --->  

Object  'c'  --->  
'''




# Find outputs
class    parent:
	How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,  How  to  print  static  variable  'a'  in  another  way)
		print(self . a)  
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  How  to  print  static  variable  'a')
	def   __del__(self):
		print('parent  destructor  :  ' ,  How  to  print  variable  'x')
class  child(parent):
	How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		How  to  call  parent  class  constructor
		print('Child  constructor')
		How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method' , How  to  print  variable  'y')
	@classmethod
	def   m2(cls):
		How  to  call  m2()  method  of  parent  class
		How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  another  object
		cls . m2()  
		self . m2() 
		print('Child  class  "class"  method')
		print(How  to  print  static  variable  'a')
		print(How  to  print  static  variable  'a'  in  another  way)
		print(How  to  print  static  variable  'a'  in  one  more  way)
		print(How  to  print  static  variable  'a'  in  last  way)
		print(How  to  print  static  variable  'b')
		print(How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		How  to  call  m3()  method  of  parent  class
		How  to  call  m3()  method  of  parent  class  in   another  way
		super() . m3()  
		self . m3() 
		cls . m3()  
		print('child  class  static  method' ,  How  to  print  static  variable  'a')
		print(How  to  print  static  variable  'a'  in  another  way)
		print(How  to  print  static  variable  'b')
	def __del__(self):
		How  to  call  destructor  of  parent  class
		print('child  destructor' ,  How  to  print  variable  'y')
#end of the class
How  to  call  m2()  method  of  child  class
How  to  call  m3()  method  of  child  class
How  to  call  m1()  method  of  child  class




# Find  outputs
class   father:
	def  m1(self):
		print('m1  method  of  Father  class')
class   mother:
	def  m1(self):
		print('m1  method  of  Mother  class')
class   uncle:
	def  m1(self):
		print('m1  method  of  Uncle  class')
class   child(father , mother , uncle):
	def  m1(self):
		print('m1  method  of  child  class')
		How  to  call  m1()  method  of  father  class  without  creating  another  object
		How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  mother  class   without  creating  an  object
		How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() 
# End of the class
print(child . __mro__)  
How  to  call  m1()  method  of  child  class
print('Bye')




# Find outputs  (Home  work)
class  A:
	def  m1(self):
		super() . m1() 
		print('class A method')    
class  B:
	def m1(self):
		super() . m1()  
		print('class B method') 
class  C:
	def m1(self):
		super() . m1() 
		print('class C method') 
class  D:
	def m1(self):
		super() . m1()  
		print('class D method')  
class  X(A , B):
        def m1(self):
                super() . m1()  
                print('class X method') 
class  Y(B , C , D):
        def m1(self):
                super() . m1()  
                print('class Y method') 
class  P(X , Y , C):
        def m1(self):
                super() . m1() 
                print('class P method') 
# End  of  the  class
print(P . mro())   
obj = P()
obj . m1()
print('Bye')





# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()  
                print('class D constructor') 
class  E:
        def __init__(self):
                super() . __init__()  
                print('class E constructor') 
class  F:
        def __init__(self):
                super() . __init__()  
                print('class F constructor')  
class  B(D , E):
        def __init__(self):
                super() . __init__()  
                print('class B constructor')  
class  C(D , E , F):
        def __init__(self):
                super() . __init__()  
                print('class C constructor')  
class  A(B , C):
        def __init__(self):
                super() . __init__()  
                print('class A constructor') 
# End  of  the  class
print(A . mro())  
obj = A()
print('Bye')