#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{None, True, 'Hyd', 25, 10.8, (3+4j)}
print(type(a))#class set 
print(len(a))#6
print(a[2])# no index in set
print(a[1 : 4]) # slicing not possible 
a[2] = 'Sec' # error no modification 
print(a * 2) #error 
print(a * a) #error
: # Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1,'Hyd',False, True, "}
print(len(a))#4
print(type(a))# class set
: # Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #class 'list'
print(type(b)) #class 'tuple'
print(type(c)) #class 'dict'
print(type(d)) #class 'set'
print(a) #empty
print(b) # empty 
print(c) # empty
print(d) # empty: # Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # {25,10.8,'Hyd',True,None}
print(len(a))#5
a . remove(25)
print(a) #{10.8,'Hyd',True,None}
a . append(100) #error 
a . add(set())#error
a . add(())#error
a . add([])#error
print(a)#{10.8,'Hyd',True,None}
a . add({})#error
 # How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(???)
print('Iterate  thru  set  with  for  loop')
How  to  iterate  thru  set  with  for  loop # for x in a:
Print(x)
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)#{10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
print(type(a))# class dict
print(How  to  print  value  key  10) #print(a[10])
print(How  to  print  value  key  20) #print(a[20])
print(How  to  print  value  key  15) #print(a[15])
print(How  to  print  value  key  18) ##print(a[18])
print(a[19]) #error
print(a[0]) #error
print(a['Amar']) #error 
How  to  moify  value  of   key  15  to  'Krishna' # print(a[15])='Krishna'
How  to  remove  20 :    'Kiran'  from  dict  'a' #del a[20]
How  to  append  25 :  'Vamsi'  to  dict  'a' #a[25]='vamsi'
print(a) #{10: 'Ramesh',  15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) #4
print(a * 2) #error
 # Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10: 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b)) #4
:#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{1:'No'}
print(len(a)) 1
# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b) # error
c = { { } : 25} #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #error
# Find  outputs
a = {}
print(type(a))#dict
print(len(a))#1
print(a)#empty
b = dict()
print(type(b))#dict 
print(len(b))#1
print(b)#empty
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) #class set
print(a) #Hyd
Sec
Cyb
print(len(a))#3
#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_))#int
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
	print(_ , 'Hello') #Hello,Hello, Hello,Hello,Hello
