# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))    #<class 'float'> 
print(a)          # range(10,50,5)
print(*a)         # unpacking 10 15 20 25 30 35 40 45 i.e,it will print elements from 10 to 49 in steps of 5
print(id(a))      # address of range object
print(len(a))     # 8, number of elements in
print(*a[2 : 7] , sep = ' , ') # 20 25 30 35 40 
print(*a[ : : -1])        # elements of range object from -1 to -9 in steps of -1, i.e, 45 40 35 30 25 20 15 10
a[4] = 32     # error because it is an immutable 
print(a * 2)  # duplicate elements ar not allowed in range


#  Find  outputs  (Home  work)
a = range(10 , 20)     # range(10,20,1), here default step is 1
print(*a , sep = ',')  # 10,11,12,13,14,15,16,17,18,19 i.e,unpack of range, elements start from 10 to 19 in steps of 1

b = range(5)           # range(1,5,1) i.e, range start from 1  to 4 in steps of 1
print(*b)              #  1 2 3 4 

c = range(10 , 1 , -1)  # elements of range start from 10 to 1 in steps of -1 
print(*c , sep = '...') # 10...9...8...7...6...5...4...3...2

d = range(-10 , 0)      # elements start from -10 to -1 in steps of 1
print(*d)               # -10 -9  -8 -7 -6 -5 -4 -3 -2 -1

e = range(-10)        
print(*e)               # no output  because it will never goes back on positive step

f = range(2 , 2)       
print(*f)                # empty object we cannot reach 2 from 2 in steps of 1

g = range(10 , 11 , 0.1) # erroe because range cannot hold float objects
h = range('A' , 'F')     # error range cannot hold str values

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3) # start from 10 to 16 in steps of 3, i.e, 10,13,16
a , b , c = r  
print(a , b , c)        # 10 13 16 

r = range(3)   
x , y = r                # error because of excess elements
p , q  , r , s = r       # error because of excess elements
a , b , c = *r           # error because *
m = r                    # reference m points to r
print(id(r))             # address of r
print(id(m))             # same address 

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)        # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)       # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a))  # <class 'list'>
print(id(a))    # address of list
print(len(a))   # 8, number of elements in the list

a[2] = 'Sec'    # Hyd is modified to sec
print(a)        # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # ['Sec' , True , 3 + 4j]  

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)            # [] empty
a . append(25)      # [25] 
a . append(10.8)    # [25,10.8]
a . append('Hyd')   # [25,10.8,'Hyd']
a . append(True)    # [25,10.8,'Hyd',True]
print(a)            # [25,10.8,'Hyd',True]
a . remove('Hyd')  
print(a)            #[25,10.8,,True]
a . remove('25')
print(a)            # error there is no string 25 in the list

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)          #[25 , 10.8 , 'Hyd']
print(id(a))      # address of list a
print(a * 3)      #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)      #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)      #[25 , 10.8 , 'Hyd']
print(a * 0)      # no output
print(a * -1)     # no output
print(a * 4.0)    # it not contains float values

a = a * 3          #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a)           #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a))       # address of list with 9 elements
a = [25]           # ref is modified to [25]
print(a , id(a))   # [25] address of a 
print(a * a)       # list element is int

# list()  function  demo  program
a = list('Hyd')
print(a)        #['H','y','d']
print(type(a))  #<class 'float'>
print(len(a))   # 3

b = (10 , 20 , 15 , 18)
print(list(b))        #[10 , 20 , 15 , 18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25))       #error its not a sequence

# Find  outputs
a = [ ]
print(type(a)) # <class 'list'>
print(a)       # []
print(len(a))  # 0
b = list()  
print(b)       # []
print(len(b))  # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 ,   10.8 ,     3 + 4j , 'Hyd' ,   True ,   None ,    10.8 ,  'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])     # [3 + 4j , 'Hyd' ,   True ,   None ,    10.8]
print(list[ : : ])     # list[ 0:8 :1 ] from 0 to 7 in steps of 1, i.e,[25 ,  10.8 ,3 + 4j,'Hyd', True,None, 10.8 ,'Hyd']
print(list[:])         # list[ 0:8 :1 ] from 0 to 7 in steps of 1, i.e,[25 ,  10.8 ,3 + 4j,'Hyd', True,None, 10.8 ,'Hyd']
print(list[ : : -1])   #List  -1  to  -8  in  steps  of   -1  i.e.  ['Hyd , 10.8 , None , True , 'Hyd' , 3 + 4j , 10.8 , 25]
print(list[ : : 2])    #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])   #list[1 : 8 :2] i.e,  1  to  7 in  steps  of   2  i.e.  [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])    #[-1:-9:-2]--->List  from  indexes   -1  to  -8  in  steps  of   -2 i.e['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #  list[-2 : -9 : -2]   List  of indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])      #[1:4:1]  List  from  indexes   1  to  3  in  steps  of   1  i.e[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])    #[-4:-9:-1]--->List  from  indexes   -4  to  -8  in  steps  of   -1 i.e[True, 'Hyd', (3+4j), 10.8, 25]
print(list[3 : -3])     #  list[3 : -3 :1]  --->  List  from  indexes   3  to  -4  in  steps  of   1  i.e.  ['Hyd' , True]
print(list[2 : -5])     #  list[2 : -5 :1]--->  List  from  indexes   2 to -6 in steps of 1 i.e [3 + 4j]
print(list[-1:-5])     #  list[-1 : -5 :1]--->  List  from  indexes -1 to -6 in steps of 1 i.e []

#  Find  outputs  (Home  work)
#        0      1         2        3          4       5         6        7
list = [25 ,  10.8 ,    3+4j ,    'Hyd' ,   True ,   None ,    10.8 ,  'Hyd']
x ,  y = list[3 : 5]  #  x , y = ['Hyd' , True]
print('x : ' , x)  #  x :  Hyd
print('y : ' , y) #   y : True
for  x  in  list[2:7]:  #  for   x  in  [3+4j , 'Hyd' , True , None ,  10.8]
	print(x) #  3+4j  <new line>  Hyd  <new line>  True  <new line>  None  <new line>   10.8  <new line>

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10 , 20 , 30 , 40 , 50]   <space>  Address of list
a[1 : 4] = [60 , 70]   #   Modifies  elements  of  list  from  indexes  1  to  3  to  60 , 70
print(a , id(a)) # [10 , 60 , 70 ,  50]   <space>  Same  address
a[2: 4] = [100 , 200 ,  300]  #   Modifies  elements  of  list  from  indexes   2  to  3  to  100 , 200 , 300
print(a , id(a)) #[10,60,100,200,300]  <space> Same  address


#  Find  outputs  (Home  work)
a =  [25]
#print(a[1]) # Error
print(a[1:]) # List  without  first  element  i.e. []




