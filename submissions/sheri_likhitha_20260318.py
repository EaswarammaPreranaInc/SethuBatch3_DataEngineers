input=input("Enter the sentence: ").upper()
vowels={'A','E','I','O','U'}
result={char for char in input if char in vowels}
print(result)


#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])		#How  to  print  value  25  in  dict  'a'
print(a['Ename'])		#How  to  print  'Rama Rao'  in  dict  'a'
print(a['Sal'])			#How  to  print  value  1000.65   in  dict  'a'



# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)		#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(id(a))		#Address of object 'a'
a['Sal'] = 2000		#How  to  modify  1000.65  to  2000
a['Ename'] = 'Sita'	#How  to  modify  'Rama  Rao'  to  'Sita'
a['Empno'] = 35		#How  to  modify  25   to  35
print(a)		#{'Empno'  :  35,  'Ename'  :  'Sita'  ,  'Sal'  :  2000  }
print(id(a))		#Address of the object 'a'(same address)



#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)   		#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a['gender']= 'M'	#How  to  append  'Gender' : 'M'  to  dictionary  'a'
a['Married']= True 	#How  to  append  'Married' :  True  to  dictionary  'a'
print(a)		#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65,'gender': 'M', 'Married': True}






# Find  outputs (Home  work)
a = { }
a[10] = 'Rama'	 #How  to  append  10 : 'Rama'  to  dictionary  'a'
a[20] = 'Sita'   #How  to  append  20 : 'Sita'  to  dictionary  'a'
a[15] = 'Rajesh' #How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[18] = 'Kiran'  #How  to  append  18 : 'Kiran'  to  dictionary  'a'
print(a)



#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)		#{'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
a.pop('Sal')		#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
print(a)		#{'Empno': 25, 'Ename': 'Rama  Rao'}



#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())	#True
print(60  in  a . keys())	#False
print(60  in  a . values())	#True
print(30  in  a . values())	#False
print(50  in  a)		#True
print(20  in  a)		#False
print(70  not  in  a . keys())	#False
print(40  not  in  a . values()) #False
print(25  not  in  a)		#True



#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)	#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))	#<class 'str'>
b = eval(a)	
print(b)	#{10:'A',20:'B',15:'C',20:'D'}
print(type(b))	#<class 'dict'>



#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)	#{10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
print(a  is  b)  #False
print(a  ==  b)  #True
c = a
print(a  is   c) #True
print(a  ==  c)  #True



#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)	 #{10, 14, 15, 18, 19, 20, 25}
print(type(d))   #<class 'set'>
e = {**a , **b , **c}
print(e)	 #{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))	 #<class 'dict'>



#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
print(a + b)	#error
c = {**a , **b}
print(c)	#{10: 60, 30: 50}
d = a | b
print(d)	#{10: 60, 30: 50}



a={}
employees=int(input("Enter the number of emplloyees:  "))
for i in range(employees):
    name=input("Enter name for employee: ")
    salary=float(input("Enter the salary: "))
    a[name]=salary
    print(f"final employee dictionary: {employees}")
print(a)




input=input("Enter the dicyionary: ").split(",")
a={}
for item in input:
    key_value=item.split("=")
    key=key_value[0].strip()
    value=key_value[1].strip()
    a[key]=value
print(a)