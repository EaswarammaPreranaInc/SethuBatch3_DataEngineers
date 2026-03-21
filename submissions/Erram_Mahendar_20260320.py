# len() function demo program (Home work)
a = {'Empno' : 25, 'Ename' : 'Rama Rao' , 'Sal' : 1000.65 }
print(len(a)) # 3
b = {}
print(len(b)) #0




'''
What does len(dict) do ? ---> Returns number of key : value pairs in the dictionary
'''


# sum() function demo program (Home work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values())) #120
print(sum(a)) #90
print(sum(a . items())) #Error




# max() and min() functions demo program (Home work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #40
print(min(a . keys())) #7
print(max(a . values())) #50
print(min(a . values())) #5
print(max(a . items())) #(40,5)
print(min(a . items())) #(7,28)
print(max(a))#40
print(min(a)) #7


# dict() function demo program (Home work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a) #{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
print(b)
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d) #{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e)) #Error
f = [[10] , [20] , [30]]
print(dict(f)) #Error
print(dict([10 , 20]))
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10: [20, 30], 40: [50, 60], 70: [80, 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h)) #Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10, 20): 30, (40, 50): 60, (70, 80): 90}




'''
dict() function
------------------
1) What is the argument of dict() function ? --->
           Nested sequence such as list of tuples , list of lists , tup…




# sorted() function (Home work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) #[5, 10, 15, 18, 20]
c = sorted(a . values())
print(c) #['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f = sorted(a , reverse = True)
print(f) #[20, 18, 15, 10, 5]
print(a) #{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}




'''
Write a program to sort dictionary wrt keys (Home work)


1) Let input be {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What is the output ? ---> {5 : 'D' , 10 : 'A' , 12 : 'E' , 15 : 'C' , 20 : 'B'}


2) Both input and output are dictionaries


3) Hint: Use sorted() function
'''
a=eval(input("Enter the Dictionary: "))
b=sorted(a.items())
print(dict(b))




# clear() method demo program (Home work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a) # a = {10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a) #{}
del a
print(a) #ERror




# copy() method demo program (Home work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b) #{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a is b) #False
print(a == b) #True




# keys() method demo program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) #[10,20,15,18]
print(type(b)) #<class dict_keys>
for x in b:
        print(x)
'''
10
20
15
18
'''










'''
1) What does keys() method do ---> Returns dict_keys object which has list of all the dictionary keys
[11:59 am, 20/03/2026] +91 99482 50500: # values() method demo program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) #['Hyd', 'Sec', 'Cyd', 'Pune']
print(type(b)) #<class dict_values>
for x in b:
 print(x)
'''
Hyd
Sec
Cyd
Pune
'''






'''
1) What does values() method do ---> Returns dict_values object which has list of all the dictionary values




# items() method demo program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) #([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b)) #<dict_items>
for x in b:
        print(x) 
'''
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
'''
for x , y in b:
        print(x , y , sep = ' ... ')
'''
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''




'''
1) What does items() method do ---> Returns dict_items object which has list of tuples


2) What are the two elements of each tuple ? ---> (key , value)
'''




# Find outputs (Home work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for x , y in a . items():
'''
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''
       print(x , y , sep = ' ... ')
for x , y in a . keys():
       print(x , y , sep = ' ... ')#Error
for x , y in a . values():
       print(x , y , sep = ' ... ') #Error
for x , y in a:
       print(x , y , sep = ' ... ') #Error




# Find outputs (Home work)
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
x , y , z = a . items()
print(x) #(10,Rama)
print(y) #(20,Sita)
print(z) #(15,Rajesh)
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) #10 Rama
print(rno2 , sname2) #20 Sita
print(rno3 , sname3) #15 Rajesh




'''
(Home work)
Write a program to determine frequency of each alphabet in the string in alphabetical order
(ignoring the case)


Let input be RamA raO
What is the output ? ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2} in alphabetical order


1) What is the string after it is converted to uppercase ? ---> 'RAMA RAO'


2) What is the result of sorted('RAMA RAO') ? ---> [' ' , 'A' , 'A' , 'A' , 'M' , 'O' , 'R' , 'R']


3) What is dictionary 'a' initially ? ---> { }


4) What is the first element in list ? ---> ' '
    What action to be made for ' ' ? ---> Ignore becoz it is not an alphabet


5) What is the 2nd element in list ? ---> 'A'
    What is a['A'] ? ---> a . get('A' , 0) + 1 …


'''


a=input("Enter a mixed case String: ")
b=sorted(a.upper())
print(b)
c={}
for i in b:
    if i !=" ":
        c[i]=c.get(i,0)+1
print(c)




# Find outputs (Home work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b) #{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a . update(b)


# Find outputs (Home work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a) #Error
print(b) #Error
c = [(10,) , (20,) , (30,)]
b . update(c) #Error
print(b) #{}


# Find outputs (Home work)
d = {x : x ** 3 for x in range(5)}
print(d) #{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) #<class 'dict'>






# Find outputs (Home work)
d = { x : 2 * x for x in range(5) }
print(d)




# Find outputs (Home work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k : v for k , v in a .items() if k % 2 != 0}
print(b)
c = {k : a[k] for k in a if a[k] . startswith('R')}
print(c)