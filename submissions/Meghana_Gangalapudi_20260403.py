#  Tricky  program
# Find  outputs (Home  work)
def   f1():                    #25
	yield  25              #10.8
	yield  10.8            #Hyd
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))

# Find  outputs (Home  work)
def   f1():                    #25
	yield  25              #10.8
	yield  10.8            #Hyd
	yield  'Hyd'        
# End of  generator
g = f1()
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)
for  x  in  g:
	print(x)

# Most  tricky  program
# Find  outputs(Home  work)
import  time                    #25
def   f1():                     #25 10.8 Hyd
	yield  25               #25 10.8 Hyd
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

# Find  outputs (Home  work)          #0 Hello
import  time                          #1 Hello
g = (x * x   for  x  in  range(5))    #4 Hello
for  y  in   g:                       #9 Hello
	print(y)                      #16 Hello
	time . sleep(1)               #0 1 4 9 16
	print('Hello')
for  y  in   g:
	print(y)

# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1) #0 1 4 9 16
for  y  in   (x * x   for    x    in    range(5)):
	print(y)    #0 1 4 9 16
	time . sleep(1)

# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1           #0 1 4 9 16
for  y  in  g1:
	print(y)    
	time . sleep(1)
for  y  in  g2:
	print(y)
print(g1  is  g2)

# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:  #waiting time
	print(y)

#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))
		time . sleep(0.5)
	except:
		break    