'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
s = input("Enter string: ")
vowels = "AEIOU"
a =""
s = s.upper()
s=set(s)
for ch in s:
    if ch in vowels:
        a+=ch
print(a)


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])#How  to  print  value  25  in  dict  'a'
print(a['Ename'])#How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])#How  to  print  value  1000.65   in  dict  'a'


# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['sal']=2000#How  to  modify  1000.65  to  2000
a['Ename']="Sita"#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']=35#How  to  modify  25   to  35
print(a)
print(id(a))

      
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender']='M'#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']=True#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)
      
# Find  outputs (Home  work)
a = { }
a[10]:"Rama"#How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]:"Sita"#How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]:"Rajesh"#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]:"Kiran"#How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)


#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal']#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)

      
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())#true
print(60  in  a . keys())#false
print(60  in  a . values())#true
print(30  in  a . values())#false
print(50  in  a)#true
print(20  in  a)#false
print(70  not  in  a . keys())#false
print(40  not  in  a . values())#false
print(25  not  in  a)#true


      
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10: 'A', 20: 'B', 15: 'C' }
print(type(b))#<class 'dict'>

      
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)#false
print(a  ==  b)#true
c = a
print(a  is   c)#true
print(a  ==  c)#true

      
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10, 14, 15, 18, 19, 20, 25}
print(type(d))#<class 'set'>
e = {**a , **b , **c}
print(e)#{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))#<class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)#error dict cannot added
c = {**a , **b}
print(c)#{10: 60, 30: 50}
d = a | b
print(d)#{10: 60, 30: 50}

      
'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
d={}
n=int(input("How many employees?"))
for i in range(n):
    a=input("enter employee name")
    b=int(input("enter salary:"))
    d[a]=b
print(d)


      
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
a=input("Enter input")
a=a.split(",")
d={}
for i in a:
    i=i.split("=")
    try:
        d[i[0]]=eval(i[1])
    except:
        d[i[0]]=i[1]
print(d)
    
