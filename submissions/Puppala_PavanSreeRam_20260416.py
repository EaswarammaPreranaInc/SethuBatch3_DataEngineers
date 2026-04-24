# Find  outputs (Home  work)

class c1:
    x = 10
    def  _init_(self):
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
print('Object  a : ', a . _dict_)
print('Object b : ', b . _dict_)
print(c1 . _dict_)


'''
static  variable   ---> 10

Object  'a'  ---> 30

Object  'b'  ---> 40

'''

#..............................................................................................>

# Find  outputs (Home  work)

class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x)
print(a . _dict_)
print(b . _dict_)
print(c1 . _dict_)


'''
static   variable  ---> 10

Object  'a'  ---> 11

Object  'b'  ---> Error ==> No Variables

#..............................................................................................>

# Find  outputs (Home  work)

class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)
print(a . x)


'''
static   variable   ---> 10

object  'a'   ---> 20

'''

#..............................................................................................>