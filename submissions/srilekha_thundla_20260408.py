'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way

1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again
'''
from srilekha_thundla_20260407 import triangle
 
t = triangle()
t.get()
t.test()

print('Area : ',  t.area())
print('Perimeter: ', t.peri())

# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  srilekha_thundla_20260407  import  student
s = student()
print(s . __dict__)
s . get()
print(s . __dict__)
s . compute()
print(s . __dict__)

'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
# from  srilekha_thundla_20260407  import  student
# How  to  read  number  of  students  into   variable  'n'
# How  to  store  'n'  student  class  objects   in  list  'a'
# How  to   read  each  student  data  into   the  object  held  by  the  list
# How  to   store  results  in   each  object  held  by  the  list
# How  to   print  each  object  held  by  the  list


#  dir()  function  demo  program  (Home  work)

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
# import  math
# class  Rat:
# 	def  get(self):
# 		self.numerator  = eval(input("Enter numerator value : "))
# 		self.denominator  = eval(input("Enter denominator value : "))
		
# 		# How  to  call  test()  method
# 		a.test()
# 	def  test(self):
# 		if self.denominatorc==0:
# 			self.denominator  = eval(input("Re-enter non zero value : "))
			
		# Ask  user  to  reenter  denom  when  denom  is  zero
	# def    __str__(self):
	# 		 return  values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	# def   add(self , a , b):
	# 	self.c = a.numerator+b.denominator 
	# '''
	# c . add(a , b)
	# object  a  --->  2 / 3
	# object  b  --->  5 / 9
	# object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	# '''
	# def   sub(self , a , b):
	#      self.d = a.numerator-b.denominator 
	# '''
	# d . sub(a , b)
	# object  a  --->  2 / 3
	# object  b  --->  5 / 9
	# object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	# '''
	# def   mul(self , a , b):
	# 	 self.e = a.numerator*b.denominator
	# '''
	# e . mul(a , b)
	# object  a  --->  2 / 3
	# object  b  --->  5 / 9
	# object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	# '''
	# def    div(self , a , b):
	# 	self.f = a.numerator/b.denominator
	# '''
	# f . div(a , b)
	# object  a  --->  2 / 3
	# object  b  --->  5 / 9
	# object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	# '''
	# # def   simplify(self):
	# # 		How  to  find  gcd  of  numerator  and   denominator
	# # 		How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	# '''
	# c . simplify()
	# 1)  12 / 15  --->  4 / 5
	# 2) 10 / 27   --->  10 / 27
	# 3) 0 / 27  --->   0 / 27
'''
# End  of the class

# How  to  read  rational  number  into  object  'a'
# How to  read  rational  number  into  object  'b'
# How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
# How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
# How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
# How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
How  to  print  object   'c'
How  to  print  object   'd'
How  to  print  object   'e'
if  ???
	How  to  print  object  'f
else:
	print('Division  is  not  permitted')

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
print(c.__str__())
'''
# Object  'a'  --->  

# Object  'b'  --->  

# Object  'c'  --->  

# Object  'd'  --->  

# Object  'e'  --->  

# Object  'f'  --->  

# import math

# class Rat:

#     def get(self):
#         self.numerator = int(input("Enter numerator value : "))
#         self.denominator = int(input("Enter denominator value : "))
#         self.test()

#     def test(self):
#         while self.denominator == 0:
#             print("Denominator cannot be zero")
#             self.denominator = int(input("Re-enter non zero value : "))

#     def __str__(self):
#         return str(self.numerator) + " / " + str(self.denominator)

#     def add(self, a, b):
#         self.numerator = a.numerator * b.denominator + b.numerator * a.denominator
#         self.denominator = a.denominator * b.denominator
#         self.simplify()

#     def sub(self, a, b):
#         self.numerator = a.numerator * b.denominator - b.numerator * a.denominator
#         self.denominator = a.denominator * b.denominator
#         self.simplify()

#     def mul(self, a, b):
#         self.numerator = a.numerator * b.numerator
#         self.denominator = a.denominator * b.denominator
#         if self.numerator != 0:
#             self.simplify()

#     def div(self, a, b):
#         if b.numerator == 0:
#             self.numerator = 0
#             self.denominator = 0
#         else:
#             self.numerator = a.numerator * b.denominator
#             self.denominator = a.denominator * b.numerator
#             self.simplify()

#     def simplify(self):
#         if self.numerator != 0:
#             gcd = math.gcd(self.numerator, self.denominator)
#             self.numerator = self.numerator // gcd
#             self.denominator = self.denominator // gcd


# # Objects
# a = Rat()
# b = Rat()
# c = Rat()
# d = Rat()
# e = Rat()
# f = Rat()

# # Input
# print("Enter 1st rational number")
# a.get()

# print("Enter 2nd rational number")
# b.get()

# # Operations
# c.add(a, b)
# d.sub(a, b)
# e.mul(a, b)
# f.div(a, b)

# # Output
# print("\nObject a --->", a)
# print("Object b --->", b)
# print("Sum (c) --->", c)
# print("Difference (d) --->", d)
# print("Product (e) --->", e)

# if b.numerator == 0:
#     print("Division is not permitted")
# else:
#     print("Division (f) --->", f)
#  dir()  function  demo  program  (Home  work)
# from  prog10a   import  Rat
# a = Rat()
# a . nr = 22
# a . dr = 7
# print(dir(Rat))
# print()
# print()
# print(dir(a))

#  Find  outputs  (Home  work)
# class      Rat:
# 	def    m1():
# 		pass
# # End  of  the  class
# a = Rat()
# a . nr = 22
# print(hasattr(a , 'nr'))#True
# print(hasattr(a , 'dr'))#False
# print(hasattr(a , 'm1'))#True
# print(hasattr(a , 'm2'))#False
# print(hasattr(Rat , 'm1'))#True
# print(hasattr(Rat , 'm2'))#False
# print(hasattr(Rat , 'nr'))#False



# Object  'a'  --->

# Find  outputs  (Home  work)
# class  Cat:
# 	def  talk(self):
# 		print('Meow Meow Meow ....')
# class  Dog:
# 	def  bark(self):
# 		print('Bhow Bhow Bhow ....')
# class  Goat:
# 	def  talk(self):
# 		print('Mehar  Mehar  Mehar  ....')
# #end of the class
# a = [Cat() , Dog() , Goat()]
# for  x  in   a:
# 	if   hasattr(x , 'talk'):
# 		x . talk()#1.Meow Meow Meow .... #3.Mehar  Mehar  Mehar  ....
# 	else:
# 		x . bark() #2. Bhow Bhow Bhow ....


'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
# class  Emp:
#         pass
# #End  of  the  class
# dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
