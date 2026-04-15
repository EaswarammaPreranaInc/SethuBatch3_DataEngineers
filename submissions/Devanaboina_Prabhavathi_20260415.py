'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 																							
39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		How  to  read  real  and  imag
	def    __str__(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		How  to  add  objects  a  and  b
	def  __sub__(a ,  b):
		How  to  subtract  objects  a  and  b
	def  __mul__(a ,  b):
		How  to  multiply  objects  a  and   b
	def  __truediv__(a ,  b):
		How  to  divide  objects   a  and  b
# End  of  the  class
How  to  create  two  complex  class  objects # c1 = complex()  c2 = complex()
How  to  read   inputs  into  1st  object # c1.get
How  to  read   inputs  into  2nd  object # c2.get
print('Sum :  ' , c1 + c2)
print('Difference :  ' , c1 - c2)
print('Product :  ' , c1 * c2)
print('Division  : ' , c1 / c2)



# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor') # outer class constructor
	def  m1(self):
		print('Outer  class  method') # outer class method
	class   inner:
		def __init__(self):
			print('Inner  class  constructor') # Inner class constructor
		def m1(self):
			print('Inner  class  method') # Inner class method
#end of the class
How  to  call  m1()  method  of  outer  class # o.m1()
How  to  call  m1()  method  of  inner  class # i.m1()
How  to  call  m1()  method  of  inner  class  in  another  way
How  to  call  m1()  method  of  inner  class  in  one  more  way # outer.inner().m1()
i = inner()



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		How  to  create  date  class  object
	def   disp(self):
		How  to  print  empno , ename , sal  of  object  self
		How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
How  to  call  disp()  method  of  emp  class


  
class emp:
    def __init__(self):
        # initialize emp details
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0

        # create date class object
        self.d = emp.date()

    def disp(self):
        # print emp details
        print("Emp No :", self.empno)
        print("Emp Name :", self.ename)
        print("Salary :", self.sal)

        # call date class method
        self.d.disp()

    class date:
        def __init__(self):
            # initialize date values
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            # print date values
            print("Date :", self.dd, "-", self.mm, "-", self.yy)



           
# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		How  to  initialize  variable  'x'  of  object  self  to  25 # self x = 25
		How  to  create  inner1  class  object #  self.i1 = outer.inner1()
		How  to  create  inner2  class  object # self.i2 = outer.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method') # 1st inner class method
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method') # 2nd inner class method
#end of the class
How  to  call   disp()  method  of outer  class # o.disp()
How  to  call   disp()  method  of inner1  class  # o.i1.disp()
How  to  call   disp()  method  of inner2  class  # o.i2.disp()



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
How  to  create  c1  class  object # object=c1()
How  to  create  inner  c2  class  object # i=c1.c2()
How  to  create  outer  c2  class  object # o2=c2()
        



# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object # o = c2()
How  to  create  inner  c2  class  object # i = c2.c2()
How  to  create  inner  c2  class  object  in  another  way  #i=o.c2()
How  to  create  inner  c2  class  object  in  one  more  way # i = c2().c2()