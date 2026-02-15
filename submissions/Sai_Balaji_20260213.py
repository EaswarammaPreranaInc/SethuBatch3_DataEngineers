# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))                 #<class 'range'>
print(a)                       #range(10 , 50 , 5)
print(*a)                      #10 15 20 25 30 35 40 45
print(id(a))                   #address of object a
print(len(a))                  #8
print(*a[2 : 7] , sep = ' , ') #20,25,30,35,40
print(*a[ : : -1])             #45 40  35 30 25 20 15 10
a[4] = 32                      #error range is immutable
print(a * 2)                   #error range can not be repeated

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')          #10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)                      #0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')        #10,9,8,7,6,5,4,3,2
d = range(-10 , 0)
print(*d)                      #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)                      #-1 -2 -3 -4 -5 -6 -7 -8 -9 
f = range(2 , 2)
print(*f)                      #error
g = range(10 , 11 , 0.1)       #error range contains only int elements 
h = range('A' , 'F')           #error range contains only int elements 

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c)               #10 13 16  
r = range(3)   
x , y = r                      #error   less objects to assign
p , q  , r , s = r             #error too many objects to assign 
a , b , c = *r                 #a=0 b=1 c=2 
m = r  
print(id(r))                   #address of object r 
print(id(m))                   #address of object m

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                       #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)                      #25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a))                 #<class 'tuple'>
print(id(a))                   #address of object a
print(len(a))                  #8
a[2] = 'Sec'                   #[25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                       #[25 , 10.8 , 'sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])                #['sec' , True , 3 + 4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)                       #[]
a . append(25)                 #[25]
a . append(10.8)               #[25,10.8]
a . append('Hyd')              #[25,10.8,'Hyd]
a . append(True)               #[25,10.8,'Hyd',True]
print(a)                       #[25,10.8,'Hyd',True]
a . remove('Hyd')              #[25,10.8,True]
print(a)                       #[25,10.8,True]
a . remove('25')               
print(a)                       #[10.8,True]

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)                       #[25 , 10.8 , 'Hyd']
print(id(a))                   #address of object a
print(a * 3)                   #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)                   #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)                   #[25 , 10.8 , 'Hyd']
print(a * 0)                   #[]
print(a * -1)                  #[]
print(a * 4.0)                 #error cant be repeated with float
a = a * 3
print(a)                       #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a))                   #address of object a
a = [25]
print(a , id(a))               #[25] address of object a
print(a * a)                   #error list can be repeated with only int objects 

# list()  function  demo  program
a = list('Hyd')
print(a)                       #['H','y','d']
print(type(a))                 #<class 'list'>
print(len(a))                  #3
b = (10 , 20 , 15 , 18)
print(list(b))                 #[10 , 20 , 15 , 18]
print(list(range(5)))          #[0,1,2,3,4]
print(list(25))                #error should be sequence


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
print(type(a))           #<class'list'>
print(a)                 #[]
print(len(a))            #1
b = list()
print(b)                 #[]
print(len(b))            #0


# Slice  demo  program (Home  work)
#        0      1     2        3       4    5        6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7    -6        -5      -4    -3       -2     -1
print(list[2 : 7])                    #[3 + 4j , 'Hyd' , True , None , 10.8]
print(list[ : : ])                    #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])                        #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])                  #['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])                  #[10.8,'Hyd',None,'Hyd']
print(list[ : : -2])                  #['Hyd',10.8,None,True,'Hyd',3+4j,10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])                    #[ 10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])                  # [True , None , 10.8 ]
print(list[3 : -3])                   #['Hyd' , True]
print(list[2 : -5])                   #[ 3 + 4j]
print(list[-1:-5])                    #[]


#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]                  #['Hyd' , True]
print('x : ' , x)                     #x : 'Hyd'
print('y : ' , y)                     #y : True
for  x  in  list[2:7]:
	print(x)
                                      #3+4j 
                                      'Hyd'
                                       True 
                                       None 
                                       10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))                          #[10 , 20 , 30 , 40 , 50] address of object a
a[1 : 4] = [60 , 70]                      #[10 , 60 , 70 , 50]
print(a , id(a))                          #[10 , 60 , 70 , 50] address of object a
a[2: 4] = [100 , 200 ,  300]              #[10 , 60 , 100 , 200 , 300]
print(a , id(a))                          #[10 , 60 , 100 , 200 , 300] address of object a

#  Find  outputs  (Home  work)
a =  [25]
print(a[1])                                  #error index gives error
print(a[1:])                                 #[]
