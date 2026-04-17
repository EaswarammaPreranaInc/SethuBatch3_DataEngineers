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

output
10
40
30
20
10
Object a :  {'y': 20, 'x': 30}
Object b :  {'y': 40}

'''
static variable ---> x = 10

Object 'a' ---> {'y': 20, 'x': 30}

Object 'b' ---> {'y': 40}
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
print(a . x)
print(a . y)
print(b . x)
print(b . y)
print(c1 . x)
print(a . __dict__)
print(b . __dict__)
print(c1 . __dict__)


output
11
20
10
21
10
{'y': 20, 'x': 11}
{'y': 21}

'''
static variable ---> x = 10

Object 'a' ---> {'y': 20, 'x': 11}

Object 'b' ---> {'y': 21}




# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)
print(a . x)

output
10
20

'''
static variable ---> x = 10

object 'a' ---> {'x': 20}
'''
