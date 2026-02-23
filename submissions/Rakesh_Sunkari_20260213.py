# Find  outputs    (Home  work)
a = range(10 , 50 , 5) 
print(type(a))# class 'range'
print(a) # range (10,50,5)
print(*a) # 10
print(id(a)) # id of object
print(len(a)) # 8	
print(*a[2 : 7] , sep = ' , ')# 20,25,30,35,40
print(*a[ : : -1]) # 
a[4] = 32
print(a * 2)


#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')# 10,11,12,13,14,15,16,17,18,19
b = range(5) # 0 1 2 3 4
print(*b)
c = range(10 , 1 , -1)# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(*c , sep = '...') 
d = range(-10 , 0)
print(*d) #
e = range(-10)
print(*e)
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1) # error bez float value is not acceptable
h = range('A' , 'F') #error



#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #10 13 16
r = range(3) # error no index 3  
x , y = r   #
p , q  , r , s = r #  
a , b , c = *r  
m = r  
print(id(r)) 
print(id(m))




#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)# [25, 10.8, 'Hyd', True, (3+4j), None, 'Hyd', 25]
print(*a) # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a)) # <class 'list'>
print(id(a)) # id of object
print(len(a)) # 8
a[2] = 'Sec'
print(a) # [25, 10.8, 'Sec', True, (3+4j), None, 'Hyd', 25]
print(a[2 : 5])



# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # []
a . append(25)  # 
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) # [25, 10.8, 'Hyd', True]
a . remove('Hyd') # [25, 10.8, True]
print(a) 
a . remove('25')
print(a)




#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #[25, 10.8, 'Hyd']
print(id(a)) # id of object
print(a * 3) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 2) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd']
print(a * 1) # [25, 10.8, 'Hyd']
print(a * 0) # []
print(a * -1)# []
print(a * 4.0)# error
a = a * 3
print(a) # [25, 10.8, 'Hyd', 25, 10.8, 'Hyd', 25, 10.8, 'Hyd'] 
print(id(a)) # id of object
a = [25] 
print(a , id(a)) # 25 id of object
print(a * a) #error bez cant multiply sequence 




# list()  function  demo  program
a = list('Hyd')
print(a) # ['H', 'y', 'd']
print(type(a)) # <class 'list'>
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # (10 , 20 , 15 , 18)
print(list(range(5))) # 
print(list(25))


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''





# Find  outputs
a = [ ]
print(type(a)) # <Class 'list'>
print(a) #[]
print(len(a))# 0
b = list()
print(b)#[]
print(len(b)) #0




# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # [3+4j, 'Hyd', True, None, 10.8]
print(list[ : : ]) # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[:]) # [25, 10.8, (3+4j), 'Hyd', True, None, 10.8, 'Hyd']
print(list[ : : -1]) # ['Hyd', 10.8, None, True, 'Hyd', (3+4j), 10.8, 25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) # ['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # [True, None, 10.8]
print(list[3 : -3]) # ['Hyd', True]
print(list[2 : -5]) # []
print(list[-1:-5]) #[]







#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #
print('y : ' , y)
for  x  in  list[2:7]:
	print(x)






#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10, 20, 30, 40, 50] id
a[1 : 4] = [60 , 70] 
print(a , id(a)) 
a[2: 4] = [100 , 200 ,  300]
print(a , id(a))





#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # error
print(a[1:]) # []