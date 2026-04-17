#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)                                #(25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)                 
print(*a)                               #25 10.8 Hyd true 3+4j None Hyd 25
print(type(a))                          # <class 'tuple'>
print(len(a))                           # 8
print(a[2 : 5])                         #('Hyd', True,3+4j)
print(*a[2 : 5])                        # Hyd True 3+4j
#a[2] = 'Sec'                           # error (tuples are immutable)
#a . append('Sec')                      # error 
#a . remove('Hyd')                      # error  
b =  10 , 20 , 30
print(b)                                #(10,20,30)                             
print(b * 2)                            #(10,20,30,10,20,30)
c = 40 , 50 , 60,                 
print(c)                                #(40,50,60)
print(type(c))                          #<class "tuple">


a = (25)                               # error                
b = 25,                         
c = 25       
d = (25,)
print(type(a))                         # <class 'int'>
print(type(b))                         # <class 'tuple'>
print(type(c))                         #<class 'int'>
print(type(d))                         # <class 'tuple'>
print(a * 4)                           # 100
print(b * 4)                           #(25,25,25,25)
print(c * 4)                           #100
print(d * 4)                           #(25,25,25,25)


a = tuple('Hyd')
print(a)                               # ('H','y','d')
print(type(a))                         # <class 'tuple'>
print(len(a))                          # 3
b = [10 , 20 , 15 , 18]                 
print(tuple(b))                        # (10,20,15,18)       
print(tuple(range(5)))                 # (0,1,2,3,4)
#print(tuple(25))                       # error


a = ()
print(type(a))                        # <class 'tuple'>
print(a)                              #()
print(len(a))                         #0
b = tuple()
print(b)                              #()
print(len(b))                         #0