#----- Find Outputs -----

a = 25
print(id(a))  # 3000 address of object a
a = 35
print(id(a))   # 4000 address of new object a


#----- Find Outputs -----

a = 25.7
print(id(a))  #2000 address of object 25.7
print(a)      # 25.7
a = 35.6      
print(id(a))  # 2500 
print(a)      # 35.6
b = True
print(id(b))  # 3000
b = False
print(id(b))  # 3500
c = None
print(id(c))  #4000 
c = None
print(id(c))  # 4000 same address of object c


#----- Find Outputs -----

a = 'Hyd'
print(id(a))              # 2000 
#a[1] = 'e'                  # error 
a = 'Sec'                 
print(id(a))              # 3000 
b = (10 , 20 , 15 , 18)   
print(id(b))               #4000
b[2] = 19                    # (10, 20, 19, 18)
b = (30 , 40 , 35 , 32)
print(id(b))               #5000
c = range(5)
print(id(c))              # 6000
#c[3] = 10             # Error because range does not support item assignment
c = range(5)
print(id(c))            # 7001


#----- Find Outputs -----

a = 25                
b = 25
print(a  is  b)   #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)   #True
e = False
f = False
print(e  is  f)   #True
g = range(10)
h = range(10)
print(g  is  h)   #False  because it creates a new range object every time


#----- Find Outputs -----

a = [10 , 20 , 15 , 18]  
b = [10 , 20 , 15 , 18]
print(a  is  b)              # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)               # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)            #True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)             # False


#----- Find Outputs -----

print(10 + 20)                  #30
print(10.8 + 20.6)              #31.40
print(3 + 4j + 5 + 6j)            #8+10j
print(True + False)               #1+0= 1
print('Hyder' + 'abad')               #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')   #SankarDayalSarma
print('10' + '20')                    #30
print([10 , 20 , 30] + [1 , 2 , 3])     #([10 , 20 , 30, 1 , 2 , 3 )
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   # (25 , 10.8 , 'Hyd', 3 + 4j , True , None)
#print({10 , 20} + {30 , 40})             #error set
#print({10 : 'Hyd'} + {20 : 'Sec'})       #error dict
#print(range(4) + range(5))               #error range
#print(10 + '20')                           #error  it has both int and str
#print([10 , 20 , 30] + 5)                 # error list and int
#print([10 , 20 , 30] + (40 , 50 , 60))      #error list and tuple


#----- Find Outputs -----
 
print(25 * 3)                  # 75
print(10.8 * 25.6)             #276.48
print(True * False)            #0
print((3 + 4j) * (5 + 6j))    # (-9+38j)
print(3 + 4j * 5 + 6j)        # (3+26j)
print('25' * 3)                #252525
print(3 * '25')                #252525
print('Hyd' * 4)                 #HydHydHydHyd
print([10 , 20 , 15] * 2) # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0) # Error because list cannot be multiplied by float
#print({10 , 20 , 15} * 2) # Error because set does not support multiplication
#print({10 : 20 , 30 : 40} * 2) # Error because dictionary does not support multiplication
#print([10] * [20]) # Error because list cannot be multiplied by list


