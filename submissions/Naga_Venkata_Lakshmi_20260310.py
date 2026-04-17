#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #False
print(a  ==  b) #True
b[2] = 12 #[10 , 20 , 12 , 15 , 18]
print(a) #[10 , 20 , 12 , 15 , 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[110 , 220 , 165 , 18]
print(a + 5) #[15 , 25 , 20 , 23]
print(a + '5') #
print([10 , 20] + (30 , 40)) #Error


# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3] , Address of list a with three elements.
a += b
print(a , id(a)) #[ 4 , 5 , 6],Address of list a with  three elements.


# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3], Address of list a with three elements.
a  = a + b  #[1 , 2 , 3 , 4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3 , 4 , 5 , 6] , Address of list a with six elements.


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) #a: 25
print('b : ' , b) #b: [10.8 , 'Hyd']
print('c : ' , c) #c: True
print(type(b)) # <class 'list'> 
x , *y = list
print('x : ' , x) # x: 25 
print('y : ' , y) # y: [10.8 , 'Hyd' , True]
*p , q = list
print('p : ' , p) # p: [25 , 'Hyd' , True] 
print('q : ' , q) # q: 10.8  


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) #a: 25
print('b : ' , b) #b: 10.8
print('c : ' , c) #c: ['Hyd']
print('d : ' , d) #d: True
print('e : ' , e) #e: True
a , b , *c , d , e , f = list #Error because list has four elements.


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a: 25
print('b : ' , b) #b: 10.8
print('_ :  ' , _) #_: 'Hyd'
print('d : ' , d)  #d: True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) # a : 25 , 'Hyd' , 3+4j
print('b : ' , b) # b : 10.8
print('d : ' , d) # d : True


#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a: 25
print('b : ' , b) #b: 10.8
print('_ : ' , _) #_: 'Hyd'
print('d : ' , d) #d: True
print('_: ' , _) #_: 3+4j


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list # Syntax error because two starred.


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) # a: [25 , 10.8]
print('b :  ' , b) # b: 'Hyd'
print('c :  ' , c) #c: True


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)  # True
print(a  is   b) #False
print(a < c) # True
print(a > d) # True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False


#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #4


# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # 8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # 39.8 + 4j
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) #Error


#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) #Error
print(sum(i)
print(How  to  determine  sum  of  inner  list  elements  in  another  way)


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) #25
d = [25 , '35']
print(max(d)) #25
print(max([])) #Error
print(min([])) #Error


# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) 
print(b) #[10 , 20 , 15 , 18]
print(type(b)) #<class 'list'>
print(a  is  b) #False
print(a == b) #False


#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) #[4 , 6 , 8]
print(b) #[4 , 6 , 8]
print(type(b)) #<class 'list'>
a = list('Vamsi') #['Vamsi']
print(a) #['Vamsi']
a = list() #[]
print(a) #[]
print(list(25)) #Error because argument is non-sequence which is not iterable.
print(list(10.8)) #Error because argument is non-sequence which is not iterable.
print(list(True)) #Error because argument is non-sequence which is not iterable.
print(list(None)) #Error because argument is non-sequence which is not iterable.


# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[ (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[ (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[ [10 , 20] , (30 , 40) , {50 , 60}]


# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a) #['5' , '10' , '12' , '15' , '20']
print(b)  #['5' , '10' , '12' , '15' , '20']
print(type(b)) #<class 'list'>
c = sorted(a , reverse = True)
print(c) #['20' , '15' , '12' , '10' , '5']
print(a) #[10 , 20 , 15 , 5 , 12]


a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) #['Amar' , 'Kiran' , 'Rajesh' , 'Rama Rao' , 'Rama' , 'Sita' , 'Vamsi']
print(b) # ['Amar' , 'Kiran' , 'Rajesh' , 'Rama Rao' , 'Rama' , 'Sita' , 'Vamsi']

c = sorted(a , reverse = True)
print(c) #['Vamsi' , 'Sita' , 'Rama' , 'Rama Rao' , 'Rajesh' , 'Kiran' , 'Amar']
print(a) #['Rama' , 'Rajesh' , 'Amar' , 'Sita' , 'Vamsi' , 'Kiran' , 'Rama Rao']


# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #True


# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #True

# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
del    a[2] #[10 , 20 , 18]
print(a) #[10 , 20 , 18]
del  a[3] #[10 , 20]
del  a  # No result
print(a) #Error


#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . append(19) #[10 , 20 , 15 , 18 , 19]
print(list) #[10 , 20 , 15 , 18 , 19]


#  Find  outputs (Home  work)
list = []
print(list) #[]
list . append(25) #[25]
list . append(10.8) #[25 , 10.8 ]
list . append('Hyd') #[25 , 10.8 , 'Hyd']
list . append(True)  #[25 , 10.8 , 'Hyd' , True]
print(list) #[25 , 10.8 , 'Hyd' , True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0 , 10 , 20 , 30 , 40]


#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd') #[10 , 20 , 30 , 'Hyd']
print(a)  #[10 , 20 , 30 , 'Hyd']
print(len(a)) #4
print(a[3])
print(How to print  'H') #Error
print(How  to  print  'y') #Error
print(How  to  print  'd') #Error


#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) #[10 , 20 , [50 , 60 , 70] , 30 , 40]
print(len(a)) # 7
print(a[2])
print(a[2][0])
print(a[2][1])
print(a[2][2])


# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) #[10 , 20 , 18 , 15 , 12 , 15 , 19] 
	list . remove(25) #Error
except:
	print('25  is   not  in  the  list')



#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) #15
print(a) #[10 , 20 , 18 , 12]
print(a . pop(len(a))) # 4
print(a . pop(-3)) #20
print(a) #[10 , 18 , 12]
print(a . pop(-4)) #Index error
print(a . pop()) #12
print(a) #[10 , 18]
b = []
b . pop() #Index error


# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]


# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
a . reverse() #[18 , 15 , 20 , 10]
print(a) #[18 , 15 , 20 , 10]


#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort() #[5 , 10 , 15 , 18 , 20]
print(list) #[5 , 10 , 15 , 18 , 20]
list . sort(reverse = True)
print(list) #[20 , 18 , 15 , 10 , 5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a) #['Amar' , 'Kiran' , 'Rajesh' , 'Rama' , 'Rama Rao' , 'Sita' , 'Vamsi']
a . sort(reverse = True)
print(a) #['Vamsi' , 'Sita' , 'Rama Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']


# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() #sort() is a function not a method.sort is not a attribute of list class.To call a method object is mandatory.

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #Error
print(len(a)) #9


L = []
n= int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    L.append(num)

First = L[0]
Same = True

for i in L:
   if  i != First:
      Same = False
      break
if Same:
   print("All  elements are identical")
else:
   print("Elements are not identical")


L = []
n = int(input("Enter number of elements:  "))

for i in range(n):
    num = int(input("Enter element: "))
    L.append(num)

new_list = [] 
for i in L:
    if i not in new_list:
        new_list.append(i) 
print("List after removing duplicates:" , new_list)



L = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    L.append(num)
x = int(input("Enter value to delete: "))
new_list = []
for i in L:
    if i != x:
        new_list.append(i)

print("List after deleting", x , ":", new_list)
          























