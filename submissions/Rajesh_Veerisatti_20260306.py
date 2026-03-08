

# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  twocharacters  of  the  two  strings.Assume  that  each  string  has  a   minimum  of  two  characters

a=input("Enter 1st  string: ")
b=input("Enter 2nd string: ")

if len(a)<=2 and len(b)<=2:
    print("Strings should be minumum of two charecters")
else:
	c=b[:2]+a[-2:]
	d=a[:2]+b[2:]
	print("Result: ",c +" "+ d)
	
#Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  stringPrint  an  empty  string  if  string  has  less  than  four  characters

a = input("Enter a string: ")
if len(a)<=3:
      print("result: ")
      
else:
      print("result: ",a[:2]+a[-2:])

# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

a=input("Enter astring: ")
print("string from left to right:")
for i in range(0,len(a)):
		
    print(f"Character at index {i}: {a[i]}")
print("string from  right to left:")      
for i in range(-1,-len(a)-1,-1):
    	
    print(f"Character at index {i}: {a[i]}")
    


# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

a= input("Enter a string: ")
b=""
c=""
for i in range(len(a)):
    if i%2==0:
        b+=a[i]
    else:
        c+=a[i]      
	 
print("sting at even index: ",b)
print("sting at odd index: ",c)



# Let  input  be    A   4   B   3   C   2   $   5
try:
	a=input("Enter string with alternate character dight: ")
	d=""
	for i in range(0,len(a),2):
		b=a[i]
		
		c=eval(a[i+1])
		d+=b*c
		
	print(d)	

except TypeError,NameError:
	print("string should have alternate character and dight")
    


# Write  a  program  to  merge  two  strings  to  form  a  new  string

a=input("Enter 1st string: ")

b=input("Enter 2nd string: ")
i=0
c=""
while i < len(a) and i<len(b) :
    c+= a[i]+b[i]
    i+=1
    
c+=a[i:]+b[i:]
print(c)


#  Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  se  
a=input("Enter a string: ")
b=""

for i in range(len(a)):
	if a[i] not in b:
		b+=a[i]
print(b)


#Let  input  be  A4M3Z5D2 What  is  the  output ?  --->  AEMPZ_DF
try:
	a=input("Enter string with alternate character dight: ")
	e=""
	for i in range(0,len(a),2):
		b=a[i]
		
		c=eval(a[i+1])
		d=ord(b)+c
		e+=b+chr(d)
		
	print(e)	

except TypeError,NameError:
	print("string should have alternate character and dight")
    



# Modify  following  program  with  walrus  operator  

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

i=-1
while (i := a.find('is', i+1 )) !=-1:
    print(i)

print('End')


# Modify  following  program  with  index method  

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
	i=0
	while (i := a.index('is', i+1 )) !=-1:
		print(i)
except ValueError:
	print('End')
    

# Modify  following  program  with  rfind method  

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

i=len(a)
while (i := a.rfind('is',0,i)) !=-1:
    print(i)

print('End')



# Modify  following  program  with  rindex method  
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

	i=len(a)
	while (i := a.rindex('is',0,i)) !=-1:
		print(i)
except ValueError:
	print('End')
    

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) # 0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3


# ord()  function  demo  program
print(ord('A')) #65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32


# len()  function  demo  program  (Home  work)
print(len('Hyd'))   # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) # 1
print(len('A2#')) # 3
# print(len(3456))
# print('Sec'. len())



# outputs
a = 'Rama Rao'
print(a [ : 7 : 2]) #  a[0 : 7 : 2]  
print(a [ : 7]) #  a[0 : 7 : 1]  
print(a [2 : 4]) #  a[2 : 4 : 1]  
print(a [2 : ])  #  a[2 : 8 : 2]  
print(a [ : 4 ]) #  a[0 : 4 : 1]  
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) #  a[-6 : -1 : 1]  
print(a [-6 : ]) #  a[-6 : 8 : 1]  
print(a [: -4 : -1]) #  a[-1 : -4 : -1]  
print(a [-3 : -1]) #  a[-3 : -1 : 1]  
print(a [-3 : ]) #  a[-3 : 8 : 1]  
print(a [ : : ]) #  a[0 : 8 : 1]  
print(a [ : ]) #  a[0 : 8 : 1]  
print(a [ : : -1]) #  a[-1 : -9 : -1]  
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) #  a[-2 : 8 : -2]  
print(a [2 : 8]) #  a[2 : 8 : 1]  
print(a [2 : 8 : -1]) #  a[2 : 8 : -1]  
print(a [ : -6 : -1]) #  a[-1 : -6 : -1]  
print(a [2 : -3]) #  a[2 : -3 : 1]  
print(a [1 : 6 : 2]) #  a[1 : 6 : 2]  
print(a [ : -5 : -5]) #  a[-1 : -5 : -5]  
print(a [2 : -5])  #  a[2 : -5 : 1]
print(a [2 : -5 : 2])  #  a[2 : -5 : 2]
print(a [ : 0 : -1])  #  a[-1 : 0 : -1]
print(a [-5 : 0 : -2])  #  a[-5 : 0 : -2]


# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True 
print('iniv'   not   in   'Srinivas') # False
