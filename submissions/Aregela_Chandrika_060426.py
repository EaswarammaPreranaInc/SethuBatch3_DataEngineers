'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   words(s):
	list = s . split()  #  ['Hyd' , 'is' , 'green' , 'city']
	for  x  in  list:
		yield  x
# End of generator
s = input('Enter  any   string  :  ')#   M.G.Story
g = words(s) #  Gen  object
print('Words  of  the  string')
for  y  in   g:
	print(y)  #  Hyd , is , green , city
	time . sleep(1)
# Modify  the  program  without  using  list




import time
def words(s):
    word = ""   
    for ch in s:
        if ch != ' ':          
            word += ch
        else:
            if word != "":     
                yield word
                word = ""      
    if word != "":             
        yield word

# End of generator

s = input("Enter any string: ")
g = words(s)

print("Words of the string")
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
print('Begin') # Begin
print(*g) # Unpack
print('End')



#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)  # Unpack



    
    
#  Find  outputs (Home  work)
def  f1():
	print('One') # one
	yield    1    # 1
	print('Two')  # Two
	yield    2    # 2
	print('Three') # Three
	yield    3      # 3
	print('End')   # End
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1() # one two three
print(x) # 1
print(y) # 2
print(z) # 3





# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()   # Error
p , q , r , s , m = f1() # Error




#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() 
print(len(g))   # Error
print(g * 3)   # Error
print(g[0])  # Error
print(g[1 : 3]) # Error
print(*g) # 1 2 3 





# Identify  error  (Home work)
class   c1:
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
print(id(a)) # Address of a
print(type(a)) # <class '__main__.c1'>
print(a . _dict_) # Error 
print(a) # Address and type
del  a
print(a) # Error a not defined
    
    
    
    
#  Find  outputs  (Home  work)
def   m1():
		print('Function') # Function
class   c1:
	def   m1(self): # discarted
		print('1st  method')
	def   m1(self): # discarted
		print('2nd  method')
	def   m1(self): # Recognised
		print('3rd  method') # 3rd Method
# End  of  class  c1
a = c1()
a . m1() # calls class method
m1() # calls global function
 
 
 
 
 
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y) # Two argument method :  10 20
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30) # Error Only 1 argument given But method needs 2 (x, y)
a . m1() # No arguments given Method expects 2






#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method') # Two argument method :  1 2
	def   m1(self , x):
		print('Single  argument  method : ' , x) # Two argument method :  30 2
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y) # Two argument method :  10 20
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()





# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class') # Method of third c1 class
a = c1()
a . m1()





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
a . m1() # Error




#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) # {}
a . x = 10
print(a . _dict_) # {'x': 10}
a . y = 20
print(a . _dict_) # {'x': 10, 'y': 20}
a . x = 30
print(a . _dict_) # {'x': 30, 'y': 20}
a . y = 40
print(a . _dict_) # {'x': 30, 'y': 40}
del  a . x
print(a . _dict_) # {'y': 40}
del  a . y
print(a . _dict_) # {}
del   a
print(a . _dict_) # Error due to not defined