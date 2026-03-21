# #1 .  Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

# # 1) Let  input  be  RamA  Rao
# #     What  is  the  output  ?  ---> AO  (case  is  ignored)

# # 2) Both  input  and  output  are  strings

# # 3) Hint:  Same  as  prog19  with  minor  changes

# output : 
a = input('Enter any mixed string: ')
a = a.upper()
b=' '
vowel = 'AEIOU'
for ch in a:
    if ch in vowel and ch not in b:
        b+=ch
print('Distinct vowels: ',b)        


# #------------------------------------------------------------------------------------------------ 
# # 2. #  How  to  access  values  of  dictionary (Home  work)
# # a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# # print(How  to  print  value  25  in  dict  'a')
# # print(How  to  print  'Rama Rao'  in  dict  'a')
# # print(How  to  print  value  1000.65   in  dict  'a')       

# output :
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

# #-------------------------------------------------------------------------------------------------

# # 3 . # How  to  modify  values  of  dictionary  (Home  work)
# # a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# # print(a)
# # print(id(a))
# # How  to  modify  1000.65  to  2000
# # How  to  modify  'Rama  Rao'  to  'Sita'
# # How  to  modify  25   to  35
# # print(a)
# # print(id(a))

# output :
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))

# #-----------------------------------------------------------------------------------------
# # 4 . #  How  to  append  key : value  pairs  to dictionary  (Home  work)
# # a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# # print(a)
# # How  to  append  'Gender' : 'M'  to  dictionary  'a'
# # How  to  append  'Married' :  True  to  dictionary  'a'
# # print(a)

# # output :
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)

# #---------------------------------------------------------------------------------------------

# #5. Find  outputs (Home  work)
# # a = { }
# # How  to  append  10 : 'Rama'  to  dictionary  'a'
# # How  to  append  20 : 'Sita'  to  dictionary  'a'
# # How  to  append  15 : 'Rajesh'  to  dictionary  'a'
# # How  to  append  18 : 'Kiran'  to  dictionary  'a'
# # print(a)

# # output : 
a = { }
a[10]='Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)

# # ----------------------------------------------------------------------------------------------

# # # 6. How  to  remove  key : value  pairs  of  dictionary  (Home  work)
# a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# print(a)
# How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
# print(a)

# output : 
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal')
print(a)

# # ------------------------------------------------------------------------------------------------
# # 7. in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # output : True
print(60  in  a . keys()) # output : False
print(60  in  a . values()) # output : True
print(30  in  a . values()) # output : False
print(50  in  a) # output : True
print(20  in  a) # output : False
print(70  not  in  a . keys()) # output : False
print(40  not  in  a . values()) # output : False
print(25  not  in  a) # output : True
 
# #-----------------------------------------------------------------------------------------
# # 8 . #  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
# # a = input('Enter  dictionary  :  ')
# # print(a)
# # print(type(a))
# # b = eval(a)
# # print(b)
# # print(type(b))

# output : 
a = input('Enter dictionary : ')
print(a) # output : {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) # output : <class 'str'>
b = eval(a)  # to convert 'str' to 'dict' and remove the duplicate keys
print(b) # output : {10: 'A', 20: 'D', 15: 'C'}
print(type(b)) # output : <class 'dict'>

# #--------------------------------------------------------------------------------------------

# 9 . #  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b) # output : 10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'
print(a  is  b) # output : False
print(a  ==  b) # output : True
c = a # output : {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is   c) # output : True
print(a  ==  c) # output : True

# # --------------------------------------------------------------------------------------------

# 10 .#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} 
print(d) # output : {10, 14, 15, 18, 19, 20, 25}
print(type(d)) # output : <class 'set'>
e = {**a , **b , **c}
print(e) # output : {10 : 'Rama' , 14 : 'Amar', 15 : 'Rajesh', 18 : 'Kiran', 19 : 'Krisha', 20 : 'Sita', 25 : 'Ramesh'}
print(type(e)) # output : <class 'dict'>


# # ------------------------------------------------------------------------------------------------

# 11 . #  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b) # output : TypeError 
c = {**a , **b} # {10:60, 30:50} , {10:60, 30:50}
print(c)  # output :{10:60, 30:50} 
d = a | b
print(d)# output :  {10:60, 30:50}

# # ----------------------------------------------------------------------------------------

# # 12 .(Home  work)
# # Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

# # Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
  
a = {}

num = int(input('Enter a number of employees : '))

for i in range(num):
    employeeName = input('Enter employee Name : ')
    employeeSalary = float(input('Enter employee salary: '))
    a[employeeName] = employeeSalary
print('employee Dictionary: ',a) 

# #------------------------------------------------------------------------
# # 13 . ' (Home  work)
# # Write  a  program  to  convert  a  string  to  dictionary
# # Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
# # What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}
# # Hint :  Use  split()  method  twice
# # input  --->  "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"
# # input . split(',') --->  ['Emp no = 25'  , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
# # a = {} 
# # Iteration  1    --->  ['Emp no' ,  '25']   --->  a['Empno'] = '25'
# # Iteration  2    --->  ['Emp name' , 'Rama  Rao']   --->  a['Emp  name'] = 'Rama   Rao'
# # Iteration  3    --->  ['sal' , '10000.0']   --->  a['sal'] =  '10000.0'
# # Iteration  4    --->  ['gender' , 'm']   --->  a['gender'] =  'm'
# # '''   

s = input("Enter string: ")
#"Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"

a = s.split(',')
b = {}

for i in a:
    key_value = i.split('=')   
    key = key_value[0].strip()
    value = key_value[1].strip()
    
    b[key] = value

print("Dictionary:", b)
