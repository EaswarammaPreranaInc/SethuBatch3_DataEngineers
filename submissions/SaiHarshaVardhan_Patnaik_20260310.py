#1
# Find outputs (Homework)
a = [10, 20, 15, 18]
b = a
print(a is b)   # True as b is just another name for same object (same memory address)
print(a == b)   # True as values are equal
b[2] = 12       # modifies the shared list (b and a point to same object)
print(a)        # [10, 20, 12, 18] as 'a' also reflects the change made via b



#2
# Find outputs (Home work)
a = [10, 20, 15, 18]
b = [100, 200, 150]
print(a + b)        # [10, 20, 15, 18, 100, 200, 150] i.e. list concatenation
print(a + 5)        # Error as one can only concatenate list (not "int") to list
print(a + '5')      # Error as can only concatenate list (not "str") to list
print([10, 20] + (30, 40))  # Error as one can only concatenate list (not "tuple") to list



#3
# Tricky program
# Find outputs
a = [1, 2, 3]
b = [4, 5, 6]
print(a, id(a))     # [1, 2, 3] and its memory address assigned by PVM
a += b              
print(a, id(a))     # [1, 2, 3, 4, 5, 6] <same_id> i.e. id remains the same as above



#4
# Tricky program
# Find outputs
a = [1, 2, 3]
b = [4, 5, 6]
print(a, id(a))     # [1, 2, 3] and its memory address asssigned by PVM
a = a + b           
print(a, id(a))     # [1, 2, 3, 4, 5, 6] <different_id> i.e. id is different from above



#5
# Find outputs
list = [25, 10.8, 'Hyd', True]
a, *b, c = list
print('a : ', a)        # a : 25       
print('b : ', b)        # b : [10.8, 'Hyd']  
print('c : ', c)        # c : True
print(type(b))          # <class 'list'>
x, *y = list
print('x : ', x)        # x : 25
print('y : ', y)        # y : [10.8, 'Hyd', True]
*p, q = list
print('p : ', p)        # p : [25, 10.8, 'Hyd']
print('q : ', q)        # q : True



#6
# Find outputs (Home work)
list = [25, 10.8, 'Hyd', True]
a, b, c, d, e = list            # Error as not enough values to unpack (expected 5, got 4)
a, b, *c, d, e = list          
print('a : ', a)        # a : 25
print('b : ', b)        # b : 10.8
print('c : ', c)        # c : []       
print('d : ', d)        # d : Hyd
print('e : ', e)        # e : True
a, b, *c, d, e, f = list  # Error as not enough values to unpack (expected at least 5, got 4)



#7
# Find outputs (Home work)
list = [25, 10.8, 'Hyd', True]
a, b, _, d = list
print('a : ', a)        # a : 25
print('b : ', b)        # b : 10.8
print('_ :  ', _)       # _ : Hyd    
print('d : ', d)        # d : True



#8
# Find outputs (Home work)
list = [25, 10.8, 'Hyd', True, 3+4j]
a, b, a, d, a = list    # 'a' is reassigned 3 times; final value is the last assigned
print('a : ', a)        # a : (3+4j)  i.e. last value assigned to a (5th element)
print('b : ', b)        # b : 10.8 
print('d : ', d)        # d : True 



#9
# Tricky program
# Find outputs (Home work)
list = [25, 10.8, 'Hyd', True, 3+4j]
a, b, _, d, _ = list    
print('a : ', a)    # a : 25
print('b : ', b)    # b : 10.8
print('_ : ', _)    # _ : (3+4j) i.e. last value assigned to _ (5th element)
print('d : ', d)    # d : True
print('_: ', _)     # _: (3+4j)  



#10
# Identify error (Home work)
list = [25, 10.8, 'Hyd', True, 3+4j]
a, *b, c, *d, e = list  # Error as multiple starred expressions in assignment , Only one starred variable is allowed per unpacking statement



#11
# Find outputs (Home work)
list = [[25, 10.8], 'Hyd', True]
a, b, c = list
print('a :  ', a)   # a : [25, 10.8]   
print('b :  ', b)   # b : Hyd
print('c :  ', c)   # c : True



#12
# Find outputs (Home work)
list = [[25, 10.8], 'Hyd', True]
[a, b], c, d = list  
print('a : ', a)        # a : 25
print('b : ', b)        # b : 10.8
print('c : ', c)        # c : Hyd
print('d : ', d)        # d : True
a, b, c, d = list       # Error as not enough values to unpack (expected 4, got 3)



#13
# Comparing Lists
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
c = [10, 20, 25, 9]
d = [10, 20, 7, 22]
print(a == b)   # True   i.e. same values at all positions
print(a is b)   # False  i.e. different objects in memory
print(a < c)    # True   i.e. compared element-by-element; 15 < 25 at index 2
print(a > d)    # True   i.e. compared element-by-element; 15 > 7 at index 2
print(a >= c)   # False  i.e. 15 is not >= 25 at index 2
print(a <= d)   # False  i.e. 15 is not <= 7 at index 2
print(a != c)   # True   i.e. lists are not equal
print(a != b)   # False  i.e. lists are equal, so != is False
print(a == c)   # False  i.e. values differ at index 2



