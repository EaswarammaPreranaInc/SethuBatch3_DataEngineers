1) sorted()  function 
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)#[5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)#['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)#[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)#[20, 18, 15, 10, 5]
print(a)#{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

2) Write  a  program  to  sort  dictionary  wrt  keys  

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
#Program
a = eval(input("Enter dictionaries: "))

b= dict(sorted(a.items()))

print(b)



3) clear()  method  demo  program 
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a){}
del  a
print(a)#Error because it is empty

4) copy()  method demo  program 
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)#{'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b)#False
print(a  ==  b)#True

5) keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#dict_keys([10, 20, 15, 18])
print(type(b))<class 'dict_keys'>
for  x  in   b:
        print(x)#10
                 20
                 15
                 18
'''
1) What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys

6) values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#dict_values([Hyd, Sec, Cyb, Pune])
print(type(b))<class 'dict_vales'>
for  x   in   b:
	print(x)#Hyd
                 Sec
                 Cyb
                 Pune



'''
1) What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values

7)  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))#<class 'dict_items'>
for  x   in   b:
        print(x)#(10, 'Hyd')
                 (20, 'Sec')
                 (15, 'Cyb')
                 (18, 'Pune')
for  x , y   in  b:
        print(x , y , sep = ' ... ')#10 ... Hyd
                                     20 ... Sec
                                     15 ... Cyb
                                     18 ... Pune


'''
1) What  does  items()  method  do  ---> Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  ---> (key , value)
'''
8) outputs 
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')#10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')#Error becasue it is not valid
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')#Error becasue it is not valid
for  x , y   in  a:
       print(x , y , sep = ' ... ')#Error becasue it is not valid

9) outputs  
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)#10
print(y)#20
print(z)#20
print()#Nothing
x , y , z = a . values()
print(x)#Rama
print(y)#Sita
print(z)#Rajesh
print()#Nothing
x , y ,  z = a . items()
print(x)#(10, 'Rama')
print(y)#(20, 'Sita')
print(z)#(15, 'Rajesh')
print()#Nothing
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#10 Rama
print(rno2 , sname2)#20 Sita
print(rno3 , sname3)#15 Rajesh

10) Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order
(ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

1) What  is  the  string  after  it  is  converted  to  uppercase ?  --->  'RAMA RAO'

2) What  is  the  result  of  sorted('RAMA RAO') ?  --->  [' ' , 'A' , 'A' , 'A' , 'M' , 'O' , 'R' , 'R']

3) What  is  dictionary  'a'  initially ?  --->  { }

4) What  is  the  first  element  in  list ?  ---> ' '
    What  action  to  be  made  for  ' ' ?  ---> Ignore  becoz  it  is  not  an  alphabet

5) What  is  the  2nd  element  in  list ?  ---> 'A'
    What  is  a['A']  ?  ---> a . get('A' , 0) + 1 =  0 + 1 = 1
    What  does  a['A']  =  1  do ?  ---> Appends  'A' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 1}

6) What  is  the  3rd  element  in  list ?  --->  'A'
    What  is  a['A']  ?  ---> a . get('A' , 0) + 1 = 1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2  in dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 2}

7) What  is  the  4th  element  in  list ?  --->  'A'
    What  is  a['A']  ?  --->  a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A'] = 3  do ?  ---> Modifies  value  of  'A'  to  3  in dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 3}

8) What  is  the  5th  element  in  list ?  --->  'M'
     What  is  a['M']  ?  ---> a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M'] = 1  do ?  ---> Appends  'M' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  --->  {'A' : 3 , 'M' : 1}

9) What  is  the  6th  element  in  list ?  ---> 'O'
     What  is  a['O']  ?  ---> a . get('O' , 0) + 1 = 0 + 1 = 1	 	 	
    What  does  a['O'] = 1  do ?  ---> Appends  'O' : 1  to  dict  'a'
    What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1}

10) What  is  the  7th  element  in  list ?  --->  'R'
     What  is  a['R']  ?  ---> a . get('R' , 0) + 1 =  0 + 1 = 1
     What  does  a['R'] = 1  do ?  --->  Appends  'R' : 1  to  dict  'a'
     What  is  dictionary  'a' ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 1}

11) What  is  the  8th  element  in  list ?  --->  'R'
      What  is  a['R']  ?  ---> a . get('R' , 0) + 1 = 1 + 1 = 2
      What  does  a['R'] = 2  do ?  ---> Modifies  value  of  'R'  to  2  in dict  'a'
      What  is  dictionary  'a' ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}

11) Finally  what   is  dict  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''
#Program
a = input("Enter a string: ")

a = a.upper()
b = sorted(a)

c = {}

for ch in b:
    if ch.isalpha():   
        c[ch] = c.get(ch, 0) + 1

print(c)

11) outputs 
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'G': 'Green', 'R': 'Red', 'B': 'Blue','Y': 'Yellow',}
a . update(b)

12) outputs 
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)#Error because it is not valid
c = [(10,) , (20,) , (30,)]
b . update(c)
print(b)#Error because it is not valid

13) outputs 
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))#<class 'dict'>

14) outputs  
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

15) outputs 
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#{15: 'Sita', 17: 'Kiran'}
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}