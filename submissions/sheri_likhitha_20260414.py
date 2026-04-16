from prog10a import Rat   # Importing Rat class

# Creating objects
a = Rat()
b = Rat()
c = Rat()

# Input
print("Enter 1st rational number:")
a.get()

print("Enter 2nd rational number:")
b.get()

# Addition
c.add(a, b)
print("\nc = a + b --->", c)

# Subtraction
c.sub(a, b)
print("c = a - b --->", c)

# Multiplication
c.mul(a, b)
print("c = a * b --->", c)

# Division
if c.div(a, b):
    print("c = a / b --->", c)
else:
    print("Division is not permitted")






from prog10a import Rat   # Import Rat class

# Create list of 6 objects
a = [Rat() for i in range(6)]

# Input
print("Enter 1st rational number:")
a[0].get()

print("Enter 2nd rational number:")
a[1].get()

# Operations
a[2].add(a[0], a[1])   # Sum
a[3].sub(a[0], a[1])   # Difference
a[4].mul(a[0], a[1])   # Product
division_possible = a[5].div(a[0], a[1])   # Division

# Output
print("\na[0] --->", a[0])
print("a[1] --->", a[1])
print("a[2] (Sum) --->", a[2])
print("a[3] (Difference) --->", a[3])
print("a[4] (Product) --->", a[4])

if division_possible:
    print("a[5] (Division) --->", a[5])
    print("Successful division")
else:
    print("Division is not permitted")







# mod1.py  (Home  work)
print('Hyd')	#Hyd
print('Sec')	#Sec
print('Cyb')	#Cyb
#print('India')	#skipped
#print('USA')	#skipped




# Find  outputs  (Home  work)
import  mod1	#Hyd <next> Sec <next> Cyb
import  mod1	#no execution
import  mod1	#no exection because module importedd only once





# reload()  function  demo  program   (Home  work)
import    importlib
import  mod1
print()
importlib . reload(mod1)
print()
importlib . reload(mod1)
importlib . reload('mod1')	#error reload argument must be a module not a string
reload(mod1)




#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))		#list of all members of sys module
print()		#blank line
print()		#blank line
print(dir(time))	#list of all members of time module in string
print()
print(dir(math))	#list of strings of all members in math module and environment variables




#  Find  outputs  (Home  work)
import  cal
print(dir(cal))  #['add', 'sub', 'mul', 'div', 'c1', 'x', 'y'] and environmental variables



#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())	#shows current module members with environmental variables
print(type(dir()))	#<class'list'>
print(type(dir))	#<class 'builtin_function_or_method'>




import cal

# list to store non-environment members
a = []

# get all members of module cal
members = dir(cal)

# filter out environment variables (dunder names)
for item in members:
    if not (item.startswith('__') and item.endswith('__')):
        a.append(item)

# print final list
print(a)






#  Find  outputs
print(dir())
print()
import  cal
print()		#blamk line
print(dir())	#members of current module




#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())	#['add', 'sub', 'mul', 'div', 'c1', 'x', 'y'] and environmental variables





#  Find  outputs
print(dir())	#default module environmental variables
print()		#blank line
from  cal  import  add , mul , x
print()	#blank line
print(dir())	#['add','mul','x'] and enivironmental variables





# sys . path  demo   program
import  sys
print('Original  sys.path')	#Original sys.path
for  x  in   sys . path:
	print(x)		#it's a list prints step by step
print(len(sys . path))		#4
import  cal			#adds to the directory





# sample.py

x = 50

def f1():
    print("Function f1 of sample module")

class c1:
    def m1(self):
        print("Method m1 of class c1 in sample module")


import sys

# 1) Print number of directories in sys.path
print("Initial sys.path length =", len(sys.path))

# 2) Append C:\sairam to sys.path
sys.path.append(r"C:\sairam")

# 3) Print number of directories again
print("After append sys.path length =", len(sys.path))

# 4) Import sample module
import sample

# 5) Print object x of sample module
print("x =", sample.x)

# 6) Call function f1()
sample.f1()

# 7) Call method m1() of class c1
obj = sample.c1()
obj.m1()
 