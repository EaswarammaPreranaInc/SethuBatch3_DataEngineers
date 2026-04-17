#Topic-1
 # Find  outputs    (Home  work)
a = range(10 , 50 , 5) 
print(type(a)) # <class ‘range’ >
print(a) # range(10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # address of the range(10 , 50 , 5)
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') # 20, 25, 35, 40, 45
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
a[4] = 32 # error it is immutable 
print(a * 2) # error no repetition is not allowed 
#Topic-2

#  Find  outputs  (Home  work)
a = range(10 , 20) 
print(*a , sep = ',') #10to19 with “, ” saparated
b = range(5) 
print(*b) #0to4
c = range(10 , 1 , -1) 
print(*c , sep = '...') #10to2 with “...” saparated 
d = range(-10 , 0) 
print(*d)# -10 to - 1
e = range(-10) #range(0,-10,1)
print(*e)  # empty range
f = range(2 , 2) 
print(*f) # empty range #error difference is 0 so step cannot be zero 
g = range(10 , 11 , 0.1) # error no float in range 
h = range('A' , 'F') # error no str in range
#Topic-3
 #  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) # 10 13 16
r = range(3)   
x , y = r # error less references  
p , q  , r , s = r # error more references  
a , b , c = *r  #error it is used for unpacking 
m = r  
print(id(r))  # address of range (3)
print(id(m))# same address of range (3)

#Topic-4

 #  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 10.8   Hyd   True  3 + 4j  None Hyd 25 
print(type(a)) #<class 'list'>
print(id(a)) # address of the list
print(len(a)) # 9
a[2] = 'Sec' 
print(a) #[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) # ['Sec' , True , 3 +4 j] 
#Topic-5

 # append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) [ ] 
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25, 10.8, ‘Hyd’, True] 
a . remove('Hyd')
print(a)  #[25, 10.8, True] 
a . remove('25')
print(a) error because it is str 25

#Topic-6

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25 , 10.8 , 'Hyd']
print(id(a)) #address of list
print(a * 3) # 3times same list
print(a * 2) # 2times same list
print(a * 1) # 1times same list
print(a * 0) #empty list 
print(a * -1) #empty list 
print(a * 4.0)  # error not possible to repetitive for float 
a = a * 3 
print(a) # 3times same list
print(id(a)) # new address of list
a = [25]
print(a , id(a)) # [25] address of list 
print(a * a) #error cannot multiply

#Topic-7
 # list()  function  demo  program
a = list('Hyd')
print(a) # [‘H’, ‘y’, ‘d’] 
print(type(a)) #<class ‘list’>
print(len(a)) #3
b = (10 , 20 , 15 , 18) 
print(list(b))  #[10,20,15,18 ] 
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(25)) # error non- sequenced type 

'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''
#Topic-8

 # Find  outputs
a = [ ]
print(type(a)) #<class ‘list’>
print(a) #[ ] 
print(len(a)) #0
b = list() 
print(b) # [ ] 
print(len(b)) # 0
#Topic-9
 # Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #[3 + 4j , 'Hyd' , True , None , 10.8 ] 
print(list[ : : ])  #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'] 
print(list[ : : -1]) # reverse list
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # index 1 3 5 7
print(list[ : : -2]) # index -1 -3 -5 -7 
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # index 1 2 3 
print(list[-4 : -1]) # index - 4 - 3 - 2
print(list[3 : -3]) #index 3 4 
print(list[2 : -5]) # index 2
print(list[-1:-5]) # [] it will go to positive side
#Topic-10

 #  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # x: Hyd
print('y : ' , y) # y: True
for  x  in  list[2:7]:
print(x) #3+4j\n Hyd\n True\n None\n 10.8\n
#Topic-11

 #  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # Full list  address of list
a[1 : 4] = [60 , 70] 
print(a , id(a)) # [10,60,70,50] same address 
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))# [10,60,100,200,300] same address
#Topic-12

 #  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # error out of range 
print(a[1:]) # [] 
