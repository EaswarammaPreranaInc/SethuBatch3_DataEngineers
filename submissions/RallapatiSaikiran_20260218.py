#  Find  outputs
a = 25
print(id(a))
a = 35
print(id(a))


# Find  outputs (Home  work)
a = 25.7
print(id(a))  # Address of Object a
print(a)      #25.7
a = 35.6      
print(id(a))   #Address of new object a
print(a)       #35.6
b = True       
print(id(b))   #Address of object b
b = False      
print(id(b))   #Address of new object b
c = None
print(id(c))   #Address of object c
c = None
print(id(c))   # Address of new object c



#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a))     # Address of object a
a[1] = 'e'       # Error
a = 'Sec'       
print(id(a))     # Address of object a
b = (10 , 20 , 15 , 18)
print(id(b))     # Address of object b
b[2] = 19        # Error
b = (30 , 40 , 35 , 32)
print(id(b))     #Address of object b
c = range(5)     # c(0,5,1)
print(id(c))     # Address of object c
c[3] = 10        #Error
c = range(5)     #(0,1,2,3,4)
print(id(c))     # Address of object c




# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)   # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)    # True
e = False
f = False
print(e  is  f)    # True
g = range(10)
h = range(10)
print(g  is  h)    # False




#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)           # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)          # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)          # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)          # False





# Find outputs (Home work)
print(10 + 20)       # 30
print(10.8 + 20.6)   # 31.4
print(3 + 4j + 5 + 6j)  # 8+10j
print(True + False)     # 1
print('Hyder' + 'abad')  # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')  # SankarDayalSarma
print('10' + '20')   #1020
print([10 , 20 , 30] + [1 , 2 , 3])  # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))   # (25,10.8,'Hyd',3+4j,True,None)
print({10 , 20} + {30 , 40})   # {10,20,30,40}
print({10 : 'Hyd'} + {20 : 'Sec'})  # {10: 'Hyd', 20: 'Sec'}
print(range(4) + range(5))    # Range(9)
print(10 + '20')    #Error
print([10 , 20 , 30] + 5)    # Error
print([10 , 20 , 30] + (40 , 50 , 60))    # Error







# Find outputs (Home work)
print(25 * 3)          #75
print(10.8 * 25.6)     # 276.48
print(True * False)    #1
print((3 + 4j) * (5 + 6j)) # 15+62j
print(3 + 4j * 5 + 6j)    # 8+10j
print('25' * 3)      #252525
print(3 * '25')      #252525
print('Hyd' * 4)     #'HydHydHydHyd'
print([10 , 20 , 15] * 2)    # [10,20,30,10,20,30]
print((25, 10.8, 'Hyd', True) * 3) (25,10.8,'Hyd',True)
print([10 , 20 , 15] * 3.0)# Error
print({10 , 20 , 15} * 2) # Error
print({10 : 20 , 30 : 40} * 2) # Error
print([10] * [20]) # Error









