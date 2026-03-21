'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
s = input("Enter a string: ")
vowels = set("aeiou")
result = set()
for ch in s.lower():  
    if ch in vowels:
        result.add(ch)
output = "".join(sorted(result)).upper()
print(output)


#  How  to  access  values  of  dictionary (Home  work)
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])   # prints 25
print(a['Ename'])   # prints 'Rama Rao'
print(a['Sal'])     # prints 1000.65


# How  to  modify  values  of  dictionary  (Home  work)
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)        #{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(id(a))    #address of a
a['Sal'] = 2000   
a['Ename'] = 'Sita'    
a['Empno'] = 35        
print(a)        #{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
print(id(a))    #same address


#  How  to  access  values  of  dictionary (Home  work)
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)    #{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a['Gender'] = 'M'      
a['Married'] = True    
print(a)    #{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}


# Find  outputs (Home  work)
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)        #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)      #{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
a.pop('Sal')
print(a)    #{'Empno': 25, 'Ename': 'Rama Rao'}

#  in  and  not  in  operators  (Home  work)
a = {10: 20, 30: 40, 50: 60, 70: 80}
print(30 in a.keys())        # True
print(60 in a.keys())        # False
print(60 in a.values())      # True
print(30 in a.values())      # False
print(50 in a)               # True
print(20 in a)               # False
print(70 not in a.keys())    # False
print(40 not in a.values())  # False
print(25 not in a)           # True


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter dictionary : ')    #{10: 'A', 20: 'B', 15: 'C', 20: 'D'}
print(a)        #{10: 'A', 20: 'B', 15: 'C', 20: 'D'}
print(type(a))  #<class 'str'>
b = eval(a)
print(b)        #{10: 'A', 20: 'D', 15: 'C'}
print(type(b))  #<class 'str'>

#  Find  outputs  (Home  work)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)    #{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a is b)   #False
print(a == b)   #True
c = a
print(a is c)   #True
print(a == c)   #True


#Find  outputs  (Home  work)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)        #{10, 20, 15, 18, 14, 25, 19}
print(type(d))  #<class 'set'>
e = {**a, **b, **c}
print(e)        #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))  #<class 'dict'>


#  Find  outputs  (Home  work)
a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
print(a + b)    #Error due to unsupport operand type(s)
c = {**a, **b}
print(c)        #{10: 60, 30: 50}
d = a | b
print(d)        #{10: 60, 30: 50}


'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input(f"Enter name of employee {i+1}: ")
    salary = float(input(f"Enter salary of {name}: "))
    a[name] = salary
print("\nEmployee Dictionary:")
print(a)


''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice

'''

#Program:

s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
items = s.split(',')
a = {}
for item in items:
    key, value = item.split('=', 1)  
    a[key.strip()] = value.strip()
print(a)    #{'Emp no': '25', 'Emp name': 'Rama Rao', 'sal': '10000.0', 'gender': 'm'}