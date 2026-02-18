a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a)) #<class set>
print(len(a)) #6
print(a[2]) #Error
print(a[1 : 4]) #Error
a[2] = 'Sec' #Error
print(a * 2) #Error
print(a * a) #Error


a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)#{False, 1, 'Hyd', ''}
print(len(a))#4
print(type(a))#<class set>



a = set('Rama rAo')
print(a #{'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a))#7
print(set([10 , 20 , 15 , 20])) #{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3))) #10, 13, 16, 19
print(set(25)) #Error
print(set([25 , 10.8 , [] , 'Hyd'])) #Error




a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #<class list>
print(type(b)) #<class tuple>
print(type(c)) #<class dict>
print(type(d)) #<class set>
print(a) #[]
print(b)#()
print(c)#{}
print(d)#set()


a = set()
a . add(25) #set(25)
a . add(10.8)#set(25 ,10.8)
a . add('Hyd')#set(25,10.8,'Hyd')
a . add(True)#set(25,10.8,'Hyd',True)
a . add(None)#set(25,10.8,'Hyd',True,None)
a . add('Hyd')#duplicates not allowed
a . add(1)#duplicates not allowed
print(a) #set(25,10.8,'Hyd',True,None)
print(len(a))#5
a . remove(25)#set(10.8,'Hyd',True,None)
print(a) #set(10.8,'Hyd',True,None)
a . append(100) #Error
a . add(set()) Error
a . add(())#allowed
a . add([])#Error
print(a)#Error
a . add({})#Error



a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function') 
print(???) #{True, 25, 10.8, 'Hyd'}
print('Iterate  thru  set  with  for  loop') 

for item in a:
    print(item)

How  to  iterate  thru  set  with  for  loop


a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#<class dict>
print(How  to  print  value  key  10) #a[9]
print(How  to  print  value  key  20) #a[19]
print(How  to  print  value  key  15) #a[14]
print(How  to  print  value  key  18) #a[17]
print(a[19])#Not there 
print(a[0])#not valid
print(a['Amar'])#15
How  to  moify  value  of   key  15  to  'Krishna' #a[15] = 'Krishna'
How  to  remove  20 :  'Kiran'  from  dict  'a' #a.pop(20)  
How  to  append  25 : 'Vamsi'  to  dict  'a' #a[25] = 'Vamsi'
print(a) #{10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a))#4
print(a * 2)#Error cannot do



a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10 : 'Sec'}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R':'Red', 'G':'Gray', 'B':'Black', 'Y':'Yellow'}
print(len(b)) #4


a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True: 'may be'}
print(len(a)) #1


a = { [ ] : 25}
b = { ( ) : 25}
print(b) #{ ( ):25}
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8}



a = {}
print(type(a)) #<class dect>
print(len(a)) #0
print(a) #{}
b = dict()
print(type(b)) #<class dict>
print(len(b)) #0
print(b) #{}