'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class


Modify  the  program  without  using  list
'''
import time

def words(s):
    word = ""
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if word != "":
                yield word
                word = ""
    
    if word != "":
        yield word

# End of generator

s = input('Enter any string: ')
g = words(s)

print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)


#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')
'''
Begin
It may have waiting time and memory error because of *g , where it stores values in generator
'''


#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)
'''
Again same it may have waiting time and it may raise memory error as all values stored in generator because of *g
'''


#  Find  outputs (Home  work)
def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()  #creates empty generator
for   m   in   g:
	print(m)
'''
One
1
Two
2
Three
3
End
'''
x ,  y ,  z  =  f1()  #x,y,z=1 2 3
print(x)  #1
print(y)  #2
print(z)  #3


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  # More values less references  
p , q , r , s , m = f1()  # More references less values



#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()  # Empty generator object
print(len(g))  # Error , because for len() the argument must be sequence.
print(g * 3)  # Error, because generator is empty,it cannot be repeated
print(g[0]) # Error, because generator is not indexed. 
print(g[1 : 3])  # Error as generator has no indexes, so there will be no slicing
print(*g)  #1 2 3


# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:  # Error , because the class should have either methods inside class or pass statement.


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()  # It creates an object for c1 class
print(id(a))  # Address of a is printed
print(type(a))  # <class '__main__.c1'>
print(a . __dict__)  #{}
print(a)  # Type and Address of a.
del  a  # It deletes object a.
print(a)  # Error , because you can not print the deleted object.


#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()  # It creates object for c1 class
a . m1()  # 3rd method
m1()  # Function m1 is called


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()  # It created object for c1 class.
a . m1(10 , 20)  # Two  argument  method :   10  20
a . m1(30)  # Error , because m1 method expects two arguments 
a . m1()  # Error, because m1 method expects two arguments, but no argument is sent to method


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)  # Two  argument  method :   10  20
a . m1(30)  # Two  argument  method :  30 2
a . m1()  # Two  argument  method : 1 2


# Find  outputs  (Home  work)
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
a . m1()  # Method  of  third  c1  class is called


# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()  # Error


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  # {}
a . x = 10
print(a . __dict__)  # {x: 10}
a . y = 20
print(a . __dict__)  # {x: 10, y:20}
a . x = 30
print(a . __dict__)  # {x: 30, y:20}
a . y = 40
print(a . __dict__)  # {x: 30, y:40}
del  a . x
print(a . __dict__)  # {y:20}
del  a . y
print(a . __dict__)  # {}
del   a
print(a . __dict__)  # Error