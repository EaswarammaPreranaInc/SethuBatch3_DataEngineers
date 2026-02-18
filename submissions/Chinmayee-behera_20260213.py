# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) #<class 'range'>
print(a)#range(10,50,5)
print(*a)#(10,15,20,25,30,35,40,45)
print(id(a)) #address of object 
print(len(a)) #8
print(*a[2 : 7] , sep = ' , ') # [20,25,30,35,40]
print(*a[ : : -1])  # [45,40,35,30,25,20,15,10]
a[4] = 32 # (10,15,20,25,30,32,40,45)
print(a * 2) #(10,15,20,25,30,32,40,45,10,15,20,25,30,32,40,45)


-----------------------------------------------------------------


#  Find  outputs  (Home  work)
a = range(10 , 20) =>it begins with 10 to 20-1 in steps of 1    =  if step is +ve then we will do (len-1)
print(*a , sep = ',') =>#(10, 11, 12, 13, 14, 15, 16, 17, 18, 19)  
b = range(5)=>range(0,5,1) 
print(*b) # (0,1,2,3,4)
c = range(10 , 1 , -1) =>it begins with 10 to 1+1 in steps of -1  = if step is -ve then we will do (end+1)
  
print(*c , sep = '...') (10...9...8...7...6...5...4...3...2)
d = range(-10 , 0) it will begins with -10 to 0 in steps of 1.
print(*d) #(-10,-9,-8,-7,-6,-5,-4,-3,-2,-1) 
e = range(-10) it begins with 0 to -10-1=-11 in steps of 1 =>0,1,2,3,4,5,
print(*e) # ""
f = range(2 , 2) #it begins with 2 to 2-1=1 in steps of 1. =>2,3,4,5
print(*f)  # "" 
g = range(10 , 11 , 0.1) => Error here float is there so we can't step in this .
h = range('A' , 'F') => Error in range we will consider only integers not alphabets

-----------------------------------------------------------

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  =>it will begins with 10 to 17 in steps of 3 .=>r=10,13,16
a , b , c = r  
print(a , b , c)   #10,13,16
r = range(3)    => it will begins with 0 to 3-1 in steps 1. =>(0,1,2)
x , y = r   # Error 
p , q  , r , s = r # Error 
a , b , c = *r  # Error         *r it will give unpack but sir will give like already it has unpack either you have unpacked that is not possible so it through error.         
m = r                
print(id(r))  #address of the object 10,13,16 it may be 1000.            
print(id(m))  #address of the object same as r .

----------------------------------------------------------

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25] 
print(a)  #25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(*a) => 2*2=>4 =>multipler
          =>a*2=>a,a =>repetating
          =>*a=> unpacked   

#   25 10.8 'hyd' True 3+4j  None Hyd 25 
print(type(a)) #<class 'list'>
print(id(a)) #address of the object .
print(len(a)) #8
a[2] = 'Sec' 
print(a) # [25,10.8,'sec',True,3+4j,None,'hyd',25]
print(a[2 : 5]) =>it will begins with 2 to 5-1 in steps of 1.
     #['sec',True,3+4j]

----------------------------------------------------------------

# append()  and  remove()  methods  (Home  work)  
a = [ ]
print(a) #[]
a . append(25) 
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a) #[25,10.8,'Hyd',True]
a . remove('Hyd')
print(a) ##[25,10.8,True,]
a . remove('25')
print(a) #Error because in our list there is no string 25.

----------------------------------------------------------

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) #25 , 10.8 , 'Hyd'
print(id(a)) #address of the object may be 3000.
print(a * 3) #25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'
print(a * 2) #25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'
print(a * 1) #25 , 10.8 , 'Hyd'
print(a * 0) #[]
print(a * -1)  #[]
print(a * 4.0) #Error  it must be integer not float.
a = a * 3
print(a)  #25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd'
print(id(a)) # address of the object may be 1000.
a = [25]
print(a , id(a)) # 25, address of the object may be 200.
print(a * a)#Error becoz it must be integer but not alphabets.

---------------------------------------------------------

# list()  function  demo  program
a = list('Hyd')  =>['H','y','d']
print(a)  #['H','y','d']
print(type(a)) =><class 'list'>
print(len(a)) #3
b = (10 , 20 , 15 , 18)
print(list(b)) #[10,20,15,18]
print(list(range(5))) =>[0,1,2,3,4]  it will begins with 0 to 5 in steps of 1.
print(list(25)) #Error 


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''

--------------------------------------------------------------------------------------

# Find  outputs
a = [ ]
print(type(a)) <class 'list'>
print(a) #[]
print(len(a)) #0
b = list() 
print(b) #[]
print(len(b)) #0

-----------------------------------------------

# Slice  demo  program (Home  work)
#        0      1       2      3      4      5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']  
#       -8     -7  -6        -5       -4      -3     -2    -1
print(list[2 : 7]) # it will begins with 2 to 7-1=6 in steps of 1.=> [3+4j,'Hyd',True,None,10.8]
print(list[ : : ]) #it will begins with 0 to len -1 in steps of 1.=>[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) #it will begins with 0 to len-1 in steps of 1.=>[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #it will begins with -1 to -8-1=-9 in steps of -1. =>['Hyd',10.8,None,True,'hyd',3+4j,10.8,25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # it will begins with 1 to len-1 in steps of 2. =>[10.8,'Hyd',none,'hyd']
print(list[ : : -2]) # it will begins with -1 to -len-1 in steps of -2. =>['Hyd',None,'Hyd',10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # it will begins with 1 to 4 in steps of 1 .=>[10.8,3+4j,'hyd']
print(list[-4 : -1])# it will begins with -4 to -len+1 in steps of -1.=>[True,'Hyd',3+4j,10.8,25]
print(list[3 : -3])# it will begins with 3 to -3 in steps of 1.=> ['hyd',none]
print(list[2 : -5])# it will begins with 2 to -5 in steps of 1.=>[]
print(list[-1:-5])# []

-----------------------------------------------------

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) #'hyd'
print('y : ' , y) #True
for  x  in  list[2:7]:
	print(x) 
#3+4j , 'Hyd' , True , None , 10.8 , 'Hyd'

--------------------------------------------------------

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) #10 , 20 , 30 , 40 , 50 ,address of the object may be 3000.
a[1 : 4] = [60 , 70]
print(a , id(a))#10,60,30,40,70 ,address of the object may be 4000.
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) #error list is out of index.

----------------------------------------------------

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) #error 
print(a[1:]) #[]


