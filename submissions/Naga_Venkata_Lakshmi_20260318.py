#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno']) #25
print(a['Ename']) #'Rama Rao'
print(a['Sal']) #1000.65





# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

print(id(a)) # Address of dictionary.
How  to  modify  1000.65  to  2000
a['Sal'] = 200
How  to  modify  'Rama  Rao'  to  'Sita'
a['Ename'] = 'Sita'
How  to  modify  25   to  35
a['Empno'] = 35
print(a) #{'Empno' : 35 , 'Ename' : 'Sita' , 'Sal' : 2000}
print(id(a)) #Same Address.




#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Gender'] = 'M'
How  to  append  'Married' :  True  to  dictionary  'a'
a['Married'] = True
print(a) #{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65 , 'Gender' : 'M' , 'Married' : True}



# Find  outputs (Home  work)
a = { }
How  to  append  10 : 'Rama'  to  dictionary  'a'
a[10] = 'Rama'
How  to  append  20 : 'Sita'  to  dictionary  'a'
a[20] = 'Sita'
How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[15] = 'Rajesh'
How  to  append  18 : 'Kiran'  to  dictionary  'a'
a[18] = 'Kiran'
print(a) #{ 10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}





#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }

How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
del a['Sal']
print(a) # {'Empno'  :  25,  'Ename'  :  'Rama  Rao'}




#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) #True
print(60  in  a . keys()) #False
print(60  in  a . values()) #True
print(30  in  a . values()) #False
print(50  in  a) #True 
print(20  in  a) #True
print(70  not  in  a . keys()) #False
print(40  not  in  a . values()) #False
print(25  not  in  a)#True



#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ') #'{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'

print(a) #'{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}'

print(type(a)) #<class 'str'> 
b = eval(a) #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(b) #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) #<class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a} #it returns a new dictionary with same key value pairs i.e {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(b) #{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b) #False
print(a  ==  b) #True
c = a # it is shallow clone and both c and a pointing to same dictionary.
print(a  is   c) #True
print(a  ==  c) #True


#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c} #{10 , 20 , 15 , 18 , 14 ,  25 , 19}
print(d) #{10 , 20 , 15 , 18 , 14 ,  25 , 19}

print(type(d)) #<class 'set'>
e = {**a , **b , **c} #it returns new dictionary with same key value pairs i.e #{10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'}
print(e) #{10 : 'Rama' , 20 : 'Manohar' , 15 : 'Radha' , 18 : 'Kiran' , 14 : 'Srinivas' , 25 : 'Ramesh' , 19 : 'Krishna'} here as the key is repeated the value is replaced.
print(type(e)) #<class 'dict'>


#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b) #Type Error
c = {**a , **b} #{10 : 60 , 30 : 50}
print(c) #{10 : 60 , 30 : 50}
d = a | b
print(d) #{10 : 60 , 30 : 50}


n = int(input("How many Employees: " ))


a ={}
for i in range(n):
  N = input("Enter Employee name: ")
  S = eval(input("Enter salary:"))
  
  a[N] = [S]

print(a) 




n = input("Enter any string: ") 
p = n.split(',')
print(p)
a ={}
for ch in p:
    print(ch)
    res=ch.split('=')
    print(res)
    a[res[0].strip()] = res[1].strip()
print(a)



s = input("Enter any mixed string:  ")
b = s.upper()
Vowels ='AEIOU'
distinct_vowels = ''.join(set(ch for ch in b if ch in Vowels))

print("Distinct Vowels:" , distinct_vowels)




