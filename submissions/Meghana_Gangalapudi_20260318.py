
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''

CODE:

a = input('Enter  string  :  ')
a = a . upper()
vowels = 'AEIOU'
distinct_vowels = set()
for char in a:              
    if char in vowels:
        distinct_vowels . add(char) 
output = ''.join(distinct_vowels)
print(output)
'''

Output: AO

'''


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])  # How  to  print  value  25  in  dict  'a'
print(a['Ename'])  # How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])    # How  to  print  value  1000.65   in  dict  'a'


# How  to  modify  values  of  dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))

#  How  to  append  key : value  pairs  to dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)

# Find  outputs (Home  work)

a = { }
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)

a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal']
print(a)

#  in  and  not  in  operators  (Home  work)

CODE:

a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys()) # False
print(40  not  in  a . values()) # False
print(25  not  in  a) # True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}

CODE:

a = input('Enter  dictionary  :  ') # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(a) # {10: 'A', 20: 'D', 15: 'C'}
print(type(a)) # <class 'str'>
b = eval(a) # {10: 'A', 20: 'D', 15: 'C'}
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # <class 'dict'>

#  Find  outputs  (Home  work)

CODE:

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'} 
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is   c) # True
print(a  ==  c) # True

#Find  outputs  (Home  work)

CODE:

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 20, 15, 18, 14, 25, 19}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'}
print(type(e)) # <class 'dict'>

#  Find  outputs  (Home  work)

CODE:

a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
c = {**a , **b}
print(c) # {10 : 60 , 30 : 50}
d = a | b
print(d) # {10 : 60 , 30 : 50}

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

CODE:

a = {}
n = int(input('Enter  number  of  employees  :  '))
for i in range(n):
    name = input('Enter  employee  name  :  ')
    salary = float(input('Enter  employee  salary  :  '))
    a[name] = salary
print(a)

'''
Output: {'John': 5000.0, 'Alice': 6000.0}'''

'''
(Home  work)

Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice

input  --->  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

input . split(',') --->  ['Emp no = 25'  , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']

a = {} 

Iteration  1    --->  ['Emp no' ,  '25']   --->  a['Empno'] = '25'

Iteration  2    --->  ['Emp name' , 'Rama  Rao']   --->  a['Emp  name'] = 'Rama   Rao'

Iteration  3    --->  ['sal' , '10000.0']   --->  a['sal'] =  '10000.0'

Iteration  4    --->  ['gender' , 'm']   --->  a['gender'] =  'm'

'''

CODE:

a = input('Enter  string  :  ') 
a = a . split(',')
b = {}
for item in a:
    key_value = item . split('=')
    key = key_value[0] . strip()
    value = key_value[1] . strip()
    b[key] = value
print(b)

'''
Output: {'Emp no': '25', 'Emp name': 'Rama Rao', 'sal': '10000.0', 'gender': 'm'}'''