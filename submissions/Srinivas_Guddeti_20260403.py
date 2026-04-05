
#  Tricky  program
# Find  outputs (Home  work)
...
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))   #25 is printed infinite times


# Find  outputs (Home  work)

def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)    #25
for  x  in  g:
	print(x)    #10.8
for  x  in  g:
	print(x)    #Hyd
	

# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))     #25
for  x  in   g:
	print(x)       #10.8
print()
for  x  in   f1():
	print(x)        #25
print()
gen = f1()
print(next(gen))     #25
for  x  in   f1():
	print(x)          #25
print(next(gen))     #10.8




 #4) outputs 
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y)#0
	time . sleep(1)
	print('Hello')#Hello
for  y  in   g:
	print(y)
#0
Hello
1
Hello
4
Hello
9
Hello
16
Hello

#5) outputs 
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)# 0 <next line> 1 <next line>  4 <next line> 9 <next line> 16
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)# 0 <next line> 1 <next line>  4 <next line> 9 <next line> 16
	time . sleep(1)

#6) outputs
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)# 0 <next line> 1 <next line>  4 <next line> 9 <next line> 16
	time . sleep(1)
for  y  in  g2:
	print(y)# 0 <next line> 1 <next line>  4 <next line> 9 <next line> 16
print(g1  is  g2)#True

#7) # Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)

#8) #  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g))#0 <next line> 1 <next line>  4 <next line>...
		time . sleep(0.5)
	except:
		break