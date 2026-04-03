#  Tricky  program
# Find  outputs (Home  work)
def   f1():   #execution starts from begining and pauses at first yield.
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) #empty generator object is created and next method is used
'''infinite 25:
cause infinite generator objects are created
f1 → generator FUNCTION
f1() → generator OBJECT
next() works on OBJECT, not function

'''
#-----------------------------------------------------------------------------
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1() #creates an empty generator object.
for  x  in  g:
	print(x)
for  x  in  g:  #Does not execute
	print(x)
for  x  in  g:  #Does not execute
	print(x)

'''
25
10.8
'Hyd'
'''
#-------------------------------------------------------------------------
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
for  x  in  g:
	print(x)   #10.8<nextline> 'Hyd'
print()           #blank
for  x  in   f1():  #new generator object
	print(x)        #25<nextline>10.8<nextline>'Hyd'
print()             #blank
gen = f1()          
print(next(gen))    #25
for  x  in   f1():  
	print(x)       #25<nextline>10.8<nextline>'Hyd'
print(next(gen))   #10.8

'''
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
#--------------------------------------------------------------
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
#------------------------------------------------------------
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
#------------------------------------------------
import  time
for  y  in   (x * x   for    x    in    range(5)):#loops through existing generator object
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
#---------------------------------------------------------
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(1)
for  y  in  g2:
	print(y)#nothing is printed.
print(g1  is  g2) # True
'''
0
1
4
9
16
True
'''
#--------------------------------------------------
# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y) #waiting time and MemoryError
#-------------------------------------------------
# #  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break
#no waiting time and no MemoryError