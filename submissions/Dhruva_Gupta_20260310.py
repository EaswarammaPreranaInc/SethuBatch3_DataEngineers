Name-Dhruva Gupta
Roll Number-D238

1)
#  Find  outputs (Home  work)
a = [10, 20, 15, 18] 
b = a
print(a  is  b) #False
print(a  ==  b) #True
b[2] = 12
print(a) #[10,20,12,28]

2)
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[110,220,165,18]
print(a + 5) #Cannot add non sequence to sequence 
print(a + ‘5') #[10,20,15,18,’5’]
print([10 , 20] + (30 , 40)) #Invalid as tuple immutable

3)
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1,2,3],Address of object
a += b #[1,2,3,4,5,6]
print(a , id(a)) #[1,2,3,4,5,6],Address of Object which is different

4)
# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1,2,3],address of object
a  = a + b
print(a , id(a)) #[1,2,3,4,5,6],Address of object

5)
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) #25
print('b : ' , b) #[10.8,’Hyd’]
print('c : ' , c) #True
print(type(b)) #class list
x , *y = list
print('x : ' , x) #25
print('y : ' , y) #[10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p) #[25 , 10.8 , ‘Hyd]
print('q : ' , q) #True

6)
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list
a , b , *c , d , e = list
print('a : ' , a) #Error
print('b : ' , b) #b:10.8
print('c : ' , c) #c:’Hyd’
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list

7)
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a: 25
print('b : ' , b) #b: 10.8
print('_ :  ' , _) #_:’Hyd’
print('d : ' , d) #d: True

8)
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #3+4j
print('b : ' , b) #10.8
print('d : ' , d) #True

9)
#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ : ' , _) #Hyd
print('d : ' , d) #True
print('_: ' , _) #3+4j

10)
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #2 unpacking not allowed

11)
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #[25,10.8]
print('b :  ' , b) #Hyd
print('c :  ' , c) #True

12)
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)  #[25]
print('b : ' , b) #[10.8]
print('c : ' , c) #Hyd
print('d : ' , d) #True
a , b , c , d = list

13)
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b) #False
print(a < c) #True
print(a > d) #True
print(a >= c) #True
print(a <= d) #False
print(a != c) #True
print(a != b) #False
print(a == c) #False

14)
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False

15)
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40]
print(len(c)) #3

16)
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #Error
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e)) #Error

17)
a = [[10,20,15,18]]
total = 0
for i in range(len(a[0])):
    total = total + a[0][i]
print(total)

a = [[10,20,15,18]]
total = 0
for row in a:
    for num in row:
        total += num
print(total)


18)
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c)) #Error
d = [25 , '35']
print(max(d)) #Error
print(max([])) #Error
print(min([])) #Error

19)
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b) #[10,20,15,18]
print(type(b)) #class list
print(a  is  b) #False
print(a == b) #True

20)
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) 
print(b) #[4,6,8]
print(type(b)) #class list
a = list(‘Vamsi') 
print(a) #[‘V’,’a’,’m’,’s’,’i’]
a = list()
print(a) #[]
print(list(25)) #Error
print(list(10.8)) #Error
print(list(True)) #Error
print(list(None)) #Error

21)
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10,20), (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #c = [[10 , 20] , (30 , 40) , {50 , 60}]

22)
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) #[5,10,13,15,20]
print(type(b)) #class list
c = sorted(a , reverse = True)
print(c) #[20,15,12,10,5]
print(a) # [10 , 20 , 15 , 5 , 12]

23)
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b) #Sorted in ascending based on string, first non matching character
c = sorted(a , reverse = True)
print(c) #Sorted in descending based on string, first non matching character
print(a) #['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao’]

24)
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
print(all(e)) #False

25)
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c)) #False
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) #False
e = []
print(any(e)) #False

26)
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
del    a[2]
print(a) #[10,20,18]
del  a[3]
del  a
print(a) #[10,20]

27)
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list) [10,20,15,18]
list . append(19)
print(list) #[10,20,15,18,19]

28)
#  Find  outputs (Home  work)
list = []
print(list)
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list) [25,10.8,’Hyd’,True]

29)
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)

#Output
[0,50,10]

30)
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append(‘Hyd')
print(a) #[10,20,30,[‘Hyd’]]
print(len(a)) #4
print(How  to  print  4th  element  of  list  ‘a') #a[3]
print(How  to  print  ‘H') #a[3][0]
print(How  to  print  ‘y') #a[3][1]
print(How  to  print  ‘d') #a[3][2]

31)
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a) #[10, [50 , 60 , 70],20,30,40]
print(len(a)) #5
print(How  to  print  inner  list)  #a[2])
print(How  to  print  50) #a[2][0]
print(How  to  print  60) #a[2][1]
print(How  to  print  70) #a[2][2]

32)
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15) 
	print(list) #[10,20,18,15,12,15,19]
	list . remove(25)
except:
	print('25  is   not  in  the  list’)

33)
a=eval(input("Enter the list: "))
b=int(input("Enter the element you want to get removed: "))
try:
    for i in a:
        a.remove(b)
    print(a)
except Exception:
    print(a)


34)
#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2)) #15
print(a) #[10,20,18,12]
print(a . pop(len(a))) #12
print(a . pop(-3)) #10
print(a) #[20 , 18]
print(a . pop(-4)) #Index Error
print(a . pop()) #18
print(a) #[20]
b = []
b . pop() #Error

35)
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list) #[10 , 20 , 15 , 18]
list . clear()
print(list) #[]

36)
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
a . reverse() 
print(a) #[18,15,20,10]

37)
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list) #[10 , 20 , 15 , 18 , 5]
list . sort() 
print(list) #[5,10,15,18,20]
list . sort(reverse = True)
print(list) #[20,18,15,10,8]

38)
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a) #['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort() 
print(a) #Sort in ascending order based on the non matching characters
a . sort(reverse = True)
print(a) #Sort in descending order based on the non matching characters

39)
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort() #Invalid datatypes comparison

40)
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) #3 
print(a . count(25)) #0
print(len(a)) #9

41)
a=eval(input("Enter the list: "))
cnt=0
ans=[]
for i in a:
    cnt=a.count(i)
    if(cnt==1):
        ans.append(i)
    else:
        continue
print(ans)
