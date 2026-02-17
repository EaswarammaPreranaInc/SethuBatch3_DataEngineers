# Find outputs (Home work) a = range(10 , 50 , 5)
print(type(a)) #OUTPUT: <class ‘range’>
print(a) #OUTPUT:range(10 ,15 ,20 ,25, 30, 35, 40, 45)
print(*a) #OUTPUT:10 15 20 25 30 35 40 45
print(id(a)) #OUTPUT:address of object
print(len(a)) #OUTPUT: 8
print(*a[2 : 7] , sep = ' , ') #OUTPUT: 20 ,25, 30, 35
print(*a[ : : -1]) a[4] = 32
print(a * 2) #OUTPUT: error





# Find outputs (Home work) a = range(10 , 20)
print(*a , sep = ',') #OUTPUT:10,20 b = range(5)
print(*b) #OUTPUT:0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') #OUTPUT:10…9…8…7…6…5…4…3…2 d = range(-10 , 0)#-10 ,-1,1
print(*d) #OUTPUT:-10 -9 -8 -7 -6 -5 – 4 -3 -2
e = range(-10) print(*e) #OUTPUT: f = range(2 , 2)
print(*f) #OUTPUT: error
g = range(10 , 11 , 0.1)
h = range('A' , 'F')
 
# Find outputs (Home work) r = range(10 , 17 , 3)
a , b , c = r
print(a , b , c) #OUTPUT:
r = range(3) x , y = r
p , q , r , s = r a , b , c = *r m = r
print(id(r)) #OUTPUT:
print(id(m)) #OUTPUT:


# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #OUTPUT: [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25] print(*a) #OUTPUT: 25 10.8 'Hyd' True 3 + 4j None 'Hyd' 25 print(type(a)) #OUTPUT: <class ‘list’>
print(id(a)) #OUTPUT:address of the object list
print(len(a)) #OUTPUT: 8
a[2] = 'Sec'
print(a) #OUTPUT: [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #OUTPUT:[ 'Sec' , True , 3 + 4j]


# append() and remove() methods (Home work) a = [ ]
print(a) #OUTPUT: []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #OUTPUT:[25,10.8,’hyd’,True]
 
a . remove('Hyd')
print(a) #OUTPUT:[25,10.8,True]
a . remove('25')
print(a) #OUTPUT: error




# Find outputs (Home work) a = [25 , 10.8 , 'Hyd']
print(a) #OUTPUT: [25 , 10.8 , 'Hyd']
print(id(a)) #OUTPUT: Address of list object
print(a * 3) #OUTPUT: [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2) #OUTPUT: [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1) #OUTPUT: [25 , 10.8 , 'Hyd']
print(a * 0) #OUTPUT:empty print(a * -1) #OUTPUT:error
print(a * 4.0) #OUTPUT:error, list is a group of integer elements
a = a * 3
print(a) #OUTPUT: [25 , 10.8 , 'Hyd'] [25 , 10.8 , 'Hyd'] [25 , 10.8 , 'Hyd']
print(id(a)) #OUTPUT: : Address of list object
a = [25]
print(a , id(a)) #OUTPUT: [25], Address of list object
print(a * a) #OUTPUT: error, cannot be a string




# list() function demo program a = list('Hyd')
print(a) #OUTPUT:[ 'H’,’y’,’d']
print(type(a)) #OUTPUT:<class ‘ list ‘>
print(len(a)) #OUTPUT:3 b = (10 , 20 , 15 , 18)
print(list(b)) #OUTPUT:[ 10 , 20 , 15 , 18]
 
print(list(range(5))) #OUTPUT:[ 0,1,2,3,4]
print(list(25)) #OUTPUT: error, list do not contain non sequence.




# Find outputs a = [ ]
print(type(a)) #OUTPUT:<class ‘ list ‘>
print(a) #OUTPUT :[] print(len(a)) #OUTPUT:0 b = list()
print(b) #OUTPUT:[] print(len(b)) #OUTPUT:0

# Slice demo program (Home work)
#	0	1	2	3	4	5	6	7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd'] #	-8	-7	-6	-5	-4	-3	-2	-1
print(list[2 : 7]) #OUTPUT:[ 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : ]) #OUTPUT: [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])#OUTPUT: [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #OUTPUT: ['Hyd' ,10.8 , None, True , 'Hyd', 3 + 4j, 10.8, 25] print(list[ : : 2]) # OUTPUT: [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # OUTPUT: [10.8 , 'Hyd', None, 'Hyd']
print(list[ : : -2]) # OUTPUT: [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # OUTPUT: [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1]) # OUTPUT: [True, ‘None’, 10.8]
print(list[3 : -3]) # OUTPUT:[ 'Hyd',’True’] print(list[2 : -5]) # OUTPUT: [3 + 4j] print(list[-1:-5]) # OUTPUT: empty
 
# Find outputs (Home work)
#	0	1	2	3	4	5	6	7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd'] x , y = list[3 : 5] #OUTPUT:[ 'Hyd' , True]
print('x : ' , x) #OUTPUT:
print('y : ' , y) #OUTPUT:
for x in list[2:7]:
print(x) #OUTPUT: [3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']




# Find outputs (Home work) #	0	1	2 3	4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #OUTPUT: [10 , 20 , 30 , 40 , 50]
a[1 : 4] = [60 , 70]
print(a , id(a)) #OUTPUT: [10 , 60 , 70 , 50]
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) #OUTPUT: [10 , 60 , 100 , 200 , 300]


# Find outputs (Home work) a = [25]
print(a[1])#OUTPUT: Error,there is no element at index 1
print(a[1:]) )#OUTPUT: Empty
