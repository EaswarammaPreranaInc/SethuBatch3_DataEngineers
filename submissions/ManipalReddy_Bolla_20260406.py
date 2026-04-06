'''
Write  a  generator  to  divide  a  string  into  words
Hint1:  Use  generator  function  and  for   loop
Hint2: write the  program  without  using  list
'''
def words(s):
    current_word = ""
    for char in s:
        if char != " ":
            current_word += char
        else:
            if current_word:
                yield current_word
                current_word = ""
    if current_word:
        yield current_word

s = input('Enter any string: ')
g = words(s)

print('Words of the string:')
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
print('Begin')#Begin
#print(*g)#memory error
print('End')


#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)#memory error


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
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)


'''
output
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
'''


# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()#error
p , q , r , s , m = f1()#error


#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
print(len(g))#error if commented then next statements are will get run
print(g * 3)#error if commented  then next statements are will get run
print(g[0])#error generator object is not indexed if commented then next statements are will get run
print(g[1 : 3])#error generator object is not indexed if commented then next statements are will get run
print(*g)#1 2 3 


# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass#executes but does nothing
class   c2:
        pass#executes but does nothing
class   c3:#error because class cannot be empty


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()# cl class object is created  i.e a 
print(id(a))#address of a
print(type(a))# class '__main__.c1'
print(a . __dict__)#object a is now dictionary i.e {}
print(a)#object type and address 
del  a#object a is deleted
print(a)#a doesn't exist


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
a . m1()#3rd method remaining 2nd and 1st method are discarded
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
a . m1(10 , 20)#Two argument method : 10 20
a . m1(30)#error
a . m1()#error


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
a . m1(10 , 20)#Two  argument  method : 10 20
a . m1(30)#Two  argument  method : 30 2
a . m1()#Two  argument  method : 1 2


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
a . m1()#error c1 class now newly created c1 class which don't have m1 method


#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)#{}
a . x = 10
print(a . __dict__)#{'x':10}
a . y = 20
print(a . __dict__)#{'x':10,'y':20}
a . x = 30
print(a . __dict__)#{'x': 30, 'y': 20}
a . y = 40
print(a . __dict__)#{'x': 30, 'y': 40}
del  a . x
print(a . __dict__)#{'y':40}
del  a . y
print(a . __dict__)#{}
del   a
print(a . __dict__)#a is deleted




