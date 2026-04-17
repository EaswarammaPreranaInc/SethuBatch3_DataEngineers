#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) # 25<nl>10.8<nl>Hyd

# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)# 25 10.8 Hyd
for  x  in  g:
	print(x) # nothing
for  x  in  g:
	print(x) # nothing

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
print()
for  x  in   f1():
	print(x) # 25
print()
gen = f1()
print(next(gen)) # 25 10.8 Hyd
for  x  in   f1():
	print(x)
print(next(gen)) # 25

# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y) # 0 Hello 1 Hello 4 Hello 9 Hello 16 Hello
	time . sleep(1)
	print('Hello')
for  y  in   g:
	print(y) # nothing

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0 1 4 9 16
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # 0
	time . sleep(1)

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y) # 0 1 4 9 16
	time . sleep(1)
for  y  in  g2:
	print(y) # nothing 
print(g1  is  g2) #True

# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y) # Error, memory error and time waiting 

#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g)) # it can take any number of elements to be yield 
		time . sleep(0.5)
	except:
		break