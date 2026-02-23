# 1
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{None, True, 'Hyd', 25, 10.8, 3+4j}
print(type(a)) #class 'set'
print(len(a)) #6
print(a[2]) #Error as set don't have indexing or doesn't support random access through indexing
print(a[1 : 4]) #Error as set don't have indexing or doesn't support slicing
a[2] = 'Sec' #Error as set don't have indexing which doesn't support random modification through indexes
print(a * 2) #Error as set can't have duplicates
print(a * a) #Error as set can't have duplicates



#2
#  set()  function demo  program
a = set('Rama rAo')
print(a) #{'R', 'r', ' ', 'a', 'o', 'm', 'A'}
print(len(a)) #7
print(set([10 , 20 , 15 , 20])) #{10, 20, 25}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{10.8, 25, 'Hyd'}
print(set(range(10 , 20 , 3))) #{10, 19, 16, 13}
print(set(25)) #Error as the argument should be sequence object or an iterable object but 'int' can't be iterated
print(set([25 , 10.8 , [] , 'Hyd'])) #Error as a set can not have a mutable element



#3
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{False, 1, 'Hyd', ''} i.e. False == 0.0 and True == 1.0
print(len(a)) #4
print(type(a)) #class 'set'



#4
# Find  outputs  (Home  work)
a =   []
b =   () 
c =   {} 
d =   set() 
print(type(a)) #class 'list'
print(type(b)) #class 'tuple'
print(type(c)) #class 'dict'
print(type(d)) #class 'set'
print(a) #[]
print(b) #()
print(c) #{}
print(d) #set()



#5
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
print(a) #{None, True, 10.8, 'Hyd', 25}
print(len(a)) #5
a . remove(25)
print(a) #{None, True, 10.8, 'Hyd'}
a . append(100) #Error as set doesn't support append() method
a . add(set()) #Error as nested set is invalid 
a . add(()) #Valid as immuatble elements i.e. tuple is allowed inside a set
a . add([]) #Error as muatble elements i.e. list is not allowed inside a set
print(a) #{None, True, 10.8, 'Hyd', ()}
a . add({}) #Error as muatble elements i.e. dictionary is not allowed inside a set



#6
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #{25, 10.8, True, 'Hyd'}
print('Iterate  through  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop
for i in a:
    print(i) #25<next line>10.8<next line>True<next line>Hyd



#7
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #class 'dict'
print(a[10]) #To  print  value  key  10 i.e. 'Ramesh'
print(a[20]) #To  print  value  key  20 i.e. 'Kiran'
print(a[15]) #To  print  value  key  15 i.e. 'Amar'
print(a[18]) #To  print  value  key  18 i.e. 'Sita'
print(a[19]) #Error as given key is invalid key or not found
print(a[0]) #Error as given key is invalid key or not found
print(a['Amar']) #Error as dict[key] will return value, but dict[value] can't return key
a[15]='Krishna' #To  modify  value  of   key  15  to  'Krishna'
del a[20] #To  remove  20 :  'Kiran'  from  dict  'a'
a[25] = 'Vamsi' #To  append  25 : 'Vamsi'  to  dict  'a'
print(a) #{10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) #4
print(a * 2) #Error as repetiton of dictionary leads to duplicate keys which is not permitted in a dictionary



#8
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10: 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Grey' , 'B' : 'Black'}
print(b) #{'R' : 'Red', 'G' : 'Grey', 'B' : 'Black', 'Y' : 'Yellow'}
print(len(b)) #4



#9
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True :'May be'}
print(len(a)) #1



#10
# Find  outputs
a = { [ ] : 25} #Error a key must and should be a immutable object or a immutable element
b = { ( ) : 25} #Valid as key is immuatble i.e. tuple
print(b) #{() : 25}
c = { { } : 25} #Error a key must and should be a immutable object or a immutable element
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #Error a key must and should be a immutable object or a immutable element



#11
# Find  outputs
a = {}
print(type(a)) #class 'dict'
print(len(a)) #0
print(a) #{}
b = dict()
print(type(b)) #class 'dict'
print(len(b)) #0
print(b) #{}



#12
#How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a) #How  to  print  dictionary  with  print()  function i.e. {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Keys  of  dictionary')
#How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
for k in a.keys():
    print(k) #10<next line>20<next line>15<next line>18
print('Values  of  dictionary')
#How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
for v in a.values():
    print(v) #Ramesh<next line>Kiran<next line>Amar<next line>Sita
print('Tuples  of  dict_items   object')
#How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
for i in a.items():
    print(i) #(10, 'Ramesh')<next line>(20: 'Kiran')<next line>(15, 'Amar')<next line>(18, 'Sita')
print('Elements  of  each   tuple')
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for k,v in a.items():
    print("Key:", k, "Value:", v) #Key:10<space>Value:Ramesh<next line>Key:20<space>Value:Kiran<next line>Key:15<space>Value:Amar<next line>Key:18<space>Value:Sita
print('Keys  and  values  of  dictionary')
#How  to  print  each  key  and  corresponding  value  in  dict  'a'
for k,v in a.items():
    print(k,":",v) #10:Ramesh<next line>20:Kiran<next line>15:Amar<next line>18:Sita
    


#13
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	} #Hyd<next line>Sec<next line>Cyb
print(type(a)) #class 'set'
print(a) 
print(len(a)) #1



#14
#Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #class 'int'
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello') # 0<space>Hello<next line>1<space>Hello<next line>2<space>Hello<next line>3<space>Hello<next line>4<space>Hello<next line>