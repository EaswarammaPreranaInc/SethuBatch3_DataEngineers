 
from functions import Triangle

# Create object
a=float(input("Enter the value: "))
b=float(input("Enter the value: "))
c=float(input("Enter the value: "))

t=Triangle(a,b,c)

# Call methods using ClassName.method(object)
if Triangle.is_valid(t):   # instead of t.is_valid()
    
    print("Area :", Triangle.area(t))          # instead of t.area()
    print("Perimeter :", Triangle.perimeter(t))  # instead of t.perimeter()

else:
    print("Not a triangle")




# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)	#{'roll': 55, 'name': 'likku', 'gender': 'f', 'm1': 45, 'm2': 90, 'm3': 95}
s . compute()
print(s . __dict__)	#{'roll': 55, 'name': 'likku', 'gender': 'f', 'm1': 45, 'm2': 90, 'm3': 95, 'total': 230, 'avg': 76.6, 'grade': 'Distinction'}





#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat))
print()
print()
print(dir(a))





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
		x . talk()	#Meow Meow Meow .... <next> Bhow Bhow Bhow ....  <next>  Mehar  Mehar  Mehar  ....
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
print(a . __dict__)	#{'x': 10, 'a': 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')	#a
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))	#20
	except:
		print(F'Invalid  variable   name   :  {varname}')	#Invalid variable name : c
		break






