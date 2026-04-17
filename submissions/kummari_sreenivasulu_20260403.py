1.
#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))
	
'''
25
25
25
25
25
25
25
25
25
25
infinite 25 becoz every time  we  call  f1()  it  creates  a new generator object and starts from the beginning of the generator function, yielding 25 every time. To get the next values, we need to create a single generator object and call next() on that object repeatedly.
'''

2.
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
'''
25
10.8
Hyd
'''


3.
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
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))
'''
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8
'''


4.
# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)
	print('Hello')
for  y  in   g:
	print(y)
'''
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
'''


5.
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
'''
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
'''


6.
# Find  outputs(Home  work)
# import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)
'''
0
1
4
9
16
True
'''


7.
#Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)
'''
Huge memory consunption.
A list is a squence that stores all its elements in memory.
Crash program due to memory error.
Hang system due to memory error.
'''


8.
#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break
'''
A generator does NOT create all values at once.
it produces only one value ata a time .when we call next()
'''