#14
# Comparing Lists (Home work)
a = [10, 20, 15, 18]
b = [20, 18, 15, 10]
print(a == b)   # False i.e. element at index 0 differs (10 != 20); order matters in lists
print(a is b)   # False i.e. two separate objects in memory



#15
# len() function demo program (Home work)
a = [25, 10.8, 'Hyd', True]
print(len(a))           # 4
b = []
print(len(b))           # 0  
c = [[10, 20], 30, 40]
print(len(c))           # 3 



#16
# sum() function demo program (Home work)
a = [25, 10.8, True]
print(sum(a))           # 36.8   
b = [3+4j, 5+6j]
print(sum(b))           # (8+10j)  
c = [25, 10.8, True, 3+4j, False]
print(sum(c))           # (39.8+4j) 
d = [10, 20, 15, 18]
print(sum(d))           # 63
e = [25, 10.8, 'Hyd', True]
print(sum(e))           # Error as 'str' object can't be added to 'float' obejects simply, sum() cannot add strings



#17
# Find outputs
a = [[10, 20, 15, 18]]
print(sum(a))        # Error
print(sum(a[0]))     # 63   i.e a[0] = [10, 20, 15, 18]; sum of inner list
print(sum(*a))       # 63   i.e unpacks a to [10, 20, 15, 18]; another way



#18
# max() and min() functions demo program (Home work)
a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))           # 30
print(min(a))           # 5
b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))           # Vamsi    
print(min(b))           # Amar    
c = [25, 10.8, 3+4j, True]
print(max(c))           # Error as '>' not supported between instances of 'complex' and 'int' or simply complex numbers cannot be compared with > or <
d = [25, '35']
print(max(d))           # Error as '>' can't compare 'str' and 'int'
print(max([]))          # Error as max() needs an argument
print(min([]))          # Error as min() needs an argument



#19
# list() function demo program
a = (10, 20, 15, 18)
b = list(a)
print(b)         # [10, 20, 15, 18]  
print(type(b))   # <class 'list'>
print(a is b)    # False   
print(a == b)    # False  



#20
# Find outputs (Home work)
a = range(4, 10, 2)
b = list(a)
print(b)                # [4, 6, 8] 
print(type(b))          # <class 'list'>
a = list('Vamsi')
print(a)                # ['V', 'a', 'm', 's', 'i']  
a = list()
print(a)                # []  
print(list(25))         # Error as 'int' object is not iterable
print(list(10.8))       # Error as 'float' object is not iterable
print(list(True))       # Error as 'bool' object is not iterable
print(list(None))       # Error as 'NoneType' object is not iterable



#21
# Find outputs (Home work)
a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(list(a))          # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]  
b = {(10, 20), (30, 40, 50), (60, 70, 80, 90)}
print(list(b))          # [(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10, 20], (30, 40), {50, 60})
print(list(c))          # [[10, 20], (30, 40), {50, 60}] 



#22
# sorted() function demo program
a = [10, 20, 15, 5, 12]
b = sorted(a)
print(b)                # [5, 10, 12, 15, 20]  
print(type(b))          # <class 'list'>  
c = sorted(a, reverse=True)
print(c)                # [20, 15, 12, 10, 5] 
print(a)                # [10, 20, 15, 5, 12]  



#23
# Find outputs (Home work)
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
b = sorted(a)
print(b)    # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']   
c = sorted(a, reverse=True)
print(c)    # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']   
print(a)    # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']  



#24
# all() function demo program
a = [12 > 10, 5 < 20, 30 == 30]    # [True, True, True]
print(all(a))           # True   
b = [9 >= 6, 12 <= 9, 6 == 6]      # [True, False, True]
print(all(b))           # False  
c = [25, 10.8, '', True, 3+4j, 'Hyd']
print(all(c))           # False  
d = [10, 0, 20]
print(all(d))           # False  
e = []
print(all(e))           # True



#25
# any() function demo program (Home work)
a = [12 > 18, 5 < 20, 35 == 30]    # [False, True, False]
print(any(a))           # True   
b = [12 > 18, 25 < 20, 35 == 30]   # [False, False, False]
print(any(b))           # False 
c = [0, 0.0, '', 25, 0+0j, False]
print(any(c))           # True
d = [0, 0.0, '', 0+0j, False]
print(any(d))           # False  
e = []
print(any(e))           # False 



#26
# del operator demo program (Home work)
a = [10, 20, 15, 18]
print(a)        # [10, 20, 15, 18]
del a[2]        # deletes element at index 2 (value 15)
print(a)        # [10, 20, 18] 
del a[3]        # Error no index '3' is found i.e. 0, 1, 2
del a           # deletes the variable 'a' from memory entirely
print(a)        # Error as name 'a' is not defined i.e. deleted upon execution of 'del a'



#27
# append() method demo program (Home work)
list = [10, 20, 15, 18]
print(list)             # [10, 20, 15, 18]
list.append(19)        
print(list)             # [10, 20, 15, 18, 19]



