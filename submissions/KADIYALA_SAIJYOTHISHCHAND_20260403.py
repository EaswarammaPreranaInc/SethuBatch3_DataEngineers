#Topic - 1


#Topic - 1.1
#  Tricky  program
# Find  outputs (Home  work)
import time
def f1():
    yield  25
    yield  10.8
    yield  'Hyd'
# End of  generator
while  True:
    print(next(f1())) #each time new generator is created

'''
OUTPUT:
25
25
25
....
'''

#Topic - 1.2
# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x)#25<\n>10.8<\n>'Hyd'
for  x  in  g: #Not executed
	print(x)
for  x  in  g: #Not Executed
	print(x)

#Topic - 1.3    
# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))#25<\n>
for  x  in   g:
	print(x)#10.8<\n>'Hyd'
print()#<\n>
for  x  in   f1():
	print(x) #25<\n>10.8<\n>'Hyd'
print()#<\n>
gen = f1()
print(next(gen))#25
for  x  in   f1():
	print(x)#25<\n>10.8<\n>'Hyd'
print(next(gen))#10.8

#Topic - 1.4
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
OUTPUT:
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

#Topic - 1.5    
# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(1)
'''
OUTPUT:
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

#Topic - 1.6
# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)#0<\n>1<\n>4<\n>9<\n>16
	time . sleep(1)
for  y  in  g2: #Not Executed
	print(y)
print(g1  is  g2) #True

#Topic - 1.7
# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)#No Memory Error
    
#Topic - 1.8    
#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(100000000000000000000))
#g is zero
while   True:
	try:
		print(next(g)) #Generates squares till range() ends
		time . sleep(0.5)
	except:
		break # after range is yielded the loop is breaked
 
