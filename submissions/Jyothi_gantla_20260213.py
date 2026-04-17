#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                     # [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a)                    # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))               # <class 'list'>
print(id(a))                 # memory address (changes every run)
print(len(a))                # 8
a[2] = 'Sec'
print(a)                     # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])              # ['Sec', True, (3+4j)]

# append()  and  remove()  methods
a = [ ]
print(a)                     # []
a.append(25)
a.append(10.8)
a.append('Hyd')
a.append(True)
print(a)                     # [25, 10.8, 'Hyd', True]
a.remove('Hyd')
print(a)                     # [25, 10.8, True]
a.remove('25')               # Error – '25' (string) is not in list
print(a)                     # [25, 10.8, True]









#  Find  outputs
a = [25 , 10.8 , 'Hyd']
print(a)                     # [25, 10.8, 'Hyd']
print(id(a))                 # address of the object
print(a * 3)                 # list repeated 3 times
print(a * 2)                 # list repeated 2 times
print(a * 1)                 # same list
print(a * 0)                 # []
print(a * -1)                # [] (negative gives empty list)
print(a * 4.0)               # Error – list can multiply only with integer
a = a * 3
print(a)                     # list repeated 3 times
print(id(a))                 # new address (new list created)
a = [25]
print(a , id(a))             # [25] memory address
print(a * a)                 # Error – cannot multiply list with list






# list()  function
a = list('Hyd')
print(a)                     # ['H', 'y', 'd']
print(type(a))               # <class 'list'>
print(len(a))                # 3
b = (10 , 20 , 15 , 18)
print(list(b))               # [10, 20, 15, 18]
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(list(25))              # Error 




# Find  outputs
a = [ ]
print(type(a))               # <class 'list'>
print(a)                     # []
print(len(a))                # 0
b = list()
print(b)                     # []
print(len(b))                # 0







# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])      #[3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ])      #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])         #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])   #['Hyd', 10.8, None, True, 'Hyd', 3+4j,10.8, 25 ]
print(list[ : : 2])   #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])   #[10.8 , 'Hyd' , None , 'Hyd']
print(list[ : : -2])   #['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])   #[10.8 , 3 + 4j , 'Hyd' ]
print(list[-4 : -1])   #[True , None , 10.8 , 'Hyd']
print(list[3 : -3])   #['Hyd']
print(list[2 : -5])  #[3 + 4j ]
print(list[-1:-5]) #['Hyd', 10.8, None, True]



#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #x: 'Hyd'
print('y : ' , y) #y: True
for  x  in  list[2:7]:
	print(x) #3+4j 
                  Hyd
                  True 
                  None 
                  10.8 
                  Hyd



#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10,20,30,40,50] 1000
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10,60, 70,50] 1000
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))   #[10,60,100,200,400] 1000



#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) #Error  
print(a[1:])#[ ]
