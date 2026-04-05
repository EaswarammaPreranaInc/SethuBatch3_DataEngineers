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
#25........
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
	print(x)#10.8<\n>Hyd
print()
for  x  in   f1():
	print(x)#25<\n>10.8<\n>Hyd
print()
gen = f1()
print(next(gen))#25
for  x  in   f1():
	print(x)#25<\n>10.8<\n>Hyd
print(next(gen))

# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)
	time . sleep(1)
	print('Hello')
for  y  in   g:
	print(y)#0<\n>Hello <\n>1<\n>Hello <\n>2<\n>Hello<\n>2<\n>Hello<\n>3<\n>Hello<\n>4<\n>Hello
 
 # Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0<\n>1<\n>4<\n>9<\n>16
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)#0<\n>1<\n>4<\n>9<\n>16
	time . sleep(1)
 
 # Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)#0<\n>1<\n>4<\n>9<\n>16
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)#

# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)#0<\n>1<\n>4........
 
 #  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break

#0<\n>1<\n>2<\n>3.......