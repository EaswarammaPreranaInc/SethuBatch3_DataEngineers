'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from vishalnagatej_20260407 import triangle

a = triangle() # How  to  create  triangle  object
a.get()         # How  to  call  get()  method  in  another  way
a.test()        # How  to  call  test()  method  in  another  way
print('Area : ',  a.area())
print('Perimeter: ',  a.peri())

#=============================================================================================================================

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  vishalnagatej_20260407  import  Student
s = Student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)

# {'rollno': 1, 'sname': 'vishal', 'gender': 'm', 'm': [25, 58, 48]}
# {'rollno': 1, 'sname': 'vishal', 'gender': 'm', 'm': [25, 58, 48], 'total_marks': 131, 'average': 65.5, 'grade': 'Fail'}

#=============================================================================================================================

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))
print(hasattr(a , 'dr'))
print(hasattr(a , 'm1'))
print(hasattr(a , 'm2'))
print(hasattr(Rat , 'm1'))
print(hasattr(Rat , 'm2'))
print(hasattr(Rat , 'nr'))

# Object  'a'  --->

# True
# False          # hasattr return True or False. based on class and method
# True
# False
# True
# False
# False

#=============================================================================================================================

#  dir()  function  demo  program  (Home  work)
# import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))  # methods of class
print()
print()
print(dir(a))	# true

# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

# Meow Meow Meow ....
# Bhow Bhow Bhow ....
# Mehar  Mehar  Mehar  ....

#=============================================================================================================================

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

# {'x' : 10 , 'y' : 20}
# 10

#=============================================================================================================================

'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
# How  to  convert  dictionary  to  object  'e'  with  for  loop
# How  to  print  object  'e'  with  for  loop