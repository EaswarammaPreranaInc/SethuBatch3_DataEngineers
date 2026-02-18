# Find outputs (Home work)
a = range(10 , 50 , 5)
print(type(a)) #O/P : <class ‘range’>
print(a) #O/P : range (10,50,5)
print(*a) #O/P : 10,15,20,25,30,35,40,45
print(id(a)) #O/P : #any example id say (1000)
print(len(a)) #O/P : 8
print(*a[2 : 7] , sep = ' , ') #O/P :20,25,30,35,40
print(*a[ : : -1]) #O/P : 45,40,35,30,25,20,15,10
a[4] = 32
print(a * 2) #O/P : error (range doesn’t support item assignment)
# Find outputs (Home work)
a = range(10 , 20)
print(*a , sep = ',') #O/P : 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) #O/P : 0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...') #O/P :10…9…8…7…6…5…4…3…2
d = range(-10 , 0)
print(*d) #O/P :- -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e) #O/P :
f = range(2 , 2)
print(*f) #O/P : empty
g = range(10 , 11 , 0.1) #O/P : error (step should always be integer)
h = range('A' , 'F') #O/P : str cannot be used as int
# Find outputs (Home work)
r = range(10 , 17 , 3)
a , b , c = r
print(a , b , c) #O/P : 10,13,16
r = range(3)
x , y = r
p , q , r , s = r
a , b , c = *r
m = r
print(id(r)) #O/P :
print(id(m)) #O/P :
# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #O/P : [25 , 10.8 , 'Hyd' , True , (3 + 4j) , None , 'Hyd' , 25]
print(*a) #O/P : 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) #O/P : <class ‘list’>
print(id(a)) #O/P : some system address say(1200)
print(len(a)) #O/P : 8
a[2] = 'Sec'
print(a) #O/P : [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #O/P : ['Sec' , True , ( 3 + 4j) ]
# append() and remove() methods (Home work)
a = [ ]
print(a) #O/P : [ ]
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #O/P : [ 25,10.8,’Hyd’,True]
a . remove('Hyd')
print(a) #O/P : [ 25,10.8,True]
a . remove('25')
print(a) #O/P :error ‘25’ not in list
# Find outputs (Home work)
a = [25 , 10.8 , 'Hyd']
print(a) #O/P : [25 , 10.8 , 'Hyd']
print(id(a)) #O/P : some system generated address
print(a * 3) #O/P : [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) #O/P : [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1) #O/P : [25 , 10.8 , 'Hyd']
print(a * 0) #O/P :[ ]
print(a * -1) #O/P :[ ]
print(a * 4.0) #O/P :[ ]
a = a * 3
print(a) #O/P : [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a)) #O/P : some system generated address.
a = [25]
print(a , id(a)) #O/P : [25] some system generated output
print(a * a) #O/P : error
# list() function demo program
a = list('Hyd')
print(a) #O/P : [‘H’,’y’,’d’]
print(type(a)) ) #O/P : <class ‘list’>
print(len(a)) ) #O/P : 3
b = (10 , 20 , 15 , 18)
print(list(b)) ) #O/P : [10 , 20 , 15 , 18]
print(list(range(5))) #O/P : [0, 1, 2, 3, 4]
print(list(25)) #O/P :
# Find outputs
a = [ ]
print(type(a)) #O/P : <class ‘list’>
print(a) #O/P : []
print(len(a)) #O/P : 0
b = list()
print(b) #O/P : []
print(len(b)) #O/P : 0
# Slice demo program (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
# -8 -7 -6 -5 -4 -3 -2 -1
print(list[2 : 7]) #O/P : [3+4j,’Hyd’,True, None , 10.8 , 'Hyd']
print(list[ : : ]) #O/P : [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #O/P : [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #O/P : ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2]) # list[0 : 8 : 2] ---> List from indexes 0 to 7 in steps of 2 i.e.
[25 , 3+4j , True ,10.8]
print(list[1 : : 2]) #O/P : [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #O/P : ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # list[-2 : -9 : -2]---> List from indexes -2 to -8 in steps of -2 i.e.
[10.8 , True , 3+4j , 25]
print(list[1 : 4]) #O/P : [10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1]) #O/P : [True, None, 10.8]
print(list[3 : -3]) #O/P : ['Hyd', True]
print(list[2 : -5]) #O/P : [(3+4j)]
print(list[-1:-5]) #O/P : []
Find outputs (Home work)
0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x , y = list[3 : 5]
print('x : ' , x) O/P: ‘Hyd’
print('y : ' , y) O/P: True
for x in list[2:7]:
print(x)
O/P:
3+4j
‘Hyd’
True
None
10.8
# Find outputs (Home work)
# 0 1 2 3 4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) O/P: [ 10 , 20 , 30 , 40 , 50] some system generated output
a[1 : 4] = [60 , 70]
print(a , id(a)) O/P: [10, 60, 70, 50] same_system_id_1
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) #O/P : [10, 60, 100, 200, 300] same_system_id_1
a= [25]
print(a[1]) #O/P : error #(out of range)
print(a[1:]) #O/P : [ ]
