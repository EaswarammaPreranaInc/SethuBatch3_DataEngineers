# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
a = outer()
a.m1()           # How  to  call  m1()  method  of  outer  class
a.inner().m1()   # How  to  call  m1()  method  of  inner  class
b = a.m1()       # How  to  call  m1()  method  of  inner  class  in  another  way
# How  to  call  m1()  method  of  inner  class  in  one  more  way
# i = inner()     # error , becoz inner is inner class object. so, cannot call inner object without outer class object

#=============================================================================================================================

# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25     # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		a = emp.date()        # How  to  create  date  class  object
	def   disp(self):
		print(self.empno , self.ename , self.sal)   # How  to  print  empno , ename , sal  of  object  self
		a.date().disp()        # How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd = 15 # How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.mm = 8
			self.yy = 1947
		def disp(self):
			print(self.dd,self.mm,self.yy)# How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
a = emp()   # How  to  call  disp()  method  of  emp  class
a.disp()

# Object  'e'  --->  25  Rama Rao  10000.0
                  #  15  8  1947
				  
#======================================================================================================================

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		a = outer.inner1()  # How  to  create  inner1  class  object
		a = outer.inner2()  #How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a = outer()
a.disp()          # How  to  call   disp()  method  of outer  class
a.inner1().disp() # How  to  call   disp()  method  of inner1  class
a.inner2().disp() # How  to  call   disp()  method  of inner2  class


# Object  'o'  ---> 25 

#======================================================================================================================

# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a = c1()    # How  to  create  c1  class  object
a.c2()      # How  to  create  inner  c2  class  object
b = c2()    # How  to  create  outer  c2  class  object

#======================================================================================================================

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2()    # How  to  create  outer  c2  class  object
a.c2()      # How  to  create  inner  c2  class  object
b = a.c2()  # How  to  create  inner  c2  class  object  in  another  way
            # How  to  create  inner  c2  class  object  in  one  more  way

