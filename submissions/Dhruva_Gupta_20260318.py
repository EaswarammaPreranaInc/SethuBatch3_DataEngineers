Name-Dhruva Gupta
Roll Number-D238

'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
s="RamA Rao"
s.lower()
l=['a','e','i','o','u']
ans=""
for i in s:
    if i in l:
        if i not in ans:
            ans=ans+i
print(ans)

How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
#print(How  to  print  value  25  in  dict  'a') 
#print(How  to  print  'Rama Rao'  in  dict  'a')
#print(How  to  print  value  1000.65   in  dict  'a')
print(a['Empno'])   
print(a['Ename'])   
print(a['Sal'])     

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)

Find  outputs (Home  work)
a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
del a['Sal']   # removes 'Sal': 1000.65
print(a)

True
False
True
False
True
False
False
False
True

{10: 'A', 20: 'B', 15: 'C', 20: 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>

{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True

{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>

 Find  outputs  (Home  work)
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
{10: 60, 30: 50}
{10: 60, 30: 50}

a = {}  
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    a[name] = salary  
print("Employee Dictionary:", a)

s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
a = {}
parts = s.split(',')  
for item in parts:
    key_value = item.split('=')  
    key = key_value[0].strip()    
    value = key_value[1].strip()
    a[key] = value
print(a)
