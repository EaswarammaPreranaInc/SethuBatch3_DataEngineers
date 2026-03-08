 
# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') #True
print('iniv'   not   in   'Srinivas') # False


'''
1) What  does  in  and  not  in  operators  do ?  --->  Searches  for  a  string  in  another  string

2) What  does  str1  in  str2  do ? --->  Returns  True  if  str1  is  in  str2  and  False  otherwise

3) What  does  str1  not  in  str2  do ? --->  Returns  True  if  str1  is  not  in  str2  and  False  otherwise

4) not  in  operator  is  quite  opposite  to  in  operator
'''
 '''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) # Rm a
print(a [ : 7]) #Rama Ra
print(a [2 : 4]) # ma
print(a [2 : ]) # ma Rao
print(a [ : 4 ]) #Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) #ma Ra
print(a [-6 : ]) #ma Rao
print(a [: -4 : -1]) # ''
print(a [-3 : -1]) # Ra
print(a [-3 : ]) #Rao 
print(a [ : : ]) # Rama Rao
print(a [ : ]) # Rama Rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a mR
print(a [2 : 8]) #ma Rao
print(a [2 : 8 : -1]) #''
print(a [ : -6 : -1])#''
print(a [2 : -3]) #ma  
print(a [1 : 6 : 2])# aaR
print(a [ : -5 : -5])#''
print(a [2 : -5])#m
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#''
print(a [-5 : 0 : -2])#aa

 '''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
try:
	s=''
	s1=input('Enter first string')
	s2=input('Enter second string')
	print(F'Result : {s2[:2]+s1[2:]} {s1[:2]+s2[2:] }')
except:
	print('Error occured')
	

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''

try:
	s=''
	s1=input('Enter any string')
	if(len(s1)<4):
		print('Nothing')
	else:
		print(s1[:2]+s1[-2:])
except:
	print('Error occured')


	
 '''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
Character  at  index  1  : A
Character  at  index  2  :  M
 Character  at  index  3  :  S
Character  at  index  4  :  I
Character  at  index  -1  :  I
 Character  at  index  -2  :  S
Character  at  index  -3  :  M
Character  at  index  -4  :  A

try:
	s=input('Enter any string')
	for i in range(len(s)):
		print(F'Character  at  index  {i}  : {s[i]}')
	for i in range(1,len(s)+1):
		print(F'Character  at  index  {-i}  : {s[-i]}')

except:
	print('Error')	

						
'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  ---> Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->  Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''


try:
	s=input('Enter any string')
	odd=''
	even=''
	for i in range(len(s)):
		if(i%2):
			odd+=s[i]
		else:
			even+=s[i]
	print(F'string at even indexes : {even}')
	print(F'string at odd indexes : {odd}')
except:
	print('Error')
'''
Let  input  be    A   4   B   3   C   2   $   5
                         0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
    0         'A'          '4'			   '' + 'A' * 4 = 'AAAA'
	2         'B'          '3'             'AAAA' +  'B' * 3  = 'AAAABBB' 
	4         'C'          '2'             'AAAABBB' +  'C' * 2  = 'AAAABBBCC' 
	6         '$'          '5'             'AAAABBBCC' +  '$' * 5  = 'AAAABBBCC$$$$$' 
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->  a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''
try:
	s=input('Enter string with alternative character and number')
	res=''
	for i in range(0, len(s), 2):
		res+=eval(s[i+1])*s[i]
	print(res)	
except:
	print('Enter valid string')


'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  ---> HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0       'H'        'V'         '' + 'H' + 'V = 'HV'									
1       'Y'        'A'         'HV' + 'Y' + 'A = 'HVYA'									
2       'D'        'M'        'HVYA' + 'D' + 'M = 'HVYADM'									
--------------------------------------------------------

Concatenate  remainging  characters   of  the  other  string  to  object  'c'
What  is  the  final  result ?  --->  'HVYADMSI'

Hint:  Use  single  while  loop  and  slice
'''
s1=input('Enter first string')
s2=input('Enter first string')
res=''
l=0
if(len(s1) <len(s2)):
	l=len(s1)
	extra = s2[l:]
else:
	l=len(s2)
	extra = s1[l:]
for i in range(0, l):
	res+=s1[i]+s2[i]
print(res+extra)

 '''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator
'''

try:
	s=input('Enter a string')
	res=''
	for i in s:
		if(i not in res):
			res+=i
	print(res)
except:
	print('enter valid input')


 # len()  function  demo  program  (Home  work)
print(len('Hyd'))  #3
print(len('Rama Rao')) #8
print(len('9247'))# 4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
print(len(3456))#Error
print('Sec'. len())#Error


'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''
# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) # ' '


'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) #122
print(ord('0')) # 48
print(ord('9')) #57
print(ord('$')) # 36
print(ord(' ')) # 32


'''
ord()  function
------------------
1) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

2) How  many  unicode  values  exist ?  --->  512

3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

4) What  are  the  unicode  values  of  'A'  -  'Z' ?  --->  65  to  90
     What  are  the  unicode  values  of  'a'  -  'z' ?  --->  97  to  122
     What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

Note:  chr()  and  ord()  are  quite  opposite  functions
'''
 '''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


    i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                           ''
   0        'A'        '4'             '' + 'A' +  'E' = 'AE'
   2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
   4        'Z'        '5'             'AEMP' + 'Z' +  '' = 'AEMPZ'
   6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'															 
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''
a=input()
s=''
for i in range(0,len(a), 2):
	s+=a[i]+chr(ord(a[i])+eval(a[i+1]))
print(s)


 '''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

 '''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index >= 0:
	print(index)
	index = a . find('is' , index + 1)
print('End')

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  (index :=a . find('is' , index + 1)) >= 0:
	print(index)
print('End')

'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''

 '''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
	index = a .rfind('is')
	while  index >= 0:
		print(index)
		index = a . rfind('is' ,0, index)
	print('End')
except:
	print('End')

'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(…

 '''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
	index = a .rindex('is')
	while  index >= 0:
		print(index)
		index = a . rindex('is' ,0, index)
	print('End')
except:
	print('End')
	
'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''

#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #3
print(a . count('is' , 19 , 48)) # 2
print(a . count('was')) #0
'''

count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
																	Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1
'''
 #  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3
