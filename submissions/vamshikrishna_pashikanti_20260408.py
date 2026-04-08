Name-Dhruva Gupta
Roll Number-D238

1)
import OOPS
t = OOPS.Triangle()
OOPS.Triangle.get(t)
OOPS.Triangle.test(t)
print("Area:", OOPS.Triangle.area(t))
print("Perimeter:", OOPS.Triangle.peri(t))

2)
# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)

Output-
{}
{'age': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
{'age': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55, 'total': 155, 'avg': 51.67}

3)
from OOPS import Student 
n = int(input("Enter number of students: "))
a = []
for i in range(n):
    print(f"\nEnter details of student {i+1}")
    s = Student()
    s.get()
    a.append(s)
for s in a:
    s.compute()
print("\n--- Student Details ---")
for s in a:
    print(s)  

4)
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



# Object  'a'  —>


Output-
True
False
True
False
True
False
False

5)
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

Output-
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ….

6)
#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
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

Output-
{'x': 10, 'y': 20}
10
10
20
Invalid variable name : z
