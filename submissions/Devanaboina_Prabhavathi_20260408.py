'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)


from Devanaboina_Prabhavathi_20260407 import triangle
a = triangle()
a.get()
a.test()
print('Area:',a.area())
print('Perimeter:',a.peri())




# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__) # {}
s . get()  # 
print(s . __dict__) # 'sno': 25, 'name': 'Rama Rao','gender': 'male','m1': 52,'m2': 48,'m3': 55,
s . compute()
print(s . __dict__) 
# {
 'sno': 25,
 'name': 'Rama Rao',
 'gender': 'male',
 'm1': 52,
 'm2': 48,
 'm3': 55,
 'total': 155,
 'avg': 51.666666666666664
}

   

#  dir()  function  demo  program  (Home  work)
from  Devanaboina_Prabhavathi_20260407   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a)) # error



#  Find  outputs  (Home  work)
class   Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) ##  Find  outputs  (Home  work)
class   Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) # True
print(hasattr(a , 'dr')) # False
print(hasattr(a , 'm1')) # True
print(hasattr(a , 'm2')) # False
print(hasattr(Rat , 'm1')) # True
print(hasattr(Rat , 'm2'))# False
print(hasattr(Rat , 'nr')) # False

# Object  'a'  --->



# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....') # Meow Meow Meow
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....') # Bhow Bhow Bhow
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....') # Mehar  Mehar  Mehar
#end of the class
a = [Cat() , Dog() , Goat()]  
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk() # talk
	else:
		x . bark()
		


#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) #{'x'=10 , 'y'= 20}
print(a . x) # 10 10 20
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
	



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
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop
	

class Emp:
    pass
# End of the class

d = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# Convert dictionary to object
e = Emp()
for key, value in d.items():
    setattr(e, key, value)

# Print object data
for key in d:
    print(key, "=", getattr(e, key))