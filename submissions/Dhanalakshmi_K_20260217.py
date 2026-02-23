#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #  {None, True, 'Hyd', 25, 10.8, (3+4j)}
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # ERROR because set can not be sliced
print(a[1 : 4]) # ERROR because set can not be sliced
a[2] = 'Sec' # ERROR because set don't have append method
print(a * 2) # ERROR because set can't be repeated
print(a * a) # ERROR because set can't be repeated or multiplied with another set

 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {False, 1, 'Hyd', ''}
print(len(a)) # 4
print(type(a)) # <class 'set'>

#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R','a','m',' ','r','A','o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) # {10, 13, 16, 19}
print(set(25)) # ERROR because 25 is an integer and a single element which can't be converted into set
print(set([25 , 10.8 , [] , 'Hyd'])) # ERROR because set can have only immutable elements but we have a list in a set which cause error


 # Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) #  <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # [ ]
print(b) # ( )
print(c) # {}
print(d) # set()

 # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) # {25}
a . add(10.8) # {25,10.8}
a . add('Hyd') # {25,10.8,'Hyd'}
a . add(True) # {25,10.8,'Hyd',True}
a . add(None) # {25,10.8,'Hyd',True,None}
a . add('Hyd') # ignored
a . add(1) # ignored
print(a) # {25,10.8,'Hyd',True,None}
print(len(a)) # 5
a . remove(25) # {10.8,'Hyd',True,None}
print(a) # {10.8,'Hyd',True,None}
a . append(100) # ERROR because no append method in set
a . add(set()) # ERROR because set() can't be used inside a set
a . add(()) # {10.8, 'Hyd', True, None, ()}
a . add([]) # ERROR because list is mutable hence can't be used inside set
print(a) # {10.8, 'Hyd', True, None, ()}
a . add({}) # ERROR because dict is mutable hence can't be used inside set

 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') # set with print function ---> print(a) -> {25 , True , 'Hyd' , 10.8}
print(???) # {25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop') # Iterate thru set with for loop
                                                  25<nextline>True<nextline>Hyd<nextline>10.8
How  to  iterate  thru  set  with  for  loop   for i in a:
                                                    print(i) -->25<nextline>True<nextline>Hyd<nextline>10.8

 # Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a)) # < class 'dict'>
print(How  to  print  value  key  10) # print(a[10])
print(How  to  print  value  key  20) # print(a[20])
print(How  to  print  value  key  15) # print(a[15])
print(How  to  print  value  key  18) # print(a[18])
print(a[19]) # ERROR because there is no key value pair with key 19
print(a[0]) # ERROR because there is no key value pair with key 0
print(a['Amar']) # ERROR because there is no key value pair with key Amar and key should be immutable 
How  to  moify  value  of   key  15  to  'Krishna' # a[15]='Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a' # del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # a[25]='Vamsi'
print(a) # {10 : 'Ramesh' , 25 : 'Vamsi' , 15 : 'Krishna' , 18 : 'Sita'}
print(len(a)) # 4
print(a * 2) # ERROR because no repeatation allowed 

 # Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red', 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b)) # 4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True: 'May  be'}
print(len(a)) # 1

 # Find  outputs
a = { [ ] : 25} # ERROR because list is mutable and can't used as key as they are mutable
b = { ( ) : 25} 
print(b) # {(): 25}
c = { { } : 25} # ERROR because dict can't be used as key as they are mutable
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # ERROR because set can't be used as key as they are mutable

# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}

 # How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') 
How  to  print  dictionary  with  print()  function # print(a) --> {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print('Keys  of  dictionary') 
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop #  for key in a.keys:
                                                                        print(key) ---> 10<nextline>20<nextline>15<nextline>18
print('Values  of  dictionary') 
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop # for value in a.values():
                                                                         print(value) --> Ramesh<nextline>Kiran<nextline>Amar<nextline>Sita
print('Tuples  of  dict_items   object') 
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop # for item in a.items():
                                                                          print(item) -->(10, 'Ramesh')<nextline>(20, 'Kiran')<nextline>(15, 'Amar')<nextline>(18, 'Sita')
print('Elements  of  each   tuple') 
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object # for key, value in a.items():
                                                                                        print(key, value) --> 10 Ramesh<nextline>20 Kiran<nextline>15 Amar<nextline>18 Sita
print('Keys  and  values  of  dictionary') 
How  to  print  each  key  and  corresponding  value  in  dict  'a' # for key, value in a.items():
                                                                           print(key, ':', value) --> 10 : Ramesh<nextline>20 : Kiran<nextline>15 : Amar<nextline>18 : Sita

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) # <class 'set'>
print(a) # Hyd
           Sec
           Cyb
print(len(a)) # 1

#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # _ takes each value from range(5) ---> range from 0 to 4 in steps of 1 i.e.,-> 0 Hello<nextline>1 Hello<nextline>2 Hello<nextline>3 Hello<nextline>4 Hello
                         