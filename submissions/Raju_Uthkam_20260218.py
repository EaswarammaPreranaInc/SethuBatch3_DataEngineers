#  Find  outputs
a = 25
print(id(a)) #Address of object 25
a = 35
print(id(a)) #Address of object 35

# Find  outputs (Home  work)
a = 25.7
print(id(a)) #Address of object 25.7
print(a) #25.7
a = 35.6
print(id(a)) #Address of object 35.6
print(a) #35.6
b = True
print(id(b)) #Address of object True
b = False
print(id(b)) #Address of object False
c = None
print(id(c)) #Address of object None 
c = None
print(id(c)) #same Address because there is no change in refrence and object 


#  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #Address of object 'Hyd'
#a[1] = 'e'  #string is immutable #Error 
a = 'Sec'
print(id(a)) #Address of object 'Sec'
b = (10 , 20 , 15 , 18)
print(id(b)) #Address of object with 4 elements 
#b[2] = 19 #tuple is immutable 
b = (30 , 40 , 35 , 32)
print(id(b)) #Address of object with 4 elements 
c = range(5) #0 1 2 3 4 
print(id(c)) #Address of range object 
#c[3] = 10 #range is immutable 
c = range(5)
print(id(c)) #Address of range object 


# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) #True
e = False
f = False
print(e  is  f) #True
g = range(10) #range(0,10) 
h = range(10) #range(0,10)
print(g  is  h) #True


#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) #False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) #False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) #False
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) #False


# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) #1
print('Hyder' + 'abad') #Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3]) #[10,20,30,1,2,3] #list concatenation
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25,10.8,'Hyd',3+4j,True,None)
#print({10 , 20} + {30 , 40}) #Error  We can't add set +set
#print({10 : 'Hyd'} + {20 : 'Sec'}) #Error We can't add dict + dict
#print(range(4) + range(5)) #Error wwe can't add range +range
#print(10 + '20') #Error we can't add integer with string 
#print([10 , 20 , 30] + 5) #we can't add squence with non squence 
#print([10 , 20 , 30] + (40 , 50 , 60)) #Error we can only concatenate with list to list but not tuple 


# Find outputs (Home work)
print(25 * 3) #75
print(10.8 * 25.6) #276.48
print(True * False) #0
print((3 + 4j) * (5 + 6j)) #-9+38j
print(3 + 4j * 5 + 6j) #3+26j
print('25' * 3) #252525
print(3 * '25') #252525
print('Hyd' * 4) #HydHydHydHyd
print([10 , 20 , 15] * 2) #[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) #(25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True) 
#print([10 , 20 , 15] * 3.0) #can't multiply sequence with non int
#print({10 , 20 , 15} * 2) #Error #can't multiply sequence with non int
#print({10 : 20 , 30 : 40} * 2) #Error 
#print([10] * [20]) #Error


