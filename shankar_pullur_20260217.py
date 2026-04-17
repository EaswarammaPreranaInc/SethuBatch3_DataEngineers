#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)                            #{25,10.8,'Hyd',True,3+4j,None}
print(type(a))                      #<class 'set'>
print(len(a))                       # 6
#print(a[2])                        # error 
#print(a[1 : 4])                    # error (no slicing)
#a[2] = 'Sec'                       # error (no modifing using index)
#print(a * 2)                       #error  
#print(a * a)    


a = set('Rama rAo')
print(a)                               #{'r','A',' ','a','m','0'}
print(len(a))                          # 6
print(set([10 , 20 , 15 , 20]))        # {10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {25,'Hyd',10.8}
print(set(range(10 , 20 , 3)))         #{19,13,16,10} 
#print(set(25))                        # error
#print(set([25 , 10.8 , [] , 'Hyd']))  #error 


a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)                                # {1,'Hyd',False,''}
print(len(a))                           # 4
print(type(a))                          # <class 'set'>


a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))               #<class 'list'>
print(type(b))               #<class 'tuple'>
print(type(c))               #<class 'set'>
print(type(d))               #<class 'set'>
print(a)                     #[]
print(b)                     #()
print(c)                     #{}
print(d)                     #{}



a = set()
a . add(25)  
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)                    #{10.8,'Hyd',True,None,25}
print(len(a))               # 5
a . remove(25)        
print(a)                    #{10.8,True,None,'Hyd'}
#a . append(100)             # error
#a . add(set())              # error
a . add(())                                 
#a . add([])                 #error
print(a)                    #{10.8,True,None,'Hyd',()}
#a . add({})



a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print('Iterate  thru  set  with  for  loop')
for i in a:
    print(i)




a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)                                       #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))                                 #<class 'dict'>
print(a[10])          # 
print(a[20])          # 
print(a[15])          # 
print(a[18])          # 
#print(a[19])                                   # error
#print(a[0])                                    # error
#print(a['Amar'])                               # error
#How  to  moify  value  of   key  15  to  'Krishna'
#How  to  remove  20 :  'Kiran'  from  dict  'a'
#How  to  append  25 : 'Vamsi'  to  dict  'a'
 
a[15]='Krishna'
del a[20]
a[25]='vamshi'
print(a)                        #{10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'vamshi'}
print(len(a))                   # 4
#print(a * 2)



a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)                      #{10:sec}
print(len(a))                 # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)       # {'R' : 'Red' ,'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(len(b))  # 4


a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)                                # {True:'May be'}
print(len(a))                           # 1




#a = { [ ] : 25}    #Error
b = { ( ) : 25}
print(b)            #{():25}
#c = { { } : 25}     #error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)         #{'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))    #1
#e = {set() : 10.8} # error


a = {}
print(type(a))       # <class 'dict'>
print(len(a))        # 0
print(a)             #{}
b = dict()       
print(type(b))      # <class 'dict'>
print(len(b))       # 0
print(b)            #{}




a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')

print('Keys  of  dictionary')
for i in a.keys():
    print(i)
#How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
for i in a.values():
    print(i)
#How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
for i in a.items():
    print(i)


a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
	}
print(type(a))       #<class 'set'>
print(a)              #none
print(len(a))         #1


_ = 25
print(_)       # 25
print(type(_)) #  <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)       # 10
print(_)       # 20
print(c)       #30
for  _  in  range( 5):
	print(_ , 'Hello')          # 0 hello # 1 hell0 # 2 hello# 3 hello  # 4 hello
