Name-Dhruva Gupta			Subject-Python			Date-17/2/26			

1)
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) #Set printed
print(type(a)) #class set
print(len(a)) #6
print(a[2]) #error as set is not indexed
print(a[1 : 4]) #error as set is not indexed
a[2] = 'Sec' 
print(a * 2) #error as set doesn’t have duplicates
print(a * a)  #error as set doesn’t have duplicates

2)
# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) #{1 , 'Hyd' , False ,’ ’}
print(len(a)) #4
print(type(a)) #class set

3)
#  set()  function demo  program
a = set('Rama rAo')
print(a) #{‘R’ , ‘a’, ‘m’, ‘ ‘,’r’,’A’, ’o’}
print(len(a)) #7
print(set([10 , 20 , 15 , 20])) #{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{25,10.8,’Hyd’}
print(set(range(10 , 20 , 3))) #{10,13,16,19}
print(set(25)) #argument should be a sequence 
print(set([25 , 10.8 , [] , 'Hyd'])) #error as sets allows only immutable elements 

4)
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a)) #class list
print(type(b)) #class tuple
print(type(c)) #class dict 
print(type(d)) #class set
print(a) #[]
print(b)#()
print(c)#{}
print(d) #set()

5)
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
print(a) {25,'Hyd', True, None,10.8}
print(len(a)) #5
a . remove(25)
print(a) #{'Hyd', True, None,10.8}
a . append(100) #not valid with set
a . add(set()) #error
a . add(()) #{'Hyd', True, None,10.8,()}
a . add([])
print(a) #{'Hyd', True, (),None,10.8}
a . add({}) #error as dict in mutable

6)
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a) #{25 , True , 'Hyd' , 10.8}
print('Iterate  thru  set  with  for  loop')
for i in a:
   print(i) #prints each element in new line 
How  to  iterate  thru  set  with  for  loop

7)
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #class dict 
print(How  to  print  value  key  10) #a[10]
print(How  to  print  value  key  20) a[20]
print(How  to  print  value  key  15) a[15]
print(How  to  print  value  key  18) a[18]
print(a[19]) #error as element does not exist 
print(a[0]) #not present
print(a['Amar']) #error as we can’t access value
How  to  moify  value  of   key  15  to  'Krishna' #a[15]=Krishna
How  to  remove  20 :  'Kiran'  from  dict  'a' #del a[20]
How  to  append  25 : 'Vamsi'  to  dict  'a' a[25]='Vamsi'
print(a) #{10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita',25:'Vamsi'}
print(len(a)) #4
print(a * 2) #dictionary is not multiplied

8)
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) #{10:’Sec’}
print(len(a)) #1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))#4

9)
#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) #{True:’May be’}
print(len(a)) #1

10)
# Find  outputs
a = { [ ] : 25} #error
b = { ( ) : 25}
print(b) #{ ( ) : 25}
c = { { } : 25} #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d)) #1
e = {set() : 10.8} #error as dictionary can only have int, float, string, tuple only

11)
# Find  outputs
a = {}
print(type(a)) #class dict
print(len(a)) #0
print(a) #{}
b = dict()
print(type(b)) #class dict
print(len(b)) #0
print(b) {}

12)
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') #print(a)
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary') #print(a.keys())
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop 
#for k in a:
        print(k.keys)
print('Values  of  dictionary’) #print(a.values())
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
##for k in a:
        print(k.values)
print('Tuples  of  dict_items   object')
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
#print(a.items)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary’)
#for k,v in a.items():
    #print(k,v)
How  to  print  each  key  and  corresponding  value  in  dict  'a' #print(a)
#for k,v in a.items():
	print(‘Key=‘,k,’Value=‘,v)

13)
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a)) #class set
print(a) #{None}
print(len(a))  #1

14)
#  Anonymous  object  demo  program
_ = 25
print(_) #25
print(type(_)) #class int 
a , _ , c = 10 , 20 , 30
print(a) #10
print(_) #20
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello') #_ , 'Hello' is printed 5 times with _ changing 0 to 5