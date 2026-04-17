1) set object demo program outputs
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))#<class 'set'>
print(len(a))#6
print(a[2])#Error because indexing is not possible
print(a[1 : 4])#Error because slicing is not possible
a[2] = 'Sec'#Error because indexing is not possible
print(a * 2)#Error because no duplicates
print(a * a)#Error because no duplicates

2) Tricky  program outputs 
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{1 , 'Hyd' , False , '' }
print(len(a))#4
print(type(a))#<class 'set>

3) set()  function demo  program outputs
a = set('Rama rAo')
print(a)#{'R', 'a', 'm', 'r', 'A', 'o', ' '}
print(len(a))#7
print(set([10 , 20 , 15 , 20]))#{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#Error because it is not permitted
print(set([25 , 10.8 , [] , 'Hyd']))#Error because it is not permitted

4) outputs  
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>
print(type(c))#<class 'dict'>
print(type(d))#<class 'set'>
print(a)#[ ]
print(b)#( )
print(c)#{}
print(d)#set()

5) Tricky  program output
- add()  and  remove()  methods  
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)#{25, 10.8, 'Hyd', True, None}
print(len(a))#5
a . remove(25)
print(a)#{10.8, 'Hyd', True, None}
a . append(100)
a . add(set())
a . add(())
a . add([])
print(a)#Error because it is not permitted
a . add({})



6) How  to  print  set  in  two  different ways outputs
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#{25 , True , 'Hyd' , 10.8}
print(???)
print('Iterate  thru  set  with  for  loop')#
How  to  iterate  thru  set  with  for  loop



7) outputs  
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)# {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#<class 'dict'>
print(How  to  print  value  key  10)#a[10]
print(How  to  print  value  key  20)#a[20]
print(How  to  print  value  key  15)#a[15]
print(How  to  print  value  key  18)#a[18]
print(a[19])#Error because not valid 
print(a[0])#Error because not valid 
print(a['Amar'])#Error because not valid 
How  to  modify  value  of   key  15  to  'Krishna'#a[15]='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'# del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'#a[19]='vamsi'
print(a)#{10: 'Ramesh', 15: 'krishna', 18: 'Sita', 19: 'vamsi'}
print(len(a))#4
print(a * 2)#Error because no duplicates


8) outputs  
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#4

9)  Tricky  program outputs
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True : 'May be'}
print(len(a))#1

10) outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)#Error because it is not permitted
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#Error because it is not valid

11) outputs
a = {}
print(type(a))#<class 'dict'>
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#<class 'dict'>
print(len(b))#0
print(b)#{}


12) How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')#print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')#print(key)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')#print(value)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')#print(items)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')#print(key=a[], value='  ')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')#print(key,value)
How  to  print  each  key  and  corresponding  value  in  dict  'a'



13) outputs
a = {
		print('Hyd') ,#Hyd
		print('Sec') ,#Sec
		print('Cyb')  #Cyb
	}
print(type(a))#<class 'set'>
print(a)#{None}
print(len(a))#1

14) Anonymous  object  demo  program outputs
_ = 25
print(_)#25
print(type(_))#<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello')# 0 Hello
                            1 Hello
                            2 Hello
                            3 Hello
                            4 Hello







































































