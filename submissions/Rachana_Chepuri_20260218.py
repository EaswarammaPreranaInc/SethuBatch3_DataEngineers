#  Find  outputs
a = 25						
print(id(a))		#address of the object 25			
a = 35
print(id(a))		#address of the object 35

_________________________________________________

# Find  outputs (Home  work)
a = 25.7
print(id(a))			#address of the object 25.7
print(a)			#25.7
a = 35.6
print(id(a))			#address of the object 35.6
print(a)			#35.6
b = True
print(id(b))			#address of the object True
b = False
print(id(b))			#address of the object False
c = None
print(id(c))			#address of the object None
c = None
print(id(c))			#same address

___________________________________________________________________________________

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))				#address of the object 'Hyd'
a[1] = 'e'				#error because string does not support item assignment    
a = 'Sec'				
print(id(a))				#address of the object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))				#address of the tuple object 
b[2] = 19				#error because 'tuple' object does not support item assignment
b = (30 , 40 , 35 , 32)
print(id(b))				#address of the tuple object 
c = range(5)				#(0,1,2,3,4)
print(id(c))				#address of the range object
c[3] = 10				#error because range does not support item assignment
c = range(5)				#(0,1,2,3,4)
print(id(c))				#address of the range object

______________________________________________________________________________

# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)			#True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)			#True
e = False
f = False
print(e  is  f)			#True
g = range(10)
h = range(10)
print(g  is  h)			#False

____________________________________________________________________________

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)			#False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)			#False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)			#True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)			#False

__________________________________________________________________________

# Find outputs (Home work)
print(10 + 20)						#30
print(10.8 + 20.6)					#31.4
print(3 + 4j + 5 + 6j)					#8+10j
print(True + False)					#1
print('Hyder' + 'abad')					#Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')			#SankarDayalSarma
print('10' + '20')					#1020
print([10 , 20 , 30] + [1 , 2 , 3])			#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))	#(25,10.8,'Hyd',(3+4j),True, None)
print({10 , 20} + {30 , 40})				#error because sets does not support +
print({10 : 'Hyd'} + {20 : 'Sec'})			#error because sets does not support +
print(range(4) + range(5))				#error because range objects does not support + operator
print(10 + '20')					#error because does not add int objects and string objects
print([10 , 20 , 30] + 5)				#error because cannot add sequences and non sequence
print([10 , 20 , 30] + (40 , 50 , 60))			#error because can only concatenate list to list not list to tuple

______________________________________________________________________________-

# Find outputs (Home work)
print(25 * 3)				#75
print(10.8 * 25.6)			#276.48
print(True * False)			#0
print((3 + 4j) * (5 + 6j))		#(-9+38j)
print(3 + 4j * 5 + 6j)			#(3+26j)
print('25' * 3)  			#252525
print(3 * '25')				#252525
print('Hyd' * 4)			#HydHydHyd
print([10 , 20 , 15] * 2)		#[10 , 20 , 15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)	#(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)		#error because second operand must be integer
print({10 , 20 , 15} * 2)		#error because set does not allows duplicates
print({10 : 20 , 30 : 40} * 2)		#error because dictionary does not allows duplicate keys
print([10] * [20])			#error because second operand must be integer

__________________________________________________________________________________

