'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
#Program 1:
a=set(input("Enter a string :"))
b='AEIOU'
c=''
for i in a:
    if i in b:
        c=c+i
print(str(c))





#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(How  to  print  value  25  in  dict  'a')
print(How  to  print  'Rama Rao'  in  dict  'a')
print(How  to  print  value  1000.65   in  dict  'a')	



# Program 2

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

print(a['Empno'])
print(a['Ename'])
print(a['Sal'])




# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
How  to  modify  1000.65  to  2000
How  to  modify  'Rama  Rao'  to  'Sita'
How  to  modify  25   to  35
print(a)

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

a['Empno']=35
a['Ename']='Sita'
a['Sal']=20000

print(a)  #{'Empno': 35, 'Ename': 'Sita', 'Sal': 20000}

print(id(a))  # Address of object a





#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)  # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

How  to  append  'Gender' : 'M'  to  dictionary  'a'  # a['Gender']= 'M'
a['Married']= True

How  to  append  'Married' :  True  to  dictionary  'a'  # a['Married']= True


print(a)





# Find  outputs (Home  work)
a = { }
How  to  append  10 : 'Rama'  to  dictionary  'a'
How  to  append  20 : 'Sita'  to  dictionary  'a'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'
How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)




#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
How  to  remove  'Sal' : 1000.65  from  dictionary  'a'  # del a['Sal']  


print(a)





#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())
print(60  in  a . keys())
print(60  in  a . values())
print(30  in  a . values())
print(50  in  a)
print(20  in  a)
print(70  not  in  a . keys())
print(40  not  in  a . values())
print(25  not  in  a)






#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))






#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)
print(a  is  b)
print(a  ==  b)
c = a
print(a  is   c)
print(a  ==  c)




#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)
print(type(d))
e = {**a , **b , **c}
print(e)
print(type(e))




#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b)
c = {**a , **b}
print(c)
d = a | b
print(d)





(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'

Program :
a={}
n=int(input('Enter num of employees :'))
for i in range(n):
    name=input('Enter employee name : ')
    salary=float(input("Enter Emp salary : "))
    a[name]=salary
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
'''


Progran :


a={}
n=input('Enter num of employees :')
b=n.split(',')
for i in b:
    key_value=i.split('=')
    key=key_value[0]
    value=key_value[1]

    a[key]=value
print(a)




