#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)		#True
print(a  ==  b)		#True
b[2] = 12
print(a)		#[10,20,12,18]


#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)		#[10,20,15,18,100,200,150]
print(a + 5)		#error
print(a + '5')		#error
print([10 , 20] + (30 , 40))	#error


# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]
b = [4 , 5 , 6]
print(a , id(a))	#[1,2,3] #address of the object
a += b
print(a , id(a))	#[1,2,3,4,5,6] #same address of the object


# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]		
b = [4 , 5 , 6]
print(a , id(a))	#[1,2,3] #address of the object
a  = a + b
print(a , id(a))	#[1,2,3,4,5,6] #address of the object


# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list
print('a : ' , a)	#a : 25
print('b : ' , b)	#b : [10.8,'Hyd'] 
print('c : ' , c)	#c : True
print(type(b))		#<class 'list'>
x , *y = list
print('x : ' , x)	#25
print('y : ' , y)	#[10.8,'Hyd',True]
*p , q = list
print('p : ' , p)	#[25,10.8,'Hyd']
print('q : ' , q)	#True


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list	#Error
a , b , *c , d , e = list
print('a : ' , a)	#a : 25
print('b : ' , b)	#b : 10.8
print('c : ' , c)	#c : []
print('d : ' , d)	#d : Hyd
print('e : ' , e)	#e : True
a , b , *c , d , e , f = list	#Error


# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)	#a : 25
print('b : ' , b)	#b : 10.8
print('_ :  ' , _)	#_ : 'Hyd'
print('d : ' , d)	#d : True


# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)	#a : 25
print('b : ' , b)	#b : 10.8
print('d : ' , d)	#d : True


#  Tricky  program
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)	#a : 25
print('b : ' , b)	#b : 10.8
print('_ : ' , _)	#_ : 3+4j
print('d : ' , d)	#d : True
print('_: ' , _)	#_ : 3+4j


# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list		#error because multiple * assignment 


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)	#[25,10.8]
print('b :  ' , b)	#'Hyd'
print('c :  ' , c)	#True


# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)	#25
print('b : ' , b)	#10.8
print('c : ' , c)	#'Hyd'
print('d : ' , d)	#True
a , b , c , d = list	#Error


# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)		#True
print(a  is   b)	#False	
print(a < c)		#True
print(a > d)		#True
print(a >= c)		#False
print(a <= d)		#False
print(a != c)		#True
print(a != b)		#False
print(a == c)		#False


# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)		#False
print(a  is   b)	#False


#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))		#4
b = []
print(len(b))		#0
c = [[10 , 20] , 30 , 40]
print(len(c))		#3


# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))		#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))		#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))		#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))		#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))		#error



#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))			#63
print(a[0])
sums=[sum(inner) for inner in a]   #How  to  determine  sum  of  inner  list  elements
print(sums[0]			   #How  to  determine  sum  of  inner  list  elements  in  another  way


# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))		#30
print(min(a))		#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))		#Vamsi
print(min(b))		#Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))		#error
d = [25 , '35']
print(max(d))		#error
print(max([]))		#error
print(min([]))		#error


# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)		#[10,20,15,18]
print(type(b))		#<class 'list'>
print(a  is  b)		#False
print(a == b)		#False


#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)	#[4,6,8]
print(type(b))	#<class 'list'>
a = list('Vamsi')	#['V','a','m','s','i']
print(a)
a = list()
print(a)		#[]
print(list(25))		#error
print(list(10.8))	#error
print(list(True))	#error
print(list(None))	#error



# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))				#[(10,20),(30,40,50),(60,70,80,90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))				#{(10,20),(30,40,50),(60,70,80,90)}
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))				#([10,20],[30,40,50],[60,70,80,90])


# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)		#[5,10,12,15,20]
print(type(b))		#<class 'list'>
c = sorted(a , reverse = True)
print(c)		#[20,15,12,10,5]
print(a)		#[10,20,15,5,12]



# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)	#['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c)	#['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']
print(a)	#['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama  Rao']


# all()  function demo  program 
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))		#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))		#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))		#False
d = [10 , 0 , 20]
print(all(d))		#False
e = []
print(all(e))		#True


# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))		#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))		#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))		#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))		#False
e = []
print(any(e))		#False




# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)		#[10,20,15,18]
del    a[2]
print(a)		#[10,20,18]
del  a[3]		#error
del  a			#error
print(a)		#[10,20,18]


#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)		#[10,20,15,18]
list . append(19)
print(list)		#[10,20,15,18,19]


#  Find  outputs (Home  work)
list = []
print(list)		#[]
list . append(25)	
list . append(10.8)	
list . append('Hyd')
list . append(True)	
print(list)		#[25,10.8,'Hyd',True]


# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)		#[0,10,20,30,40]



#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)	#[10,20,30,'Hyd']
print(len(a))	#4
print(a[3])     #How  to  print  4th  element  of  list  'a'
print(a[3,0]	#How  to  print  'H'
print(a[3,1]	#How  to  print  'y'
print(a[3,2]	#How  to  print  'd'


#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)		#[50,60,70,2]
print(len(a))		#4
print(a[3,0])		#How to print inner list
print([a[0])            #How  to  print  50
print(a[1]		#How  to  print  60
print(a[2]		#How  to  print  70


# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)		#[10,20,18,12,15,19]
	list . remove(25)	#error
except:
	print('25  is   not  in  the  list')



user_input=eval(input("Enter list: "))
target=int(input("Enter element to be deleted: "))
while target in user_input:
    user_input.remove(target)
print(f"List without {target} : {user_input}")


#  pop()  method  demo  program
a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))	#15
print(a)		#[10,20,18,12]
print(a . pop(len(a)))  #error
print(a . pop(-3))	#20
print(a)		#[10,18,12]
print(a . pop(-4))	#error index out of range
print(a . pop())	#12
print(a)		#[10,18]
b = []
b . pop()		#error



										
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)	#[10,20,15,18]
list . clear()
print(list)	#[]


# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)	#[10,20,15,18]
a . reverse()
print(a)	#[18,15,20,10]



#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)	#[10,20,15,18,5]
list . sort()
print(list)	#[5,10,15,18,20]
list . sort(reverse = True)
print(list)	#[20,18,15,10,5]


# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)	#['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
a . sort()
print(a)	#['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
a . sort(reverse = True)
print(a)	#['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']


# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a . sort()	#error '<' not supported between 'str' and 'float' 

#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))	#3
print(a . count(25))	#error
print(len(a))		#9   



nums=eval(input("Enter list: "))
result=[]
for x in nums:
    if nums.count(x)==1:
        result.append(x)
print(result)        



user_input=input("Enter the elements seperated by spaces: ").split()
total_elements=len(user_input)
first_element=user_input[0]
count=user_input.count(first_element)
if count==total_elements:
    print("All the elements are identical")
else:
    print("print all elements are not identical")

    



