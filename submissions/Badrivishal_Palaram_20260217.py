1) set object demo program outputs
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)#O/P:{25 , 10.8 , 'Hyd' , True , 3+4j , None }
print(type(a))#O/P:<class 'set'>
print(len(a))#O/P:6
print(a[2])#O/P:Error because indexing is not possible
print(a[1 : 4])#O/P:Error because slicing is not possible
a[2] = 'Sec'#O/P:Error because indexing is not possible
print(a * 2)#O/P:Error because no duplicates
print(a * a)#O/P:Error because no duplicates


2) Tricky program outputs
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 , 0}
print(a) #O/P:{1 , 'Hyd' , False , '' }
print(len(a))#O/P:4
print(type(a))#O/P:<class 'set>


3) set() function demo program outputs
a = set('Rama rAo')
print(a)#{'R', 'a', 'm', 'r', 'A', 'o', ' '}
print(len(a))#O/P:7
print(set([10 , 20 , 15 , 20]))#O/P:{10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8)))#O/P:{25, 10.8, 'Hyd'}
print(set(range(10 , 20 , 3)))#O/P:{10,13,16,19}
print(set(25))#O/P:Error because it is not permitted
print(set([25 , 10.8 , [] , 'Hyd']))#O/P:Error because it is not permitted


4) outputs
a = [ ]
b = ( )
c = {}
d = set()
print(type(a))#O/P:<class 'list'>
print(type(b))#O/P:<class 'tuple'>
print(type(c))#O/P:<class 'dict'>
print(type(d))#O/P:<class 'set'>
print(a)#O/P:[ ]
print(b)#O/P:( )
print(c)#O/P:{}
print(d)#set()


5) Tricky program output
- add() and remove() methods
a = set()
a . add(25)
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a)#O/P:{25, 10.8, 'Hyd', True, None}
print(len(a))#O/P:5
a . remove(25)
print(a)#O/P:{10.8, 'Hyd', True, None}
a . append(100)
a . add(set())
a . add(())
a . add([])
print(a)#O/P:Error because it is not permitted
a . add({})


6) How to print set in two different ways outputs
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')#O/P:{25 , True , 'Hyd' , 10.8}
print(???)
print('Iterate thru set with for loop')#
How to iterate thru set with for loop


7) outputs
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)# {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))#O/P:<class 'dict'>
print(How to print value key 10)#O/P:a[10]
print(How to print value key 20)#O/P:a[20]
print(How to print value key 15)#O/P:a[15]
print(How to print value key 18)#O/P:a[18]
print(a[19])#O/P:Error because not valid
print(a[0])#O/P:Error because not valid
print(a['Amar'])#O/P:Error because not valid
How to modify value of key 15 to 'Krishna'#O/P:a[15]='krishna'
How to remove 20 : 'Kiran' from dict 'a'#O/P: del a[20]
How to append 25 : 'Vamsi' to dict 'a'#O/P:a[19]='vamsi'
print(a)#{10: 'Ramesh', 15: 'krishna', 18: 'Sita', 19: 'vamsi'}
print(len(a))#O/P:4
print(a * 2)#O/P:Error because no duplicates


8) outputs
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)#{10:'Sec'}
print(len(a))#O/P:1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' ,
'B' : 'Black'}
print(b)#O/P:{'R': 'Red', 'G': 'Gray', 'B': 'Black', 'Y': 'Yellow'}
print(len(b))#O/P:4


9) Tricky program outputs
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May be'}
print(a)#{True : 'May be'}
print(len(a))#O/P:1


10) outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)#O/P:Error because it is not permitted
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)#O/P:{'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d))#O/P:1
e = {set() : 10.8}#O/P:Error because it is not valid


11) outputs
a = {}
print(type(a))#O/P:<class 'dict'>
print(len(a))#O/P:0
print(a)#O/P:{}
b = dict()
print(type(b))#O/P:<class 'dict'>
print(len(b))#O/P:0
print(b)#O/P:{}


12) How to print dictionary in different ways
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary with print function')#O/P:print(a)
How to print dictionary with print() function
print('Keys of dictionary')#O/P:print(key)
How to iterate thru each key of dict 'a' with for loop
print('Values of dictionary')#O/P:print(value)
How to iterate thru each value of dict 'a' with for loop
print('Tuples of dict_items object')#O/P:print(items)
How to iterate thru each tuple of dict 'a' with for loop
print('Elements of each tuple')#O/P:print(key=a[], value=' ')
How to print elements of each tuple in the list of dict_items object
print('Keys and values of dictionary')#O/P:print(key,value)
How to print each key and corresponding value in dict 'a'


13) outputs
a = {
print('Hyd') ,#O/P:Hyd
print('Sec') ,#O/P:Sec
print('Cyb') #O/P:Cyb
}
print(type(a))#O/P:<class 'set'>
print(a)#{None}
print(len(a))#O/P:1


14) Anonymous object demo program outputs
_ = 25
print(_)#25
print(type(_))#O/P:<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#O/P:10
print(_)#O/P:20
print(c)#O/P:30
for _ in range(5):
print(_ , 'Hello')# 0 Hello
1 Hello
2 Hello
3 Hello
4 Hello
