#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#OUTPUT: {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a))#OUTPUT:<class 'set'>
print(len(a))#OUTPUT:6
print(a[2])#OUTPUT:error
print(a[1 : 4])#OUTPUT:error
a[2] = 'Sec'
print(a * 2)#OUTPUT:error
print(a * a)#OUTPUT:error


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#OUTPUT:{'Hyd' , False , True , '' }
print(len(a))#OUTPUT:4
print(type(a))#OUTPUT:<class 'set'>


#  set()  function demo  program
a = set('Rama rAo')
print(a)#OUTPUT:{'R', 'a' ,'m' 'o', 'r', 'A'}
print(len(a))#OUTPUT:6
print(set([10 , 20 , 15 , 20]))#OUTPUT:error
print(set((25 , 10.8 , 'Hyd' , 10.8)))#OUTPUT:{25 , 10.8 , 'Hyd' }
print(set(range(10 , 20 , 3)))#OUTPUT:{10 , 20 , 3}
print(set(25))#OUTPUT:error
print(set([25 , 10.8 , [] , 'Hyd']))#OUTPUT:error


# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#OUTPUT:<class 'list>
print(type(b))#OUTPUT:<class 'tuple'>
print(type(c))#OUTPUT:<class 'dict'>
print(type(d))#OUTPUT:<class 'set'>
print(a)#OUTPUT:[]
print(b)#OUTPUT:()
print(c)#OUTPUT:{}
print(d)#OUTPUT:set()






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
print(a)#OUTPUT:{25,10.8,'Hyd',True,None}
print(len(a))#OUTPUT:5
a . remove(25)
print(a)#OUTPUT:{10.8,'Hyd',True,None}
a . append(100)#OUTPUT:error
a . add(set())#OUTPUT:error
a . add(())#OUTPUT:{10.8,'Hyd',True,None,()}
a . add([])#OUTPUT:error
print(a)
a . add({})


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#OUTPUT:{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#OUTPUT:<class 'dict'>
print(How  to  print  value  key  10)#OUTPUT:print(a[10])
print(How  to  print  value  key  20)#OUTPUT:print(a[20])
print(How  to  print  value  key  15)#OUTPUT:print(a[15])
print(How  to  print  value  key  18)#OUTPUT:print(a[18])
print(a[19])#OUTPUT:error
print(a[0])#OUTPUT:error
print(a['Amar'])#OUTPUT:error
How  to  moify  value  of   key  15  to  'Krishna'#OUTPUT: a[15] ='krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a'#OUTPUT:a.remove[20]
How  to  append  25 : 'Vamsi'  to  dict  'a'#OUTPUT:a[25]= 'Vamsi'
print(a)OUTPUT:{10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}

print(len(a))
print(a * 2)#OUTPUT:error


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#OUTPUT:{10 : 'Sec'}
print(len(a))#OUTPUT:1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#OUTPUT:{'R' : 'Red' ,'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))#OUTPUT:4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a){True : 'Yes'}
print(len(a))#OUTPUT:1


# Find  outputs
a = { [ ] : 25}#OUTPUT:error
b = { ( ) : 25}
print(b)#OUTPUT:{(),25}
c = { { } : 25}#OUTPUT:error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#OUTPUT:{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#OUTPUT:1
e = {set() : 10.8}#OUTPUT:error


# Find  outputs
a = {}
print(type(a))#OUTPUT:<class 'dict'>
print(len(a))#OUTPUT: 0
print(a)#OUTPUT: {}
b = dict()
print(type(b))#OUTPUT:<class 'dict'>
print(len(b))#OUTPUT: 0
print(b)#OUTPUT: {}




# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')#OUTPUT: {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')#OUTPUT:
for key in a:
   print(a[key])

How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')#OUTPUT:
for t in a.items():
   print(t)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
How  to  print  each  key  and  corresponding  value  in  dict  'a'
#OUTPUT:
for key,value in a.items(): 
   print(key,value)


#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#OUTPUT:<class 'set'>
print(a)#OUTPUT:{None}
print(len(a))#OUTPUT:1



#  Anonymous  object  demo  program
_ = 25
print(_)#OUTPUT:25
print(type(_))#OUTPUT:<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#OUTPUT:10
print(_)#OUTPUT:20
print(c)#OUTPUT:30
for  _  in  range(5):
	print(_ , 'Hello')#OUTPUT:
0  Hello
1  Hello
2  Hello
3  Hello
4  Hello
