# Find  outputs (Home  work)
class c1:
    x = 10
    def  _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x = 30
b . y = 40
print(b . x)#10
print(b . y)#40
print(a . x)#30
print(a . y)#20
print(c1 . x)#10
print('Object  a : ', a . _dict_)#  {'y': 20, 'x': 30}
print('Object b : ', b . _dict_)#  {'y': 40}
print(c1 . _dict_)#  {'x': 10}



# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)#11
print(a . y)#20
print(b . x)#11
print(b . y)#
print(c1 . x)#
print(a . _dict_)# {'y': 20}
print(b . _dict_)#{'y': 21}
print(c1 . _dict_)# {'x': 10}



# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#20
print(a . x)#20


