 #  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#{25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))#<class set>
print(len(a))#8
print(a[2])# 'Hyd'
print(a[1 : 4])#{ 10.8 , 'Hyd' , True }
a[2] = 'Sec'
print(a * 2)#error
print(a * a)#error

 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))#7
print(type(a))#<class set>

 #  set()  function demo  program
a = set('Rama rAo')
print(a)#('Rama rAo')
print(len(a))#7
print(set([10 , 20 , 15 , 20]))#{10 , 20 , 15 , 20}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#{25 , 10.8 , 'Hyd' , 10.8}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#{25}
print(set([25 , 10.8 , [] , 'Hyd']))#{25 , 10.8 , [] , 'Hyd'}


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
print(type(a))#<classlist>
print(type(b))#<classtuple>
print(type(c))#<emptydictionary>
print(type(d))#<classset>
print(a)#emptylist
print(b)#emptytuple
print(c)#emptydictionary
print(d)#set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)#{25}
a . add(10.8)#{10.8}
a . add('Hyd')#{'Hyd'}
a . add(True)#{true}
a . add(None)#{none}
a . add('Hyd')#{'hyd'}
a . add(1)#{1}
print(a)#{25,10.8,'hyd,true,none'}
print(len(a))#5
a . remove(25)#{10.8,'hyd,true,none'}
print(a)#{10.8,'hyd,true,none'}
a . append(100)#error
a . add(set())#error
a . add(())#empty
a . add([])#error
print(a)#{10.8,'hyd,true,none'}
a . add({})#error

 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')#a
print(???)# {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')#printx
How  to  iterate  thru  set  with  for  loop# for i in a :printI

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#<classset>
print(How  to  print  value  key  10)#a{10}
print(How  to  print  value  key  20)#a{20}
print(How  to  print  value  key  15)#a{15}
print(How  to  print  value  key  18)#a{18}
print(a[19])#error
print(a[0])#error
print(a['Amar'])#error
How  to  moify  value  of   key  15  to  'Krishna'#a{15}
How  to  remove  20 :  'Kiran'  from  dict  'a'#dela{20}
How  to  append  25 : 'Vamsi'  to  dict  'a'#error
print(a)#{10 : 'Ramesh'  , 15 :  'Krishna' , 18 : 'Sita'}
print(len(a))#3
print(a * 2)#error


 # Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10 : 'Hyd' , 10 : 'Sec'}
print(len(a))# 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))#6

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True : 'Yes' ,  1.0 : 'May  be'}
print(len(a))#1

 # Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)# {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#error

 # Find  outputs
a = {}
print(type(a))#<classset>
print(len(a))#empty
print(a)#0
b = dict()
print(type(b))#<classdictionary>
print(len(b))#0
print(b)#dictionary()

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')# {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')#{10,20,15,18}
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')#{ 'Ramesh' ,   'Kiran' ,  'Amar' ,'Sita'}
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')# (10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')# (10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')# {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
How  to  print  each  key  and  corresponding  value  in  dict  'a'#{10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))#error'Hyd
print(a)#error'Sec'
print(len(a))#error

 #  Anonymous  object  demo  program
_ = 25
print(_)#25
print(type(_))#<classint>
a , _ , c = 10 , 20 , 30
print(a)#a=10
print(_)#b=20
print(c)#c=30
for  _  in  range(5):#(0_'Hello',1_'Hello',2_'Hello',3_'Hello',4_'Hello')
	print(_ , 'Hello')#Hello