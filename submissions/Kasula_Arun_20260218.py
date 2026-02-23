#  Find  outputs
a = 25
print(id(a))       #address of int object 25
a = 35
print(id(a))       #address of int obj 35 



# Find  outputs (Home  work)
a = 25.7
print(id(a))      #address of float obj 25.7
print(a)          #25.7
a = 35.6
print(id(a))      #address of float obj 35.6
print(a)          #35.6
b = True
print(id(b))    #address of bool obj True
b = False
print(id(b))     #address of bool obj False
c = None
print(id(c))     #address of None type obj None
c = None
print(id(c))     #same address like the above




#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))         #address of str obj 'Hyd'
a[1] = 'e'   
a = 'Sec'            
print(id(a))         #address of str obj 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b))         #address of tuple b
b[2] = 19            #error due to no modification
b = (30 , 40 , 35 , 32) 
print(id(b))         #different address of tuple b
c = range(5)
print(id(c))         #address of range obj c
c[3] = 10            #error due to range is immutable 
c = range(5)
print(id(c))         #different address of range obj c




# Find  outputs  (Home  work)
a = 25
b = 25                               
print(a  is  b)                #True           
c = 'Hyd'
d = 'Hyd'
print(c  is  d)                #True
e = False
f = False
print(e  is  f)                #True
g = range(10)
h = range(10)
print(g  is  h)                #False



#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)                       #False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)                       #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)                       #True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)                        #Frue




# Find outputs (Home work)
print(10 + 20)          #30 
print(10.8 + 20.6)      #31.40
print(3 + 4j + 5 + 6j)   #(8+10j)
print(True + False)      #1
print('Hyder' + 'abad')  #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')     #SankarDayalSarma
print('10' + '20')                   #1020
print([10 , 20 , 30] + [1 , 2 , 3])    #[10 , 20 , 30, 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd', 3 + 4j , True , None)
print({10 , 20} + {30 , 40})        #error + operation is not done on set and set
print({10 : 'Hyd'} + {20 : 'Sec'})  #error + operation is not done on dict and dict
print(range(4) + range(5))          #error + operation is not done on range and range
print(10 + '20')                    #error + operation is not done on int and str
print([10 , 20 , 30] + 5)           #error no concatenation is done
print([10 , 20 , 30] + (40 , 50 , 60))  #error tuple is not concatenated




# Find outputs (Home work)
print(25 * 3)              #75                   
print(10.8 * 25.6)         #276.48
print(True * False)          #0
print((3 + 4j) * (5 + 6j))    #(-9 +38j)
print(3 + 4j * 5 + 6j)       #(3+ 26j)
print('25' * 3)              #252525
print(3 * '25')              #252525
print('Hyd' * 4)             #HydHydHydHyd
print([10 , 20 , 15] * 2)     #[10 , 20 , 15, 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)     # error due to second operator should be int 
print({10 , 20 , 15} * 2)       #error multiple set and int
print({10 : 20 , 30 : 40} * 2)    #error multiple dict and int
print([10] * [20])               # #error multiple list and non-int