# Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
s=input("Enter mixed case string : ")
s=s.upper()
s=set(s)
v="AEIOU"
vs=''
for x in s:
    if x in v:
        vs+=''.join(x)
print("Distinct vowels are : " ,vs)

#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # id of dict a
a['Sal']=2000
a['Ename']='Sita'
a['Empno']=35
print(a) # {'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a)) # Same address

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['Gender']='M'
a['Married']=True
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
print(a) # '{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # <class str>
b = eval(a) 
print(b) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) # <class dict>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False , bcz dict is mutable but not reusable
print(a  ==  b) # True, bcz elements of both are same
c = a
print(a  is   c) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  ==  c) # True

#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} # unpacks the dict and return keys
print(d) # {10,20,15,18,14,25,19} in any order
print(type(d)) # <class set>
e = {**a , **b , **c}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class dict>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # Error
c = {**a , **b}
print(c) # {10 : 60 , 30 : 50}
d = a | b
print(d) # {10 : 60 , 30 : 50}

# Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries
d={}
n=int(input("Enter how many dicts : "))
for i in range(n):
    empname=input("Enter Emp name : ")
    sal=int(input("Enter sal : "))
    d[empname]=sal
print(d)

# Write  a  program  to  convert  a  string  to  dictionary
s=input("Enter dict : ")
p=s.split(',')
d={}
for x in p:
        k,v= x.split('=')
        d[k]=v
print(d)








