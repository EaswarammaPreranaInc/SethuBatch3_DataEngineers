
#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))# it runss for infinite time



#-----------------------------------------
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)
 #25
 #10.8
 #Hyd


 #-----------------------------------------------
 
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
	print(x)#25
 #10.8
 #Hyd
print()
for  x  in   f1():
	print(x)#25
 #10.8
 #Hyd
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)#25
 #10.8
 #Hyd
 
print(next(gen))#error
#--------------------------------------------------
# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)
	print('Hello')
 #hello
 #hello
 #hello
 #hello
 #hello
for  y  in   g:
	print(y)
 #0
 #1
 #4
 #9
 #16
 
 # Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
#0
#1
#4
#9
#16
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
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
	print(y)#0
 #1
 #4
 #9
 #16
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)#True
#----------------------------------------------------

# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)#it stoes all values in memory
 
 #---------------------------------------------------------
 #  Advantage  of  generator  itdoes not  store  all  values  in  memory
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break
