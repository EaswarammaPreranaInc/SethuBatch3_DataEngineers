a = 25
print(id(a))  # address of object 25
a = 35
print(id(a))  # address of object 35



a = 25.7
print(id(a))    # address of object 25.7
print(a)        # 25.7
a = 35.6
print(id(a))    # address of object 35.6
print(a)        # 36.6
b = True         
print(id(b))    # addresss of object True
b = False
print(id(b))    # address of object False
c = None
print(id(c))    # address of object None


a = 'Hyd'
print(id(a))    # address of object 'hyd'
#a[1] = 'e'     # error immutable
a = 'Sec'
print(id(a))    # address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))    # address of tuple
#b[2] = 19      # error(tuples are immutable)
b = (30 , 40 , 35 , 32)
print(id(b))    # address of new tuple 
c = range(5)    
print(id(c))     # address of range(5)
#c[3] = 10       # error (range are immutable)


a = 25
b = 25
print(a  is  b)   # True 
c = 'Hyd'
d = 'Hyd'
print(c  is  d)   # true
e = False
f = False
print(e  is  f)   # True
g = range(10)
h = range(10)
print(g  is  h)   # false


a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)             # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)             # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)              #true
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)               # False


print(10 + 20)                      # 30
print(10.8 + 20.6)                  # 31.4
print(3 + 4j + 5 + 6j)              # 8 +10j
print(True + False)                 # 1
print('Hyder' + 'abad')             #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20')                  # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))                               #(25 , 10.8 , 'Hyd',3+4j,None)
# print({10 , 20} + {30 , 40})       #error
#print({10 : 'Hyd'} + {20 : 'Sec'})  #error
#print(range(4) + range(5))          # error
#print(10 + '20')                     #error
#print([10 , 20 , 30] + 5)              # error (both side should be  list )
#print([10 , 20 , 30] + (40 , 50 , 60))  # error(both sides should be either list or tuple )



  
print(25 * 3)                #100
print(10.8 * 25.6)           #276.48
print(True * False)          # 0
print((3 + 4j) * (5 + 6j))   #
print(3 + 4j * 5 + 6j)        
print('25' * 3)              #252525
print(3 * '25')              #252525
print('Hyd' * 4)             #HydHydHydHyd
print([10 , 20 , 15] * 2)    # [10 , 20 , 15,10 , 20 ] 
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0)    # error   
#print({10 , 20 , 15} * 2)       # error
#print({10 : 20 , 30 : 40} * 2)   # error
#print([10] * [20])                # error