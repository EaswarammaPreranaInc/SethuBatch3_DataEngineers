"# Find outputs (Home work)
a = range(10 , 50 , 5)
print(type(a)) # <class range>
print(a) #range(10 , 50 , 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) # address of object range
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') # 20,25,30,35,40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
a[4] = 32 # error because range object is not mutable
print(a * 2) # error because range doesnt have duplicate elements

# Find outputs (Home work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...') # 10…9…8…7…6…5…4…3…2
d = range(-10 , 0)
print(*d) # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10) # not possible empty
print(*e) # empty
f = range(2 , 2)
print(*f) # empty
g = range(10 , 11 , 0.1) # error .. range cannot be in float
h = range('A' , 'F') # error range cannot be in letters

# Find outputs (Home work)
r = range(10 , 17 , 3) # 10 13 16
a , b , c = r
print(a , b , c) # range(10 , 17 , 3) range(10 , 17 , 3) range(10 , 17 , 3)
r = range(3)
x , y = r
p , q , r , s = r
a , b , c = *r
m = r
print(id(r)) # address of range(0,3,1)
print(id(m)) #address of range(0,3,1) asme address

# Find outputs (Home Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #[25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a) # 25 10.8 'Hyd' True 3 + 4j None 'Hyd' 25
print(type(a)) # class list
print(id(a)) # address of object list
print(len(a)) # 8
a[2] = 'Sec'
print(a) #[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5]) #[ 'Sec' , True , 3 + 4j]

# append() and remove() methods (Home work)
a = [ ]
print(a) # empty list
a . append(25) #[25]
a . append(10.8) # [25,10.8]
a . append('Hyd') # [25,10.8,'Hyd']
a . append(True) # [25,10.8,'Hyd',True]
print(a) # [25,10.8,'Hyd',True]
a . remove('Hyd')
print(a) # [25,10.8,True]
a . remove('25')
print(a) # error because there is no element

# Find outputs (Home work)
a = [25 , 10.8 , 'Hyd']
print(a) # [25 , 10.8 , 'Hyd']
print(id(a)) #address of the object which is referred to a
print(a * 3) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1) # [25 , 10.8 , 'Hyd']
print(a * 0) # empty
print(a * -1) # empty
print(a * 4.0) # empty because of float
a = a * 3
print(a) # [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(id(a)) # address of the object which is referred to a
a = [25]
print(a , id(a)) # 25 address of a referred to 25
print(a * a) # error because of strings in the list

# list() function demo program
a = list('Hyd')
print(a) # ['Hyd']
print(type(a)) # class list
print(len(a)) # 1
b = (10 , 20 , 15 , 18)
print(list(b)) # [10 , 20 , 15 , 18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25)) #[25]
'''
list() function
-----------------
1) What does list(sequence) do ? ---> Converts sequence to list
2) Is list(non-sequence) valid ? ---> No becoz argument should be sequence only
3) What does list(No-args) do ? ---> Returns an empty list i.e. []
4) Finally list() function does typecasting
'''

# Find outputs
a = [ ]
print(type(a)) # class list
print(a) # []
print(len(a)) #0
b = list()
print(b) # []
print(len(b)) #0

# Slice demo program (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
# -8 -7 -6 -5 -4 -3 -2 -1
print(list[2 : 7]) # [3 + 4j , 'Hyd' , True , None , 10.8 ]
print(list[ : : ]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #['Hyd', 10.8 , None , True ,'Hyd' , 3 + 4j , 10.8 , 25 ]
print(list[ : : 2]) # list[0 : 8 : 2] ---> List from indexes 0 to 7 in steps of 2 i.e. [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # [ 10.8 , 'Hyd' , None , 'Hyd']
print(list[ : : -2]) #[ 10.8 , True , 3 + 4j , 25 ]
print(list[-2 : : -2]) # list[-2 : -9 : -2] ---> List from indexes -2 to -8 in steps of -2 i.e. [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # [10.8 , 3 + 4j , 'Hyd' ]
print(list[-4 : -1]) # List from indexes -4 to -2 in steps of 1 i.e [True , None , 10.8]
print(list[3 : -3]) # empty List from indexes 3 to -4 in steps of 1 doesnt happen
print(list[2 : -5]) #empty List from indexes 2 to -6 in steps of 1 doesnt happen
print(list[-1:-5]) #empty List from indexes -1 to -6 in steps of 1 doesnt happen

# Find outputs (Home work)
# 0 1 2 3 4 5 6 7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x , y = list[3 : 5]
print('x : ' , x) # x: [ 'Hyd' , True]
print('y : ' , y) # y: [ 'Hyd' , True]
for x in list[2:7]:
    print(x) # index out of bounds

# Find outputs (Home work)
# 0 1 2 3 4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10 , 20 , 30 , 40 , 50] adress of object a
a[1 : 4] = [60 , 70] # cannot happen
print(a , id(a)) # [10 , 60 , 70 , 50] adress of object a same adress
a[2: 4] = [100 , 200 , 300]
print(a , id(a)) # [10 , 60 ,100 , 200 , 300] adress of object a same adress

# Find outputs (Home work)
a = [25]
print(a[1]) # error because of no element
print(a[1:]) # error because of no element"