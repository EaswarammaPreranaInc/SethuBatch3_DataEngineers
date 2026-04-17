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
10.8
Hyd 
StopIteration Error
'''


# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()
for  x  in  g:
	print(x) # 25 <> 10.8 <> Hyd
for  x  in  g: # does not iterate anything
	print(x)
for  x  in  g: #does not iterate anything 
	print(x)


# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g)) # 25
for  x  in   g:
	print(x) # 10.8 <> Hyd 
print()
for  x  in   f1(): #does not iterate anything 
	print(x)
print()
gen = f1()
print(next(gen)) # 25
for  x  in   f1():
	print(x) # 10.8 <> Hyd
print(next(gen)) # StopIteration Error


# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))
for  y  in   g:
	print(y) # prints squares of numbers from 0 to 4 in different lines
	time . sleep(1) # suspends the program for 1 second 
	print('Hello') # waits for 1 second printing Hello after each iteration of the loop
for  y  in   g: #does not iterate anything
	print(y) 


# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # prints squares of numbers from 0 to 4 in different lines
	time . sleep(1) # suspends the program for one second before moving to the next line
for  y  in   (x * x   for    x    in    range(5)):
	print(y) # prints squares of numbers from 0 to 4 in different lines
	time . sleep(1) #suspends the program for 1 second before moving to the next line 
 


# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y) # prints squares of numbers from 0 to 4 in different lines
	time . sleep(1) # suspends the program for 1 second before moving to the next line 
for  y  in  g2: #does not iterate anything 
	print(y)
print(g1  is  g2) # True


# Drawback  of  sequences 
list = [x * x   for   x   in   range(500000000)]
for  y  in  list:
	print(y)
'''
Takes a long time to store the values in the sequence

Memory Error
'''


#  Advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000))
while   True:
	try:
		print(next(g)) # prints squares of numbers from 0 to (1000000000000000000000000000000000000000000000000000000000000000 - 1) in different lines
		time . sleep(0.5) # suspends the program for 0.5 second before moving to the next line 
	except:
		break #  breaks out the the loop when StopIteration Error occurs instead of throwing an error because of the except suite
'''
Because Generators don't store the value and instead sends them one at a time and on demand, they neither have waiting time, nor do they raise a Memory Error regardless of the amount of Outputs.