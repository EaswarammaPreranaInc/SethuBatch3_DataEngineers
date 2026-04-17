#  Find  outputs
a = 25
print(id(a))	#address of the object 25
a = 35
print(id(a))	#address of the object 35


# Find  outputs (Home  work)
a = 25.7
print(id(a))	#address of the object 25.7
print(a)	#25.7
a = 35.6	
print(id(a))	#address of the object 35.7
print(a)        #35.6
b = True
print(id(b))    #address of the object True
b = False
print(id(b))    #address of the object False
c = None
print(id(c))    #address of the object None
c = None
print(id(c))    #address of the object None--->same address of previous one


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))		#address of object 'Hyd'
a[1]='e'		#error string object does not support item assignment
a = 'Sec'
print(id(a))		#address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))		#address of object 'tuple'
b[2] = 19		#error tuple object does not support item assignment 
b = (30 , 40 , 35 , 32)
print(id(b))		#address of object 'tuple' 
c = range(5)		
print(id(c))		#address of object 'range'
c[3] = 10		#error 'range' object does not support item assignment 
c = range(5)		
print(id(c))		#address of object 'range'


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)		#True-->uses integer caching for small integers
c = 'Hyd'
d = 'Hyd'
print(c  is  d)		#True-->due to string interning it optimizes memory by storing identical short strings at the same address 
e = False
f = False
print(e  is  f)		#True-->booleans are singletons in python, there is only one True and False object in memory
g = range(10)
h = range(10)
print(g  is  h)		#False-->range() creates new object every time it is called even same sequence also,they are distinct object in memory


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)		#False-->lists are mutable,it creates two distinct objects in memory
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)		#False-->dictionaries are mutable,these are two seperate objects
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)		#True-->Tuples are immutable,identical small literal tuples are same memory address
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)		#False-->sets are mutable,it creates two seperate set objects


# Find outputs (Home work)
print(10 + 20)			#30
print(10.8 + 20.6)		#31.4
print(3 + 4j + 5 + 6j)		#(8+10j)
print(True + False)		#1
print('Hyder' + 'abad')		#Hyderabad--->string concatenation
print('Sankar' + 'Dayal' + 'Sarma')	#SankarDayalSarma-->string concatenation
print('10' + '20')			#1020--->string concatenation
print([10 , 20 , 30] + [1 , 2 , 3])	#[10,20,30,1,2,3]--->list concatenation
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))	#(25,10.8,'Hyd',(3+4j),True,None)--->tuple concatenation
print({10 , 20} + {30 , 40})		#error it does not support for 'set' concatenation
print({10 : 'Hyd'} + {20 : 'Sec'})	#error it does not support for 'dict' concatenation
print(range(4) + range(5))		#error it does not support for 'range' concatenation
print(10 + '20')			#error it does not support for 'str' and 'int' concatenation
print([10 , 20 , 30] + 5)		#error it can only concatenate  list, not int with list 
print([10 , 20 , 30] + (40 , 50 , 60))	#error it can only concatenate list,not tuple with list


# Find outputs (Home work)
print(25 * 3)			#75
print(10.8 * 25.6)		#276.4
print(True * False)		#0
print((3 + 4j) * (5 + 6j))	#(-9+38j)
print(3 + 4j * 5 + 6j)		#(3+26j)
print('25' * 3)			#252525
print(3 * '25')			#252525
print('Hyd' * 4)		#HydHydHydHyd
print([10 , 20 , 15] * 2)	#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) #(25,10.8,'Hyd',True,25,10.8,'Hyd',True,25,10.8,'Hyd',True)
print([10 , 20 , 15] * 3.0)	#error we cannot multiply with float
print({10 , 20 , 15} * 2)	#error we can't repeat set and int
print({10 : 20 , 30 : 40} * 2)  #error it does not support 'dict' and 'int' 
print([10] * [20])		#error cannot multiply sequence by non-int of type 'list'