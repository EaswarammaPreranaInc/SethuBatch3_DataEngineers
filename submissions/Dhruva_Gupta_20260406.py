Name-Dhruva Gupta
Roll Number-D238

1)
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:

#class cannot be empty need to have pass

2)
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))
print(type(a))
print(a . _dict_)
print(a)
del  a
print(a)

Output-
Id of class
Type main class
{}
Type,id
Error

3)
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
a = c1()
a . m1()
m1()

Output-
3rd method
Fucntion

4)
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()

Output-
Two  argument  method : 10,20
Error

5)
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
a . m1(10 , 20)
a . m1(30)
a . m1()

Output-
Two  argument  method : 10,20
Two  argument  method : 30,2
Two  argument  method : 1,2

6)
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
a . m1()

Output-
Method of third c1 class

7)
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
a . m1()

Output-
Error

8)
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)
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

Output-
{}                 
{'x': 10}    
{'x': 10, 'y': 20}       
{'x': 30, 'y': 20}       
{'x': 30, 'y': 40}   
{'y': 40}            
{}                  
Error

9)
import time
def words(s):
    word = ""
    for ch in s:
        if ch != ' ':
            word += ch
        else:
            if word:        # avoid empty words
                yield word
                word = ""
    if word:                # last word
        yield word
s = input('Enter any string: ')
g = words(s)
print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)

10)
Begin

11)
#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

Output-
Infinte

12)
#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  
print(g * 3)  
print(g[0])  
print(g[1 : 3])
print(*g)

Output-
Error