#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #Outout: {Nonee, True, 25, 10.8, 'Hyd', (3+4j)}
print(type(a)) #Output:<class 'set'>
print(len(a)) #Output:6
print(a[2]) #Output:Error
print(a[1 : 4]) #Output:Error
a[2] = 'Sec' #Output:Error
print(a * 2) #Output:Error
print(a * a) #Output:Error
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #Output:{False, 1, 'Hyd', ''}
print(len(a)) #Output:4
print(type(a)) #Output:<class 'set'>
#  set()  function demo  program
a = set('Rama rAo')
print(a) # #Output:{'R', 'm', 'a', '', 'r', 'A', 'o'}
print(len(a)) #Output:7
print(set([10 , 20 , 15 , 20])) #Output:{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #Output:{25,10.8,'Hyd'}
print(set(range(10 , 20 , 3))) #Output:{10,13,16,19}
print(set(25)) #Output:Error
print(set([25 , 10.8 , [] , 'Hyd'])) #Output:Error


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
print(type(a)) #Output: <class 'list'>
print(type(b)) #Output: <class 'tuple'>
print(type(c)) #Output: <class 'dict'>
print(type(d)) #Output: <class 'set'>
print(a) #Output: []
print(b) #Output: ()
print(c) #Output: {}
print(d) #Output: set()
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
print(a) #Output:{25,10.8,'Hyd',True,None}
print(len(a)) #Output:5
a . remove(25) 
print(a) #Output:{10.8,'Hyd',True,None}
a . append(100) 
a . add(set()) 
a . add(()) 
a . add([]) 
print(a) #Output:Error
a . add({}) #Output:Error
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #Output:{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a)) #Output:<class 'dict'>
print(How  to  print  value  key  10) #Output: print(a[10])
print(How  to  print  value  key  20) #Output: print(a[20])
print(How  to  print  value  key  15) #Output: print(a[15])
print(How  to  print  value  key  18) #Output: print(a[18])
print(a[19]) #Output: Error
print(a[0]) #Output: Error
print(a['Amar']) #Output: Error
How  to  moify  value  of   key  15  to  'Krishna' #Output:a[15]='Krishna'
                                                           print(a)
How  to  remove  20 :  'Kiran'  from  dict  'a'  #Output:del a[20]
                                                         print(a)
How  to  append  25 : 'Vamsi'  to  dict  'a'  #Output:new_items={25 : 'Vamsi'}
                                                      a.append(new_items)
print(a) #Output:{10: 'Ramesh', 20: 'Kiran', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) #Output:5
print(a * 2) #Output:Error
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #Output:{10 : 'Sec'}
print(len(a)) #Output: 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #Output: {'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) #Output: 4
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #Output: {True: 'May  be'}
print(len(a)) #Output:1
# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) #Output: { ( ) : 25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #Output:{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) #Output:1
e = {set() : 10.8} 
# Find  outputs
a = {}
print(type(a)) #Output:<class 'dict'>
print(len(a)) #Output:0
print(a) #Output:{}
b = dict() 
print(type(b)) #Output:'<class dict'>
print(len(b)) #Output:0
print(b) #Output:dict()
 #Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
#Output:'Hyd'
        'Sec'
        'Cyb'
print(type(a)) #Output: <class 'set'>
print(a) #Output:None
print(len(a)) #Output:1
#  Anonymous  object  demo  program
_ = 25
print(_) #Output: 25
print(type(_)) #Output: <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) #Output: 10
print(_) #Output: 20
print(c) #Output: 30
for  _  in  range(5):
	print(_ , 'Hello') #Output: 0 'Hello'
                                    1 'Hello'
                                    2 'Hello'
                                    3 'Hello'
                                    4 'Hello'