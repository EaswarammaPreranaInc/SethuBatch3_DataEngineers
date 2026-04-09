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


# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . _dict_)
s . get()
print(s . _dict_)
s . compute()
print(s . _dict_)


'''
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
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  1…
'''
import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.denom = int(input("Enter denominator: "))
        if self.denom == 0:
            print("Denominator cannot be zero")
            exit()

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.denom)
            self.num //= g
            self.denom //= g
        return self

    def add(self, a, b):
        r = Rat()
        r.num = (a.num * b.denom) + (b.num * a.denom)
        r.denom = (a.denom * b.denom)
        return r.simplify()

    def sub(self, a, b):
        r = Rat()
        r.num = (a.num * b.denom) - (b.num * a.denom)
        r.denom = (a.denom * b.denom)
        return r.simplify()

    def mul(self, a, b):
        r = Rat()
        r.num = (a.num * b.num)
        r.denom = (a.denom * b.denom)
        return r.simplify()

    def div(self, a, b):
        r = Rat()
        r.num = (a.num * b.denom)
        r.denom = (a.denom * b.num)
        return r.simplify()


# Main program
a = Rat()
b = Rat()

print("Enter 1st rational number:")
a.get()

print("Enter 2nd rational number:")
b.get()

c = Rat()

add = c.add(a, b)
sub = c.sub(a, b)
mul = c.mul(a, b)
div = c.div(a, b)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


#  dir()  function  demo  program  (Home  work)
from  prog10a   import  Rat
a = Rat()
a . nr = 22
a . dr = 7
print(dir(Rat)) #[m1]
print() 
print()
print(dir(a)) #[m1]

#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr')) #false
print(hasattr(a , 'dr')) #false
print(hasattr(a , 'm1')) #True
print(hasattr(a , 'm2')) #False
print(hasattr(Rat , 'm1')) #True
print(hasattr(Rat , 'm2')) #false
print(hasattr(Rat , 'nr')) #false



# Object  'a'  --->

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
'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....

'''

#  Find  outputs  (Home  work)
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . _dict_) #{x:10,y:20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname)) # 10 20
	except:
		print(F'Invalid  variable   name   :  {varname}') #invalid for z
		break


'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
e=Emp()
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
for key,value in dict.items():
    setattr(e,key,value)
for key in dict:
    print(f'e.{key}={getattr(e,key)}')