 #  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)   # {25 , 10.8 , 'Hyd' , True , 3+4j , None} 
print(type(a)) # class 'dict'
print(len(a))  # 6
print(a[2])   # error Index is not permitted 
print(a[1 : 4])   # error when index is not permitted ,so slicing is not possible
a[2] = 'Sec'    # Error index is not permitted
print(a * 2)   # Error duplicates are not allowed  
print(a * a)   # Error duplicates are not permitted


 # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)     # {1, 'Hyd', False, ''}
print(len(a))  # 4
print(type(a))  # class 'set  '


 #  set()  function demo  program
a = set('Rama rAo')
print(a)   # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a))  # 7
print(set([10 , 20 , 15 , 20]))     # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))  #  {25 , 10.8 , 'Hyd'}
print(set(range(10 , 20 , 3)))    # {10, 13, 16, 19}
print(set(25))     # error 
print(set([25 , 10.8 , [] , 'Hyd']))  # Error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  argument  should  be  sequence  only

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''
 # Find  outputs  (Home  work)
a =   [ ]   #  empty list
b =   ( )  # empty tuple
c =   {}    # empty set
d =   set()  # empty set
print(type(a))  # class 'list'
print(type(b))   # class 'Tuple'
print(type(c))   # class 'set'
print(type(d))   # class 'set'
print(a)   # []
print(b)   # ()
print(c)   # {}
print(d)   # {}


# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)  # insertion at any place in set
a . add(10.8)  # insertion at any place in set
a . add('Hyd')  #insertion at any place in set  
a . add(True)    # insertion at any place in set
a . add(None)    # insertion at any place in set
a . add('Hyd')   # insertion at any place in set
a . add(1)    # duplicate values are not allowed
print(a)   # {25,10.8,True}
print(len(a))
a . remove(25)  # removes 25 from set 
print(a)    # {10.8, 'Hyd', True, None}
a . append(100)   # Error no append method in set
a . add(set())    # Error because set is mutable but not 100% 
a . add(())      # Valid
a . add([])   # invalid
print(a)     # {10.8, 'Hyd', True, None, ()}
a . add({})  # error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
[12:44 pm, 17/2/2026] +91 99482 50500: # Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
print(type(a))
print(How  to  print  value  key  10)  # print(a[10])
print(How  to  print  value  key  20)   # print(a[20])
print(How  to  print  value  key  15)   # print(a[15])
print(How  to  print  value  key  18)   # print(a[18])
print(a[19])  # Error because of no key-Value pair
print(a[0])   #  Error because of no key-Value pair
print(a['Amar'])  # Error
How  to  moify  value  of   key  15  to  'Krishna'   # a[15] = 'Krishna'

How  to  remove  20 :  'Kiran'  from  dict  'a'     # del[20] = 'Kiran'
How  to  append  25 : 'Vamsi'  to  dict  'a'        # a[25] = 'Vamsi'
print(a) # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))  #4
print(a * 2)  # error repetition not not permitted 


 # Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)    #  {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  #    {'R' : 'Red' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))   # 4


 #  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)   # {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(len(a))  # 3


 # Find  outputs
a = { [ ] : 25}   # Invalid === New key - value pair
b = { ( ) : 25}   # valid 
print(b)        # { ( ) : 25} it is immutable       
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)          #  {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))     # 1
e = {set() : 10.8}   # set is mutable so can't be a key-value pair


 # Find  outputs
a = {}        #  empty dict
print(type(a))  # class 'dict'
print(len(a))   # 0
print(a)    # {}
b = dict()  
print(type(b))  # class 'dict'
print(len(b))   # 0
print(b)    # ()


 # How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
 
print('Dictionary  with  print  function')         # print(a)

How  to  print  dictionary  with  print()  function  # print(a)

print('Keys  of  dictionary')        # for x in a.keys():
                                           print(x)

How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop  # By using for loop

print('Values  of  dictionary')    # for x in a.values():
                                         print(x)

How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop

print('Tuples  of  dict_items   object')  # for x in a.items():
                                                print(x)

How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop

print('Elements  of  each   tuple') # for x in a.items():
                                          print(x[0], x[1])

How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object

print('Keys  and  values  of  dictionary')    # for k, v in a.items():
                                                    print(k, v)

How  to  print  each  key  and  corresponding  value  in  dict  'a'

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,      # #  'Hyd' 'Sec' 'Cyb'
		print('Cyb')
	}
print(type(a))    # class 'str'
print(a)    #  None
print(len(a)) 1

 

#  Anonymous  object  demo  program
_ = 25
print(_)  # 25 
print(type(_))  # class 'int'
a , _ , c = 10 , 20 , 30   # 
print(a)  #  10
print(_)  # 20
print(c)   # 30
for  _  in  range(5):
	print(_ , 'Hello')  #  0, 'Hello'
                               1, 'Hello'
                               2, 'Hello'
                               3, 'Hello'
                               4, 'Hello'
                          