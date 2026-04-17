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
print(b . y)  # 40
print(a . x) # 30
print(a . y) # 20
print(c1 . x) # 10
print('Object  a : ', a . __dict__) # {'y':20, 'x':30}
print('Object b : ', b . __dict__) # {'y': 40}
print(c1 . __dict__) # Type and Address


'''
static  variable   ---> x = 10

Object  'a'  ---> y = 20 , x = 30

Object  'b'  ---> y  = 40
'''


# Find  outputs (Home  work)
class c1:
    x = 10 #---> SV
    def __init__(self):
	    self . y = 20 # ---> IV    a.y = 20, b.y = 20
a = c1() # obj 'a' is created to class c1 
b = c1() # obj 'b' is created to class c1 
a . x += 1
b . y += 1
print(a . x) # 11
print(a . y) #  20
print(b . x) # 10
print(b . y) # 21
print(c1 . x) # 10
print(a . __dict__) # {'y':20, 'x':11}
print(b . __dict__) # {'y': 21}
print(c1 . __dict__) # Type and Address


'''
static   variable  ---> x = 10

Object  'a'  ---> y = 20, x = 11

Object  'b'  ---> y =21'''





# Find  outputs (Home  work)
class  c1:
	x = 10  # -----> SV
	def  m1(self):
		self . x = 20 #  (IV)  --> var 'x' is initilalized into obj 'a' with value 20
a = c1() # obj created for c1 class
a . m1() # calling m1() method
print(c1 . x)  # 10
print(a . x) # 20


'''
static   variable   ---> x = 10

object  'a'   ---> x = 20 
'''