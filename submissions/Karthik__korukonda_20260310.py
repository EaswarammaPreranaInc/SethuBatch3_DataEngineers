#  Find  outputs (Home  work)
'''a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12
print(a) #[10, 20, 12, 18]'''


#  Find  outputs  (Home  work)
'''a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10, 20, 15, 18, 100, 200, 150]
print(a + 5) #Error
print(a + '5') #Error
print([10 , 20] + (30 , 40)) #Error'''



# Tricky  program
#  Find  outputs
'''a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1 , 2 , 3] , address of object a
a += b 
print(a , id(a)) #[1 , 2 , 3 , 4 , 5 , 6] , Same address
a  = a + b 
print(a , id(a)) #[1 , 2 , 3 , 4 , 5 , 6] , Different address'''



# Find  outputs
'''list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list 
print('a : ' , a)#25
print('b : ' , b)# [10.8, 'Hyd']
print('c : ' , c)#True
print(type(b)) #<class 'list'>
x , *y = list
print('x : ' , x) # 25
print('y : ' , y) # [10.8 , 'Hyd' ,  True]
*p , q = list
print('p : ' , p)#[25 , 10.8 , 'Hyd']
print('q : ' , q)# True
'''


# Find  outputs  (Home  work)
'''list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list # Error
a , b , *c , d , e = list #Error
print('a : ' , a) #25
print('b : ' , b)#10.8
print('c : ' , c)#[]
print('d : ' , d)#'Hyd'
print('e : ' , e)# True
a , b , *c , d , e , f = list #Error
'''



# Find  outputs  (Home  work)
'''list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ :  ' , _)#Hyd
print('d : ' , d)#True
'''


#  Tricky  program
# Find  outputs (Home  work)
'''list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('_ : ' , _) #'Hyd'
print('d : ' , d) #True
print('_: ' , _) #3+4j'''



# Identify  error (Home  work)
'''list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list''' #Error due to multiple *expression.


# Find  outputs  (Home  work)
'''list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #25
print('b : ' , b) #10.8
print('c : ' , c) #'Hyd'
print('d : ' , d) #True
a , b , c , d = list #Error
'''



'''
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b) #False
print(a < c) #True
print(a > d) #True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#False
'''



# Comparing  Lists  (Home  work)
'''a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False
'''




#  len()  function demo   program  (Home  work)
'''a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3
'''

'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''



# sum()  function  demo  program  (Home  work)
'''a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j]
print(sum(b)) #8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#Error due to str cannot be added.'''


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''



'''
a = [[10 , 20 , 15 , 18]]
print(sum(a)) #Error 
print(sum(a[0])) #63'''


# max()  and  min()  functions  demo  program  (Home  work)
'''a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamsi
print(min(b)) #Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))#Error
d = [25 , '35']
print(max(d)) #Error due to str cannot be determined.
print(max([])) #Error
print(min([]))#Error'''





# sorted()  function   demo  program
'''a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b) #[5, 10, 12, 15, 20]
print(type(b)) #<class 'list'>
c = sorted(a , reverse = True)
print(c)#[20, 15, 12, 10, 5]
print(a)#[10, 20, 15, 5, 12]
'''



# all()  function demo  program 
'''a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True
'''



# any()  function demo program  (Home  work)
'''a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False
'''



# del  operator  demo  program (Home  work)
'''a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del    a[2]
print(a)#[10, 20, 18]
del  a[3]
del  a
print(a) #Error 

'''





#  append()  method  demo  program (Home  work)
'''list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . append(19)
print(list)#[10 , 20 , 15 , 18 , 19]
'''




# Find  outputs  (Home  work)
'''list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list) #[0, 10, 20, 30, 40]'''




'''#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)# [10, 20, [50, 60, 70], 30, 40]
print(len(a))#5
print(a[2])#How  to  print  inner  list
print(a[2][0])#How  to  print  50
print(a[2][1])#How  to  print  60
print(a[2][2])#How  to  print  70
'''


# remove()  method  demo  program  (Home  work)
'''try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)#[10, 20, 18, 15, 12, 15, 19]
	list . remove(25)
except:
	print('25  is   not  in  the  list') #25  is   not  in  the  list
	
'''



#  pop()  method  demo  program
'''a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))#15
print(a)#[10, 20, 18, 12]
print(a . pop(len(a)))#Error
print(a . pop(-3)) #20
print(a)#[10, 18, 12]
print(a . pop(-4)) #Error
print(a . pop())#12
print(a)#[10, 18]
b = []
b . pop() #Error
'''


'''
Write  a  program  to  determine  all  the  list  elements  are  identical  or  not

1) Let  input  be  [25 , 25 , 25 , 25]
    What  is  the  output ?  --->  All  the  elements  are  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ?  ---> 4

2) Let  input  be  [10 , 10 , 20 ,  10]
    What  is  the  output ?  --->  All  the  elements  are  not  identical
    How  many  elements  are  in  the  list ?  ---> 4
    How  many  times  is  first  element  repeated ? ---> 3
'''

a = eval(input("Enter list: "))

total = len(a)
repeat = a.count(a[0])

if total == repeat:
    print("All the elements are identical")
else:
    print("All the elements are not identical")

print("How many elements are in the list", total)
print("How many times is first element repeated", repeat)




