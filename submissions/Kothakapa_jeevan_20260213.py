# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))    --- Class range
print(a)   ---- (10,50,5)
print(*a) --- 10 15 20 25 30 35 40 45 50
print(id(a)) --- 5000 ( address of the object range)
print(len(a)) --- 8
print(*a[2 : 7] , sep = ' , ') -- 20,25,30,35,40
print(*a[ : : -1])  ---  50 45 40 35 30 25 20 15 10
a[4] = 32 ---  10 15 20 25 32 35 40 45 50 
print(a * 2)  - Error
0   	 1  	  2 	 3 	   4	   5 	  6  	 7    	 8
10 	15 	20 	25	 30	 35	 40	 45	 50
-9	-8	-7	-6	-5	-4	-3	-2	-1

								

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')  - 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)  -- 01234
c = range(10 , 1 , -1) --  9 8 7 6 5 4 3 2
print(*c , sep = '...')  -- 9…8…7…6…5…4…3…2
d = range(-10 , 0)  
print(*d)  --- 10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)   ---  error
f = range(2 , 2)
print(*f)   - 
g = range(10 , 11 , 0.1)  -- error step must int not float
h = range('A' , 'F')   --- range must be int elements not str

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c)  -- 10 13 16
r = range(3)   
x , y = r   - error
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r))  -- 1000
print(id(m)) - 1000  (both will get same id coz r object elements are assigned to m)

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)  --- [25,10.8,Hyd,True,(3+4j),None,Hyd,25]
print(*a) -- 25,10.8,Hyd,True,(3+4j),None,Hyd,25
print(type(a)) class list  
print(id(a)) 55500   - reference of object a 
print(len(a))   - 8
a[2] = 'Sec'
print(a) -- [ 25,10.8,Sec,True,(3+4j),None,hyd,25]
print(a[2 : 5]) - [Sec,True,(3=+4j)]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) -- []
a . append(25) -- [25]
a . append(10.8) - [25,10.8]
a . append('Hyd') - [25,10.8,Hyd]
a . append(True) -- [25,10.8,Hyd,True]
print(a)  -- [25,10.8,Hyd,True]
a . remove('Hyd')
print(a) -- [25,10.8,True]
a . remove('25')
print(a) --- error  (error because there Is no str25 in the list elements)


#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)  - [25,10.8,Hyd] 
print(id(a)) ---> 6666 (id is the reference of list a)
print(a * 3) -- [25,10.8,Hyd, 25,10.8,Hyd, 25,10.8,Hyd]
print(a * 2) --- [25,10.8,Hyd, 25,10.8,Hyd]
print(a * 1) ---  [25,10.8,Hyd]
print(a * 0) -- []
print(a * -1)  --  []
print(a * 4.0) -- error  
a = a * 3
print(a) --- [25,10.8,Hyd, 25,10.8,Hyd, 25,10.8,Hyd]
print(id(a))
a = [25]
print(a , id(a))  - [25] 14545
print(a * a)   -- error

# list()  function  demo  program
a = list('Hyd')
print(a)  - Hyd
print(type(a)) - class list
print(len(a)) -- 1
b = (10 , 20 , 15 , 18)
print(list(b)) -[10,20,15,18]
print(list(range(5))) - [0,1,2,3,4]
print(list(25)) - error (single element can’t be converted into list)


# Find  outputs
a = [ ]
print(type(a)) - class list
print(a) - []
print(len(a)) -- 0
b = list()
print(b) - []
print(len(b)) -0  


# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])  -[( 3 + 4j) , Hyd , True , None , 10.8]
print(list[ : : ])  -- [25 , 10.8 , (3 + 4j) , Hyd , True , None , 10.8 , Hyd]
print(list[:])  --  [25 , 10.8 , (3 + 4j) , Hyd , True , None , 10.8 , Hyd]
print(list[ : : -1])  - [Hyd,10.8,None,True,Hyd,(3+4j),10.8,20]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) -- [10.8,HYd,None,Hyd]
print(list[ : : -2]) -- [Hyd,None,Hyd,10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) -- [10.8,(3+4j),Hyd]
print(list[-4 : -1]) -- [True,None,10.8,]
print(list[3 : -3]) - [Hyd,True]
print(list[2 : -5]) - [
print(list[-1:-5]) -
