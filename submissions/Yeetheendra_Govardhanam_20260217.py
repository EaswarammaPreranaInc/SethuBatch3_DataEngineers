# Topic-1
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None} 
print(type(a)) #<class ‘set’>
print(len(a)) #<6>
print(a[2]) #error no index or subscriptable as it is unordered 
print(a[1 : 4]) #error no slicing as it is unordered
a[2] = 'Sec' #error no modification possible in set
print(a * 2) # error no repetition because no duplicate elements allowed 
print(a * a) # error when sequenced data on left side while using repetition operation , we need to use integer only on right side. 

# Topic-2
 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)  #{1,'Hyd' , False, '’} 
print(len(a)) #4
print(type(a)) #<class ‘set’>
# Topic-3
 #  set()  function demo  program
a = set('Rama rAo')
print(a) #{‘R’, ‘a’, ‘m’, ‘ ’ , ‘r’, ‘A’, ‘o’} 
print(len(a)) #7
print(set([10 , 20 , 15 , 20])) # {10,20,15} 
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, Hyd}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) #error as it is non-sequenced element 
print(set([25 , 10.8 , [] , 'Hyd'])) # error as list is inside 

'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''
# Topic-4
 # Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<class ‘list’>
print(type(b)) #<class ‘tuple’>
print(type(c)) #<class ‘dict’>
print(type(d)) #<class ‘set’>
print(a) #[] 
print(b) #() 
print(c) #{} 
print(d) #set() 
# Topic-5
 # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) #{25}
a . add(10.8) # {25,10.8}
a . add('Hyd') #{25,10.8, Hyd} 
a . add(True) #{25,10.8, Hyd, True} 
a . add(None) #{25,10.8, Hyd, True, None} 
a . add('Hyd') #{25,10.8, Hyd, True, None}
a . add(1) #{25,10.8, Hyd, True, None}
print(a) #{25,10.8, Hyd, True, None} 
print(len(a)) #5
a . remove(25) 
print(a) #{10.8, Hyd, True, None} 
a . append(100) #error there is no that function 
a . add(set()) #error  we can't add set method 
a . add(()) #{10.8, Hyd, True, None, () } 
a . add([]) #error as it is list which is mutable 
print(a)  #{10.8, Hyd, True, None, () }
a . add({})   #error as it is dict which is mutable

# Topic-6
 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # set  with  print  function
print(???) #a it prints  {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop
# for Y is a:
#print(Y)
# Topic-7
 # Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  #<class ‘dict’>
print(a[10])
print(a[20])
print(a[15])
print(a[18])
print(a[19]) # error no key like that 
print(a[0]) # error no key like that 
print(a['Amar']) # error not possible to print key from value
How  to  moify  value  of   key  15  to  'Krishna'
a[15] = 'Krishna’
How  to  remove  20 :  'Kiran'  from  dict  'a'
del a[20] 
How  to  append  25 : 'Vamsi'  to  dict  'a'
a[25] = 'Vamsi'
print(a) # {10 : 'Ramesh' , 20 : 15 : 'Krishna’ , 18 : 'Sita', 25 : ‘Vamsi’}
print(len(a)) #4
print(a * 2) # error no duplicate keys allowed 

# Topic-8
 Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10: ‘Sec’} 
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b)) #4
# Topic-9
 #  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True : ‘May be’} 
print(len(a)) #1
# Topic-10
 # Find  outputs
a = { [ ] : 25}  # error no list in dict key
b = { ( ) : 25} # new dict 0 tuple with 25
print(b) # { ( ) : 25}
c = { { } : 25} # error no set  in dict key
d ={'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} # error no set () in dict key
# Topic-11
 # Find  outputs
a = {}
print(type(a)) #<class ‘dict’>
print(len(a)) #0
print(a) #{} 
b = dict() 
print(type(b)) #<class ‘dict’>
print(len(b)) #0
print(b) #{  } 
# Topic-12
 # How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
#How  to  print  dictionary  with  print()  function
print(a) 
print('Keys  of  dictionary')
#How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
for x in a.keys():
    print(x) 
print('Values  of  dictionary')
#How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
for x in a.values():
    print(x) 
print('Tuples  of  dict_items   object')
#How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
for x in a.items():
    print(x) 
print('Elements  of  each   tuple')
#How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
for key, value in a.items()
    print(key, value) 
print('Keys  and  values  of  dictionary')
#How  to  print  each  key  and  corresponding  value  in  dict  'a'print(a)
for x in a.keys():
    print(x, a[x]) 
# Topic-13
 #  Find  outputs (Home  work)
a = {
print('Hyd') ,
print('Sec') ,
print('Cyb')
} 
New set is 
a = {
 None,
None,
None
} 
# Hyd
# Sec
#Cyb
print(type(a)) #<class ‘set’>
print(a) # {None}
print(len(a)) #1
The function performed the operation and returns a value 
For print it returns none
# Topic-14
#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #<class ‘int’>
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
print(_ , 'Hello') #5 times 
#0 Hello
#1 Hello
#2 Hello
#3 Hello
#4 Hello
