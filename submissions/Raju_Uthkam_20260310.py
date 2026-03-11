#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b) #True
print(a  ==  b) #True
b[2] = 12 
print(a) #[10, 20, 12, 18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b) #[10,20,15,18,100,200,150]
#print(a + 5) #Error
#print(a + '5') #Error we can't add int and str
#print([10 , 20] + (30 , 40)) #Error we can;t add list and tuple 



# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a)) #[1,2,3],Address of list a
a += b #[1,2,3,4,5,6] #Adding elements to exiating list
print(a , id(a)) ##[1,2,3,4,5,6] Address of list a
a = a+b
print(a,id(a)) #Here concatenating and forming a new list



# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a) #a : 25
print('b : ' , b) #b : [10.8,'Hyd']
print('c : ' , c) #c : True
print(type(b)) # <class 'list'>
x , *y = list
print('x : ' , x) #x : 25
print('y : ' , y) #y : [10.8,'Hyd',True]
*p , q = list
print('p : ' , p) #p : [25,10.8,'Hyd']
print('q : ' , q) #q : True



# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list #Error
a , b , *c , d , e = list
print('a : ' , a) #Error
print('b : ' , b) #Error
print('c : ' , c) #Error
print('d : ' , d) #Error
print('e : ' , e) #Error
#a , b , *c , d , e , f = list #Error beacuse there is not enough values to unpack



# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a) #a : 25
print('b : ' , b) #b : 10.8
print('_ :  ' , _) #_ : 'hyd'
print('d : ' , d) #d : True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a) #3+4j
print('b : ' , b) #10.8
print('d : ' , d) #True



#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a) #a : 25
print('b : ' , b) #b : 10.8
print('_ : ' , _) #_ : 3+4j
print('d : ' , d) #d : True
print('_: ' , _) #_ : 3+4j


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a) #a : [25,10.8]
print('b :  ' , b) #b : 'Hyd'
print('c :  ' , c) #c : True



# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a) #a : 25
print('b : ' , b) #b : 10.8
print('c : ' , c) #c : 'Hyd'
print('d : ' , d) #d : True
#a , b , c , d = list 


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) #True
print(a  is   b) #False
print(a < c) #True
print(a > d) #False
print(a >= c) #False
print(a <= d) #True
print(a != c)#True
print(a != b) #False
print(a == c) #False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b) #False
print(a  is   b) #False


#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a)) #4
b = []
print(len(b)) #0
c = [[10 , 20] , 30 , 40] 
print(len(c)) #3


'''
What  does  len(list)  do ?  --->  Returns  number  of  elements  in  the  list
'''



# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a)) #36.8
b= [3 + 4j , 5 + 6j] 
print(sum(b)) #(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c)) #39.8 + 4j
d = [10 , 20 , 15 , 18]
print(sum(d)) #63
#e = [25 , 10.8 , 'Hyd' , True] 
#print(sum(e)) #Error


'''
What  does  sum(list)  do ?  ---> Returns  sum  of  list  elements
'''


#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) #Error we can't add int+list
print(sum(a[0]))
print()#How  to  determine  sum  of  inner  list  elements  in  another  way)


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a)) #30
print(min(a)) #5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b)) #Vamshi
print(min(b)) #Amar
#c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c)) #Error
d = [25 , '35']
#print(max(d)) #Error
#print(max([])) #Error
#print(min([])) #error


'''
1) What  does  max(list)  do ?  --->  Returns  largest  element  of  the  list

2) What  does  min(list)  do ?  --->  Returns  smallest  element  of  the  list
'''

# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a) #[10,20,15,18]
print(b) #Error
print(type(b)) #Error
print(a  is  b) #Error
print(a == b) #Error 


#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a) 
print(b) #[4,6,8]
print(type(b)) #<class 'list'>
a = list('Vamsi') 
print(a) #['Vamshi']
a = list()
print(a) #Empty list
print(list(25)) #Error 
print(list(10.8)) #Error
print(list(True)) #Error
print(list(None)) #Error



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->  Throws  error
'''

# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a)) #[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b)) #Error
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c)) #[[10,20],(30,40),{50,60}]



