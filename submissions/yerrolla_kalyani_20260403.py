#  Tricky  program
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))#25<nxt>25<nxt>25<nxt>25<nxt>25<nxt>25<nxt>25<nxt>..........25<nxt>infinite times 


# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)#25 <nxt>10.8<nxt>Hyd
for  x  in  g:
	print(x)#Si error and itself for loop handels it internally ie for loop is not executed 
for  x  in  g:
	print(x)#Si error and itself for loop handels it internally ie for loop is not executed 


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
	print(x)#10.8<nxt>Hyd
print()#nothig is printed
for  x  in   f1():
	print(x)#25<nxt>10.8<nxt>Hyd
print()#nothig is printed
gen = f1()
print(next(gen))#25
for  x  in   f1():
	print(x)#25<nxt>10.8<nxt>Hyd
print(next(gen))#10.8


# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)#time gap is 1 seccond 
	print('Hello')
for  y  in   g:
	print(y)#not executeed itself stoped due to stop iteration error which is for loop internally handelled.
# output:=
# 0
# Hello
# 1
# Hello
# 4
# Hello
# 9
# Hello
# 16
# Hello


# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0,1,4,9,16
	time . sleep(1)#texecution time is 1second
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0,1,4,9,16
	time . sleep(1)#texecution time is 1second



 # Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)#0,1,4,9,16
	time . sleep(1)#texecution time is 1second
for  y  in  g2:
	print(y)# g1 and g2 are pointing to same so the generator g1 is fully iterated so g2 is not possible to iterate ,not executeed itself stoped due to stop iteration error which is for loop internally handelled.
print(g1  is  g2)#True



# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)
#here the in this the elmts to store in the list it takes the more time and it creates the waiting time and memory error .
 #  Advantage  of  generator ?#no memory error and no waiting time 
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break
	
#in this genarator (iterator) no memory error and no waiting time
