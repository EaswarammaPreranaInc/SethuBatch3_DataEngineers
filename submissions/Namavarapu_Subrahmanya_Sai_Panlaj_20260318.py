'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
x = input('Enter a string : ')
y = 'AEIOU'
x = x.upper()
b = []
for i in x:
    if i in y and i in x:
       b.append(i)
b = set(b)
b = list(b)
b = ''.join(b)
print(b)



''' #  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a')
print(How  to  print  'Rama Rao'  in  dict  'a')
print(How  to  print  value  1000.65   in  dict  'a') '''
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # 1000
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a)) # 1000


#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)



# Find  outputs (Home  work)
a = { }
a[10] = 'Sita'
a[20] =  'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a) # {10: 'Sita', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
del a['Sal']
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(list(a.keys())[0])
print(list(a.keys())[2])
print(list(a.values())[2])
print(list(a.keys())[3])
print(60  in  a . keys())
print(60  in  a . values())
print(30  in  a . values())
print(50  in  a)
print(20  in  a)
print(70  not  in  a . keys())
print(40  not  in  a . values())
print(25  not  in  a)
output:
'''
10
50
60
70
False
True
False
True
False
False
False
True'''

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) # string dict
print(type(a)) # <class 'str'>
b = eval(a) # string dict to dict
print(b) # dict
print(type(b)) # <class 'dict'>



#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} # returns key and values of a dict
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
print(d) # Error
print(type(d)) # <class 'set'>
e = {**a , **b , **c} # {{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}, {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}, {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'} }
print(e) #  {{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}, {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}, {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'} }
print(type(e)) # <class 'set'>


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b) # Error
c = {**a , **b} # {10 : 20 , 30 : 40, 30 : 50 , 10 : 60}
print(c) # {10 : 20 , 30 : 40, 30 : 50 , 10 : 60}
d = a | b 
print(d) # {10 : 20 , 30 : 40, 30 : 50 , 10 : 60}

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
i = 0
a = int(input('enter a integer : '))
b = {}
while i < a:
    j = eval(input('Enter a key :'))
    k = eval(input('Enter a Value : '))
    b[j] = k
    i+=1
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
a = eval(input('Enter a key = values pair'))
a = a.split(',')
b = {}
c = []
for x in a:
    c = x.spillt('=')
    b[c[0]] = c[1]
    c = []
print(b)

