Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes


a=input("enter mixed case string:")
b='aeiou'.upper()
c=[]
count=0
for x in a:
    if x in a and x in b:
        c.append(x)
        count==1
d=set(c)
print('Distinct vowels:',''.join(d))


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a') #print(a['Empno'])
print(How  to  print  'Rama Rao'  in  dict  'a') #print(a['Ename'])
print(How  to  print  value  1000.65   in  dict  'a') #print(a['Sal'])

#How  to  modify  1000.65  to  2000 #a['Sal']=2000
#How  to  modify  'Rama  Rao'  to  'Sita's #a['Ename']='sita'
#How  to  modify  25   to  35 #a['Empno']=5
print(a) #{'Empno': 5, 'Ename': 'sita', 'Sal': 2000}
print(id(a)) #88550336


#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
How  to  append  'Gender' : 'M'  to  dictionary  'a' #a.update({'Gender' : 'M'})
How  to  append  'Married' :  True  to  dictionary  'a' #a.update({'Married' : 'True'})
print(a) #{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': 'True'}

# Find  outputs (Home  work)
a = { }
#How  to  append  10 : 'Rama'  to  dictionary  'a' #a.update({10:'Rama'})
#How  to  append  20 : 'Sita'  to  dictionary  'a' #a.update({20:'Sita'})
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'#a.update({15:'Rjesh'})
#How  to  append  18 : 'Kiran'  to  dictionary  'a' #a.update({18:'Kiran'})
print(a) #set{}

print(a) #{10: 'Rama', 20: 'Sita', 15: 'Rjesh', 18: 'Kiran'}


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
How  to  remove  'Sal' : 1000.65  from  dictionary  'a' #a.pop('Sal')

print(a) #{'Empno': 25, 'Ename': 'Rama  Rao'}

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys()) #False
print(60  in  a . values()) #True
print(30  in  a . values()) #True
print(50  in  a) #True
print(20  in  a) #False
print(70  not  in  a . keys()) #False
print(40  not  in  a . values()) #False
print(25  not  in  a) #True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) #<class 'str'>
b = eval(a)
print(b) #{10: 'A', 20: 'D', 15: 'C'}
print(type(b)) #<class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} 
print(b) ##{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b) #False
print(a  ==  b) #True
c = a
print(a  is   c)#True
print(a  ==  c) #True

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) #{10, 14, 15, 18, 19, 20, 25}
print(type(d)) #<class 'set'>
e = {**a , **b , **c}
print(e) #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) #<class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) #Error
c = {**a , **b}
print(c) #{10: 60, 30: 50}
d = a | b
print(d) #{10: 60, 30: 50}

(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'


n = int(input("Enter how many employees: "))
a = {}
for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    a[name] = salary
print(a)

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


s = input("Enter employee details: ")
n = s.split(',')
a = {}
for item in n:
    key_value = item.split('=')
    key = key_value[0].strip()
    value = key_value[1].strip()
    a[key] = value
print(a)





