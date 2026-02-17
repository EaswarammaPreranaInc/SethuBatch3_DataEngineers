# Find  outputs    (Home  work)                                     
a = range(10 , 50 , 5)                                                                            
print(type(a))                                                                                           #<class’range’>
print(a)                                                                                                       #range(10, 50, 5)
print(*a)                                                                                                    # 10 15 20 25 30 35 40 45
print(id(a))                                                                                               #address of range object (10, 50, 5)
print(len(a))                                                                                            #8
print(*a[2 : 7] , sep = ' , ')                                                                    #20, 25, 30, 35, 40
print(*a[ : : -1])                                                                                       #45 40 35  30 25 20 15 10
a[4] = 32                                                                                                   #error due we can’t assign                                                                                   
print(a * 2)                                                                                              #error due to duplicates are formed  



#  Find  outputs  (Home  work)
a = range(10 , 20)                            
print(*a , sep = ',')                                                                #10, 11, 12, 13, 14, 15, 16, 17,18,19
b = range(5)                                                                            
print(*b)                                                                                  #0 1 2 3 4
c = range(10 , 1 , -1)                                                           
print(*c , sep = '...')                                                         #10…9…8…7…6…5…4…3…2
d = range(-10 , 0)
print(*d)                                                                               #-10 -9 -8 -7 -6 -5 -4 -3  -2 -1
e = range(-10)
print(*e)                                                                               #-1 -2 -3 -4 -5 -6 -7 -8 -9
f = range(2 , 2)
print(*f)                                                         #error due to we can’t get 1 from 2 in steps of 1
g = range(10 , 11 , 0.1)                           #error due to step can’t be a float object 
h = range('A' , 'F')                                     #error due to str is not allowed in range object 




#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)                                                     
a , b , c = r  
print(a , b , c)                         #range(10, 17, 3)
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r))                                           #address of range object ‘range(3)’
print(id(m))                                        # same address of ‘range(3)’




#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                                                        #25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(*a)                                                      #25  10.8  'Hyd'  True  3 + 4j  None  'Hyd'  25
print(type(a))                                            #<class ‘list’>
print(id(a))                                                 #address of list object ‘a’
print(len(a))                                              #8
a[2] = 'Sec'                                                
print(a)                                                       #[25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])                                          # [‘Sec’, True, 3+4j]




# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)                                               #empty list
a . append(25)                                      
a . append(10.8)                                  
a . append('Hyd')
a . append(True)
print(a)                                                                    #[25, 10.8,  ‘Hyd’, True]
a . remove('Hyd')
print(a)                                                                     #[25, 10.8, True]
a . remove('25')
print(a)                                                                    #[10.8, True ]



#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)                                                       #25, 10.8, ‘Hyd’
print(id(a))                                              # address of list object ‘a’
print(a * 3)                                              #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2)                                             #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1)                                              #[25 , 10.8 , 'Hyd']
print(a * 0)                                             #[]empty list
print(a * -1)                                            #[]  
print(a * 4.0)                                        #can’t multiple with float object
a = a * 3
print(a)                                       #[25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a))                                 # address of list object a*3
a = [25]
print(a , id(a))                                #[25]<space>address of list object[25]
print(a * a)                                      #error due to ‘a’ is not an int



# list()  function  demo  program
a = list('Hyd')                                                                                   
print(a)                                                                 #[‘H’, ‘y’, ‘d’]
print(type(a))                                                    #<class ‘list’>
print(len(a))                                                      #3
b = (10 , 20 , 15 , 18)
print(list(b))                                                   #[10, 20, 15, 18]
print(list(range(5)))                                   #[0, 1, 2, 3, 4]
print(list(25))                                              #error due to we can’t list the int 


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
print(type(a))                                                       #<class ‘list’>
print(a)                                                                  #[]
print(len(a))                                                        #0
b = list()                                                                
print(b)                                                                #[ ]
print(len(b))                                                        #0




# Slice  demo  program (Home  work)
#           0         1          2           3            4          5            6            7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#            -8     -7         -6         -5          -4           -3       -2          -1
print(list[2 : 7]) #list[2:7:1]  
                                  --->  List  from  indexes  2  to  6  in steps  of  1  i.e. [3+4j, ‘Hyd’, True, None, 10.8]
print(list[ : : ]) #list[0:8:1]  
    --->  List  from  indexes  0  to  7 in steps  of  1  i.e. [25, 10.8, 3+4j, ‘Hyd’, True, None, 10.8, ‘Hyd’]

print(list[:])#list[0:8:1]  
     --->  List  from  indexes  0 to  7 in steps  of  1  i.e. . [25, 10.8, 3+4j, ‘Hyd’, True, None, 10.8, ‘Hyd’]

print(list[ : : -1]) #[-1:-9:-1]
                                  --->  List  from  indexes  -1  to -8   in steps  of  1  i.e. [‘Hyd’, 10.8, None, True, ‘Hyd’, 3+4j, 10.8, 25]


print(list[ : : 2])  #  list[0 : 8 : 2] 
  --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) 
#list[1:8:2]-List from indexes 1 to 7 in steps of 2 i.e. [10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -2]) #list[-1:-9:-2]-List from indexes -1 to -8 in steps of -2 i.e. [ 'Hyd' , None , 'Hyd', 10.8]
  
print(list[-2 : : -2])  #   list[-2 : -9 : -2] 
--->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) #[1:4:1] List from indexes 1 to 3 in steps of 1 i.e.[10.8, 3+4j, ‘Hyd’]
print(list[-4 : -1]) #[-4:-1:1]List from indexes -4 to -1 in steps of 1 i.e.[True, None , 10.8]
print(list[3 : -3])#[3:-3:1] List from indexes 3 to -2 in steps of 1 i.e.[ 'Hyd' , True , None , 10.8]
print(list[2 : -5])#[2:-5:1] List from indexes 2 to -4 in steps of 1 i.e. [3 + 4j , 'Hyd' , True ]
print(list[-1:-5])#[-1:-5:1]
# List from indexes -1 to -4   in steps of 1 i.e. error we can’t get -4 in steps of 1




#  Find  outputs  (Home  work)
#            0       1         2           3           4            5           6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]                                                                      
print('x : ' , x)                                                               #x : Hyd
print('y : ' , y)                                                               #y : True
for  x  in  list[2:7]:                                               
	print(x)                                      #3+4j                                        
                                                                    #’Hyd’ 
                                                                    #True
                                                                    #None
                                                                   #10.8



#  Find  outputs  (Home  work)
#        0      1      2      3      4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))                                            #[10 , 20 , 30 , 40 , 50]<space> address of list ‘a’
a[1 : 4] = [60 , 70]
print(a , id(a))                                           # [10, 60, 70, 50] ]<space> same address of list ‘a’

a[2: 4] = [100 , 200 ,  300]
print(a , id(a))                                             # [10, 60, 100, 200, 300] ]<space> same address of list ‘a’




#  Find  outputs  (Home  work)
a =  [25]
print(a[1])                                                         #error due to index out of range
print(a[1:])                                                        #error due to index out of range


