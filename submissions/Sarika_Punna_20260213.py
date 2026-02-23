#Python Homework (Feb 13 2026 Friday)
# Find  outputs(Homework)
a = range(10, 50, 5)
print(type(a))#<class range>
print(a) #range(10,50,5)
print(*a) #10 15 20 25 30 35 40 45
print(id(a)) #address of range object 
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') # 20,25,30,35,40
print(*a[ : : -1]) #45 40 35 30 25 20 15 10
a[4] = 32 #error range is immutable 
print(a * 2) # error range does not support repetition

#  Find outputs (Homework)
a = range(10 , 20)
print(*a , sep = ',') #10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) #0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) 
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1)#error range cannot support float
h = range('A' , 'F') #error range doesn't support alphabets only int is supported

#  Find outputs (Homework)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #10 13 16
r = range(3)   
x , y = r   #Error r has 3 elements 
p , q  , r , s = r #Error r has only 3 elements so p,q,r,s 4 references are not allowed 
a , b , c = r  #0 1 2
m = r  
print(id(r)) # 1000 address of object r
print(id(m)) 1000adress of object m which is same as object r both refers to same object

#  Find outputs (Home Work)
a = [25, 10.8, 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) #<class List>
print(id(a)) #1000 address of object 
print(len(a)) #8
a[2] = 'Sec' 
print(a) [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #['Sec' , True , 3 + 4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) #[ ]
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25,10.8,'Hyd',True]
a . remove('Hyd')
print(a) #[25,10.8,True]
a . remove('25') #Error no string 25
print(a) #[25,10.8,True]

#  Find outputs  (Homework)
a = [25 , 10.8 , 'Hyd']
print(a) #[25 , 10.8 , 'Hyd']
print(id(a)) #1000 address of object 
print(a * 3) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'25 , 10.8 , 'Hyd']
print(a * 2) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1) #[25 , 10.8 , 'Hyd']
print(a * 0) #[ ]
print(a * -1) #[ ]
print(a * 4.0) #Error cannot have float
a = a * 3 
print(a) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a)) #2000 address of object now a refers to other object 
a = [25] 
print(a , id(a)) #[25] 3000
print(a * a) # Error

# list()  function  demo  program
a = list('Hyd')
print(a) #['H', 'y', 'd']
print(type(a)) #<class list>
print(len(a)) #4
b = (10 , 20 , 15 , 18)
print(list(b)) #[10, 20, 15, 18]
print(list(range(5))) #[0, 1, 2, 3, 4, 5]
print(list(25)) #[25]

# Find  outputs
a = [ ]
print(type(a)) #<class list>
print(a) #[ ]
print(len(a)) #0
b = list() 
print(b) #[ ]
print(len(b)) #0

# Slice demo program (Homework)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #[3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #['Hyd', 10.8, None, True, 'Hyd', 3+4j,10.8, 25 ]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) #[10.8 , 'Hyd' , None , 'Hyd']
print(list[ : : -2]) #['Hyd', None, 'Hyd', 10.…

#  Find outputs  (Homework)
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

#  Find outputs (Homework)
#     0     1     2    3     4
a = [10, 20, 30, 40, 50]
print(a , id(a)) #[10,20,30,40,50] 1000
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10,60, 70,50] 1000
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) #[10,60,100,200,400] 1000


#  Find outputs (Homework)
a = [25]
print(a[1]) #Error  
print(a[1:]) #[ ]
