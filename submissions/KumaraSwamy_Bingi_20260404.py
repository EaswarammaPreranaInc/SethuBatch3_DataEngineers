def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)
for  x  in  f1():
	print(x)

'''
25
10.8
hyd
25
10.8
hyd
25
10.8
hyd
'''

l = [x * x   for   x   in   range(5)]
print(l)      # [0,1,4,9,16]
print(type(l))# <class 'List'>

s = {x * x   for   x   in   range(5)}
print(s)      # {0,1,4,9,16}
print(type(s))# <class 'set  

g = (x * x   for   x   in   range(5))
print(g)
print(type(g)) #<class 'generator'>
import time
def cal(a,b):
	try:
		print("sum : ",end="")
		yield a+b
		
		print("sub : ",end="")
		yield a-b
		
		print("multiplication : ",end="")
		yield a*b
	
		print("div : ",end="")
		yield a/b
	except:
		print("divide by zero error")
'''a=int(input("enter a value : "))
b=int(input("enter b value : "))
gen=cal(a,b)
for x in gen:
	print(x)
	time.sleep(2)'''

def  seq(a,b):
		for i in range(a,b+1):
			yield i
a=int(input("enter a value : "))
b=int(input("enter b value : "))
gen1=seq(a,b)
for x in gen1:
	print(x)
	time.sleep(1)

def fib(x):
	a=0
	b=1
	while(a<x):
		yield a
		a,b=b,a+b
		
n=int(input("enter the number values you want : "))
gen2=fib(n)
for x in gen2:
	print(x)


def words(s):
	for x in s.split():
		yield x

n=input("enter the string : ")
gen3=words(n)
for x in gen3:
	print(x)