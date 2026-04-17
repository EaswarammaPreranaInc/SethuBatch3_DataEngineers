# Find  outputs (Home  work)
class c1:
    x = 10
    def  _init_(self):
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
print('Object  a : ', a . _dict_) # Object  a : {'y' : 20, 'x' : 30}
print('Object b : ', b . _dict_) # Object  b : 'y' : 40 
print(c1 . _dict_) 
'''
 {'_module': 'main', 'firstlineno': 1, 'x': 10, 'init': <function c1.init_ at 0x000001F179897A00>,
   '_static_attributes': ('y',), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref_': 
   <attribute '_weakref' of 'c1' objects>, 'doc_': None
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
    def _init_(self):
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
print(a . _dict_) # {'y' : 20, 'x' : 11}  
print(b . _dict_) # {'y' : 21}
print(c1 . _dict_) 
'''
 {'_module': 'main', 'firstlineno': 1, 'x': 10, 'init': <function c1.init_ at 0x000001F179897A00>,
   '_static_attributes': ('y',), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref_': 
   <attribute '_weakref' of 'c1' objects>, 'doc_': None
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