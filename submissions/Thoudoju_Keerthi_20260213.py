1)# Find  outputs    (Home  work)
---------------------------------
a = range(10 , 50 , 5) 
print(type(a)) --------> <class 'range'>
print(a)	--------> range(10,50,5)
print(*a)	--------> 10 15 20 25 30 35 40 45
print(id(a))   --------> <Address of Object a>
print(len(a))  --------> 8
print(*a[2 : 7] , sep = ' , ') -----> 20 25 30 35 40
print(*a[ : : -1])		----->  40 35 30 25 20 15 10
a[4] = 32        ---------> Error(immutable)
print(a * 2)      ---------> Error(no duplicates)

2)#  Find  outputs  (Home  work)
--------------------------------
a = range(10 , 20) 
print(*a , sep = ',')  ------->10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)		------> 0 1 2 3 4
c = range(10 , 1 , -1)  ------> 9 8 7 6 5 4 3 2
print(*c , sep = '...') ------->9,8,7,6,5,4,3,2
d = range(-10 , 0) 
print(*d)               --------> -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)           
print(*e)		---------> nothing prints
f = range(2 , 2)	
print(*f)		---------> nothing prints
g = range(10 , 11 , 0.1) ---------> Error
h = range('A' , 'F')    ----------> Error

3)#  Find  outputs  (Home  work)
-----------------------------------
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) ------> 10, 17, 3
r = range(3)   
x , y = r    -------> Error (not enough values to unpack)
p , q  , r , s = r -------> Error (more values to unpack)
a , b , c = *r  -------> Error (*r is not allowed)
m = r  
print(id(r))  -----><Address1>
print(id(m))	-----><Address1>


4)#  Find  outputs  (Home  Work)
--------------------------------
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) 	---------> [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)       ---------> 25 10.8 'Hyd' True 3 + 4j None 'Hyd' 25
print(type(a))  ---------> <class 'list'>
print(id(a))    ---------><Address of object a>
print(len(a))   -------> 8
a[2] = 'Sec'
print(a)       --------> [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])		--------> ['Hyd' , True , 3 + 4j ]

5) # append()  and  remove()  methods  (Home  work)
---------------------------------------------------
a = [ ]
print(a) 	--------> []
a . append(25)  
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)    	------->[25, 10.8, 'Hyd', True]
a . remove('Hyd') 
print(a)
a . remove('25')
print(a)	 	------->[25, 10.8, True]


6)#  Find  outputs  (Home  work)
--------------------------------
a = [25 , 10.8 , 'Hyd']
print(a)	------>[25 , 10.8 , 'Hyd']
print(id(a))	------><Adress of list object a>
print(a * 3)   -------> [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)	------>[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)	------->[25 , 10.8 , 'Hyd']
(a * 0)		------->[]
print(a * -1)   ------->[]
print(a * 4.0)  -------> Error
a = a * 3
print(a)	------->[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a))    -------> <Address of modified list a>
a = [25]
print(a , id(a))  ------>25,<Address of [25]>
print(a * a)     -------->Error non-seq*non-seq

7) # list()  function  demo  program
--------------------------------------
a = list('Hyd')
print(a)	------->['Hyd']
print(type(a))  -------><class 'list'>
print(len(a))	-------> 1
b = (10 , 20 , 15 , 18)
print(list(b))  ------->[10 , 20 , 15 , 18]
print(list(range(5))) ------->[0, 1, 2, 3, 4]
print(list(25))    ---------->[25]


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''
8) # Find  outputs
------------------
a = [ ]
print(type(a))	-------><class 'list'>
print(a)	------->[]
print(len(a))  --------->0
b = list()
print(b) -------------->[]
print(len(b)) --------->0

9) # Slice  demo  program (Home  work)
----------------------------------------
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) ------>[3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ]) ------>[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])	   ------>[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) ----->['Hyd' , 10.8 , None ,  True ,'Hyd' , 3 + 4j , 10.8 , 25 ]
print(list[ : : 2])  #  list[0 : 8 : 2]--->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])	----> [10.8, True, 3 + 4j, 25 ]
print(list[ : : -2])	----> ['Hyd' ,  None ,  True ,3 + 4j , 25 ]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])  ------>[10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])------>[25 , 10.8 , 3 + 4j , 'Hyd' , True]
print(list[3 : -3])------->['Hyd' , True ]
print(list[2 : -5])------->[3 + 4j]
print(list[-1:-5])--------->[]

10) #  Find  outputs  (Home  work)
------------------------------------
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) 	------> 'x : ' , 'Hyd'
print('y : ' , y)	------>'y : ' ,True
for  x  in  list[2:7]:
	print(x)       ------->2
		               3
			       4
			       5
			       6
		

11) #  Find  outputs  (Home  work)
----------------------------------
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) -------> [10 , 20 , 30 , 40 , 50],<Address of object a>
a[1 : 4] = [60 , 70]
print(a , id(a)) -------> [10 , 60 , 70, 50],<Address of modified object a >
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) 	------>[10 , 60 , 100 , 200 ,  300],<Address of modified object a >

12)#  Find  outputs  (Home  work)
----------------------------------
a =  [25]
print(a[1])  ---> 25
print(a[1:]) ----> []