# Find  outputs (Home  work)
class c1:
    x = 10
    def  __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x = 30
b . y = 40
print(b . x)
print(b . y)
print(a . x)
print(a . y)
print(c1 . x)
print('Object  a : ', a . __dict__)
print('Object b : ', b . __dict__)
print(c1 . __dict__)


'''
static  variable   --->  x = 10 , 

Object  'a'  --->  x = 10 , 

Object  'b'  --->
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
print(a . x)  # 10
print(a . y)  # 20
print(b . x)  # 10
print(b . y)  # 20
print(c1 . x)  # 10
print(a . __dict__)  # __init__ , x , y 
print(b . __dict__)  # __init__ , x , y 
print(c1 . __dict__)  # __init__ , x , y 


'''
static   variable  --->

Object  'a'  --->

Object  'b'  --->
'''

# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)  # 10
print(a . x)  # 


'''
static   variable   --->  x = 10 , 

object  'a'   --->
'''


