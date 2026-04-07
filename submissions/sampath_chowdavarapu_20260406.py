'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   words(s):
	#list = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	ch=''
	for  x  in  s:
		yield x
		
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)
#Modify  the  program  without  using  list

#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')#Begin
print(*g)#1<nxt>2<nxt>3<nxt>4<nxt>5<nxt>6<nxt>7<nxt>8<nxt>9<nxt>10.........<nxt>100000000000000000000
print('End')#End

#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)#01<nxt>2<nxt>3<nxt>4<nxt>5<nxt>6<nxt>7<nxt>8<nxt>9<nxt>10.........<nxt>4999999999999999999


#  Find  outputs (Home  work)
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
	print(m)#One<nxt>1<nxt>Two<nxt>2<nxt>Three<nxt>3<nxt>End
x ,  y ,  z  =  f1()
print(x)#class and type of the <class generator <f1> and hexa_decimal address>
print(y)#class and type of the <class generator <f1> and hexa_decimal address>
print(z)#class and type of the <class generator <f1> and hexa_decimal address>

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  #a,b,c are pointing to generator function
p , q , r , s , m = f1() # p,q,r,s ,m are pointing to generator function

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))  #0
print(g * 3)  #nothing because generator is an empty object
print(g[0])  #generator is not indexed itis empty 
print(g[1 : 3])#not possible to d sclicing on generator it is npt supporated s sequences
print(*g)#4 jobs here entire generator function executes at once stores in generator wht ever the generator function is yielded and unpack the elments of the generator and generator is empty


# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
	#no methods or even pass so pvm reports error 


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#address of the class
print(type(a))#<class '__main__.c1' > 
print(a . __dict__)#{}
print(a)#
del  a #object a is deleted for c1 class 
print(a)#error no object a is not defined ie  it is deleted 

 #  Find  outputs  (Home  work)
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
a . m1()#3rd  method
m1()#Function

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)#Two  argument  method :   10 <space> 20
a . m1(30)#Single  argument  method : 30
a . m1()#No  argument  method


#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)#Two  argument  method : 10 <space> 20
a . m1(30)#Single  argument  method :30
a . m1()#No  argument  method


# Find  outputs  (Home  work)
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
a . m1()#Method  of  third  c1  class


# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()#nothing 


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)#{}
a . x = 10
print(a . __dict__)#{x:10}
a . y = 20
print(a . __dict__)#{x:10,y:20}
a . x = 30
print(a . __dict__)#{x:30,y:20}
a . y = 40
print(a . __dict__)#{x:30,y:40}
del  a . x
print(a . __dict__)#{y:40}
del  a . y
print(a . __dict__)#{}
del   a
print(a . __dict__)#no obect a for class a is not defined 

