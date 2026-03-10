# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True
print(a  is   b) # False
print(a < c) # True
print(a > d) # True
print(a >= c) # False
print(a <= d) # False
print(a != c) # True
print(a != b) # False
print(a == c) # False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) # False
print(a  is   b) # False


#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) # 4
b = []
print(len(b)) # 0
c = [[10 , 20] , 30 , 40]
print(len(c)) # 3


# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) # (8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) # (39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) # 63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) # Error Because Hyd Cannot be added


#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a)) # Error 
print(sum(a[0])) # How  to  determine  sum  of  inner  list  elements
print(sum(a, []))) # How  to  determine  sum  of  inner  list  elements  in  another  way


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) # 30
print(min(a)) # 5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # Vamsi
print(min(b)) # Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) # Error Because Complex numbers cannot be compared.
d = [25 , '35']
print(max(d)) # Error Because Cannot compare int and string
print(max([])) # Error because empty string
print(min([])) # Error because empty string



# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) # [10,20,15,18]
print(type(b)) # <class 'list'>
print(a  is  b) # False
print(a == b) # False


#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b) # [4, 6, 8]
print(type(b)) # <class 'list'>
a = list('Vamsi')
print(a) # ['V','a','m','s','i']
a = list()
print(a) # []
print(list(25)) # Error
print(list(10.8)) # Error
print(list(True)) # Error
print(list(None)) # Error


# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) # [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) # [[10, 20], (30, 40), {50, 60}]


# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) # [5, 10, 12, 15, 20]
print(type(b)) # <class 'list'>
c = sorted(a , reverse = True)
print(c) # [20, 15, 12, 10, 5]
print(a) # [10, 20, 15, 5, 12]



# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a) 
print(b) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) # ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
[ # all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False
d = [10 , 0 , 20]
print(all(d)) # False
e = []
print(all(e)) # True

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) # True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False
e = []
print(any(e)) # False


# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
del    a[2]
print(a) # [10, 20, 18]
del  a[3]
del  a
print(a) # Error Because its out of range in index


#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10, 20, 15, 18]
list . append(19)
print(list) # [10, 20, 15, 18, 19]

#  Find  outputs (Home  work)
list = []
print(list) # []
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) # [25, 10.8, 'Hyd', True]


# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) # [0, 10, 20, 30, 40]


#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) # [10, 20, 30, 'Hyd']
print(len(a)) # 4
print(a[3]) # How  to  print  4th  element  of  list  'a' is Hyd
print(a[3][0]) # How  to  print  'H'
print(a[3][1]) # How  to  print  'y'
print(a[3][2]) # How  to  print  'd


#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) # [10, 20, [50, 60, 70], 30, 40]
print(len(a)) # 5
print(a[2]) # How  to  print  inner  list
print(a[2][0]) # How  to  print  50
print(a[2][1]) # How  to  print  60
print(a[2][2]) # How  to  print  70


# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list) # [10, 20, 18, 15, 12, 15, 19]
	list . remove(25)
except:
	print('25  is   not  in  the  list') # 25  is   not  in  the  list



'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
#Program:

a = [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]
x = 15

while x in a:
    a.remove(x)

print(a)

#Output:

[10, 20, 18, 19, 17, 20, 14]



#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) # 15
print(a) # [10, 20, 18, 12]
print(a . pop(len(a))) # 4
print(a . pop(-3)) # Error pop index out of range 
print(a) # Error
print(a . pop(-4)) # Error
print(a . pop())  #Error
print(a) # Error
b = []
b . pop() # Error


# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) # [10 , 20 , 15 , 18]
list . clear()
print(list) # []

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
a . reverse()
print(a) # [18, 15, 20, 10]

#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10, 20, 15, 18, 5]
list . sort()
print(list) # [5, 10, 15, 18, 20]
list . sort(reverse = True)
print(list) # [20, 18, 15, 10, 5]

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a) # ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a) # ['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']


# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() # Error Because Python cannot compare int, float, string, and boolean together during sorting


#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9

'''Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  --->  [15 , 14 , 18 , 19]

Element         count               Action
---------------------------------------------
  10                  3                       Ignore
  
  20                  2                       Ignore
  
  15                  1                       [15]
  
  14                  1                       [15 , 14]
  
  18                  1                       [15 , 14 , 18]
  
  19                  1                       [15 , 14 , 18 , 19]
'''
# Program:

a = eval(input("Enter list: "))

b = []

for x in a:
    if a.count(x) == 1:
        b.append(x)

print("Output list :", b)

#Program;
Enter list : [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
Output list : [15 , 14 , 18 , 19]


'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3
'''
# Program:

a = eval(input("Enter any list: "))
n = len(a)               
c = a.count(a[0])        
if n == c:
    print("All the elements are identical")
else:
    print("List elements are not identical")

#output:
Enter any list: [25,25,25,25]
All the elements are identical

Enter any list: [10,10,20,10]
List elements are not identical
