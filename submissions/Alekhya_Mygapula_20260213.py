PYTHON 
ALEKHYA MYGAPULA


a = range(10 , 50 , 5)
print(type(a)) #<class range>
print(a) #(10,50,5)
print(*a)  #10 15 20 25 30 35 40 45 50
print(id(a)) #addres of the range object
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') #20,25,30,35,40
print(*a[ : : -1]) #50 45 40 35 30 25 20 15 10
a[4] = 32#Error due to immutable
print(a * 2) *error due to immutable



a = range(10 , 20)
print(*a , sep = ',') #10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) #0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) #Empty 
f = range(2 , 2)
print(*f) #empty string
g = range(10 , 11 , 0.1)#error due to float
h = range('A' , 'F') #error due to str




r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #(10,17,3)
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) #addres of range object
print(id(m)) #addres of range object




a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) #25 10.8 hyd true (3+4j) none hyd 25
print(type(a)) #<class list>
print(id(a)) #addresof the list
print(len(a))#8
a[2] = 'Sec'
print(a)#[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])#['Sec',True,3+4j]




a = [ ]
print(a) #[ ]
a . append(25) 
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25, 10.8,'Hyd']
a . remove('Hyd')
print(a) #[25,10.8
a . remove('25')
print(a) #Error due to string



a = [25 , 10.8 , 'Hyd']
print(a) #[25, 10.8, 'Hyd']
print(id(a)) #adrees of the ranje object
print(a * 3) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2)#[25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1)#[25, 10.8, 'Hyd']
print(a * 0)#[]
print(a * -1)#[]
print(a * 4.0) #Error
a = a * 3 #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a) #[25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(id(a))#addres of the obect a=a*3
a = [25]
print(a , id(a)) #[25] adrees of the object 25
print(a * a) #Error




a = list('Hyd')
print(a) #['H', 'y', 'd']
print(type(a)) #<class list>
print(len(a)) #2
b = (10 , 20 , 15 , 18) 
print(list(b)) #[10,20,15,18]
print(list(range(5)))#[0, 1, 2, 3, 4]
print(list(25))#Error


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
print(type(a))#<class list.
print(a)#[ ] 
print(len(a)) #0
b = list()
print(b) #[ ]
print(len(b))#0



# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) #[(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ]) #[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) #[25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1])#['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])#[10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])#['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])#[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[True, None, 10.8]
print(list[3 : -3])#['Hyd', True]
print(list[2 : -5]) #[(3+4j)]
print(list[-1:-5]) #Empty list







list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #x :  Hyd
                   y :  True
print('y : ' , y)
for  x  in  list[2:7]:
	print(x)#(3+4j)
               Hyd
               True
                None
                10.8

	
	
		a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #[10, 20, 30, 40, 50] addresof the list
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10, 60, 70, 50] addresof the index list
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#[10, 60, 100, 200, 300] addresof the list






a =  [25]
print(a[1]) #Error due to only index becoz index starts from 0
print(a[1:]) #[]
