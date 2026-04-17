#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))

#output
25
10.8
Hyd
stop iteration error


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

#output
25
10.8
Hyd



 # Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) 
for  x  in   g:
	print(x)
print()
for  x  in   f1():#error
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))

#output
25
10.8
Hyd
space
25
10.8
Hyd


# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)
	print('Hello')
for  y  in   g:
	print(y)

# output
0
Hello
1
Hello
4
Hello
9
Hello
16


# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)

# output
0
1
4
9
16
0
1
4
9
16


# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(1)
for  y  in  g2: # not executed bec g2 and g1 points to same function i.e stop iteration error 
	print(y)
print(g1  is  g2)

# output
0
1
4
9
16
True



# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)] # waiting time and memory error
for  y  in  list:
	print(y)


#  Advantage  of  generator ?  # no waiting time and no memory error
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break

# output
0
1
4
.
.
.
till 1000000000000000000000000000000000000000000000000000000000000000^2