 Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) 
	# output : 25 is printed infinite times, because  every time  we are  calling  f1()  function, it  creates  a new generator object and  starts  yielding from the beginning of the generator

# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x) # 25 10.8 Hyd
for  x  in  g:
	print(x) # No  output, because  generator  is  exhausted
for  x  in  g:
	print(x) # No  output, because  generator  is  exhausted

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) # 25 
for  x  in   g:
	print(x) # 10.8 Hyd
# print(next(g)) # StopIteration exception, because  generator  is  exhausted
print()
for  x  in   f1():
	print(x) # 25 10.8 Hyd 
print()
gen = f1()
print(next(gen)) # 25
for  x  in   f1():
	print(x) # 25 10.8 Hyd 
print(next(gen)) # 10.8

# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y) # 0 1 4 9 16
	time . sleep(1) # 1 second delay after every output
	print('Hello') # Hello  after  every  output
for  y  in   g:
	print(y) # No  output, because  generator  is  exhausted

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0 <sleep(1)> 1 <sleep(1)> 4 <sleep(1)> 9 <sleep(1)> 16
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0 <sleep(1)> 1 <sleep(1)> 4 <sleep(1)> 9 <sleep(1)> 16
	time . sleep(1)

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y) # 0 <sleep(1)> 1 <sleep(1)> 4 <sleep(1)> 9 <sleep(1)> 16
	time . sleep(1)
for  y  in  g2:
	print(y) # No  output, because  generator  is  exhausted
print(g1  is  g2) # True, because  g1 and  g2  are  references  to  same  generator

# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y) # prints squares from 0 to (500000000-1)

#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g)) # prints squares from 0 to (1000000000000000000000000000000000000000000000000000000000000000-1)
		time . sleep(0.5)
	except:
		break