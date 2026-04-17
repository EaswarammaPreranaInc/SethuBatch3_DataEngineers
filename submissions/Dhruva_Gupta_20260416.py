# Find  outputs (Home  work)
class c1:
    x = 10
    def  _init_(self):
	    self . y = 20
a = c1()  
b = c1()
a . x = 30
b . y = 40
print(b . x)    # 10
print(b . y)    # 40
print(a . x)    # 30
print(a . y)    # Error c1 class has a.y attribute
print(c1 . x)   # 10
print('Object  a : ', a . _dict_)   # Object  a :  {'x': 30}
print('Object b : ', b . _dict_)    # Object  a :  {'y': 40}
print(c1 . _dict_)    # Python gives a dictionary of all class-level attributes and methods


# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)   # 11
print(a . y)   # Error because c1 class object has no attribute like a.y
print(b . x)   # 10
print(b . y)   # Error because c1 class object has no attribute like a.y
print(c1 . x)  # 10
print(a . _dict_)   # {'x': 11}
print(b . _dict_)   # {}
print(c1 . _dict_)   # {'__module__': '__main__', 'x': 10, '_init_': <function c1._init_ at 0x00000249E6440360>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}



# Find  outputs (Home  work)
class  c1:
	x = 10     # static variable is created
	def  m1(self):
		self . x = 20   # instant variable is created
a = c1()
a . m1()
print(c1 . x)   # 10
print(a . x)    # 20

