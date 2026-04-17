 # Find  outputs    (Home  work)
a = range(10 , 50 , 5)     # 10 15 20 25 30 35 40 45          10 15 20 25 30 35 40 45
print(type(a))   # class 'range'                                   
print(a)  #  range(10, 50, 5)                                  0  1  2  3  4  5  6  7
print(*a)  # 10 15 20 25 30 35 40 45
print(id(a)) # Address of the object range
print(len(a))  # 8
print(*a[2 : 7] , sep = ' , ')   # 20,25,30,35,40
print(*a[ : : -1])              #  45 40 35 30 25 20 15 10               
a[4] = 32                       # Error because range object can't be changed or immutable.
print(a * 2)                    # Error because range can't be multiplied.


#  Find  outputs  (Home  work)
a = range(10 , 20)         #(10 11 12 13 14 15 16 17 18 19)
print(*a , sep = ',')     # 10,11,12,13,14,15,16,17,18,19
b = range(5)              # (0 1 2 3 4)                                                                     
print(*b)                 # 0 1 2 3 4                                                              
c = range(10 , 1 , -1)    # 10 9 8 7 6 5 4 3 2       Here for -ve step y+1                       
print(*c , sep = '...')   # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)        #(-10 -9 -8 -7 -6 -5 -4 -3 -2 -1)
print(*d)                 # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)  # empty
print(*e)       #  empty or nothing
f = range(2 , 2)  # () empty range object because index start 2 and end with 2 
print(*f)   #  empty range object
g = range(10 , 11 , 0.1) # Error in step float not permitted
h = range('A' , 'F')    #  Error only integers allowed 


#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)    # ( 10 13 16 )  here start = 10 and end with 17-1 because of +ve step 3 
a , b , c = r  
print(a , b , c)   # a = 10 , b = 13, c = 16
r = range(3)    # range start with 0 and end with 2 because of +ve step
x , y = r     # here there is only 2 references but r has 3 objects so it will give error and rest of the code will not be executed.
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) #  same id
print(id(m))


 #  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)   # [25 , 10.8, 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)   # 25 , 10.8, 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(type(a))  # class 'list'
print(id(a))  # address of list object
print(len(a))  # 8
a[2] = 'Sec'  # here a[2] is assigning with new string 'sec'
print(a)  #     [25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])   # ['sec' , True , 3 + 4j]


 # append()  and  remove()  methods  (Home  work)
a = [ ]  # empty list
print(a)  # []
a . append(25)   # [25] inserting or adding value at the end of the list
a . append(10.8) # [10.8] inserting or adding value at the end of the list or after 25 
a . append('Hyd') # ['Hyd']  inserting or adding value at the end of the list or after 10.8
a . append(True)  # [True] inserting or adding value at the end of the list or after 'Hyd'
print(a)          # [25,10.8,'Hyd', True]
a . remove('Hyd')  # remove is used to remove 'Hyd' from starting of the list
print(a)           #  [25,10.8, True]
a . remove('25')   #  Error because list has integer 
print(a)         # [25, 10.8,True]



#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)     # [25 , 10.8 , 'Hyd']
print(id(a))  # Address of the list 
print(a * 3)  # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'] Here * is used to repeat the list 3 times .
print(a * 2)  # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']   Here * is used to repeat the list 2 times.
print(a * 1)  # [25 , 10.8 , 'Hyd']   Here * is used to repeat the list only 1 time .
print(a * 0)  # [] Here it will give as an empty list 
print(a * -1)  # Error because list cannot repeat -1 time.
print(a * 4.0)  # Error because it didn't allow float to repeat the list.
a = a * 3  # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a)  #a = [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))   #  Address of the list object
a = [25]    # here reference has changed so new list is created  
print(a , id(a))   # Address of the list object
print(a * a)   # Error because list is repeated or multiplied by integers only.



 # list()  function  demo  program
a = list('Hyd')   # 
print(a)      # ['H', 'y', 'd']
print(type(a))  # class 'list'
print(len(a))   # 1
b = (10 , 20 , 15 , 18) 
print(list(b))  # [10,20,15,18]
print(list(range(5)))  # 0,1,2,3,4
print(list(25))   # Error 


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''


1# Find  outputs
a = [ ]
print(type(a)) # class 'list'
print(a)   # [] empty list
print(len(a))  # 0
b = list()  # 
print(b)  # [] 
print(len(b))  # 0



# Slice  demo  program (Home  work)
#        0      1      2        3      4     5       6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7    -6       -5      -4    -3      -2      -1

print(list[2 : 7])  # [3 + 4j , 'Hyd' , True , None , 10.8]  here start = 2 and end = 7-1 because of positive step
print(list[ : : ])  # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'] start = 0 and end = len(list()) and step = 1
print(list[:])      # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']  Here start = 0 and end  = len(list()) and step = 1
print(list[ : : -1]) # ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]    Here end = -len(list())
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])  # [ 10.8, 'Hyd', None, 'Hyd'] list from indexes 1 to len(lis())=7 and step = 2
print(list[ : : -2])  # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])    # [25 , 10.8 , 3 + 4j]
print(list[-4 : -1])  # [True , None , 10.8]
print(list[3 : -3])   # [ 'Hyd' , True]
print(list[2 : -5])   #  [3 + 4j]
print(list[-1:-5])    #  []  empty list
 


 #  Find  outputs  (Home  work)
#        0     1      2      3       4      5      6      7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]  # Here begin = 3 and end = 5-1=4 and step = 1 then x = 'Hyd' and y = True
print('x : ' , x)   # x: 'Hyd'
print('y : ' , y)    # y: True
for  x  in  list[2:7]:
	print(x)    # (3+4j) 'Hyd' , True , None , 10.8



 #  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))     #   [10 , 20 , 30 , 40 , 50] , Address of list object
a[1 : 4] = [60 , 70]  #  [10, 60, 70, 50]
print(a , id(a))       # [10, 60, 70, 50]
[2: 4] = [100 , 200 ,  300]  
print(a , id(a))  # [10, 60, 100, 200, 300]


#  Find  outputs  (Home  work)
a =  [25]  
print(a[1])  # [] empty list
print(a[1:])  # [] empty list