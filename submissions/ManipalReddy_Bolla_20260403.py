#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))#25 <nextline> 25 .... infinite times 25 is printed 
	
	
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)#25 10.8 Hyd
for  x  in  g:
	print(x)#no output
for  x  in  g:
	print(x)#no output
	
	
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))#25
for  x  in   g:
	print(x)#10.8 Hyd
print()#<nextline>
for  x  in   f1():
	print(x)#25 10.8 Hyd
print()#<nextline>
gen = f1()
print(next(gen))#25
for  x  in   f1():
	print(x)#25 10.8 Hyd
print(next(gen))#10.8


# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:#iteration1 iteration2 iteration3 iteration4 iteration5
	print(y)#0**2 1**2 2**2 3**2 4**5
	time . sleep(1)# wait 1 sec wait 1 sec wait 1 sec wait 1 sec wait 1 sec
	print('Hello')#Hello Hello Hello Hello Hello
for  y  in   g:
	print(y)#no output
	

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)# 0 1 4 9 16
	time . sleep(1)#wait 1 sec for each iteration in current generator after print(y) execute
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0 1 4 9 16
	time . sleep(1)#wait 1 sec for each iteration in current generator after print(y) execute
	

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)#0 1 4 9 16
	time . sleep(1)#wait 1 sec for each iteration in current generator after print(y) execute
for  y  in  g2:
	print(y)#no output The generator object is now Exhausted. The internal pointer has reached the end of the range.
print(g1  is  g2)#True


# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)#memory error


#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))#0 1 4 9 16 ........................9.99*62
		time . sleep(0.5)#wait 0.5 sec for each iteration
	except:
		break#break out of loop
