1) Write  a  generator  to  divide  a  string  into  words

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
#import time

def words(s):
    for x in s.split():   
        yield x

s = input('Enter any string: ')
g = words(s)  

print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)

2) outputs 
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
print(*g)#Empty
print('End')#End

3) outputs  
g = (x * x  for  x  in  range(500000000000000000))
print(*g)#Empty

4) outputs 
def  f1():
	print('One')#One
	yield    1 #1
	print('Two')#Two
	yield    2 #2
	print('Three')#Three
	yield    3 #3
	print('End')#End
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)#1
print(y)#2
print(z)#3

5) Identify  error 
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  
p , q , r , s , m = f1()#More than expected values

6) outputs 
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))#Error because no len in generator
print(g * 3)  #Error because it is not permitted
print(g[0])  #Error because it is not permitted
print(g[1 : 3])#Error because it is not permitted
print(*g)#1 2 3

7) Identify  error 
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#No Object is provided nor pass

8) outputs  
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#id of object a
print(type(a))#<class '__main__.c1'>
print(a . _dict_)#Error because it is not valid
print(a)#Type and address
del  a
print(a)#Error because it is empty

9) outputs 
def   m1():
		print('Function')#Function
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')#3rd method
# End  of  class  c1
a = c1()
a . m1()
m1()

10) outputs
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)#Two argument method : 10 20 
# End  of  class  c1
a = c1()
a . m1(10 , 20)#Two argument method : 10 20 
a . m1(30)#Error because only 1 arg
a . m1()#Error because no args

11) outputs  
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)#Two argument method : 10 20 
a . m1(30)#Two argument method : 30 2
a . m1()#Two argument method : 1 2

12) outputs  
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()#Method of third c1 class

13) outputs  
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()#Error because there is no method m1

14) outputs 
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)#{}
a . x = 10
print(a . _dict_)#{x : 10}
a . y = 20
print(a . _dict_)#{'x': 10, 'y': 20}
a . x = 30
print(a . _dict_)#{'x': 30, 'y': 20}
a . y = 40
print(a . _dict_)#{'x': 30, 'y': 40}
del  a . x
print(a . _dict_)#{'y': 40}
del  a . y
print(a . _dict_)#{}
del   a
print(a . _dict_)#Error because it is deleted