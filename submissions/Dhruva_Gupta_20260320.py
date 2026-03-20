Name-Dhruva Gupta
Roll Number-D238

1)
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) #3
b = {}
print(len(b)) #0


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
‘''

2)
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) #120
print(sum(a)) #90
print(sum(a . items())) #Error

3)
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #40
print(min(a . keys())) #7
print(max(a . values())) #50
print(min(a . values())) #5
print(max(a . items())) #40:5
print(min(a . items())) #7:28
print(max(a)) #40
print(min(a)) #7

4)
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a) 
print(b) #Dictionary printed
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c) #{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) #ValueError
f = [[10] , [20] , [30]]
print(dict(f)) #ValueError
print(dict([10 , 20])) #TypeError
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) #Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10, 20): 30, (40, 50): 60, (70, 80): 90}

5)
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) #Prints in ascending order of keys
c = sorted(a . values())
print(c) #Printed ASC Order based on values
d = sorted(a . items())
print(d) #ASC ORDER of keys
f  = sorted(a  , reverse = True)
print(f) #DESC ORDER of keys
print(a) #DICT PRINTED

6)
d = {10: 'A', 20: 'B', 15: 'C', 5: 'D', 12: 'E'}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


7)
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) #{10: 20, 30: 40, 50: 60}
a . clear() 
print(a) #{}
del  a
print(a) #Error

8)
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) #Dict printed
print(a  is  b) #False
print(a  ==  b) #True

9)
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #Prints list of keys
print(type(b)) #class dict_keys
for  x  in   b:
        print(x) # Prints Keys

10)
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) #Prints  values
print(type(b)) #class dict values
for  x   in   b:
	print(x) #Prints Values

11)
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) #Prints the dict in form of tuple enclosed in a list
print(type(b)) #class dict_items
for  x   in   b:
        print(x) #Prints keys in list
for  x , y   in  b:
        print(x , y , sep = ' ... ‘) #Error

12)
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ‘) #Prints dict in tuple enclosed in a list
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ‘) #Error
for  x , y   in  a . values():
       print(x , y , sep = ' ... ‘) #Error
for  x , y   in  a:
       print(x , y , sep = ' ... ‘) #Error

13)
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) #10
print(y) #20
print(z) #15
print()
x , y , z = a . values()
print(x) #Rama
print(y) #Sita
print(z) #Rajesh
print()
x , y ,  z = a . items()
print(x) #10:Rama
print(y) #20:Sita
print(z) #15:Rajesh
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) 10, Rama
print(rno2 , sname2) 20, Sita
print(rno3 , sname3) 15,Rajesh


14)
s = "RamA raO"
s1 = s.lower()
s2 = s1.replace(" ", "") 
d = {}
for i in s2:             
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
sorted_d = dict(sorted(d.items()))
print(sorted_d)


15)
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a) 
print(b) # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b) #Error

16)
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)  #Error
print(b) 
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)

17)
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) #{0:0,1:1,2:8,3:27,4:64}
print(type(d)) #class dict

18)
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d) { 0:0 , 1:2 : 2:4, 3:8, 4:16}

19)
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) #prints key value pairs where key is divisible by 2
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #Prints key value pair where value starts with R