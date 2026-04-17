1. # Find outputs (Home work)
a = range(10 , 50 , 5) => The output is : 10 15 20 25 30 35 40 45 (end is not included).
print(type(a)) => The output is : < class ‘range’>
print(a) => (10 , 50 , 5)
print(*a) => The output is : 10 15 20 25 30 35 40 45
print(id(a)) => Adrres of the object
print(len(a)) => The output : is 8 (10 15 20 25 30 35 40 45 )
print(*a[2 : 7] , sep = ' , ') => The ouput is : 20 25 30 35 40 (end is not included)
print(*a[ : : -1]) => The output is : Reverse order => 45 40 35 30 25 20 15 10
a[4] = 32 => The output is Error.
print(a * 2) => The output is Error.


2. # Find outputs (Home work)
a = range(10 , 20) => The output is : 10 11 12 13 14 15 16 17 18 19 (20) is not included
print(*a , sep = ',') => The output is : 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19
b = range(5) => The output is : 0 1 2 3 4
print(*b) => 0 1 2 3 4
c = range(10 , 1 , -1) => : -10 -9 -8 -7 -6 -5 -4 -3 -2 (end is not included)
print(*c , sep = '...') => The output is : 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) => output is : -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) => output is : (end is -10 and start is default 0 : (0 > -10)
print(*e) => : (end is -10 and start is default 0 : (0 > -10)
f = range(2 , 2)
print(*f) => The output is : nothing
g = range(10 , 11 , 0.1) => The output is Error : (float cannot converted as an intiger.)
h = range('A' , 'F') => The output Is : string cannot converted as intiger.


3. # Find outputs (Home work)
r = range(10 , 17 , 3) => 10 13 16
a , b , c = r => 10 13 16
print(a , b , c) => The output is : 10 13 16
r = range(3) => O 1 2
x , y = r => Error
p , q , r , s = r => The output is : Value error.
a , b , c = *r => The output is : error
m = r
print(id(r)) => The output is : same number
print(id(m) => The output is : same number


4. # Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) => The output is : [25 , 10.0 , ‘Hyd’, True , 3+4j , None , ‘Hyd’,
print(*a) => The output is : 25 , 10.8 , ‘Hyd’ , True , 3 + 4j , None , ‘Hyd’ , 25
print(type(a)) => The output is : <class ‘list’>
print(id(a)) => Address of the object
print(len(a)) => The output is : 8
a[2] = 'Sec' => The output is to replace ‘Hyd’ and add the ‘sec’ in the index of 2
print(a) => The output is : [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5]) => [‘sec’ , True , (3+4j)] (end is not included).



5. # append() and remove() methods (Home work)
a = [ ] => (empty list) 
print(a) => The output is : [ ]
a . append(25) => To add 25 in the list . [25]
a . append(10.8) => To add 10.8 in the list [25 , 10.8 ]
a . append('Hyd') => To add ‘Hyd’ in the list [25 , 10.8 , ‘Hyd’]
a . append(True) => To add True in the list [25 , 10.8 , ‘Hyd’ , True]
print(a) => The output is : [25 , 10.8 , ‘Hyd’ , True]
a . remove('Hyd') => The output is : [25 , 10.8 , True]
print(a) => The output is : [25 , 10.8 , True]
a . remove('25')
print(a) => The output : The output is : [ 10.8 , True]


6. # Find outputs (Home work)
a = [25 , 10.8 , 'Hyd']
print(a) => The output is : [25 , 10 .8 , ‘Hyd’]
print(id(a)) => some memory adress
print(a * 3) = > [25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’]
print(a * 2) => The output is : > [25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’]
print(a * 1) => The output is : > [25 , 10.8 , ‘Hyd’ ]
print(a * 0) => The output is : empty list [ ]
print(a * -1) => The output is ; negative numbers are also : empty list [ ]
print(a * 4.0) => Error
a = a * 3 => [25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’]
print(a) => The output is : > [25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’ , 25 , 10.8 , ‘Hyd’]
print(id(a)) => Different memory adress
a = [25]
print(a , id(a)) => The output is ; [25] (some memory address)
print(a * a) => Error


7. # list() function demo program
a = list('Hyd')
print(a) => The output is : [‘H’ , ‘y’, ‘d’]
print(type(a)) => The output is : <class ‘list’>
print(len(a)) => the length is : 3
b = (10 , 20 , 15 , 18)
print(list(b)) => The output is : [10 , 20 , 15 , 18 ]
print(list(range(5))) => The output is :[ 0 , 1 , 2 , 3 4]
print(list(25)) => Error .


8 . # Find outputs
a = [ ]
print(type(a)) => the output is class ‘list’
print(a) => The output is : [ ]
print(len(a)) The output is : 0
b = list()
print(b) => The output is : [ ]
print(len(b)) => The output is : 0


9. # Slice demo program (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
# -8 -7 -6 -5 -4 -3 -2 -1
print(list[2 : 7]) => output : [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ]) => output : [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) => output : [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1]) => output : ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2]) # list[0 : 8 : 2] ---> List from indexes 0 to 7 in steps of 2 i.e. [25 ,
3+4j , True , 10.8]
print(list[1 : : 2]) => The output is : [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) => The output is : ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) # list[-2 : -9 : -2] ---> List from indexes -2 to -8 in steps of -2 i.e.
[10.8 , True , 3+4j , 25]
print(list[1 : 4]) => The output is : [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) => The output is : [True, None, 10.8]
print(list[3 : -3]) => The output is : ['Hyd', True]
print(list[2 : -5]) => The output is : [(3+4j)]
print(list[-1:-5]) => The output is : [ ]


10 . # Find outputs (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x , y = list[3 : 5]
print('x : ' , x) => The output is : x : Hyd
print('y : ' , y) => The output is : y : True
for x in list[2:7]:
print(x) => The output is : (3+4j)
 Hyd
 True
 None
 10.8


11 .# Find outputs (Home work)
a = [25]
print(a[1]) => The output is : index is out of range
print(a[1:]) => The output is : [ ]