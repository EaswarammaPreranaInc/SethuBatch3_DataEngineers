import time

def words(s):
    word = ""
    for ch in s:
        if ch != ' ':          # keep building the word
            word += ch
        else:
            if word:           # yield completed word
                yield word
                word = ""
    if word:                   # last word (if any)
        yield word

# End of generator

s = input('Enter any string: ')
g = words(s)

print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)





#  Find  outputs (Home  work)
def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')	#Begin
print(*g)	#waiting time memory error
print('End')	#End




#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)	#unpacks the generator object






#  Find  outputs (Home  work)
def  f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')	#End
# End  of  generator
g = f1()	#One <next> 1 <next> Two <next> 2 <next> Three
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)	#!
print(y)	#2
print(z)	#3




# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  	#error too many values to unpack expecting 4 but gives 3
p , q , r , s , m = f1()#error too many values to unpack 





#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g)) 	#error generator object has no len() function 
print(g * 3) 	#error  
print(g[0]) 	#error it does not support indexing or slicing 
print(g[1 : 3])	#error it does not support indexing or slicing 
print(*g)	#1 2 3





# Identify  error  (Home work)
class   c1:	#error expected an indentation
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))
print(type(a))
print(a . __dict__)
print(a)
del  a
print(a)






#  Find  outputs  (Home  work)
def   m1():
		print('Function')	#Function
class   c1:
	def   m1(self):
		print('1st  method')	#skipped due to same function name
	def   m1(self):
		print('2nd  method')	#skipped due to same function name
	def   m1(self):
		print('3rd  method')	#3rd method
# End  of  class  c1
a = c1()
a . m1()
m1()





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
a . m1(10 , 20)	#Two argument method : 10 20
a . m1(30)	#error missed one positional argument
a . m1()	#error missing positional arguments





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
a . m1(10 , 20)	#Two  argument  method :  10 20
a . m1(30)	#Two  argument  method :  30 2
a . m1()	#Two  argument  method :  1 2






# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')	#skipped
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')	#skipped
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()	#method of third c1 class





# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')	#skipped
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')	#skipped
class   c1:
	pass
a = c1()
a . m1()	#error 





#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)	#{}
a . x = 10
print(a . __dict__)	#{'x':10}
a . y = 20
print(a . __dict__)	#{'x':10,'y':20}
a . x = 30
print(a . __dict__)	#{'x':30,'y':20'}
a . y = 40
print(a . __dict__)	#{'x':30,'y'=40}
del  a . x
print(a . __dict__)	#{'y':40}
del  a . y
print(a . __dict__)	#{}
del   a
print(a . __dict__)	#error a is not defined