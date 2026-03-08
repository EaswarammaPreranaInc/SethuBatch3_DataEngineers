# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False

'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm<space>a
print(a [ : 7]) # Rama<space>Ra
print(a [2 : 4]) # ma
print(a [2 : ]) # ma>space>Rao
print(a [ : 4 ]) # Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # maR
print(a [-6 : ]) # ma<space>Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) # []
print(a [-3 : ]) # Rao
print(a [ : : ]) # Rama<space>Rao
print(a [ : ]) # Rama<space>Rao
print(a [ : : -1]) # oaR<space>amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a<space>aR
print(a [2 : 8]) #m<space>a
print(a [2 : 8 : -1]) # []
print(a [ : -6 : -1]) # oaR<space>a
print(a [2 : -3]) # ma<space>R
print(a [1 : 6 : 2]) # ama<space>R
print(a [ : -5 : -5]) # o
print(a [2 : -5]) # ma
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # []
print(a [-5 : 0 : -2]) # aa

# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two characters  of  the  two  strings.

a = input("Enter second string :")
b = input("Enter second string :")
newa = b[:2]+a[2:]
newb = a[:2]+a[2:]
print("Result : "newa, newb)

# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string Print  an  empty  string  if  string  has  less  than  four  characters

a = input("Enter a string : ")
if len(a)<4:
	print("")
else:
	print("Result : "a[:2]+a[-2:])

# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

str = input("Enter the string : ")
print("String from left to right :")
for ch in range(len(str)):
	print(F"Character at index {ch} : {str[ch]}")
print("String from right to left :")
for ch in range(-1,-(len(str)+1),-1):
	print(F"Character at index {ch} : {str[ch]}")

# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

str = input("Enter any string : ")
even = ""
odd = ""
for i in range(len(str)):
	if i%2==0:
		even += str[i]
	else:
		odd += str[i]
print("String at even indexes : ",even)
print("String at odd indexes : ",odd)

#Let  input  be  A4M3Z5D2 What  is  the  output ?  --->  AEMPZ_DF

str = input("Enter any string with alternate character and digit : ")
out = ""
for i in range(0,len(str),2):
	ch = str[i]
	num = int(str[i+1])
	newch = chr(ord(ch)+num)
	if newch > 'Z':
		out += ch + " "
	else:
		out += ch + newch
print("Result : ",out)

# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

# len()  function  demo  program  (Home  work)
print(len('Hyd'))  # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 4
print(len('')) # empty
print(len(' ')) # 1
print(len('A2#')) # 3
print(len(3456)) # error
print('Sec'. len()) # error

# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) # ' '

# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) #122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32

# Modify  following  program  with  walrus  operator
	
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

# (Home  work) index()  method  demo  program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

# (Home  work) rfind()  method  demo  program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , index + 1)
print('End')

#(Home  work) rindex()   method  demo  program

try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
	rindex = a . find('is')
	while  rindex != -1:
		print(rindex)
		rindex = a . find('is' , rindex + 1)
	print('End')
except:
	print("String not found")

#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 3
print(a . count('is' , 19 , 48)) # 2
print(a . count('was')) # 0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3
