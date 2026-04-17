# Write  a  generator  to  divide  a  string  into  words



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

Modify  the  program  without  using  list





# 

import time



def words(s):

    word = ""

    for ch in s:

        if ch == " ":

            yield word

            word = ""

        else:

            word += ch

    yield word   # last word



s = input("Enter string: ")



for w in words(s):

    print(w)

    time.sleep(1)





#  Find  outputs (Home  work)

def   f1():

	x = 1

	while  x <= 100000000000000000000:

		yield  x

		x +=  1

# End of  generator

g = f1()

print('Begin')    # Begin

print(*g)       # it iterates through all values and end up freeze or taking time to execute complete .

print('End')    # Error because the previous or above line of code  isn't completed







#  Find  outputs  (Home  work)

g = (x * x  for  x  in  range(500000000000000000))   # empty generator

print(*g)    # nothing  because empty generator has nothing.





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



# One

   1

 Two

   2

 Three

   3

 End

 one

Two

Three

  1

  2

  3





# Identify  error (Home  work)

def  f1():

        yield  10

        yield  20

        yield  30

        yield  40

a , b , c = f1()     # Too many values

p , q , r , s , m = f1()   # Too many values





#  Find  outputs (Home  work)

def   f1():

	yield    1

	yield    2

	yield    3

# End  of  generator

g =  f1()

print(len(g))      # it doesn't has length

print(g * 3)       # unsupported operand type(s) for *: 'generator' and 'int'

print(g[0])        # it didn't has index

print(g[1 : 3])    # it is not subscriptable

print(*g)          # (1, 2, 3)







# Identify  error  (Home work)

class   c1:  # class c1 is created

	def  m1(self):  # Here method is created

		pass  # we use pass when we don't give statements

class   c2:   # here new class c2 is created

        pass   # we use pass when we don't give statements

class   c3:





# Find  outputs  (Home  work)

class   c1:

	pass

# End  of  the  class

a = c1()

print(id(a))   # address of class c1

print(type(a)) # <class '__main__.c1'>

print(a . _dict_)  # Error due to 'c1' object has no attribute '_dict_'

print(a)           #   <__main__.c1 object at address of class >

del  a     # clears the class a

print(a)   # a is not defined







 #  Find  outputs  (Home  work)

def   m1():

		print('Function')                # Function

class   c1:

	def   m1(self):                          # ignored because new class is created with same name

		print('1st  method')

	def   m1(self):                          # ignored

		print('2nd  method')             # ignored

	def   m1(self):

		print('3rd  method')             # 3rd method

# End  of  class  c1

a = c1()  # class a pointing to c1()

a . m1()  # method calling               # 3rd method

m1()   # function calling                # Function





#  Find  outputs  (Home  work)

class   c1:  

	def   m1(self):                                               #  ignored 

		print('No  argument  method')

	def   m1(self , x):                                           #  ignored because new class is created with same name

		print('Single  argument  method : ' , x)

	def   m1(self , x , y):

		print('Two  argument  method : ' , x , y)

# End  of  class  c1

a = c1()

a . m1(10 , 20)   #  Two  argument  method :  10 , 20

a . m1(30)         # there is no y 

a . m1()           # the two parameters are missing 







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

a . m1(10 , 20)   # Two  argument  method : 10 , 20

a . m1(30)        # Two  argument  method : 30 , 2

a . m1()          # Two  argument  method : 1 , 2







# Find  outputs  (Home  work)

class   c1:

	def   m1(self):                                       # here it is ignored

		print('Method  of  first  c1  class')

class   c1:

	def   m1(self):                                        # same here

		print('Method  of  second  c1  class')

class   c1:

	def   m1(self):

		print('Method  of  third  c1  class')

a = c1()

a . m1()   # Method  of  third  c1  class







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

a . m1()       #  type object 'c1' has no attribute 'm1'







#  Find  outputs (Home  work)

class  c1:

        pass

# End  of  class

a = c1()

print(a . _dict_)

a . x = 10

print(a . _dict_)

a . y = 20

print(a . _dict_)     # Total Error because of dunder score

a . x = 30

print(a . _dict_)

a . y = 40

print(a . _dict_)

del  a . x

print(a . _dict_)

del  a . y

print(a . _dict_)

del   a

print(a . _dict_)





or 



class c1:

    pass

# End of class



a = c1()

print(a .__dict__)   # {}

a.x = 10

print(a.__dict__)   # {'x': 10}

a.y = 20

print(a.__dict__)   # {'x': 10, 'y': 20}

a.x = 30

print(a.__dict__)   # {'x': 30, 'y': 20}

a.y = 40

print(a.__dict__)   # {'x': 30, 'y': 40}

del a.x

print(a.__dict__)   # {'y': 40}

del a.y

print(a.__dict__)   # {}

del a

#print(a.__dict__)  # cannot use after delete
