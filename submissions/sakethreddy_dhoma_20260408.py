
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
# prog5a.py 
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  
		self.a = float(input("Enter first side : "))
		self.b = float(input("Enter second side : "))
		self.c = float(input("Enter third side : "))
	def  test(self):
		if  self.a + self.b >= self.c and self.a + self.c >= self.b and self.b + self.c >= self.a:
			return
		else:
			print('Not  a  triangle')
			exit() #How  to  stop  execution
	def  area(self):
		s = ((self.a + self.b + self.c)/2)
		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
		return  self.a + self.b + self.c
# End of the class
if __name__ == '__main__':
	t = triangle()
	t.get()#How  to  read  inputs  into  object
	t.test()#How  to  test  whether  inputs  are  valid
	print('Area : ',   t.area())
	print('Perimeter : ',  t.peri())

# prog5b.py
from prog5a import * 
a = triangle()
triangle.get(a)
triangle.test(a)
print('Area : ',   triangle.area(a))
print('Perimeter : ',  triangle.peri(a))

''' Output:
Enter first side : 3
Enter second side : 4
Enter third side : 5
Area :  6.0
Perimeter :  12.0
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
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
# prog9a.py
class Student:
	def get(self):
		self.rno = int(input("Enter roll number : "))
		self.sname = input("Enter student name : ")
		self.gender = input("Enter gender(m/f) : ")
		self.marks = []
		for i in range(3):
			m = int(input(f"Enter marks of subject {i+1} : "))
			self.marks.append(m)

	def compute(self):
		self.tot = sum(self.marks)  # How to calculate total marks
		self.avg = round(sum(self.marks) / 3, 2)  # How to calculate average marks
		if self.marks[0] < 40 or self.marks[1] < 40 or self.marks[2] < 40:
			self.grade = 'Fail'
		elif self.avg >= 70:
			self.grade = 'Distinction'
		elif self.avg >= 60:
			self.grade = 'First class'
		elif self.avg >= 50:
			self.grade = 'Second class'
		else:
			self.grade = 'Third class'

	def disp(self):
		print('Roll Number : ', self.rno)
		print('Student Name : ', self.sname)
		print('Gender : ', self.gender)
		print('Total Marks : ', self.tot)
		print('Average : ', self.avg)
		print('Grade : ', self.grade)

	def __str__(self):
		return f"{self.rno} {self.sname} {self.gender} {self.tot} {self.avg} {self.grade} "

# End of the class
if __name__ == '__main__':  
    s = Student()  
    s.get()  
    s.compute()  
    s.disp()  
    print(s)

# prog9b.py
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

''' Output:
How many students ? : 4
Student 1
Enter roll number : 111
Enter student name : Rama Rao
Enter gender(m/f) : m
Enter marks of subject 1 : 52
Enter marks of subject 2 : 48
Enter marks of subject 3 : 55
Student 2
Enter roll number : 222
Enter student name : Sita
Enter gender(m/f) : f
Enter marks of subject 1 : 100
Enter marks of subject 2 : 100
Enter marks of subject 3 : 0
Student 3
Enter roll number : 333
Enter student name : Ravi
Enter gender(m/f) : m
Enter marks of subject 1 : 60
Enter marks of subject 2 : 65
Enter marks of subject 3 : 60
Student 4
Enter roll number : 444
Enter student name : Vamshi
Enter gender(m/f) : m
Enter marks of subject 1 : 78
Enter marks of subject 2 : 87
Enter marks of subject 3 : 98
111	Rama Rao	m	155 	51.67	Second class 
222	Sita		f	200	66.67	Fail
333 	Ravi 		m 	185 	61.67 	First class
444 	Vamshi 		m 	263 	87.67 	Distinction
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
	def get(self):
		self.nr = int(input("Enter numerator : "))
		self.dr = int(input("Enter denominator : "))
		self.test()
	def test(self):
		if self.dr == 0 :
			self.dr = int(input("Re-enter denominator other than zero : "))
	def  __str__(self):
		return  F"{self.nr} / {self.dr}"
	def  add(self , a , b):
		self.nr = (a.nr * b.dr ) + (b.nr * a.dr)
		self.dr = a.dr * b.dr
		self.simplify() 
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self.nr = (a.nr * b.dr ) - (b.nr * a.dr)
		self.dr = a.dr * b.dr
		self.simplify()  
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.nr = a.nr * b.nr
		self.dr = a.dr * b.dr
		self.simplify() 
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self.nr = a.nr * b.dr
		self.dr = a.dr * b.nr
		self.simplify() 
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if self.nr !=0:
			res = math.gcd(self.nr,self.dr)
			self.nr = self.nr // res
			self.dr = self.dr // res
		
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a.get()
b.get()
c.add(a,b)
d.sub(a,b)
e.mul(a,b)
f.div(a,b)
print(f"Sum :  {c}")
print(f"Difference :  {d}")
print(f"Product :  {e}")
if  f.dr != 0:
	print(f"Division :  {f}")
else:
	print('Division  is  not  permitted')


'''
Object  'a'  --->  nr = 2 , dr = 3

Object  'b'  --->  nr = 5 , dr = 9

Object  'c'  --->  nr = 11 , dr = 9

Object  'd'  --->  nr = 1 , dr = 9

Object  'e'  --->  nr = 10 , dr = 27

Object  'f'  --->  nr = 6 , dr = 5
'''

''' Output:
Enter numerator : 2
Enter denominator : 3
Enter numerator : 5
Enter denominator : 9
Sum :  11 / 9
Difference :  1 / 9
Product :  10 / 27
Division :  6 / 5

Enter numerator : 2
Enter denominator : 3
Enter numerator : 0
Enter denominator : 9
Sum :  2 / 3
Difference :  2 / 3
Product :  0 / 27
Division  is  not  permitted
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

''' Output:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
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
''' Output:
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
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
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

''' Output:
25
Rama  Rao
10000.0
'''

# Module - 3
#  How  to  reuse  mod1  ?  (Home  work)
# mod1 . py
print('Hyd')
print('Sec')
print('Cyb')
x = 25
def  f1():
	print('Function')
class   c1:
	def   m1(self):
			print('Method')

'''
print('Hello')
import mod1
print(mod1.x)
mod1.f1()
a = mod1.c1()
a.m1()
print('Bye')
import  mod4 # Module Not Found error
# print(x) # Error because there is no variable x in current module
# f1() # Error because there is no f1() function in current module

''' Output:
Hello
Hyd
Sec
Cyb
25
Function
Method
Bye