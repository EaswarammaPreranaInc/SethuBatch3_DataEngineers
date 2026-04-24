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
print(a . y) #Error no y object.
print(c1 . x) #10
print('Object  a : ', a . _dict_) #Error 
print('Object b : ', b . _dict_) # Error
print(c1 . _dict_) #Error


'''
static  variable   ---> 10

Object  'a'  ---> 10 , 30

Object  'b'  ---> 10 , 40
'''


# Find  outputs (Home  work)
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1() 
b = c1() 
a . x += 1 
b . y += 1  #error
print(a . x) #11
print(a . y) #error no y object
print(b . x) #10
print(b . y) #error
print(c1 . x) #10
print(a . _dict_) #error
print(b . _dict_) #error
print(c1 . _dict_) #error


'''
static   variable  ---> 10

Object  'a'  ---> 11

Object  'b'  ---> 10
'''


# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x) #20


'''
static   variable   ---> 10

object  'a'   ---> 20
'''
