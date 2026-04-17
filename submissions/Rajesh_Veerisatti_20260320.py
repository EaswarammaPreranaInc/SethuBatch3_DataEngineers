


# Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

a={10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}

b=sorted(a)
c={}
for i in b:
    c[i]=a[i]

print(c)



# Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

a="RamA raO"
b=a.upper()
c=sorted(b)
print(c)
d={}

for x in c:
    if x!=" ":

        d[x]=d.get(x,0)+1
print(d)






# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a)) # 3
b = {}
print(len(b)) # 0



#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys())) # 90
print(sum(a . values())) # 120
print(sum(a)) # 90
# print(sum(a . items())) # error tuples can not be sum by + operdend type



# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) # 40
print(min(a . keys())) # 7
print(max(a . values())) # 50
print(min(a . values())) # 5
print(max(a . items())) #(40,5)
print(min(a . items())) # (7,28)
print(max(a)) # 40
print(min(a)) # 7



#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b) # {10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) # {'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
# print(dict(e)) # error inner  sqe should contain only 2 elements
f = [[10] , [20] , [30]]
# print(dict(f)) # error inner  sqe should contain only 2 elements
# print(dict([10 , 20]))
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
# print(dict(h)) # error keys should have only immutable objects
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10, 20): 30, (40, 50): 60, (70, 80): 90}




# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) # [5,10,15,18,20]
c = sorted(a . values())
print(c) # ['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f) #  [20, 18, 15, 10, 5]
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}



# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) #  {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) # {}
del  a
# print(a) # error refference also deleted



# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) #  {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False
print(a  ==  b) # True



#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #dict_keys( [10,20,15,18])
print(type(b)) # ,class dict_keys>
for  x  in   b:
        print(x) # 10 \n 20\n 15\n 18




# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b)) # <class dict_values>
for  x   in   b:
	print(x) # hyd \n sec \n cyb \n pune





#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) # dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) # <class dict_items>
for  x   in   b:
        print(x) # (10,hyd) \n (20,sec) \n (15,cyb) \n (18,pune)
for  x , y   in  b:
        print(x , y , sep = ' ... ') # 10...hyd \n 20...sec \n 15...cyb \n 18...pune



# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')  # 10...hyd \n 20...sec \n 15...cyb \n 18...pune
 # for  x , y   in  a . keys():
        # print(x , y , sep = ' ... ')
 # for  x , y   in  a . values():
        # print(x , y , sep = ' ... ')
 # for  x , y   in  a:
       #  print(x , y , sep = ' ... ')




#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x) # 10
print(y) # 20
print(z) # 15 
print() # \n
x , y , z = a . values()
print(x) # Rama
print(y) # sita
print(z) # rajesh
print() # \n
x , y ,  z = a . items()
print(x) # (10, 'Rama')
print(y) # (20, 'Sita')
print(z) # (15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) # 10 Rama
print(rno2 , sname2) #  20 Sita
print(rno3 , sname3) #  15 Rajesh



# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
# a . update(b) # error list does not have update attribute



#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
# b.update(a) # error inner sqe should contain only 2 elements
print(b) # {}
c = [(10,) , (20,) , (30,)]
#b . update(c) # error inner sqe should contain only 2 elements

print(b) #   {}


#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d) # {0:0,1:1,2:8,3:27,4:64}
print(type(d)) # <class dict>



# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)# {0:0,1:2,2:4,3:6,4:8}



# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b) # {15 : 'Sita',17 : 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c) #  {10 : 'Rama' , 18 : 'Rajesh' , 12 : 'Rama Rao'}

