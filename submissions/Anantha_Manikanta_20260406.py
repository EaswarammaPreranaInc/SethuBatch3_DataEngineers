'''
1) Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class

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
'''

import time
def words(s):
    word = ''
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if word != '':
                yield word
                word = ''
    if word != '':
        yield word
s = input('Enter any string : ')
g = words(s)
print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)
'''
2) #  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')  # Begin
print(*g)  # 1 2 3 4 5 6 7 8 ... 100000000000000000000
print('End')  # End
'''
'''
3) g = (x * x for x in range(500000000000000000))
print(*g)   # 0 1 4 9 16 25 36 ...... up to last value
'''
'''
4) #  Find  outputs (Home  work)
def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
'''
'''
5) #  Find  outputs (Home  work)
def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)  #  One <nextline> 1 <nextline> Two <nextline> 2 <nextline> Three <nextline> 3 <nextline> End
x ,  y ,  z  =  f1()  # One <nextline> Two <nextline> Three <nextline> End
print(x)  # 1
print(y)  # 2
print(z)  # 3
'''
'''
6) def f1():
    yield 10
    yield 20
    yield 30
    yield 40
a, b, c = f1()  # Error because there are 4 yields but only 3 objects are assigned
p, q, r, s, m = f1()  # Error because there are 4 yields but 5 objects are assigned
'''
'''
7) #  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  # Error
print(g * 3)  # Error
print(g[0])  # Error
print(g[1 : 3])  # Error
print(*g)  # 1 2 3
'''
'''
8) # Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:  # Error because empty class is not allowed if there are no statements pass should be defined in class
'''
'''
9) # Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))  # 1AD342
print(type(a))  # <class '__main__.c1'>
print(a . __dict__)  # {}
print(a)  # <__main__.c1 at 123>
del  a
print(a)  # Error because 'a' is not defined because the created 'a' was deleted
'''
'''
10) #  Find  outputs  (Home  work)
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
a = c1()
a . m1()  # 3rd Method
m1()  # Function
'''
'''
10) #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)  # Two  argument  method :  10 20
a . m1(30)  # Error because 1 argument is missing
a . m1()  # Error because 2 arguments are missing
'''
'''
11) #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)  # Two  argument  method :  10 20
a . m1(30)  # Two  argument  method :  30 2
a . m1()  # Two  argument  method :  1 2
'''
'''
12) # Find  outputs  (Home  work)
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
a . m1()  # Method  of  third  c1  class
'''
'''
13) # Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()  # Error c1 has no method m1 and its empty
'''
'''
14) #  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  # {}
a . x = 10
print(a . __dict__)  # {'x':10}
a . y = 20
print(a . __dict__)  # {'x':10,'y':20}
a . x = 30
print(a . __dict__)  # {'x':30,'y':20}
a . y = 40
print(a . __dict__)  # {'x':30,'y':40}
del  a . x
print(a . __dict__)  # {'y': 40}
del  a . y
print(a . __dict__)  # {}
del   a
print(a . __dict__)  # Error because 'a' is not defined the previously created dictionary is deleted
'''