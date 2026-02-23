# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) #class range
print(a) #(10,15,20,25,30,35,40,45)
print(*a)#10,15,20,25,30,35,40,45
print(id(a))#20000.............
print(len(a))#8
print(*a[2 : 7] , sep = ' , ') #20,25 ,30,35,40,
print(*a[ : : -1]) #49,48,47,46 45,44,43,42,41,40,39,38,37,36 35 ,34,33,32,31,30,29,28,27,26,26 24,23,22,21,20,19,18,17,16,15,14,13,12,11,10
a[4] = 32 #False
print(a * 2)#error
 #  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') #10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) #0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...') #10...9...8...7...6...5...4...3...2..1
d = range(-10 , 0)
print(*d) #-10,-9,-8,-7,-6 -5,-4,-3,-2,-1
e = range(-10) 
print(*e) #empty 
f = range(2 , 2)
print(*f)#empty
g = range(10 , 11 , 0.1)#error due to float
h = range('A' , 'F')#error due to string
 #  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #10,13,16
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) #10000.....
print(id(m)) #20000.......
 #  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25,10,8,'hyd',True, 3+4j,None,'Hyd',25]
print(*a) #25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))# class list
print(id(a)) #30000......
print(len(a)) #8
a[2] = 'Sec' 
print(a) # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) #' [ Sec, True, (3+4j)]
 # append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) #empty
a . append(25) #[25]
a . append(10.8) #[25,10.8]
a . append('Hyd') #[25,10.8,'hyd']
a . append(True)
print(a)#[25,10.8,'hyd',True]
a . remove('Hyd') 
print(a) #[25,10.8,'hyd',True]
a . remove('25') 
print(a) #[10.8,'hyd',True]
 #  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a))#50000....
print(a * 3) #25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) #[25, 10.8, 'Hyd']
print(a * 0)#empty 
print(a * -1)#empty
print(a * 4.0)#error 
a = a * 3
print(a) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))#50000......
a = [25] 
print(a , id(a)) #25,20........
print(a * a) #error
: # list()  function  demo  program
a = list('Hyd')
print(a) #['hyd']
print(type(a)) #class list
print(len(a)) #30000......
b = (10 , 20 , 15 , 18)
print(list(b)) #[10,20,15,18]
print(list(range(5)))[0,1,2,3 4]
print(list(25)) #error
 # Find  outputs
a = [ ]
print(type(a))#class list
print(a) #empty
print(len(a))#1
b = list()
print(b) # empty
print(len(b))#0
 # Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # (3+4j,hyd,True, None,10.8
print(list[ : : ]) #25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # 'Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # 10.8
print(list[ : : -2]) # 'Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #  10.8, True, (3+4j), 25]
 list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) #10.8, (3+4j), 'Hyd'
print(list[-4 : -1])#True, None, 10.8]
print(list[3 : -3]) #hyd
print(list[2 : -5])#(3+4j)]
print(list[-1:-5]) #hyd,10.8,none
 #  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #hyd
print('y : ' , y) # True 
for  x  in  list[2:7]:
	print(x) #3+4j , 'Hyd' , True , None , 10.8
 #  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))# 10,20,30,40,3000.... 
a[1 : 4] = [60 , 70]
print(a , id(a)) #10,60,40,70,30000......
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # 10,60,5000.....
 #  Find  outputs  (Home  work)
a =  [25]
print(a[1])# empty
print(a[1:])#empty
