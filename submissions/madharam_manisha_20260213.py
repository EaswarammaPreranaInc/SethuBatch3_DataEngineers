# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) #<class range>
print(a)      #range(10,50,5)
print(*a)     #(10 15 20 25 30 35 40 45)
print(id(a))  #address of the object
print(len(a))  #8
print(*a[2 : 7] , sep = ' , ') #20,25,30,35,40
print(*a[ : : -1]) #45,40,35,30,25,20,15,10
a[4] = 32  #error range is immutable
print(a * 2) #error invalid it can be print(*a) for unpack the range 
============================================================================================================================================================
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') #10,12,13,14,15,16,17,18,19
b = range(5)
print(*b)            #0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10...9...8...7...6...5...4...3...2..
d = range(-10 , 0)
print(*d)            #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)  #no error but there are no values 
f = range(2 , 2)
print(*f)          # no error no value
g = range(10 , 11 , 0.1) # error range has only integer elements not float
h = range('A' , 'F') #error range has only integer elements not string
============================================================================================================================================================
#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #10 13 16
r = range(3)  # 0 1 2  
x , y = r   #error- there are 3 values 0 1 2 but we have only x and y
p , q  , r , s = r #error-there are 3 values 0 1 2 but we have 4 like p ,q, r, s
a , b , c = *r # error- we can't just unpack *r not the right way
m = r  
print(id(r)) #address of object r 1000
print(id(m)) # same address of object m i.e m=r 1000
============================================================================================================================================================
#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)         #[25,10.8.,'Hyd',True,3+4j,None,'Hyd',25]
print(*a)        # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a))   #<class 'list'>
print(id(a))     #address of object 1000
print(len(a))    #8
a[2] = 'Sec'     #2='Hyd is replaced with 'Sec'
print(a)         #[25 10.8 'Sec' True 3+4j None 'Hyd' 25]
print(a[2 : 5])  #['Sec' True 3+4j]
============================================================================================================================================================
# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)        #[]
a . append(25)  #[25]
a . append(10.8) #[25,10.8]
a . append('Hyd') #[25,10.8,'Hyd']
a . append(True)  #[25,10.8,'Hyd',True]
print(a)      #[ 25,10.8,'Hyd',True]
a . remove('Hyd')
print(a)      #[ 25,10.8,True]
a . remove('25') #error-'25' str is not there in list 25 int is present
print(a)    #[ 25,10.8,True]
============================================================================================================================================================
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)    #[25,10.8,'Hyd']
print(id(a)) #address of object-1000
print(a * 3)  #[25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(a * 2)  #[25,10.8,'Hyd',25,10.8,'Hyd']
print(a * 1)   #[25,10.8,'Hyd']
print(a * 0)    #[]
print(a * -1)   #[] 
print(a * 4.0)  #error-can't multiply float to list(int)
a = a * 3      
print(a)      #[25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(id(a))  #  address of object-2000
a = [25]
print(a , id(a)) #25 address of object 3000
print(a * a) #error can't multiply to list other than int
============================================================================================================================================================
# list()  function  demo  program
a = list('Hyd')
print(a) #[H,y,d]
print(type(a)) #<class list>
print(len(a))   #3
b = (10 , 20 , 15 , 18)
print(list(b)) #[10,20,15,18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25)) #error we can't list 25 because 25 is int
============================================================================================================================================================
# Find  outputs
a = [ ]
print(type(a)) #class list>
print(a)       #[]
print(len(a))  # 0
b = list()
print(b)      #[]
print(len(b))  #0
============================================================================================================================================================
# Slice  demo  program (Home  work)
#        0      1     2        3      4     5        6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8    -7       -6     -5      -4     -3     -2     -1
print(list[2 : 7]) #[3+4j, 'Hyd', True, None, 10.8]
print(list[ : : ]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8,'Hyd']
print(list[:])       #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8,'Hyd']
print(list[ : : -1])  #['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) #[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])  #['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])  #[10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) #[True, None, 10.8]
print(list[3 : -3]) #['Hyd', True]
print(list[2 : -5])#[(3+4j)]
print(list[-1:-5])#[]
============================================================================================================================================================
#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)  #x :  Hyd
print('y : ' , y)   #y :  True
for  x  in  list[2:7]:
	print(x) #(3+4j)
		   Hyd
	           True
		   None
		   10.8
============================================================================================================================================================
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10, 20, 30, 40, 50] address of object-1000
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10, 60, 70, 50] address of object-1000
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) #[10, 60, 100, 200, 300] address of object-1000
============================================================================================================================================================
#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) #error index of list for 1 is not there 
print(a[1:])#[]


