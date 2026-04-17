'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''

'''
from prog5a import triangle
a = triangle() #How  to  create  triangle  object
a.get()#How  to  call  get()  method  in  another  way
a.test()#How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(a) )  #How  to  call  area()  method  in  another  way
print('Perimeter: ',  triangle.peri(a)) #How  to  call  peri()  method  in  another  way
'''


'''
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
		self.n = int(input("Enter a numerator: ")) #How  to  read  numerator  
		self.d = int(input("Enter a denominator: ")) #How  to  read  denominator 
		self.test() #How  to  call  test()  method
	def  test(self):
		while self.d == 0:
			self.d = int(input("Re- Enter denominator: "))#Ask  user  to  reenter  denom  when  denom  is  zero
	def  __str__(self):
			 return  f"{self.n}/{self.d}"  #values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	
	def   add(self , a , b):
		self.n = (a.n * b.d) + (b.n * a.d) #How  to  add  objects  'a'  and  'b' and  store  results  in  object  
		self.d = (a.d * b.d)
		self.simplify() #How  to  simplify  object
          
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (3 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.n = (a.n *b.d) - (b.n * a.d) #How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
		self.d = (a.d * b.d) 
		self.simplify()#How  to  simplify  object  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (3 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.n = a.n * b.n#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
		self.d = a.d * b.d
		self.simplify()#How  to  simplify  object 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.n = a.n * b.d#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
		self.d = a.d * b.n
		self.simplify()#How  to  simplify  object 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		c=math.gcd(self.n,self.d)    #How  to  find  gcd  of  numerator  and   denominator
		self.n = self.n / c
		self.d = self.d / c	#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a = Rat()#How  to  create  6  objects  a , b , c , d , e , f
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a.get()#How  to  read  rational  number  into  object  'a'
b.get()#How to  read  rational  number  into  object  'b'
c.add(a,b)#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b)#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b)#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b)#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print(f"add : {c}")#How  to  print  object   'c'
print(f"sub : {d}")#How  to  print  object   'd'
print(f"mul : {e}")#How  to  print  object   'e'
print(f"div : {f}")

if  f.d!=0:
	print(f"division:{f}")#How  to  print  object  'f
else:
	print('Division  is  not  permitted')

'''

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_) # {}
s . get()
print(s . _dict_) # {'rno' : 25 , 'sname' : 'Rama Rao' , 'gender' : 'male' , 'm' : [52,48,55]}
s . compute()
print(s . _dict_) # {'rno' : 25 , 'sname' : 'Rama Rao' , 'gender' : 'male' , 'm' : [52,48,55] , 'tot' : 155 , 'avg' : 51.67 , 'grade' : 'Second class'}

'''
'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''

'''
from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list
'''
'''
from  prog9a  import  Student
n = int(input("How many students ? : "))
a = []
for i in range(n):
    print(f"Student {i+1}")
    s = Student()
    s.get()
    a.append(s) 
    a[i].compute()
for i in range(n):
    print(a[i])
'''


'''
#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) # ['add' , 'sub' , 'mul' , 'div']
print()
print()
print(dir(a)) # ['nr' , 'dr', 'add' , 'sub' , 'mul' , 'div']

#  Find  outputs  (Home  work)
class      Rat:
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
print(hasattr(Rat , 'm2')) # False
print(hasattr(Rat , 'nr')) # False

# Object  'a'  ---> nr = 22

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
		
		
Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''



'''
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1() # Object of class c1 is created
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value) # Adds variable y to the object a with a value 20
print(a . _dict_)
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
					#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
 Output:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{ 'x' : 10 , 'y' : 20}
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z
'''

'''
'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
'''
# Code :
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp()
for i in dict:
    setattr(e,i,dict[i])
for i in dict:
    print(getattr(e,i))

Output:
25
Rama  Rao
10000.0
'''
