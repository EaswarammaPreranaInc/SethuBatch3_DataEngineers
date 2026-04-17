# Find  outputs (Home  work)
class c1:
    x = 10 # static variable 
    def  __init__(self):
	    self . y = 20 #instance variable
a = c1() # object of class c1
b = c1() # object of class c1
a . x = 30 # instance variable 
b . y = 40 # instance variable 
print(b . x) # 10
print(b . y) # 40
print(a . x) # 30
print(a . y) # 20
print(c1 . x) # 10
print('Object  a : ', a . __dict__) # {x : 30 , y : 20}
print('Object b : ', b . __dict__) # {y : 40}
print(c1 . __dict__) # {x : 10, environment variables}
'''
static  variable   ---> x = 10

Object  'a'  ---> x = 30 , y = 20

Object  'b'  ---> y = 40
'''


# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x) # 11
print(a . y) # 20
print(b . x) # 11
print(b . y) # 21
print(c1 . x) # 11
print(a . __dict__) # {y : 20}
print(b . __dict__) # {y : 21}
print(c1 . __dict__) # {x : 11 , environment variables}
'''
static   variable  ---> x = 11

Object  'a'  ---> y = 20

Object  'b'  ---> y = 21
'''


 # Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) # 10
print(a . x) # 20
'''
static   variable   ---> x = 10

object  'a'   ---> x = 20
'''