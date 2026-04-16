1) outputs
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
print(a . y)#Error because y is not defined
print(c1 . x)#10
print('Object  a : ', a . _dict_)#Object a : {x : 30}
print('Object b : ', b . _dict_)#Object b : {y : 40}
print(c1 . _dict_)##{x = 30, y=40, None}


'''
static  variable   ---> x = 10

Object  'a'  ---> x = 30

Object  'b'  ---> y = 40
'''

2) outputs
class c1:
    x = 10
    def _init_(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)#11
print(a . y)#Error y is not defined
print(b . x)#10
print(b . y)#Error y is not defined
print(c1 . x)#10
print(a . _dict_)#{x : 11}
print(b . _dict_)#{}
print(c1 . _dict_)#{x = 10, None}


'''
static   variable  ---> x = 10

Object  'a'  --->x =11

Object  'b'  ---> x = 10

3) outputs 
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#10
print(a . x)#20


'''
static   variable   ---> x = 10

object  'a'   ---> x = 20
''