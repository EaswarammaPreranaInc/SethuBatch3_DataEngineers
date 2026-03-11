# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))#[1,2,3],some sys generated address
a += b
print(a , id(a))#[1,2,3,4,5,6],same sys generated address



# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)))#[1,2,3],some sys generated address
a  = a + b
print(a , id(a)))#[1,2,3,4,5,6],different sys generated address



# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list     
print('a : ' , a)#25
print('b : ' , b)#[10.8,'Hyd']
print('c : ' , c)#True
print(type(b)) #<class 'list'>                                                                           
x , *y = list
print('x : ' , x)#25
print('y : ' , y)#[10.8,'Hyd',True]
*p , q = list
print('p : ' , p)#[25,10.8.'Hyd']
print('q : ' , q)#True




# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list#error,not enough values
a , b , *c , d , e = list#error,not enough values
print('a : ' , a)#not executed 
print('b : ' , b)#not executed
print('c : ' , c)#not executed
print('d : ' , d)#not executed
print('e : ' , e)#not executed
a , b , *c , d , e , f = list#error



# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ :  ' , _)#'Hyd'
print('d : ' , d)#True



 # Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)#3+4j
print('b : ' , b)#10.8
print('d : ' , d)#'Hyd'



 #  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]

a , b , _ , d , _ = list
print('a : ' , a) # 25
print('b : ' , b)# 10.8
print('_ : ' , _)# (3+4j)
print('d : ' , d)# True
print('_: ' , _) # (3+4j)


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list #syntax error two * expressions





# Find outputs (Home work)

list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)# [25, 10.8]
print('b :  ' , b)# Hyd
print('c :  ' , c)# True




# Find outputs (Home work)

list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) # 25
print('b : ' , b)# 10.8
print('c : ' , c)# Hyd
print('d : ' , d)# True

a , b , c , d = list# ValueError ,only 3 values given





 # Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#True
print(a  is   b)#False
print(a < c)#True
print(a > d)#True
print(a >= c)#false
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#False




 # Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#False
print(a  is   b)#False




#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3



'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''

 # sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error



'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''
 #  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))#error
print(How  to  determine  sum  of  inner  list  elements)#63
print(How  to  determine  sum  of  inner  list  elements  in  another  way)#print(sum(*a))





 # max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#Vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))#error ,no > while complex
d = [25 , '35']
print(max(d))#error
print(max([]))#error
print(min([]))#error



 # list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)#[10,20,15,18]
print(b)#[10,20,15,18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a == b)#False


 #  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['V','a','m','s','i']
a = list()
print(a)#[]
print(list(25))#[25]
print(list(10.8))#[10.8]
print(list(True))#[True]
print(list(None))#[None]



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''


 # Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[[10,20],[30,40,50],[60,70,80,90]]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(10,20),(30,40,50),(60,70,80,90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10,20],(30,40),{50,60})


 # sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)#[5,10,12,15,20]
print(type(b))#<class 'list'>
c = sorted(a , reverse = True)
print(c)#[20,15,12,10,5]
print(a)#[10,20,15,5,12]
'''
