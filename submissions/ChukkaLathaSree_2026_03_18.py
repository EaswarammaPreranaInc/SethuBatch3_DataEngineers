'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
x = eval(input('enter any string:'))
def count_vowels_with_dict(x):
    vowels_counts={'a':0 , 'e':0 , 'i':0 , 'o':0 ,'u':0}
    x = x.lower
    for char in x:
        if char in vowels_counts:
            vowels_counts[char] +=1
    return vowel_counts


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a')---># (*a)
print(How  to  print  'Rama Rao'  in  dict  'a')---># a[1]
print(How  to  print  value  1000.65   in  dict  'a')--># a[2]

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)--> {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))--> adress of a
How  to  modify  1000.65  to  2000---> a['2000']
How  to  modify  'Rama  Rao'  to  'Sita'--->a['Sita']
How  to  modify  25   to  35--->a[35]
print(a)-->{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a))---> Adress of a with modified key values


#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)--->{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
How  to  append  'Gender' : 'M'  to  dictionary  'a'---> a.append('Gender':'M')
How  to  append  'Married' :  True  to  dictionary  'a'--->a.append('Married': True)
print(a)---> {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , {'Gender':'M} , 'Married': True }


# Find  outputs (Home  work)
a = { }
How  to  append  10 : 'Rama'  to  dictionary  'a'-->a[10]='Rama'
How  to  append  20 : 'Sita'  to  dictionary  'a'--->a[20]='Sita'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'--->a[15]='Rajesh'
How  to  append  18 : 'Kiran'  to  dictionary  'a'--->a[18]='Kiran'
print(a)-->{10:'Rama' , 20:'Sita' , 15:'Rajesh', 18:'Kiran'}

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a){'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)---> a['sal']

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())--> (*a[1])
print(60  in  a . keys())--> (*a[2])
print(60  in  a . values())--> (**a[2])
print(30  in  a . values())--> (**a[2])
print(50  in  a)--->a[2]
print(20  in  a)--->a[0]
print(70  not  in  a . keys())--->Error
print(40  not  in  a . values())--->Error
print(25  not  in  a)--->Error

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)---> {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))---> <class 'dict'>
b = eval(a)---> {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(b)---> {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b))---> <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)--->  {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)---> False
print(a  ==  b)---> True
c = a
print(a  is   c)---> False
print(a  ==  c)---> True


#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)---> [10,20,15, 18,14,20,25,19,15,14]
print(type(d))---> <class 'list'>
e = {**a , **b , **c}---> {{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'},{18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'},{25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}}
print(e)--->{{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'},{18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'},{25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}}
print(type(e))---> <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b)--->{10 : 20 ,30 : 50 , 10 : 60 }
c = {**a , **b}
print(c)---> {a,b}
d = a | b
print(d)---> {10 : 20 ,30 : 50 , 10 : 60}

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
dict= input()

x = input('enter the emp details:')
dict = {}
for emp in x:
    if sal in emp:
        dict.append(emp)
        
        

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


