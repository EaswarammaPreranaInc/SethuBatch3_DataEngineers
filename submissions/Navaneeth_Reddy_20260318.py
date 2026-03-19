'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''

a=input('Enter mixed case string : ')

a = a.upper()

b=set(a)

c=""

for x in b:
    if x in "AEIOU":
        c = c + x
print(c)

'''
Output :
Enter the String : Aupicious
IOUA
'''

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender']= 'M'#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']= True #How  to  append  'Married' :  True  to  dictionary  'a'
print(a)

# Find  outputs (Home  work)
a = { }
a[10]=['Rama'] #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]=['Sita'] #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]=['Rajesh'] #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]=['Kiran'] #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)

 #  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
del a['Sal'] #How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)

#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) #False
print(60  in  a . values()) #True
print(30  in  a . values()) #False
print(50  in  a) #True
print(20  in  a) #False
print(70  not  in  a . keys()) #False
print(40  not  in  a . values()) #False
print(25  not  in  a) # True

#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a) #'{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'
print(type(a)) # <class 'str'>
b = eval(a)
print(b) #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} 
print(b) #{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
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
print(d)  # {10,20,15,18,14,20,25,19,15,14}
print(type(d)) ## <class 'set'>
e = {**a , **b , **c}
print(e) # {10 : 'Rama' ,18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar',25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
print(type(e)) # # <class 'dict'>

#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) # error
c = {**a , **b} # {30 : 50 , 10 : 60}
print(c) # {30 : 50 , 10 : 60}
d = a | b # {30 : 50 , 10 : 60}
print(d) # {30 : 50 , 10 : 60}

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''

a = int(input("How many Employees ? : "))

s = {}

while a != 0 :
    
    b = input("Enter the Emp Name : ")
    
    c = float(input("Enter the Salary : "))
    
    s[b] = c
    
    a = a-1

print(s)

'''
Output :
How many Employees ? : 4
Enter the Emp Name : Rama Rao
Enter the Salary : 10000
Enter the Emp Name : Sita
Enter the Salary : 200000
Enter the Emp Name : Rajesh
Enter the Salary : 150000
Enter the Emp Name : Kiran
Enter the Salary : 175000
{'Rama Rao': 10000.0, 'Sita': 200000.0, 'Rajesh': 150000.0, 'Kiran': 175000.0}
'''

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

inp = input("Enter the string : ")

b = inp.split(',')

#print(b)

a = {}

for x in b :
    c=x.split('=')
    a[c[0]]=c[1]
print(a)

'''
Output :
Enter the string : "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
{'"Emp no ': ' 25 ', ' Emp name ': ' Rama  Rao ', ' sal ': ' 10000.0 ', ' gender ': ' m"'}
'''
