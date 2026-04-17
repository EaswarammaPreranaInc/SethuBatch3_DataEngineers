 ''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   words(s):
	list = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	for  x  in  list:
		yield  x
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)

Modify  the  program  without  using  list
--------------------------------------------------------------------------------------------------
 #  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x               #Begin
		x +=  1                #1,2,3,..........,100000000000000000000
# End of  generator                    #End
g = f1()
print('Begin')
print(*g)
print('End')
--------------------------------------------------------------------------------------------------
 #  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)       #error
------------------------------------------------------------------------------------------------
 #  Find  outputs (Home  work)
def  f1():
	print('One')            #one
	yield    1              #1
	print('Two')            #Two
	yield    2              #2
	print('Three')          #Three
	yield    3              #3
	print('End')            #End
# End  of  generator            #1
g = f1()                        #2
for   m   in   g:               #3
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
------------------------------------------------------------------------------------------------
 # Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()   #10 20 30 
p , q , r , s , m = f1() #error
--------------------------------------------------------------------------------------------
 #  Find  outputs (Home  work)
def   f1():
	yield    1          #
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  #error
print(g * 3)   #error 
print(g[0])    #1 
print(g[1 : 3]) #1 2
print(*g)       #1,2,3
------------------------------------------------------------------------------------------
 # Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:  #error
--------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))   #add of a
print(type(a))   #<class'c1'>
print(a . _dict_) #instance variables are in dict{v:v1,v:v2...}
print(a) #type and add
del  a   #obj a is deleted
print(a) #error
-------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
def   m1():                                #Function
		print('Function')          #1st method
class   c1:                                #2nd method
	def   m1(self):                    #3rd method
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1()
m1()
---------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)                             #No argument method
class   c1:
	def   m1(self):                                     #Two argument method:10,20
		print('No  argument  method')               #Single argument method:30
	def   m1(self , x):                                 #No argument method
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()
----------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')                #Two argument method:10,20
	def   m1(self , x):                                  #Single argument method:30
		print('Single  argument  method : ' , x)     #No argument method
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()
-------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):                               
		print('Method  of  first  c1  class')   #Method of third c1 class
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()
--------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')         #Nothing is printed
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()
-----------------------------------------------------------------------------------------
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)           #
a . x = 10
print(a . _dict_)
a . y = 20
print(a . _dict_)
a . x = 30
print(a . _dict_)
a . y = 40
print(a . _dict_)
del  a . x
print(a . _dict_)
del  a . y
print(a . _dict_)
del   a
print(a . _dict_)