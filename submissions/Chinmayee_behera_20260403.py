#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))
#25
#25
.........infinite times

# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)
#25
#10.8
#Hyd
Nothing prints for 2 two loops

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) #25
for  x  in   g:
	print(x)
print()

#25
#10.8
#Hyd

for  x  in   f1():
	print(x)
print()

#25
#10.8
#Hyd

gen = f1()
print(next(gen))
#25

for  x  in   f1():
	print(x)

#25
#10.8
#Hyd

print(next(gen))

#10.8


# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)
	print('Hello')
for  y  in   g:
	print(y)

#0
#Hello
#1
#Hello
#4
#Hello
#9
#Hello
#16
#Hello
#Nothing prints


 # Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
#0
#1
#4
#9
#16
#0
#1
#4
#9
#16


 # Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)

#0
#1
#4
#9
#16
#True



# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)

#First needs to store 500000000 elements
#memory error
#Waiting time



#  Advantage  of  generator ?

#No Waiting time
#No memory error


import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break

#0
#1
#2
#3
.
.
.
#(1000000000000000000000000000000000000000000000000000000000000000-1)