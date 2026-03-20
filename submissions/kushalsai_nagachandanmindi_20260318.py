s = input("enter the string: ")
vowl = set()
vowels=set("aeiou")
for ch in s.lower():
    if ch in vowels:
        vowl.add(ch)
result = ''.join(sorted(vowl)).upper()
print(result)

a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])


a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a)) # 2325689004096
a['Sal']=2000
a['Ename']='Sita'
a['Empno']=35
print(a) # {'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a)) # same address

a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65}
print(id(a)) # 2330755919936
a.update(gender='M') 
a.update(Married=True)
print(a) #{'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'gender': 'M', 'Married': True}
print(id(a)) # same address

a={}
a[10]='Rama'
a[20]='Sita'
a[30]='Rajesh'
a[40]='Kiran'
print(a) # {10: 'Rama', 20: 'Sita', 30: 'Rajesh', 40: 'Kiran'}

a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')
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

a = input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # class<Str>
b = eval(a) 
print(b) # {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # class<dict>

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True
c = a
print(a  is   c) # True
print(a  ==  c) # True

a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) #  {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class 'set'>
e = {**a , **b , **c} 
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # Error
c = {**a , **b}
print(c) # { 10 : 60, 30 : 50 }
d = a | b
print(d) # {10 : 60 ,30 : 50}


a ={}
n = int(input("how many employees: "))
for i in range(n):
    name = input(F'Enter the name of employee{i+1}: ')
    salary=float(input(F'Enter the salary of employee{name}: '))
    a[name]=salary
print("Employee dictionary: ")
print(a)

s = input("Enter the String: ")
items=s.split(',')
a={}
for item in items:
    key, value = item.split('=',1)
    a[key]=value
    
print(a)

