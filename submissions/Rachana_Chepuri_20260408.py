''' Repeat  prog5a  such  that  methods  are  called  in  a  different  way
1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)
2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from Rachana_Chepuri_20260407 import triangle
t = triangle() # How  to  create  triangle  object
triangle.get(t) # How  to  call  get()  method  in  another  way
triangle.test(t) # How  to  call  test()  method  in  another  way
print("Area t:", triangle.area(t)) # print('Area : ',  How  to  call  area()  method  in  another  way)
print("Perimeter t:", triangle.peri(t)) #print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

''' What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)'''
from Rachana_Chepuri_20260407 import Student  

if __name__ == "__main__":
    s = Student()
    print(s . __dict__)
    s . get()
    print(s . __dict__)
    s . compute()
    print(s . __dict__)
'''Repeat  student  program  for  'n'  students
1) import  student  class  defined in  prog9a  but  do  not  rewrite
2) Use  list  of  objects
'''
from Rachana_Chepuri_20260407 import Student  #from  prog9a  import  student
n=int(input("Enter no.:"))  # How  to  read  number  of  students  into   variable  'n'
a=[]# How  to  store  'n'  student  class  objects   in  list  'a'
for i in range(n):
    s=Student()
    a.append(s)# How  to   read  each  student  data  into   the  object  held  by  the  list
for i in range(n):
    a[i].get()
    a[i].compute()
    # How  to   store  results  in   each  object  held  by  the  list
for i in range(n):
    a[i].disp()# How  to   print  each  object  held  by  the  list
'''Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

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
import math

class Rat:
    def get(self):
        self.nr = int(input("Enter numerator: "))  # How  to  read  numerator  
        self.dr = int(input("Enter denominator: "))  # How  to  read  denominator 
        self.test()  # How  to  call  test()  method

    def test(self):
        while self.dr == 0:
            print('Denominator cannot be Zero.re enter dr')  # Ask  user  to  re enter  denom  when  denom  is  zero
            self.dr = int(input('Enter denominator:'))  # Ask  user  to  re enter  denom  when  denom  is  zero

    def __str__(self):
        return f"{self.nr} / {self.dr}"  # return  values  of  object  in  the form  of  rational  number  such   as  '2 / 3'

    def add(self, a, b):
        self.nr = a.nr * b.dr + a.dr * b.nr  # How  to  add  objects  'a'  and  'b' and  store  results  in  object  
        self.dr = a.dr * b.dr
        self.simplify()  # How  to  simplify  object  

    def sub(self, a, b):
        self.nr = a.nr * b.dr - a.dr * b.nr  # How  to  subtract  objects  'a'  and  'b' and  store  results  in  object 
        self.dr = a.dr * b.dr
        self.simplify()  # How  to  simplify  object  

    def mul(self, a, b):
        self.nr = a.nr * b.nr  # How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  
        self.dr = a.dr * b.dr
        self.simplify()  # How  to  simplify  object 

    def div(self, a, b):
        self.nr = a.nr * b.dr  # How  to  divide  objects  'a'  and  'b' and  store  results  in  object  
        self.dr = a.dr * b.nr
        self.simplify()  # How  to  simplify  object  

    def simplify(self):
        gcd = math.gcd(self.nr, self.dr)  # How  to  find  gcd  of  numerator  and   denominator
        self.nr //= gcd
        self.dr //= gcd  # How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5

# End  of the class
if __name__ == "__main__":
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()  # How  to  create  6  objects  a , b , c , d , e , f

a.get()  # How  to  read  rational  number  into  object  'a'
b.get()  # How to  read  rational  number  into  object  'b'

c.add(a, b)  # How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a, b)  # How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a, b)  # How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a, b)  # How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'

print("Sum :", c)  # How  to  print  object   'c'
print("Subtract:", d)  # How  to  print  object   'd'
print("Multiply:", e)  # How  to  print  object   'e'

if f.dr > 0:
    print("Division:", f)
else:
    print('Division  is  not  permitted')


'''dir()  function  demo  program  (Home  work)'''

if __name__ == "__main__":
    a = Rat()
    a . nr = 22
    a . dr = 7
    print(dir(Rat))
    print()
    print()
    print(dir(a))

''' Find  outputs  (Home  work)'''
class      Rat:
	def    m1():
		pass
# End  of  the  class
a = Rat()
a . nr = 22
print(hasattr(a , 'nr'))#True
print(hasattr(a , 'dr'))#False
print(hasattr(a , 'm1'))#True
print(hasattr(a , 'm2'))#False
print(hasattr(Rat , 'm1'))#True
print(hasattr(Rat , 'm2'))#False
print(hasattr(Rat , 'nr'))#False
'''Find  outputs  (Home  work)'''
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
'''output'''
# Meow Meow Meow 
# Bhow Bhow Bhow
# Mehar  Mehar  Mehar
'''Find  outputs  (Home  work)'''
class    c1:
        pass
# End of the class
a = c1()
a . x = 10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)
print(a . __dict__) #{'x':10,'y':20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
									#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break
'''(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0
Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
for key,value in dict.items():
        setattr(e,key,value)
for key in dict.keys():
    print(f"{key}:", getattr(e, key))   
    



