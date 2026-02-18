#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) #<class 'set'>
print(len(a)) #6
print(a[2]) #Error because it is not indexed
print(a[1 : 4]) #Error because slicing is not possible
a[2] = 'Sec' #Error because it is not indexed
print(a * 2) #Error because Repitition and duplicates are not allowed in set
print(a * a) #Error because set itself cannot be multiplied


# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{1 , 'Hyd' , False , ''}
print(len(a)) #4
print(type(a)) #<class 'set'>



#  set()  function demo  program
a = set('Rama rAo')
print(a) #{'R' , 'a' , 'm' ,  'r' , 'A' , 'o'}
print(len(a)) #7
print(set([10 , 20 , 15 , 20])) #
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3))) #{10 , 13 , 16 , 19}
print(set(25)) #Invalid because argument is Non-sequence
print(set([25 , 10.8 , [] , 'Hyd'])) #{25 , 10.8 , 'Hyd'}


a =   [ ] #Empty list
b =   ( ) #Empty tuple
c =   {}  #Empty Dictionary
d =   set() #Empty set
print(type(a)) #<class 'list'> 
print(type(b)) #<class 'tuple'>
print(type(c)) #<class 'dict'>
print(type(d)) #<class 'set'>
print(a) #[]
print(b) #()
print(c) #{}
print(d) #set()


# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set() #Empty set
a . add(25) #{25}
a . add(10.8) #{25 , 10.8}
a . add('Hyd') #{25 , 10.8 , 'Hyd'}
a . add(True) #{25 , 10.8 , 'Hyd' , True}
a . add(None) #{25 , 10.8 , 'Hyd' , True , None}
a . add('Hyd') #Set does not alloes duplicates
a . add(1) #Set does not alloes duplicates
print(a) #{25 , 10.8 , 'Hyd' , True , None}
print(len(a)) #5
a . remove(25) #{10.8 , 'Hyd' , True , None}
print(a) #{10.8 , 'Hyd' , True , None}
a . append(100) #Invalid because Set doesn't contain append method it contains add method
a . add(set()) #Error
a . add(()) #{10.8 , 'Hyd' , True , None , ()}
a . add([]) #Error because set cannot have a mutable elements
print(a) #{10.8 , 'Hyd' , True , None , ()}
a . add({}) #Error because set cannot have mutable elements


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #{25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
for x in a:
      print(x)



# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #{10 :'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #<class 'dict'>
print( a[10]) #How  to  print  value  key  10
print( a[20] ) #How  to  print  value  key  20
print( a[15]) #How  to  print  value  key  15
print( a[18]) #How  to  print  value  key  18
print(a[19]) #Error or invalid because it is invalid key
print(a[0]) #Error or invalid because it is invalid key

print(a['Amar']) #Error or invalid because it is invalid key

How  to  moify  value  of   key  15  to  'Krishna' #a[15] = 'Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a' #a.del[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' #a.add(25 : 'Vamsi)
print(a) #{10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi}
print(len(a)) #4
print(a * 2) #Error because Dictionary does not allows Repetition and duplicates


# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10 : 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b)) #4


#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True :'May be'}
print(len(a)) #1


# Find  outputs
a = { [ ] : 25} #Error because Dictionary cannot have mutable elements
b = { ( ) : 25} #{ ( ) : 25}
print(b) #{ ( ) : 25}
c = { { } : 25} #Error because Key cannot be a mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #Error because Key cannot be a mutable

# Find  outputs
a = {} #Empty Dictionary
print(type(a)) #<class 'dict'>
print(len(a)) #0
print(a) #{}
b = dict()
print(type(b)) #<class 'dict'>
print(len(b)) #0
print(b) #dict()



#  Find  outputs (Home  work)
a = {
		print('Hyd') , #Hyd
		print('Sec') , #Sec
		print('Cyb')   #Cyb
	}
print(type(a)) #<class 'set'>
print(a) #{None}
print(len(a)) #1



#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #<class 'int'>
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello') #0  Hello
                            1  Hello
                            2  Hello
                            3  Hello
                            4  Hello




# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print( a) #'Dictionary  with  print  function'
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') #dict_Keys object
for x in a.keys():
    print(x) 
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop

print('Values  of  dictionary') #dict_values object
for x in a.values():
    print(x)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object') #dict_items object
for x in a.items():
    print(x)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
for x,y in a.items():
    print(x,y,sep = '...')
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
for x in a.keys():
    print(x , a[x] , sep = '...')
How  to  print  each  key  and  corresponding  value  in  dict  'a'

