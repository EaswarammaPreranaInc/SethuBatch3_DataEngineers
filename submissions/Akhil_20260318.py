Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a = input('Enter mixed case string : ')
a = set(a)
b = 'AIEOU'
c = ''
for ch in a:
    if ch in b :
        c += ch 
print('Distinct vowels : ', c)
#  How  to  access  values  of  dictionary (Home  work)

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print( a['Sal'])


# How  to  modify  values  of  dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # Address of the object 'a' 
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] =  35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000 }
print(id(a)) # Same adress of object a


#  How  to  append  key : value  pairs  to dictionary  (Home  work)

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender'] = 'M' 
a['Married'] =  True
print(a) #  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65, 'Gender' : 'M', 'Married' : True }


# Find  outputs (Home  work)

a = { }
a[10] = 'Rama'  
a [20] = 'Sita' 
a [15] = 'Rajesh'  
a [18 ] = 'Kiran' 
print(a) # {10 : 'Rama', 20 : 'Sita', 15 : 'Rajesh', 18 : 'Kiran'}


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)

a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal')
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)

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

a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'str'>
b = eval(a)
print(b) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) # <class 'dict'>


#  Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is   c) # True 
print(a  ==  c) # True


#Find  outputs  (Home  work)

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 20, 15 , 18, 14, 20, 25, 19, 15, 14}
print(type(d)) # <class 'set'>
e = {**a , **b , **c}
print(e) # {10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha',18 : 'Kiran' , 14 : 'srinivas' , 25 : 'Ramesh' , 19 : 'Krishna}
print(type(e)) # <class 'dict'>


#  Find  outputs  (Home  work)

a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # Error
c = {**a , **b} 
print(c) # {10 : 60 , 30 : 50 }
d = a | b
print(d) # {10 : 60 , 30 : 50 }
'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

a = int(input('How many employess ? : '))
b = {}

for i in range(a) :
    c = input('Enter employee name : ')
    d = float(input('Enter salary : '))
    b[c] = d 
print(b)


''' (Home  work)
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

a = input('Input : ')
b = a.split(',')
c = {}

for i in b :
    i = i.split('=')
    c[i[0]] = i[1]
print(c)

print(b)