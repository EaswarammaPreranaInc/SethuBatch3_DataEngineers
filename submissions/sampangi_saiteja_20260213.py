a = range(10 , 50 , 5)
print(type(a))#<class 'range')
print(a)#range(10 , 50 , 5)
print(*a)#10 15 20 25 30 35 40 45
print(id(a))#Address of object of a
print(len(a))#8
print(*a[2 : 7] , sep = ' , ')#[2,6,1]==>20,25,30,35,40
print(*a[ : : -1])#45 40 35 30 25 20 15 10
a[4] = 32
print(a * 2)#error due to the agr will not chane in range



#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')#(10,20,1)==>(10,11,12,13,14,,15,16,17,18,19)
b = range(5)
print(*b)#(0,5,1)==>0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')#10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)#(-10,0,1)==>-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
e = range(-10)
print(*e)#(0,-10,1)==>-
f = range(2 , 2)
print(*f)#(2,2,1)==>enty
g = range(10 , 11 , 0.1)#error due to the agr  always be int only
h = range('A' , 'F')#error due to the agr  always be int only



#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #10,13,16
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r))#  addrese of object of r 
print(id(m))# There will be no address Reference


#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)#[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)#25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a))#<class 'list'>
print(id(a))#address of object a
print(len(a))#8
a[2] = 'Sec'
print(a)#[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])#[2:5:1]==>'Sec' , True, 3 + 4j  


# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)#[]
a . append(25)#[25]
a . append(10.8)#[25,10.8]
a . append('Hyd')#[25,10.8,'hyd']
a . append(True)#[25,10.8,'hyd',True]
print(a)#[25,10.8,'hyd',True]
a . remove('Hyd')
print(a)#[25,10.8,True]
a . remove('25')
print(a)#error ddue to str 25 not present in list



a = [25 , 10.8 , 'Hyd']
print(a)#[25 , 10.8 , 'Hyd']
print(id(a))#address of the object a
print(a * 3)#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2)#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1)#[25 , 10.8 , 'Hyd']
print(a * 0)#[]
print(a * -1)#[-25 , -10.8 , -'Hyd']
print(a * 4.0)#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'25 , 10.8 , 'Hyd']
a = a * 3
print(a)#[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a))#address of the object a
a = [25]
print(a , id(a))#[25,address of the object a]
print(a * a)#[50]



# list()  function  demo  program
a = list('Hyd')
print(a)#list('Hyd')
print(type(a))#address of the object of a
print(len(a))#1
b = (10 , 20 , 15 , 18)
print(list(b))#[10 , 20 , 15 , 18]
print(list(range(5)))#[10 , 20 , 15 , 18]
print(list(25))#error due to argument  should  be  sequence  only

# Find  outputs
a = [ ]
print(type(a))#<class 'list'>
print(a)#[]
print(len(a))#0
b = list()
print(b)#list()
print(len(b))#0

# Slice  demo  program (Home  work)
#        0     1     2         3      4      5      6       7
list = [25 , 10.8 ,3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7    -6      -5      -4     -3      -2     -1
print(list[2 : 7])#[2:6:1]==>[3 + 4j ,'Hyd',True,None,10.8 ]
print(list[ : : ])#[0:8:1]==>[25,10.8,3 + 4j,'Hyd',True,None,10.8,'Hyd']
print(list[:])#[0:8:1]==>[25,10.8,3 + 4j,'Hyd',True,None,10.8,'Hyd']
print(list[ : : -1])#[0:8:-1]==>['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2])#[1 : 8 : 2]==>[10.8,'Hyd' None 'Hyd]
print(list[ : : -2])#[0 : 8 : -2]==>[10.8 'Hyd' None 'Hyd]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4])#[1,5,1]===>[10.8 3+4j 'hyd' True]
print(list[-4 : -1])#[-4:-2:-1]===>[True 'hyd' 3+4j 10.8]
print(list[3 : -3])#[3:4:1]==>['hyd',True]
print(list[2 : -5])#[2:6:1]==>[3+4j ]
print(list[-1:-5])#[-1:6:1]==>[]


#  Find  outputs  (Home  work)
#        0    1      2     3         4       5    6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)#[hyd]
print('y : ' , y)#[True]
for  x  in  list[2:7]:
	print(x)# [3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']


#  Find  outputs  (Home  work)
#    0     1    2   3    4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#[10 , 20 , 30 , 40 , 50] Address of object a
a[1 : 4] = [60 , 70]
print(a , id(a))#[10, 60,70,50] Address of object a
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))#[10,60,100,200,300]Address of object a

