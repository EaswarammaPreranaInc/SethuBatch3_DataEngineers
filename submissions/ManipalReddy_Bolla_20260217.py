#  set  object  demo  program  (Home  work)
a = {25, 10.8, "Hyd", True, 3 + 4j, None, 25, "Hyd"}
print(a)  # {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))  # <class 'set'>
print(len(a))  # 6
print(a[2])  # Error
print(a[1:4])  # Error
a[2] = "Sec"  # Error
print(a * 2)  # Error
print(a * a)  # Error


#  set()  function demo  program
a = set("Rama rAo")
print(a)  # {'R', 'a', 'm', ' ', 'r', 'A', 'o'}
print(len(a))  # 7
print(set([10, 20, 15, 20]))  # {10 , 20 , 15}
print(set((25, 10.8, "Hyd", 10.8)))  # {25 , 10.8 , 'Hyd'}
print(set(range(10, 20, 3)))  # {10 , 13 , 16 , 19}
print(set(25))  # Error
print(set([25, 10.8, [], "Hyd"]))  # Error


# Tricky  program
# Find  outputs (Home  work)
a = {1, "Hyd", False, True, 0.0, "", 1.0, 0}
print(a)  # {1,'Hyd',False,''}
print(len(a))  # 4
print(type(a))  # <class 'set'>

# Find  outputs  (Home  work)
a = []
b = ()
c = {}
d = set()
print(type(a))  # <class 'list'>
print(type(b))  # <class 'tuple'>
print(type(c))  # <class 'dict'>
print(type(d))  # <class 'set'>
print(a)  # []
print(b)  # ()
print(c)  # {}
print(d)  # set()


# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a.add(25)  # {25}
a.add(10.8)  # {25 , 10.8}
a.add("Hyd")  # {25 , 10.8 , 'Hyd'}
a.add(True)  # {25 , 10.8 , 'Hyd' , True}
a.add(None)  # {25 , 10.8 , 'Hyd' , True , None}
a.add("Hyd")  # {25 , 10.8 , 'Hyd' , True , None}
a.add(1)  # {25 , 10.8 , 'Hyd' , True , None}
print(a)  # {25 , 10.8 , 'Hyd' , True , None}
print(len(a))  # 5
a.remove(25)  # {10.8 , 'Hyd' , True , None}
print(a)  # {10.8 , 'Hyd' , True , None}
a.append(100)  # Error
a.add(set())  # Error
a.add(())  # {10.8 , 'Hyd' , True , None , () }
a.add([])  # Error
print(a)  # {10.8 , 'Hyd' , True , None , () }
a.add({})  # Error


# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25, True, "Hyd", 10.8}
print("set  with  print  function")
print(a)  # {25 , True , 'Hyd' , 10.8}
print("Iterate  thru  set  with  for  loop")
for i in a:
    print(i)


# Find  outputs  (Home  work)
a = {10: "Ramesh", 20: "Kiran", 15: "Amar", 18: "Sita"}
print(a)  # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a))  # <class 'dict'>
print(a[10])  # Ramesh
print(a[20])  # Kiran
print(a[15])  # Amar
print(a[18])  # Sita
print(a[19])  # Error no key exist
print(a[0])  # Error no key exist
print(a["Amar"])  # Error no key exist
# How  to  moify  value  of   key  15  to  'Krishna'
a[15] = "Krishna"
# How  to  remove  20 :  'Kiran'  from  dict  'a'
del a[20]
# How  to  append  25 : 'Vamsi'  to  dict  'a'
a[25] = "Vamsi"
print(a)  # {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita' , 25 : 'Vamsi'}
print(len(a))  # 4
print(a * 2)  # Error


# Find  outputs  (Home  work)
a = {10: "Hyd", 10: "Sec"}
print(a)  # {10 : 'Sec'}
print(len(a))  # 1
b = {"R": "Red", "G": "Green", "B": "Blue", "Y": "Yellow", "G": "Gray", "B": "Black"}
print(b)  # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b))  # 4


#  Tricky  program
# Find output  (Home  work)
a = {True: "Yes", 1: "No", 1.0: "May  be"}
print(a)  # {True : 'May  be'}
print(len(a))  # 1


# Find  outputs
a = {[]: 25}  # Error
b = {(): 25}  # { () : 25}
print(b)  # { () : 25}
c = {{}: 25}  # Error
d = {"Ramesh": [9948250500, 9848565090, 9440250404]}
print(d)  # {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))  # 1
e = {set(): 10.8}  # Error


# Find  outputs
a = {}
print(type(a))  # <class 'dict'>
print(len(a))  # 0
print(a)  # {}
b = dict()
print(type(b))  # <class 'dict'>
print(len(b))  # 0
print(b)  # {}


# How  to  print  dictionary  in  different  ways
a = {10: "Ramesh", 20: "Kiran", 15: "Amar", 18: "Sita"}
print("Dictionary  with  print  function")
# How  to  print  dictionary  with  print()  function
print(a)
print("Keys  of  dictionary")
print(a.keys())  # dict_keys([10 , 20 , 15 , 18])
# How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
for i in a.keys():
    print(i)
print("Values  of  dictionary")
print(a.values())  # dict_values(['Ramesh' , 'Kiran' , 'Amar' , 'Sita'])
# How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
for i in a.values():
    print(i)
print("Tuples  of  dict_items   object")
print(
    a.items()
)  # dict_items([(10 , 'Ramesh') , (20 , 'Kiran') , (15 , 'Amar') , (18 , 'Sita')])
# How to print each key and corresponding value in dict 'a'
for k, v in a.items():
    print(k, v)

# How to print elements of each tuple in the list of dict_items object
for t in a.items():
    print(t[0], t[1])


#  Find  outputs (Home  work)
a = {print("Hyd"), print("Sec"), print("Cyb")}
print(type(a))  # <class 'set'>
print(a)  # {None , None , None} => {None}
print(len(a))  # 1


#  Anonymous  object  demo  program
_ = 25
print(_)  # 25
print(type(_))  # <class 'int'>
a, _, c = 10, 20, 30
print(a)  # 10
print(_)  # 20
print(c)  # 30
for _ in range(5):
    print(_, "Hello")


# 0 Hello
# 1 Hello
# 2 Hello
# 3 Hello
# 4 Hello
