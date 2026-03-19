

# Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

a = input("Enter a mixed case  string: ")
b=a.upper()
c=set(b)
d="AEIOU"
e=""
for x in c:
    if x in d:
        e+=x
print("Distinct vowels in string: ",e)



# Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

a =int(input("Enter a no-of employees: "))
d={}
for i in range(a):
    b=input("Enter Emp :  ")
    c=input("Enter salary : ")
    d[b]=c
print(d)



# Write  a  program  to  convert  a  string  to  dictionary

a =input("Enter a string thats what to insert in dict: ")
b=a.split(",")

c=[]
d={}
for x in b:
    c.append(x.split("="))

for y in c:
    d[(y[0])]=(y[1])
print(d)




#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a["Empno"])
print(a['Ename'])
print(a['Sal'])




# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # <class dict >
print(id(a)) # address of dict object
a['Sal']=2000  #How  to  modify  1000.65  to  2000
a['Ename']= "sita" # How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno']= 35 # How  to  modify  25   to  35
print(a) # <class dict>
print(id(a))# same address of object dict



#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender']= 'M' #  How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married' ]= True  #How  to  append  'Married' :  True  to  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}



# Find  outputs (Home  work)
a = { }
a[10]= 'Rama' #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20]= 'Sita' #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15]= 'Rajesh' #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18]= 'Krian' #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Krian'}



#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')# How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a) # {'Empno': 25, 'Ename': 'Rama  Rao'}



#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True
print(60  in  a . keys()) # False
print(60  in  a . values()) # True
print(30  in  a . values()) # False
print(50  in  a) # True
print(20  in  a) # False
print(70  not  in  a . keys())# false
print(40  not  in  a . values()) # False
print(25  not  in  a) # True



#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a =input('Enter  dictionary  :  ')
print(a) # {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # <class 'dict'>
# b = eval(a) # eval for stings not for dict
# print(b)
# print(type(b))



#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b) # False
print(a  ==  b) # True 
c = a
print(a  is   c) # true
print(a  ==  c) # True



#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d) # {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # <class set>
e = {**a , **b , **c}
print(e) # {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e)) # <class dict>



#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
# print(a + b) # unsupported operdent type "+"
c = {**a , **b}
print(c) # {30 : 50 , 10 : 60} bcz of no duplicates
d = a | b
print(d) # {30 : 50 , 10 : 60} bcz of no duplicates