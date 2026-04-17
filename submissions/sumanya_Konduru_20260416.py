# Find  outputs (Home  work)
class c1:
    x = 10
    def  __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x = 30
b . y = 40
print(b . x) # 10
print(b . y) # 40
print(a . x) # 30
print(a . y) # 20
print(c1 . x) # 10
print('Object  a : ', a . __dict__) # Object  a : {'y' : 20, 'x' : 30}
print('Object b : ', b . __dict__) # Object  b : 'y' : 40 
print(c1 . __dict__) 
'''
 {'__module__': '__main__', '__firstlineno__': 1, 'x': 10, '__init__': <function c1.__init__ at 0x000001F179897A00>,
   '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': 
   <attribute '__weakref__' of 'c1' objects>, '__doc__': None
}
'''


'''
static  variable   ---> x 

Object  'a'  --->  20 

Object  'b'  ---> 20  
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
print(b . x) # 10 
print(b . y) # 21
print(c1 . x) # 10 
print(a . __dict__) # {'y' : 20, 'x' : 11}  
print(b . __dict__) # {'y' : 21}
print(c1 . __dict__) 
'''
 {'__module__': '__main__', '__firstlineno__': 1, 'x': 10, '__init__': <function c1.__init__ at 0x000001F179897A00>,
   '__static_attributes__': ('y',), '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': 
   <attribute '__weakref__' of 'c1' objects>, '__doc__': None
}
'''


'''
static   variable  ---> 10

Object  'a'  ---> 20 

Object  'b'  ---> 20
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
static   variable   ---> 10

object  'a'   ---> 20
'''