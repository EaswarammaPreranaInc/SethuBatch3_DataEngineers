        # Python-Homework                                    Date : 17/02/2026

#1 .   #  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}  #=> The set does not allowed Duplicate Values.
print(a)               #=> The output is : {25 , 10.8 , ‘Hyd’ , True , (3+4j) , None}
print(type(a))  #=> The output is : <class ‘set’> 
print(len(a))     #=> The output is : length : 6
print(a[2])        #=>   The output is :  Set does not supporting indexing.
print(a[1 : 4])   #=>  The output is : Set does not support Sliceing.
a[2] = 'Sec'      #=>  The output is : Sets are Mutable but not indexbased
print(a * 2)      #=>  The output is : in Sets Multiplication not Supported.
print(a * a)       #=> The output is : (set * set ) Multiplication are not supported.


#2 .  #  set()  function demo  program
a = set('Rama rao')
print(a)  #=> The output is : { ‘R’, ‘a’, ‘m’, ‘ ’ , ‘r’, ‘a’, ‘o’} 
print(len(a))   #=> The output is :  7
print(set([10 , 20 , 15 , 20]))  #=> The output is : {10 , 20 , 15 } Duplicate values are not allowed.
print(set((25 , 10.8 , 'Hyd' , 10.8)))  #=> The output is : {25 , 10.8 , ‘Hyd’ }
print(set(range(10 , 20 , 3)))   #= > The output is : {10 , 13 , 16 , 19}
print(set(25))  #=> The output is : error int object is not iterable .
print(set([25 , 10.8 , [] , 'Hyd']))# => The output is : Error because list in the list  
#sets allows only immutable elements.  


#3 . # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)  #=> The output is : { 1 , 0 , ‘Hyd’ , ‘ ‘}
print(len(a)) #=> The output is  : 4 
print(type(a)) #=> The output is : <class ‘set’>

4 . # Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))   #=> The output is : <class ‘list’> 
print(type(b))  #=> The  output is : <class ‘tuple’>
print(type(c)) #=> The output is : <class ‘dict’> 
print(type(d)) #=> The output is : <class ‘set’>
print(a)   #=> The output is : [ ] => list
print(b)  #=> The output is : ( )   => tuple
print(c)  #=> The output is : { }  => dict
print(d)  #=> The output is : set()  => set

#5 . # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)  #=> To add {25}
a . add(10.8) #{25 , 10.8 }
a . add('Hyd')# => {25 , 10.8 , ‘Hyd’ }
a . add(True)  #=> {25 ,10.8 , ‘Hyd’ True}
a . add(None) #=> {25 , 10.8 , ‘Hyd’ , True , None }
a . add('Hyd')  #=>  {25 , 10.8 , ‘Hyd’ , True , None, ‘Hyd’ }
a . add(1) #=> {25 , 10.8 , ‘Hyd’ , True , None, ‘Hyd’,1 }
print(a)   #=> The output is  : {25 , 10.8 , ‘Hyd’ , True , None }  => Duplicates are not allowed 
print(len(a))  #=> The length is : 5
a . remove(25)  #=> To remove 25 in the set .
print(a)  #=> The output is : {10.8, ‘Hyd’ , None, True}
a . append(100)  #=> The append method not support in set
a . add(set())   #=> The output is : Error (set inside set not allowed )
a . add(())  #=> The tuple is immutable -allowed.
a . add([]) #=> The output is : Error
print(a)
a . add({}) #=> The output is : Error.

#6 . # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #=> The output is : {25 , True , ‘Hyd’ , 10.8}
print('Iterate  thru  set  with  for  loop')
#How  to  iterate  thru  set  with  for  loop    => The output is :   for x in a : 
for x in a:
    print(x)


#7  . # Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #=> The output is : {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  #=> The output is :  <class ‘dict’>
print(How  to  print  value  key  10)  #=> The output is : print(a[10])  value is Ramesh
print(How  to  print  value  key  20)  #=> The output is : print(a[20]) values is Kiran
print(How  to  print  value  key  15)  #=> The output is : print(a[15]) value is Amar
print(How  to  print  value  key  18) #=> The output is : print(a[18]) value is sita
print(a[19])  #=> The output is: KeyError
print(a[0])  #=> The output is : KeyError
print(a['Amar']) #=> The output is : The output is : KeyError.
How  to  moify  value  of   key  15  to  'Krishna' #=> a[15] = ‘Krishna’
How  to  remove  20 :  'Kiran'  from  dict  'a'   #=> del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' # => a[25] = ‘vamsi’
print(a)  #=> The output is :  {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) #=> The output is : 4
print(a * 2) #=> The output is : error because dublicates keys are not allowed in the ‘dict’


#8 . Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)  #=> The output is : {10 : ‘sec’}
print(len(a))  #=> The output is : 1 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)  #=> The output is : {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) #=> The output is : 4


#9  .  #  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)  #=> The output is : {1 : ‘May be’} 
print(len(a)) #=> The output is : 1

#10 . # Find  outputs
a = { [ ] : 25}  #=> The output is : list is muttable
b = { ( ) : 25}
print(b) #=>  The output is : {(): 25}
c = { { } : 25}  #=> Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)  #=> The output is : {'Ramesh': [9948250500, 9848565090, 9440250404]} 
print(len(d)) #=> The output is : 1 
e = {set() : 10.8} #=> The output is Error : Set is mutable


#11 . # Find  outputs
a = {}
print(type(a))  #=> The output is : <class ‘dict’>
print(len(a))  #=> The output is : 0
print(a)  #=> The output is : {}
b = dict()  
print(type(b))   #=> The output is : <class ‘dict’>
print(len(b))  #=> The output is : 0
print(b)  #=> The output is : {}

Answers : a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print("Dictionary with print function")
print(a)
print("Keys of dictionary")
for k in a.keys():
    print(k)
print("Values of dictionary")
for v in a.values():
    print(v)
print("Tuples of dict_items object")
for t in a.items():
    print(t)
print("Elements of each tuple")
for k, v in a.items():
    print(k, v)
print("Keys and values of dictionary")
for key in a:
    print("Key =", key, "Value =", a[key])

#12 . #  Find  outputs (Home  work)
a = {
		print('Hyd') ,  #=> ‘Hyd’
		print('Sec') ,  #=> ‘Sec’
		print('Cyb')  #=> ‘Cyb’
	}
print(type(a))  #=> <class ‘set’>
print(a)  #=> {None}
print(len(a)) #=> The output is : 1

#13 . #  Anonymous  object  demo  program
_ = 25
print(_)  #=> The output is : 25
print(type(_))   #=> Te output is : <class ‘int’>
a , _ , c = 10 , 20 , 30
print(a)  #=> The output is : 10
print(_)  #=> The output is : 20
print(c)  #=> The output is : 30
for  _  in  range(5):
	print(_ , 'Hello')  # => The output is : 0 Hello
1 Hello
2 Hello
3 Hello
4 Hello