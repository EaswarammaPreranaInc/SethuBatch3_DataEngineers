# Find  outputs (Home  work)
class c1:
    x = 10
    def  _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x = 30
b . y = 40
print(b . x) #10
print(b . y) #40
print(a . x) #30
print(a . y) #error
print(c1 . x) #10
print('Object  a : ', a . _dict_) #error
print('Object b : ', b . _dict_) #error
print(c1 . _dict_) #error

# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x) #11
print(a . y) #error
print(b . x) #10
print(b . y) #error
print(c1 . x) #10
print(a . _dict_) #error
print(b . _dict_) #error
print(c1 . _dict_) #error


# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x) #20


