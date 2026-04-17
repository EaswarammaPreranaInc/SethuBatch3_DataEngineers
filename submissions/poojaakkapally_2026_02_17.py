1.#set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)-----25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))-----<class 'set'>
print(len(a))-----6
print(a[2])-----error(cant modified)
print(a[1 : 4])-----error(no indexing)
a[2] = 'Sec'-----error(cannot modified)
print(a * 2)-----error(no repetation)
print(a * a)-----error()

2.# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a))-----
print(len(a)))-----
print(type(a)))-----<class 'set'>

3.#  set()  function demo  program
a = set('Rama rAo') 
print(a)-----{'R' 'a' 'm' 'r' 'A' 'o' ' '}
print(len(a))-----7
print(set([10 , 20 , 15 , 20]))-----{10,15,20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))----{25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3)))-----{10,13,16,19}
print(set(25))----error
print(set([25 , 10.8 , [] , 'Hyd']))----error

4.# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))-----<class 'list'>
print(type(b))-----<class 'tuple'>
print(type(c))-----<class 'dict'>
print(type(d))-----<class 'set'>
print(a)----- [ ]
print(b)-----( )
print(c)-----{}
print(d)-----set()

5.# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)-----{None, True, 10.8, 'Hyd', 25}
print(len(a))----5
a . remove(25)
print(a)-----{None, True, 10.8, 'Hyd'}
a . append(100)----no append method in set
a . add(set())----error
a . add(())----error
a . add([])---error
print(a)----{'Hyd', None, True, 10.8}
a . add({})----error

7.# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)----{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))----<class 'dict'>
print(How  to  print  value  key  10)-----print(a[10])
print(How  to  print  value  key  20)-----print(a[20])
print(How  to  print  value  key  15)-----print(a[15])
print(How  to  print  value  key  18)-----print(a[18])
print(a[19])----error(there is no key 19)
print(a[0])-----error(there is no key 19)
print(a['Amar'])----error
How  to  moify  value  of   key  15  to  'Krishna'----
How  to  remove  20 :  'Kiran'  from  dict  'a'----
How  to  append  25 : 'Vamsi'  to  dict  'a'----
print(a)----{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(len(a))----4
print(a * 2)----error(no repetation)

8.# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)----{10: 'Sec'}
print(len(a))
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)----{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))----4

9.#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)---{True: 'May  be'}
print(len(a))---1

10.# Find  outputs
a = { [ ] : 25}---error
b = { ( ) : 25}
print(b)----{ ( ) : 25}
c = { { } : 25}---error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)----{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))----1
e = {set() : 10.8}---error

11.# Find  outputs
a = {}
print(type(a))----<class 'dict'>
print(len(a))-----0
print(a)----{}
b = dict()
print(type.(b))----<class 'dict'>
print(len(b))-----0
print(b)----{}

12.#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))----<class 'set'>
print(a)----{None}
print(len(a))----1

13.#  Anonymous  object  demo  program
_ = 25
print(_)----25
print(type(_))---<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)---10
print(_)----20
print(c)----30
for  _  in  range(5):
	print(_ , 'Hello')----0 Hello
                              1 Hello
                              2 Hello
                              3 Hello
                              4 Hello