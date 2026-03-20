#1. len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0
#----------------------------------------------------------------------------------------------------
# 2. sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
print(sum(a . items())) # Error, bcz int and tuple are not concatenated
#----------------------------------------------------------------------------------------------------

# 3.max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) #(40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7
#----------------------------------------------------------------------------------------------------

#4. dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a) 
print(b) #{10 : 'Hyd', 20 : 'Sec', 15 :'Cyb',20 : 'Pune')
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {[}'R' : 'Red','G' : 'Gray','B' : 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) # error
f = [[10] , [20] , [30]]
print(dict(f)) # Error
print(dict([10 , 20])) # error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10 : [20 , 30],40 : [50 , 60], 70 :[80 , 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) #error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))# Error
#----------------------------------------------------------------------------------------------------

#5. sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys()) 
print(b) # [5,10,15,18,20]
c = sorted(a . values())
print(c) # ['Blue','Green','Red','White','Yellow']
d = sorted(a . items())
print(d) # [5 : 'White',10 : 'Red',15 : 'Blue' , 18 : 'Yellow' ,20 : 'Green']
f  = sorted(a  , reverse = True)
print(f) # [20 : 'Green',18 : 'Yellow',15 : 'Blue',10 : 'Red' ,5 : 'White']
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
#----------------------------------------------------------------------------------------------------

#6. Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)
dic=eval(input("Enter dictionary : "))
rev=sorted(dic.items())
print(rev)
sor={}
for y in rev:
        sor[y[0]]=y[1]
print(sor)
#----------------------------------------------------------------------------------------------------
#7.clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)  #{10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # {}
del  a
print(a) #Error
#----------------------------------------------------------------------------------------------------

#8.copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True
#----------------------------------------------------------------------------------------------------

#9.  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # [10,20,15,18]
print(type(b)) # <class 'list'>
for  x  in   b:
        print(x) # 10<nl>20<nl>15<nl>18
#----------------------------------------------------------------------------------------------------

#10.values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # ['Hyd','Sec','Cyb','Pune']
print(type(b)) # <class 'list'>
for  x   in   b:
	print(x) # Hyd<nl>Sec<nl>Cyb<nl>Pune
#----------------------------------------------------------------------------------------------------
        
# 11. items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # [(10 , 'Hyd') , (20 , 'Sec' ), (15 , 'Cyb' ), (18 , 'Pune')]
print(type(b)) # <class 'list'>
for  x   in   b:
        print(x) # (10,'Hyd') (20 , 'Sec') (15 , 'Cyb' )  (18 , 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10...Hyd  20...Sec  15...Cyb  18...Pune
#----------------------------------------------------------------------------------------------------

#12.Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ') # 10...Hyd  20...Sec  15...Cyb  18...Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ') # Error
for  x , y   in  a . values():
       print(x , y , sep = ' ... ') #error
for  x , y   in  a:
       print(x , y , sep = ' ... ') #Error
#----------------------------------------------------------------------------------------------------

#13.  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) #15
print()
x , y , z = a . values()
print(x) # 'Rama'
print(y) # 'Sita'
print(z) # 'Rajesh'
print()
x , y ,  z = a . items()
print(x) #(10,'Rama')
print(y) #(20,'Sita)'
print(z) #(15,'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 'Rama'
print(rno2 , sname2) # 20 'Sta'
print(rno3 , sname3) # 15 'Rajesh'
#----------------------------------------------------------------------------------------------------

#14. Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
#(ignoring  the  case)

inp=input("Enter string : ")
inp=inp.upper()
sor_inp=sorted(inp)
dic={}
for x in sor_inp:
    if x.isalpha():
        dic[x]=dic.get(x,0)+1
print(dic)
#----------------------------------------------------------------------------------------------------

#15.Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) # {'Y' : 'Yellow', 'G' : 'Green', 'R':'Red', 'B':'Blue'}
#a . update(b) #error,bcz list a dont have  update()
#----------------------------------------------------------------------------------------------------

#16.  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) # Error ,bcz nested seq , inner seq elements should be 2 only
print(b) # {}
c = [(10,) , (20,) , (30,)]
b . update(c) 
print(b) # # Error ,bcz nested seq , inner seq elements should be 2 only

#----------------------------------------------------------------------------------------------------

#17.  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0:0,1:1,2:8,3:27,4:64}
print(type(d)) # <class 'dict'>

#----------------------------------------------------------------------------------------------------

# 18.Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) # {0:1,1:2,2:4,3:8,4:16}

#----------------------------------------------------------------------------------------------------

#19. Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15:'Sita',17:'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}