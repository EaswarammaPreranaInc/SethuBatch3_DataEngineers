#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b)#True
b[2] = 12
print(a) #[10, 20, 12, 18]

#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10, 20, 15, 18, 100, 200, 150]
print(a + 5)#error
print(a + '5')#error
print([10 , 20] + (30 , 40))#error

# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1, 2, 3] 300000000000
a += b
print(a , id(a)) #[1, 2, 3, 4, 5, 6] 2000000

# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) # [1 , 2 , 3] 3000000
a  = a + b #
print(a , id(a)) #[1 , 2 , 3, 4 , 5 , 6] 40000000

# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) #a:25
print('b : ' , b) #b:[10.8, 'Hyd']
print('c : ' , c) #c:True
print(type(b))
x , *y = list
print('x : ' , x) #x:25
print('y : ' , y) #y:[10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) #[25, 10.8, 'Hyd']
print('q : ' , q) #True

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('c : ' , c) #'Hyd'
print('d : ' , d) #True
print('e : ' , e) #Error
a , b , *c , d , e , f = list

# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ :  ' , _) #'Hyd'
print('d : ' , d) #True

list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #a :  (3+4j)
print('b : ' , b) #b :  10.8
print('d : ' , d) #d :  True

# Find  outputs (Home  work)#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ : ' , _) #3+4j
print('d : ' , d) #True
print('_: ' , _) #3+4j

# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #a:[25 , 10.8]
print('b :  ' , b) #b:Hyd'
print('c :  ' , c) #c:True


# Find  outputs  (Home  work# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #25
print('b : ' , b) #10.0
print('c : ' , c) #Hyd
print('d : ' , d) #True
#a , b , c , d = list

# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b) #False
print(a < c) #True
print(a > d) #True
print(a >= c) #False
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False

 Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False

#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3

# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) # 36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #(8+10j) 
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) #error

# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) # vamsi
print(min(b)) #amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) #error
d = [25 , '35']
print(max(d)) #error
print(max([])) #error
print(min([])) #error

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) #[10, 20, 15, 18]
print(type(b)) #class list
print(a  is  b) #False
print(a == b) #False

#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) 
print(b) #[4,6,8]
print(type(b)) #class list
a = list('Vamsi') 
print(a) #['V', 'a', 'm', 's', 'i']
a = list()
print(a) #[]
print(list(25)) #error
print(list(10.8)) #error
print(list(True))#error
print(list(None)) #error

# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) #[5, 10, 12, 15, 20]
print(type(b)) #class list
c = sorted(a , reverse = True)
print(c) #[20, 15, 12, 10, 5]
print(a) #[20, 15, 12, 10, 5]

# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) #['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c) #['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
print(a) #['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']

# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) #False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) #False
d = [10 , 0 , 20]
print(all(d)) #False
e = []
print(all(e)) #True

# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #false
e = [] 
print(any(e)) # False

 del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10, 20, 15, 18]
del    a[2]
print(a) #[10, 20, 18]
del  a[3]
del  a
print(a) #error

  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10, 20, 15, 18]
list . append(19)
print(list) #[10, 20, 15, 18, 19]

#  Find  outputs (Home  work)
list = []
print(list) #[]
list . append(25) 
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) #[25, 10.8, 'Hyd', True]

# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0, 10, 20, 30, 40]

#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a) #[10, 20, 30, 'Hyd']
print(len(a)) #4
print(How  to  print  4th  element  of  list  'a' #print(a[3])
print(How  to  print  'H') #print(a[3][0])
print(How  to  print  'y') #print(a[3][1])
print(How  to  print  'd') #print(a[3][2])

#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)#[10, 20, [50, 60, 70], 30, 40]   
[10, 20, [50, 60, 70], 30, 40]
print(len(a)) #5
print(How  to  print  inner  list) #print(a[2])
print(How  to  print  50) #print(a[2][0])
print(How  to  print  60) #print(a[2][1])
print(How  to  print  70) ##print(a[2][2])

Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]

a = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = eval(input("enter the element to be deleted;"))

for i in a[:]: 
    if i == x:
        a.remove(i)
print("list without 15's:",a)  

#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) #15
print(a) #[10, 20, 18, 12]
print(a . pop(len(a))) #error
print(a . pop(-3))#15
print(a)#[10, 18, 12]
print(a . pop(-4))#20
print(a . pop())#empty
print(a)
b = []
b . pop()

print(a . pop())#error

list = [10 , 20 , 15 , 18]
print(list)#[10, 20, 15, 18]
list . clear()
print(list)#[]

# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
a . reverse()
print(a)#[18, 15, 20, 10

# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)#['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama  Rao']
a . sort()
print(a) #'Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
a . sort(reverse = True)
print(a)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']

# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() #error

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3
print(a . count(25)) #0
print(len(a)) #9

Tricky  program
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


a=[10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
b=[]
for i in a:
    if a.count(i)==1:
         b.append(i)
print(b)

Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3


a = eval(input("Enter the string:"))   

total = len(a)           
count = a.count(a[0])  

if total == count:
    print("All the elements are identical")
else:
    print("All the elements are not identical")


        


