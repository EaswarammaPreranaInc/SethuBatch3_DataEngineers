# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) --> # range object
print(a) ---> # range(10 , 50 , 5)
print(*a) ---> # 10 50 5
print(id(a)) ---> # reference to object
print(len(a)) ---> # 3
print(*a[2 : 7] , sep = ' , ') ---> [2,3,4,5,6,7]
print(*a[ : : -1]) ---> (*a[-1:50:-1])
a[4] = 32 ---> 32
print(a * 2)---> 10,50,5,10,50,5


#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')---> # 10,11,12,13,14,15,16,17,18,19,20
b = range(5) 
print(*b) ---> # 0 1 2 3 4 5 
c = range(10 , 1 , -1)
print(*c , sep = '...') ---> # Error
d = range(-10 , 0)
print(*d) ---> # -10 0
e = range(-10)
print(*e) --> # -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
f = range(2 , 2)
print(*f) # 0 1 2 , 0 1 2 
g = range(10 , 11 , 0.1) --># Error range can't hold float objects
h = range('A' , 'F') ---> # Error range can't hold string objects

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r 
print(a , b , c) r
r = range(3)   ---> (range(10,17,3) range(10,17,3) range(10,17,3) )
a =  [25]  
print(a[1]) ---> a(0:25:1)
print(a[1:])) ---> a(1: 25 : 1)
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) ---> 
print(id(m))

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) ---> [25, 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd']
print(*a) ---> 25,10.8, Hyd, True, 3+4j, None, 'Hyd'
print(type(a)) ---># range object
print(id(a)) ---> # address of object
print(len(a)) ---> # 8
a[2] = 'Sec'
print(a) ---> 'Sec'
print(a[2 : 5]) ---> (a[2 :5 :1]) --> 'Hyd' True 3 + 4j None 

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) --> # []
a . append(25) ---> # [25]
a . append(10.8) ---> #[25,10.8]
a . append('Hyd') ---># [25,10.8,'Hyd']
a . append(True) ---># [25,10.8,'Hyd',True]
print(a)----> # [25,10.8,'Hyd',True]
a . remove('Hyd')--->  # [25,10.8,True]
print(a)---> # [25,10.8,True]
a . remove('25') ---> # [10.8,True]
print(a)---> #[10.8, True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) ---> # [25 , 10.8 , 'Hyd']
print(id(a)) ---> # 
print(a * 3) # 25,10.8,'Hyd'25,10.8,'Hyd'25,10.8,'Hyd'
print(a * 2) --> # 25,10.8,'Hyd'25,10.8,'Hyd'
print(a * 1)---> 25,10.8,'Hyd'
print(a * 0)--->  # <space>
print(a * -1) ----> # <space>
print(a * 4.0) ---> # <space>
a = a * 3
print(a)--> # 25,10.8,'Hyd'25,10.8,'Hyd'25,10.8,'Hyd'
print(id(a)) ---> # address of object
a = [25]
print(a , id(a))
print(a * a)

# list()  function  demo  program
a = list('Hyd')
print(a) ---> ['Hyd']
print(type(a)) ---> list object
print(len(a))---> 3
b = (10 , 20 , 15 , 18)
print(list(b)) ---> 4 
print(list(range(5))) ---> # error
print(list(25)) ---> # error no 25 in list


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''

# Find  outputs
a = [ ]
print(type(a)) ---> list object
print(a) <space>
print(len(a)) ---> 1
b = list() 
print(b) ---> list()
print(len(b)) ---> 6

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) --> # [2 : 7 : 1] --> 3 + 4j , 'Hyd' , True ,None , 10.8 , 'Hyd'  
print(list[ : : ]) ---> # [0 : 8 : 1] 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'
print(list[:])----># 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'
print(list[ : : -1])----> #[-1 : -9 : -1]---->  'Hyd', 10.8, None , True, 'Hyd', 3 +4j, 10.8 ,25 
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])--> # list[1 : 8 : 2]   --->  List  from  indexes  1  to  7  in steps  of  2  i.e.   [10.8 , 'Hyd', None , 'Hyd']
print(list[ : : -2])--> # list[-1 : -9 : -2]   --->  List  from  indexes  -1  to  -8  in steps  of  -2  i.e.   ['Hyd',10.8 , 'Hyd', None , 'Hyd']
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])  # list [1 : 4 : 1] ---> list fom indexes 1 to 4 in steps of 1 i.e [10.8, 'Hyd', True, None]
print(list[-4 : -1]) # list [-4 : 1 : -1] ---> list fom indexes -4 to -1in steps of 1 i.e [10.8, 'Hyd', True, None]
print(list[3 : -3]) 
print(list[2 : -5])
print(list[-1:-5])

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)
print('y : ' , y)
for  x  in  list[2:7]:
	print(x)

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) ---> 
a[1 : 4] = [60 , 70]
print(a , id(a))
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) --> # 25
print(a[1:]) ---> # [1:2:1] --> 2,5

