# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city')  # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False

'''Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm a
print(a [ : 7]) # Rama Ra
print(a [2 : 4]) # ma
print(a [2 : ]) # ma Rao
print(a [ : 4 ]) # Rama 
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # ma Ra
print(a [-6 : ]) # ma Rao
print(a [: -4 : -1]) # oaR
print(a [-3 : -1]) # Ra
print(a [-3 : ]) # Rao
print(a [ : : ]) # rama Rao
print(a [ : ]) # Rama Rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a mR
print(a [2 : 8]) # ma Rao
print(a [2 : 8 : -1]) # empty string
print(a [ : -6 : -1]) # oaR a
print(a [2 : -3]) # ma 
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5]) # o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) # aa

'''Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string has a min of two chrs'''
s1=input()
s2=input()
if len(s1)>2 and len(s2):
 a=s1.replace(s1[:2],s2[:2])
 b=s2.replace(s2[:2],s1[:2])
 r=a +' '+ b
 print(r)
else:
 print("string lengths should be atlest 3")

'''Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters
'''
s=input()
if len(s)>3:
 n=s[:2]+s[-2::]
 print(n)
else:
 print()

 # Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice
 s=input()
 print("String from left to right : ")
 for i in range(len(s)):
  print(f'Character at index {i} : {s[i]}')
 print("String from right to left : ")
 for i in range(1,len(s)+1):
  print(f'Character at index {-i} : {s[-i]}')

# Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice
s=input()
e=''
o=''
for i in range(len(s)):
 if i%2==0:
  e+=s[i]
 else:
  o+=s[i]
print("String at even indexes :", e)
print("String at odd indexes :", o)

# Let  input  be    A   4   B   3   C   2   $   5
#0   1    2   3   4   5   6   7
s=input()
out=''
for i in range(0,len(s),2):
 if not s[i+1].isdigit() or s[i].isdigit:
  print("String should be alternate string and number")
else:
  out+=s[i]*int(s[i+1])
print(out)

# Write  a  program  to  merge  two  strings  to  form  a  new  string
s1=input()
s2=input()
s3=''
i=0
if len(s1)<=len(s2):
 while i<len(s1):
  s3+=s1[i]+s2[i]
s3+=s2[len(s1):]
print(s3)

# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set
s=input()
j=''
for ch in s:
 if ch not in j:
  j+=ch
print("without duplicates : ",j)

# len()  function  demo  program  (Home  work)
print(len('Hyd'))  # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) # 1
print(len('A2#')) # 3
print(len(3456)) # error 
print('Sec'. len()) # Error

# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) #  

# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32

'''Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF'''
s=input()
n=''
for i in range(0,len(s),2):
  n+=s[i]+chr(ord(s[i])+int(s[i+1]))
  break
else:
  print("Input shoild alternate aplpha and digit")
print(n)

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
while  index:=a.find('is') != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) # 0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3

 
 


 
  
  




 



 
 