#28
# Find outputs (Home work)
list = []
print(list)             # []
list.append(25)
list.append(10.8)
list.append('Hyd')
list.append(True)
print(list)             # [25, 10.8, 'Hyd', True]  



#29
# Find outputs (Home work)
list = []
for x in range(0, 50, 10):
    list.append(x)      # appends 0, 10, 20, 30, 40 one by one
print(list)             # [0, 10, 20, 30, 40]



#30
# Find outputs (Home work)
a = [10, 20, 30]
a.append('Hyd')
print(a)                # [10, 20, 30, 'Hyd']
print(len(a))           # 4
print(a[3])             # Hyd      
print(a[3][0])          # H        
print(a[3][1])          # y        
print(a[3][2])          # d       



#31
# Find outputs (Home work)
a = [10, 20, 30, 40]
b = [50, 60, 70]
a.insert(2, b)          # inserts list b as a single element at index 2
print(a)                # [10, 20, [50, 60, 70], 30, 40]
print(len(a))           # 5  
print(a[2])             # [50, 60, 70]   
print(a[2][0])          # 50
print(a[2][1])          # 60
print(a[2][2])          # 70



#32
# remove() method demo program (Home work)
try:
    list = [10, 20, 15, 18, 15, 12, 15, 19]
    list.remove(15)             # removes only the FIRST occurrence of 15
    print(list)                 # [10, 20, 18, 15, 12, 15, 19]
    list.remove(25)             # 25 not in list i.e. Error, caught by except
except:
    print('25 is not in the list')    # 25 is not in the list



#33
'''
Write a program to delete 'all' occurences of 'x' from the list

Let 1st input be [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14] and
2nd input be 15
What is the output? ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
usrip = input("Enter List : ")

cleantxt = usrip.replace("[", "").replace("]", "")
stritems = cleantxt.split(",")

a = []
for item in stritems:
    a.append(int(item))

b = int(input("Enter element to be deleted : "))

while b in a:
    a.remove(b)

print(f"List without {b}'s : {a}")



#34
# pop() method demo program
a = [10, 20, 15, 18, 12]
print(a.pop(2))         # 15 i.e removes & returns element at index 2 (value 15)
print(a)                # [10, 20, 18, 12]  
print(a.pop(len(a)))    # Error as pop index out of range
print(a.pop(-3))        # 20 i.e removes & returns element at index -3 (value 20)
print(a)                # [10, 18, 12]  
print(a.pop(-4))        # Error as pop index out of range
print(a.pop())          # 12 i.e. pop() with no argument removes & returns LAST element
print(a)                # [10, 18]
b = []
b.pop()                 # Error as cannot pop from an empty list



#35
# clear() method demo program (Home work)
list = [10, 20, 15, 18]
print(list)             # [10, 20, 15, 18]
list.clear()            
print(list)             # [] 



#36
# reverse() method demo program (Home work)
a = [10, 20, 15, 18]
print(a)                # [10, 20, 15, 18]
a.reverse()            
print(a)                # [18, 15, 20, 10]



#37
# sort() method demo program (Home work)
list = [10, 20, 15, 18, 5]
print(list)             # [10, 20, 15, 18, 5]
list.sort()             
print(list)             # [5, 10, 15, 18, 20]
list.sort(reverse=True) 
print(list)             # [20, 18, 15, 10, 5]



#38
# Find outputs (Home work)
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
print(a)    # ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a.sort()    
print(a)    # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a.sort(reverse=True)
print(a)    # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']



#39
# Identify error (Home work)
a = [25, 10.8, 'Hyd', True]
a.sort()    # Error as to sort one needs to compare elements in the list but unfortunately the elements in the list are from various type classes which can't be compared



#40
# count() method demo program (Home work)
a = [10, 20, 15, 18, 15, 12, 14, 15, 19]
print(a.count(15))      # 3   
print(a.count(25))      # 0   
print(len(a))           # 9



#41
'''
Tricky program
Write a program to remove all duplicate elements of the list (Not even single occurance)
Let input be [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What is the output? ---> [15 , 14 , 18 , 19]

Element         count           Action
---------------------------------------------
  10              3             Ignore
  
  20              2             Ignore
  
  15              1             [15]
  
  14              1             [15 , 14]
  
  18              1             [15 , 14 , 18]
  
  19              1             [15 , 14 , 18 , 19]

'''
a = [int(x) for x in input("Enter List: ").strip("[]").split(",")]

result = []

for x in a:
    if a.count(x) == 1:
        result.append(x)

print(result)
    


#42
'''
Write a program to determine all the list elements are identical or not

1)  Let input be [25 , 25 , 25 , 25]
    What is the output? --->  All the elements are identical
    How many elements are in the list? ---> 4
    How many times is first element repeated? ---> 4

2)  Let input be [10 , 10 , 20 ,  10]
    What is the output? --->  All the elements are not identical
    How many elements are in the list? ---> 4
    How many times is first element repeated? ---> 3
'''
a = [int(x) for x in input("Enter any list: ").strip("[]").split(",")]

total = len(a)
first = a[0]
repeat = a.count(first)

if repeat == total:
    print("All the elements are identical")
else:
    print("All the elements are not identical")