# Find  outputs    (Home  work)
a = range(10 , 50 , 5) # 10 15 20 25 30 35 40 45
print(type(a)) # <class ‘range’>
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # Address of the object , i.e 185000
print(len(a)) # Number of elements, that is 8
print(*a[2 : 7] , sep = ' , ') # Elements from index 2 that is 20 to index 7 that is 45 that means       20 , 25, 30, 35, 40, 45
print(*a[ : : -1]) # a[-1: -8 : -1], reversing the range elements that is 45 40 35 30 25 20 15 20
a[4] = 32 # Error, because range object is immutable
print(a * 2) # Error, because range object does not duplicates, so it does not support repeatation.

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # Default step is 1; 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
b = range(5)
print(*b) # Default start is 0 and default step value is 1 so, 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # start is 10, end is 1 with step value -1 with separator … so, 
10…9…8…7…6…5…4…3…2
d = range(-10 , 0) 
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) # Error because start is 0, end is -10 with step value 1 so with adding 1 each time with 0 reach -10 is not possible.
f = range(2 , 2)
print(*f) # Empty range because start is 2 and end is 2, where there are no elements between them.
g = range(10 , 11 , 0.1) # Error because step value should be only integer
h = range('A' , 'F') # Error, range object does not support str objects.

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # 10 , 13, 16
a , b , c = r  
print(a , b , c) # 10 13 16
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) 
print(id(m))

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25  10.8  'Hyd'  True , 3 + 4j , None 'Hyd'  25
print(type(a)) # <class ‘list’>
print(id(a)) # Address of list object
print(len(a)) # 8
a[2] = 'Sec' 
print(a) # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # ['Sec' , True , 3 + 4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # [ ]
a . append(25) 
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) # [25, 10.8, ‘Hyd’, True]
a . remove('Hyd')
print(a) # [25, 10.8, True]
a . remove('25')
print(a) # Error, because there is no element ‘25’ in the list

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) # Address of the list object 
print(a * 3) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8 , 'Hyd']
print(a * 0) # Empty list
print(a * -1) # Empty list
print(a * 4.0) # Error because , it can be multiplied only by integer
a = a * 3 
print(a) #   [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) # New address of the list object
a = [25]
print(a , id(a)) # [25]  Again New address of the list object
print(a * a)  # Error, it can be only multiplied by integer only.


# list()  function  demo  program
a = list('Hyd')
print(a) # [‘H’ , ‘y’, ‘d’]
print(type(a)) # <class ‘list’>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10 , 20 , 15 , 18]
print(list(range(5))) # First it is converted to list and range is found [0, 1, 2, 3, 4]
print(list(25)) # 

# Find  outputs
a = [ ]
print(type(a)) # <class ‘list’>
print(a) # [] Empty list
print(len(a)) # 0 because it is empty list with no elements
b = list()
print(b) # [], Empty list
print(len(b)) # 0, because it is empty list with no elements







# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # Elements from index 2 to index 7 , [3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'], because default start is 0, end is length-1 and default step value is 1.
print(list[:]) # Same , [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # Reverse list , ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # Start at index 1 with step value 2, [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # Starting at index -1 with step value -2 , reverse list with step value -2
['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # Elements from index 1 to index 3 , [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # Start index -4 , [True, None, 10.8]
print(list[3 : -3]) # Start index 3 , elements of index 3 and index 4, ['Hyd', True]
print(list[2 : -5]) # Start index 2, -5 is not included so [(3+4j)]
print(list[-1:-5]) # Start index -1 , end index -5 with default step value +1 , it is not possible to move towards left.







#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # start index 3 and stop at index 4, [‘Hyd’ , True]
print('x : ' , x)  # ‘Hyd’
print('y : ' , y) # True
for  x  in  list[2:7]:
	print(x) # Slicing start from index 2 and stops at index 6 [3+4j , 'Hyd' , True , None , 10.8 ]
	print(x) # (3+4j)
                               ‘Hyd’
                                True
                                None
                                10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] Address of the list object i.e, 123000
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10, 60, 70, 50] Same Address of the list object i.e , 123000
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [10, 60, 100, 200, 300] Same address of the object i.e, 123000

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error because there is no element at index 1 in list a
print(a[1:]) # Empty list because as there is no element at index 1 so there is no slicing happening. 
