import time
def words(s):
    word = ''
    for x in s:
        if x != ' ':
            word+=x
        else:
            yield word
            word =''
    if word:
        yield word
s = input("enter the string: ")
g = words(s)
for y in g:
    print(y)
    time.sleep(1)

def   f1():
	x = 1
	while  x <= 100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1() # will  create  a  generator  object
print('Begin')
print(*g) #  will  print  all  the  numbers  from 1 to 100000000000000000000
print('End') # will  print  'End' after  the  generator  is  exhausted


#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)#  This  code  will  generate  a  generator  expression  that  produces  the squares  of  numbers  from 0 to 499999999999999999. The `print(*g)` statement will attempt to print all of these values, which will likely result in a very large output and may not be practical to run.

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
g = f1() # creates genenator object
for   m   in   g:
	print(m) # one 1 Two 2 Three 3 
x ,  y ,  z  =  f1() # One Two Three End
print(x) # 1
print(y) # 2
print(z) # 3

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  
p , q , r , s , m = f1() # ValueError: too many values to unpack (expected 5)

#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1() # creates a generator object
print(len(g)) # error generator object has no len()  
print(g * 3) # error generator object cannot be multiplied 
print(g[0]) # error generator object is not subscriptable 
print(g[1 : 3]) # error generator object is not subscriptable
print(*g) # 1 2 3