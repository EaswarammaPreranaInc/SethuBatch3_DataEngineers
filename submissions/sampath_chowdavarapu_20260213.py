# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))   #<class 'range'>
print(a)           #range(10, 50, 5)
print(*a)    #10 15 20 25 30 35 40 45
print(id(a))  # address of the id
print(len(a))  #length of the list
print(*a[2 : 7] , sep = ' , ')    #20 , 25 , 30 , 35 , 40
print(*a[ : : -1])    #45 40 35 30 25 20 15 10
a[4] = 32    # range obj not support the asign value
print(a * 2)  # range not allowed the duplicates




#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')     #   10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)                  #  0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')    #  10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)                 #   -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)                 # error or blank space
f = range(2 , 2)
print(*f)                 # error or blank space
g = range(10 , 11 , 0.1)  # error   in range float obj can't be used
h = range('A' , 'F')     # error  str is can't be used in range 



#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c)   #  10 13 16
r = range(3)   
x , y = r   #  error   
p , q  , r , s = r    #error   no values
a , b , c = *r        #  error   due to using of star
m = r  
print(id(r))  # address of the id
print(id(m))   # address of the id



#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)   #  [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)   #   25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))  #  <class 'list'>
print(id(a))   #  address of the id
print(len(a))  #  len of the list
a[2] = 'Sec'
print(a)    #   [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])  #  ['Sec', True, (3+4j)]



# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)    #  empty list
a . append(25)   
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)      #    [25, 10.8, 'Hyd', True]
a . remove('Hyd')
print(a)      #   [25, 10.8, True]
a . remove('25')  #  error obj is not in a list
print(a)   #   [25, 10.8, True]  



#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)         #   [25, 10.8, 'Hyd']
print(id(a))     #  address of the id
print(a * 3)     #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)     #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)     #[25, 10.8, 'Hyd']
print(a * 0)    #  empty list
print(a * -1)    #  empty list
print(a * 4.0)  # error  float obj can't multiply 
a = a * 3
print(a)    #  [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))  #  address of the id
a = [25]
print(a , id(a))  #  address of the id
print(a * a)   #  can't multiply the non-int




# list()  function  demo  program
a = list('Hyd')
print(a)         # ['H', 'y', 'd']
print(type(a))    #  <class 'list'>
print(len(a))    # len of the list
b = (10 , 20 , 15 , 18)   
print(list(b))   #  [10, 20, 15, 18]
print(list(range(5)))   #  [0, 1, 2, 3, 4]
print(list(25))   # error



# Find  outputs
a = [ ]
print(type(a))   #  <class 'list'>
print(a)          # empty list
print(len(a))   #  length of the list
b = list()
print(b)    # empty list
print(len(b))   #  len of the list




# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])   #  [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])  #   [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:])      #  [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1])   #  ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])    #  [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])    #   ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])   #  [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])  #  [True, None, 10.8]
print(list[3 : -3])   #  ['Hyd', True] 
print(list[2 : -5])   #  [(3+4j)]
print(list[-1:-5])  #  empty list






#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)    #   x :  Hyd
print('y : ' , y)    #  y :  True
for  x  in  list[2:7]:
	print(x)    #   (3+4j)<nxt line>Hyd<nxt line>True<nxt line>None<nxt line>10.8




#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))   #  [10, 20, 30, 40, 50]  address of the id
a[1 : 4] = [60 , 70]
print(a , id(a))    #   [10, 60, 70, 50]   address of the id
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))   #  [10, 60, 100, 200, 300]  address of the id






#  Find  outputs  (Home  work)
a =  [25]
print(a[1])  # error due to no index
print(a[1:])   #  empty list




