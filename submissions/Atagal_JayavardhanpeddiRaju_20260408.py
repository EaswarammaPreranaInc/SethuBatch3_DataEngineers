1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

t = Triangle()  

Triangle.get(t)
Triangle.test(t)

print("Area :", Triangle.area(t))
print("Perimeter :", Triangle.peri(t))

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

{'roll': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}


Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list

from prog9a import students
n = int(input("Enter number of students: "))

a = [student() for _ in range(n)]

for i in range(n):
    print(f"\nEnter data for student {i+1}:")
    a[i].get()

for i in range(n):
    a[i].compute()

for i in range(n):
    print(f"\nStudent {i+1} details:")
    print(a[i].__dict__)


Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division


num1 = int(input("Enter numerator of 1st fraction: "))
den1 = int(input("Enter denominator of 1st fraction: "))

num2 = int(input("Enter numerator of 2nd fraction: "))
den2 = int(input("Enter denominator of 2nd fraction: "))

add_num = num1 * den2 + num2 * den1
add_den = den1 * den2
print("Sum:", add_num, "/", add_den)

sub_num = num1 * den2 - num2 * den1
sub_den = den1 * den2
print("Difference:", sub_num, "/", sub_den)

mul_num = num1 * num2
mul_den = den1 * den2
print("Product:", mul_num, "/", mul_den)

div_num = num1 * den2
div_den = den1 * num2
print("Division:", div_num, "/", div_den, "---> Successful division")


Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 =  (18 + 15) / 27 = 33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 = 3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 = 2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  needed ?  --->  When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		How  to  read  numerator  
		How  to  read  denominator 
		How  to  call  test()  method
	def  test(self):
		Ask  user  to  reenter  denom  when  denom  is  zero
	def    _str_(self):
			 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object  
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			How  to  find  gcd  of  numerator  and   denominator
			How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
How  to  create  6  objects  a , b , c , d , e , f
How  to  read  rational  number  into  object  'a'
How to  read  rational  number  into  object  'b'
How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')


'''
Object  'a'  --->  

Object  'b'  --->  

Object  'c'  --->  

Object  'd'  --->  

Object  'e'  --->  

Object  'f'  --->  


from fractions import Fraction

num1 = int(input("Enter numerator of 1st fraction: "))
den1 = int(input("Enter denominator of 1st fraction: "))
num2 = int(input("Enter numerator of 2nd fraction: "))
den2 = int(input("Enter denominator of 2nd fraction: "))

a = Fraction(num1, den1)
b = Fraction(num2, den2)

c = a + b
d = a - b
e = a * b

if b.numerator != 0:
    f = a / b
    division_ok = True
else:
    division_ok = False

print("\nResults:")
print("Sum:       ", c)
print("Difference:", d)
print("Product:   ", e)
if division_ok:
    print("Division:  ", f, "---> Successful division")
else:
    print("Division is not permitted (division by zero)")


#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))

from prog10a import Rat 
a = Rat()
a.nr = 22  
a.dr = 7   

print("dir(Rat):")
print(dir(Rat))
print("\n")

print("dir(a):")
print(dir(a))


#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))  #True
print(hasattr(a , 'dr'))  #False
print(hasattr(a , 'm1'))  #True
print(hasattr(a , 'm2'))  #False
print(hasattr(Rat , 'm1')) #True
print(hasattr(Rat , 'm2')) #False
print(hasattr(Rat , 'nr')) #False


# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....') #Meow Meow Meow ....
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....') #Bhow Bhow Bhow ....
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....') #Mehar  Mehar  Mehar  ....
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
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
print(a . __dict__)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))  {varname}') #{'x': 10, 'y': 10}
	except:
		print(F'Invalid  variable   name   :  {varname}') {'x': 10, 'y': 10}
		break


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

emp_dict = {}
emp_dict['Empno'] = int(input("Enter Empno: "))
emp_dict['Ename'] = input("Enter Ename: ")
emp_dict['Sal'] = float(input("Enter Sal: "))

e = Emp()
for key, value in emp_dict.items():
    setattr(e, key, value)
    
print("\nEmployee Details:")
for key in emp_dict:
    print(key, ":", getattr(e, key))





