#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) = {25, 10.8, 'Hyd', True, (3+4j), None}
print(type(a)) = <class 'set'>
print(len(a))  = 6
print(a[2]) = Error
print(a[1 : 4]) = Error
a[2] = 'Sec'
print(a * 2) = Error
print(a * a) = Error
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) = {1, 'Hyd', False, ''}
print(len(a)) = 4
print(type(a)) = <class 'set'>
#  set()  function demo  program
a = set('Rama rAo')
print(a) = {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a)) = 7
print(set([10 , 20 , 15 , 20])) = {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) = {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) = {10, 13, 16, 19}
print(set(25)) = Error
print(set([25 , 10.8 , [] , 'Hyd'])) = Error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set() 
print(type(a)) = <class 'list'>
print(type(b)) = <class 'tuple'> 
print(type(c)) = <class 'dict'>
print(type(d)) = <class 'set'> 
print(a) = []
print(b) = ()
print(c) = {}
print(d) = set()
# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) = {25, 10.8, 'Hyd', True, None}
print(len(a)) = 5 
a . remove(25) 
print(a) = {10.8, 'Hyd', True, None}
a . append(100) = Error
a . add(set())  = Error
a . add(()) = ()
a . add([]) = Error
print(a) = {10.8, 'Hyd', True, None, ()}
a . add({}) = Error
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') = print(a)
print(a) = {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
for x in a:
    print(x)
           25
           True
           Hyd
           10.8
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a)) = <class 'dict'>
print(How  to  print  value  key  10) = print(a[10])   # Ramesh
print(How  to  print  value  key  20) = print(a[20])   # Kiran
print(How  to  print  value  key  15) = print(a[15])   # Amar
print(How  to  print  value  key  18) = print(a[18])   # Sita
print(a[19]) = Error 
print(a[0])  = Error
print(a['Amar']) = Error
How  to  moify  value  of   key  15  to  'Krishna' = a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' = del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'    = a[25] = 'Vamsi'
print(a) = {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) = 4
print(a * 2)  = Error
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) = {10: 'Sec'}
print(len(a)) = 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) = {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) = 4 
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) = {True: 'May  be'}
print(len(a)) = 1
# Find  outputs
a = { [ ] : 25} = Error
b = { ( ) : 25} 
print(b) = {(): 25} 
c = { { } : 25} = Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) = {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) = 1
e = {set() : 10.8} = Error
# Find  outputs
a = {}
print(type(a)) = <class 'dict'>
print(len(a)) = 0
print(a) = {}
b = dict()
print(type(b)) = <class 'dict'>
print(len(b)) = 0
print(b) = {}
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
How  to  print  dictionary  with  print()  function 
                               print(a) = {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print('Keys  of  dictionary')
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
                               for k in a:
                               print(k)  
print('Values  of  dictionary')
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
                               for v in a.values():
                               print(v)
print('Tuples  of  dict_items   object')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
                              for t in a.items():
                              print(t) 
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
                               for t in a.items():
                               print(t[0], t[1])  
print('Keys  and  values  of  dictionary') 
                               for k, v in a.items():
                               print(k, '->', v) 
How  to  print  each  key  and  corresponding  value  in  dict  'a'
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) = <class 'set'>
print(a)       = {None}
print(len(a))  = 1
#  Anonymous  object  demo  program
_ = 25
print(_) = 25 
print(type(_)) = <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) = 10
print(_) = 20
print(c) = 30
for  _  in  range(5):
	print(_ , 'Hello') = 0 Hello
                             1 Hello
                             2 Hello
                             3 Hello
                             4 Hello
                            