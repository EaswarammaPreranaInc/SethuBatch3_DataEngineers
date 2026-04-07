def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')
#print(*g)
print('End')

g = (x * x  for  x  in  range(500000000000000000))
#print(*g) # memory error


def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)

x ,  y ,  z  =  f1()
print(x)  
print(y)
print(z)
'''
one
1
two
2
three
3
end
one
two
three
end
1
2
3
'''

def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1()   # error
#p , q , r , s , m = f1() # error

def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() 
#print(len(g))# error  
#print(g * 3)    # error
#print(g[0])  # error
#print(g[1 : 3]) # error
print(*g)   # 1 2 3

class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: a class should atleast one statement


class   c1:
	pass
# End  of  the  class
a = c1() 
print(id(a)) #address of class
print(type(a)) # <class'__main__.c1'>
print(a . __dict__) #{}
print(a) #<main.c1 at a234r>
del  a  
#	print(a) # error


def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
#a . m1() error
m1() # function

class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)#Two  argument  method : 10 20
#a . m1(30)  error
#a . m1() #error

class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1() # Method of third c1 class


class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
#a . m1() # error

class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) #{}
a . x = 10
print(a . __dict__) #{x:10}
a . y = 20
print(a . __dict__) #{x:10,y:20}
a . x = 30
print(a . __dict__) #{x:30,y:20}
a . y = 40
print(a . __dict__) #{x:30,y:40}
del  a . x
print(a . __dict__) #{y:40}
del  a . y
print(a .__dict__) #{}
del   a
#print(a . _dict_) # error