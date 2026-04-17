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

print(a . y) #20

print(c1 . x) #10

print('Object  a : ', a . _dict_) #{x:30,y:20}

print('Object b : ', b . _dict_) #{y:40}

print(c1 . _dict_) #{x:10}





'''

static  variable   ---> x=10



Object  'a'  ---> y=20  x=30



Object  'b'  ---> y=40

'''



# Find  outputs (Home  work)

class c1:

    x = 10

    def _init_(self):

	    self . y = 20

a = c1()

b = c1()

a . x += 1 #11

b . y += 1 #21

print(a . x) #10

print(a . y) #20

print(b . x) #20

print(b . y) #10

print(c1 . x) #10

print(a . _dict_) #{y:20}

print(b . _dict_) #{y:20}

print(c1 . _dict_) #{x:10}





'''

static   variable  ---> x=10



Object  'a'  ---> y=20



Object  'b'  ---> y=20



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

static   variable   ---> x=10



object  'a'   ---> x=20

'''
