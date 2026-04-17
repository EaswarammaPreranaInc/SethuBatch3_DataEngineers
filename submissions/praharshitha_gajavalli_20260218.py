1) How  many  objects  are  non-sequences  and  what  are  they ?  --->  5  i.e. int , float , complex , bool , NoneType
    How  many  objects  are  sequences  and  what  are  they ?  --->   6
		  i.e. str , range , list , tuple , set  and  dict

2) What  is  difference  between  sequence  and  non-sequence ?  --->  Sequence  is  a  group  of  elements
										  and  
									non-sequence  is  a  single  element

3) Which  sequences  are  homogeneous  (Total : 2) ?  ---> str  and  range
   Which  sequences  are  heterogeneous  (Total : 4) ?  ---> list , tuple , set  and  dict

4) Which  sequences  can  not  hold  duplicates (Total : 3) ?  --->  dict , set  and  range

5) Which  sequence…
#  Find  outputs
a = 25
print(id(a)) # address of obj a
a = 35
print(id(a)) # address of obj a

# Find  outputs (Home  work)
a = 25.7
print(id(a)) # address of obj a
print(a) # 25.7
a = 35.6
print(id(a)) # address of obj a
print(a) # 35.6
b = True
print(id(b)) # address of obj b
b = False
print(id(b)) # address of obj b
c = None
print(id(c)) # address of obj c
c = None
print(id(c)) # same address 

#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) # address of obj a
a[1] = 'e' # error
a = 'Sec'
print(id(a))  # address of obj 'sec'
b = (10 , 20 , 15 , 18)
print(id(b)) # address of obj b
print(id(a)) # same address as obj 'Sec'
a[1] = 'e' # error
b[2] = 19  # error as tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) # address of obj b
c = range(5)
print(id(c)) #  address of obj c
c[3] = 10    # error
c = range(5) 
print(id(c)) # same address as obj c


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)
c = 'Hyd'
d = 'Hyd'
print(c  is  d)
e = False
f = False
print(e  is  f)
g = range(10)
h = range(10)
print(g  is  h)

#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)

# Find outputs (Home work)
print(10 + 20)  # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j)  # 8+10j
print(True + False) # 1
print('Hyder' + 'abad')  # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  #(25,10.8,'Hyd',3+4j,True,None)
print({10 , 20} + {30 , 40})  # error
print({10 : 'Hyd'} + {20 : 'Sec'})  # error
print(range(4) + range(5)) # error
print(10 + '20') # error
print([10 , 20 , 30] + 5)  # error
print([10 , 20 , 30] + (40 , 50 , 60)) # error

# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 36.4
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # (-9+38j)
print(3 + 4j * 5 + 6j) # error
print('25' * 3) #252525
print(3 * '25') # 252525
print('Hyd' * 4)# HydHydHydHyd
print([10 , 20 , 15] * 2) # [10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) # error as seq*int only
print({10 , 20 , 15} * 2)  # error as set is not repeated
print({10 : 20 , 30 : 40} * 2)  # error as set doesn't have duplicates
print([10] * [20]) # error as seq*int only