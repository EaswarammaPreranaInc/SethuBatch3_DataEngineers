1.)
class c1:
    x = 10
    def  __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x = 30
b . y = 40
print(b . x)  #10
print(b . y) #40
print(a . x) #30
print(a . y) #20
print(c1 . x) #10
print('Object  a : ', a . __dict__)  #{x:30,y:20}
print('Object b : ', b . __dict__)    #{y:40}
print(c1 . __dict__) #{x:30}



'''
static  variable   ---> x=10

Object  'a'  ---> y=20,x=30

Object  'b'  ---> y=40
'''




2.)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x) #10
print(a . x)  #20



'''
static   variable   ---> x=10

object  'a'   ---> x=20
'''