
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
# s = input("Enter mixed case string: ")

# vowels = {'a', 'e', 'i', 'o', 'u'}
# result = set()

# for ch in s.lower():   
#     if ch in vowels:
#         result.add(ch.upper())   

# output = ''.join(sorted(result))   

# print('Distinct Vowels : ',output)

#  How  to  access  values  of  dictionary (Home  work)
# a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# print(How  to  print  value  25  in  dict  'a')
# print(How  to  print  'Rama Rao'  in  dict  'a')
# print(How  to  print  value  1000.65   in  dict  'a')
# print(a['Empno'])   
# print(a['Ename'])   
# print(a['Sal']) 

# How  to  modify  values  of  dictionary  (Home  work)
# a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# print(a)
# print(id(a))
# How  to  modify  1000.65  to  2000
# How  to  modify  'Rama  Rao'  to  'Sita'
# How  to  modify  25   to  35
# print(a)
# print(id(a))



# print(a)
# print(id(a))


# a['Sal'] = 2000        
# a['Ename'] = 'Sita'    
# a['Empno'] = 35       

# print(a)
# print(id(a))   

#  How  to  append  key : value  pairs  to dictionary  (Home  work)
# a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
# print(a)
# How  to  append  'Gender' : 'M'  to  dictionary  'a'
# How  to  append  'Married' :  True  to  dictionary  'a'
# print(a)





# print(a)

# a['Gender'] = 'M'
# a['Married'] = True

# print(a)

# Find  outputs (Home  work)
# a = { }
# How  to  append  10 : 'Rama'  to  dictionary  'a'
# How  to  append  20 : 'Sita'  to  dictionary  'a'
# How  to  append  15 : 'Rajesh'  to  dictionary  'a'
# How  to  append  18 : 'Kiran'  to  dictionary  'a'
# print(a)



# a[10] = 'Rama'
# a[20] = 'Sita'
# a[15] = 'Rajesh'
# a[18] = 'Kiran'

# print(a)
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
# a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

# How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
# print(a)



# print(a)


# del a['Sal']

# print(a)

#  in  and  not  in  operators  (Home  work)
# a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
# print(30  in  a . keys())#True
# print(60  in  a . keys())#False
# print(60  in  a . values())#True
# print(30  in  a . values())#False
# print(50  in  a)#True
# print(20  in  a)#True
# print(70  not  in  a . keys())#False
# print(40  not  in  a . values())#False
# print(25  not  in  a)#True


#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
# a = input('Enter  dictionary  :  ')
# print(a)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
# print(type(a))#<class 'str'>
# b = eval(a)
# print(b)#{10: 'A', 20: 'D', 15: 'C'}
# print(type(b))#<class 'dict'>


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

# s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"

# a = {}


# parts = s.split(',')

# for item in parts:
    
#     key_value = item.split('=')
    
#     key = key_value[0].strip()     
#     value = key_value[1].strip()   
    
#     a[key] = value

# print(a)

# a = {}

# n = int(input("Enter number of employees: "))

# for i in range(n):
#     name = input("Enter employee name: ")
#     sal = float(input("Enter salary: "))
    
#     a[name] = sal   # append to dictionary

# print(a)

#  Find  outputs  (Home  work)
# a = {10 : 20 , 30 : 40}
# b = {30 : 50 , 10 : 60}
# # print(a + b) # error
# c = {**a , **b}
# print(c)#{10: 60, 30: 50}
# print(c)
# d = a | b
# print(d)

#Find  outputs  (Home  work)
# a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
# b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
# c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
# d = {*a , *b , *c}
# print(d)#{10, 14, 15, 18, 19, 20, 25}
# print(type(d))#<class 'set'>
# e = {**a , **b , **c}
# print(e)# {10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
# print(type(e)) #<class 'dict'>

 # Find  outputs  (Home  work)
# a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
# b = {**a}
# print(b)#{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
# print(a  is  b)#False
# print(a  ==  b)#True
# c = a
# print(a  is   c)#True
# print(a  ==  c)#True