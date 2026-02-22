#  set  object  demo  program  (Home  work) 
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'} 
print(a) #{25 , 10.8 , 'Hyd' , True , 3+4j , None} 
print(type(a)) #<class 'set'> 
print(len(a)) #6 
print(a[2]) # Error due to set is unordered sequence. 
print(a[1 : 4]) # Error due to set is unordered sequence. 
a[2] = 'Sec' #Error we cannot access due to set is unordered. 
print(a * 2) # Error due to set does not contains duplicate values. 
print(a * a) # Error due to set does not contains duplicate values. 
# Tricky  program 
# Find  outputs (Home  work) 
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0} 
print(a) #{1 , 'Hyd' , False , ''} 
print(len(a)) #4 
print(type(a)) #<class 'set'> 
#  set()  function demo  program 
a = set('Rama rAo') 
print(a) #{'R', 'r', ' ', 'a', 'A', 'm', 'o'} 
print(len(a)) #7 
print(set([10 , 20 , 15 , 20])) #{10 , 20 , 15 , 20} 
print(set((25 , 10.8 , 'Hyd' , 10.8))) #{25 , 10.8 , 'Hyd'} 
print(set(range(10 , 20 , 3))) #{10,16,13,19} 
print(set(25)) #Error due to int object cannot be iterate. 
print(set([25 , 10.8 , [] , 'Hyd'])) #Error due to set is immutable. 
# Find  outputs  (Home  work) 
a =   [ ] 
b =   ( ) 
c =   {} 
d =   set() 
print(type(a)) #<class 'list'> 
print(type(b)) #<class 'tuple'> 
print(type(c)) #<class 'dict'> 
print(type(d)) #<class 'set'> 
print(a) # [] 
print(b) # () 
print(c) # {} 
print(d) # set() 
# Tricky  program 
# add()  and  remove()  methods  (Home  work) 
a = set() 
a . add(25)  
a . add(10.8) 
a . add('Hyd') 
a . add(True) 
a . add(None) 
a . add('Hyd') #Error set only has unique elements. 
a . add(1) #Error set only has unique elements. 
print(a) #{25, 10.8, 'Hyd', True, None} 
print(len(a))#5 
a . remove(25)  
print(a) #{10.8, 'Hyd', True, None} 
a . append(100) #Error set is unordered 
a . add(set()) #Error 
a . add(()) #Error 
a . add([]) #Error 
print(a)#{10.8, 'Hyd', True, None} 
a . add({}) #Error 
# How  to  print  set  in  two  differnet ways  (Home  work) 
a = {25 , True , 'Hyd' , 10.8} 
print('set  with  print  function')  
print(a) # {25 , True , 'Hyd' , 10.8} 
print('Iterate  thru  set  with  for  loop') 
for i in a: 
print(i)  #25 
True 
Hyd 
10.8 
# Find  outputs  (Home  work) 
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print(type(a)) #<class 'dict'> 
print(How  to  print  value  key  10) # print(a[10]) -> 'Ramesh'  
print(How  to  print  value  key  20) # print(a[20]) -> 'Kiran' 
print(How  to  print  value  key  15) # print(a[15]) -> 'Amar' 
print(How  to  print  value  key  18) # print(a[18]) -> 'Sita' 
print(a[19]) # Error no 19 key is not present 
print(a[0]) #Error key 0 not present 
print(a['Amar']) # Error value cannot be accessed. 
How  to  modify  value  of   key  15  to  'Krishna' #a[15]= 'Krishna' 
How  to  remove  20 :  'Kiran'  from  dict  'a' #del a[20] 
How  to  append  25 : 'Vamsi'  to  dict  'a'  #a[25]= 'Vamsi' 
print(a) #{10 : 'Ramesh', 15 : 'Krishna' , 18 : 'Sita', 25 : 'Vamsi'} 
print(len(a)) # 4 
print(a * 2)  # Error dict cannot multipled. 
# Find  outputs  (Home  work) 
a = {10 : 'Hyd' , 10 : 'Sec'} 
print(a) #{10 : 'Hyd' , 10 : 'Sec'} 
print(len(a)) #2 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} 
print(b) #{'R' : 'Red', 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'} 
print(len(b)) #4 
#  Tricky  program 
# Find output  (Home  work) 
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'} 
print(a) #{True : 'May  be'} # 1 = True , 1.0 = 1  
print(len(a)) #1 
# Find  outputs 
a = { [ ] : 25} #Error list is mutable we cannot use it as a key. 
b = { ( ) : 25} #We can use tuple -> It is immutable. 
print(b) # { () : 25} 
c = { { } : 25} #Error dict cannot be used as a key. 
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} 
print(d) #{'Ramesh' : [9948250500, 9848565090, 9440250404]} 
print(len(d)) # 1 
e = {set() : 10.8} #Error set is mutable cannot be used as a key. 
# Find  outputs 
a = {} 
print(type(a)) #<class 'dict'> 
print(len(a)) #0 
print(a) #{} 
b = dict()  
print(type(b)) #<class 'dict'> 
print(len(b))#0 
print(b) #{} 
# How  to  print  dictionary  in  different  ways 
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'} 
print('Dictionary  with  print  function') # print(a) 
How  to  print  dictionary  with  print()  function 
print('Keys  of  dictionary') #print(a.keys()) 
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop 
#for k in a: 
print(k) 
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop 
print('Values  of  dictionary')  
# for v in a.values(): 
print(v) 
print('Tuples  of  dict_items   object') # 
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop 
# for t in a.items(): 
print(i) 
print('Elements  of  each   tuple') 
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object 
#for dict_items in a.items(): 
print(dict_items[0],dict_items [1]) 
print('Keys  and  values  of  dictionary') 
How  to  print  each  key  and  corresponding  value  in  dict  'a' 
#for k,v in a.items():    # .items() prints tuples. 
print(k,v) 
#  Find  outputs (Home  work) 
a = { 
#Hyd 
#Sec 
#Cyb 
print('Hyd') , 
print('Sec') , 
print('Cyb') 
} 
print(type(a)) #<class 'set'> 
print(a) #{None} # Internally print() becomes none 
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
print(_ , 'Hello') 
''' 
0 Hello 
1 Hello 
2 Hello 
3 Hello 
4 Hello 
''' 