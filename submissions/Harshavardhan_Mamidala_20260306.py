 Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False


'''  (Home  work)
Slice  demo  program
0      1       2       3      4       5      6       7
R      a      m        a              R      a       o
-8    -7     -6       -5     -4      -3     -2      -1
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
print(a [ : : ]) # Rama Rao
print(a [ : ]) # Rama Rao
print(a [ : : -1]) # oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) # a mR
print(a [2 : 8]) # ma Rao
print(a [2 : 8 : -1]) # ''
print(a [ : -6 : -1]) # oaR a
print(a [2 : -3]) # ma 
print(a [1 : 6 : 2]) # aaR
print(a [ : -5 : -5]) # o
print(a [2 : -5]) # m
print(a [2 : -5 : 2]) # m
print(a [ : 0 : -1]) # oaR ama
print(a [-5 : 0 : -2]) # aa



Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Hint:  Use  slice

s=input('Enter 1st: ')
t=input('Enter 2nd: ')
try:
    if len(s)>2 and len(t)>2:
        print(t[:2]+s[2:]+' '+s[:2]+t[2:])
except:
    print('give atleast minimum 2 characters')

output:
Enter 1st: JAVA
Enter 2nd: PYTHON
PYVA JATHON


Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

s=input('Enter any string: ')
if len(s)>4:
    print('Result: ',s[:2]+s[len(s)-2:])
else:
    print('Result: ')

output:
Enter any string: PYTHON
Result:  PYON

Enter any string: HYD
Result: 



Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

s=input('Enter the string: ')
print('Starting from left to right')
for i in range(len(s)):
    print(f'Character at index {i}: ',s[i])
print('Starting from right to left')
for i in range(1,len(s)+1):
    print(f'Character at index {-i}: ',s[-i])

output:
Enter the string: vamsi
Starting from left to right
Character at index 0:  v
Character at index 1:  a
Character at index 2:  m
Character at index 3:  s
Character at index 4:  i
Starting from right to left
Character at index -1:  i
Character at index -2:  s
Character at index -3:  m
Character at index -4:  a
Character at index -5:  v



Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

s=input('Enter any string: ')
even=""
odd="" 
for i in range(len(s)):
    if i%2==0:
        even=even+s[i]
    else:
        odd=odd+s[i]
print('String at even indexes: ',even)
print('String at odd indexes: ',odd)

output:
Enter any string: RAMA RAO
String at even indexes:  RM A
String at odd indexes:  AARO



Let  input  be    A   4   B   3   C   2   $   5
                  0   1   2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                           ''
    0         'A'          '4'		   '' + 'A' * 4 = 'AAAA'
    2         'B'          '3'             'AAAA' +  'B' * 3  = 'AAAABBB' 
    4         'C'          '2'             'AAAABBB' +  'C' * 2  = 'AAAABBBCC' 
    6         '$'          '5'             'AAAABBBCC' +  '$' * 5  = 'AAAABBBCC$$$$$' 
   -------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->  a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''

s=input('Enter any string with alternate character and digit: ')
res=""
try:
    for i in range(len(s)):
        if i%2==0:
            res=res+s[i]*(int(s[i+1]))
    print(res)
except:
    print('String should have alternate character and digit')

output:
Enter any string with alternate character and digit: A4B3C2$5
AAAABBBCC$$$$$

Enter any string with alternate character and digit: hyd
String should have alternate character and digit



Write  a  program  to  merge  two  strings  to  form  a  new  string

Hint:  Use  single  while  loop  and  slice

s=input('Enter 1st string: ')
t=input('Enter 2nd string: ')
i=0
res=""
small=min(len(s),len(t))
while(i<small):
    res=res+(s[i]+t[i])
    i=i+1
if (len(s)<len(t)):
    res=res+t[len(t)-len(s)+1:]
else:
    res=res+s[len(s)-len(t)+1:]
print(res)

output:
Enter 1st string: VAMSI
Enter 2nd string: HYD
VHAYMDSI


Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

s=input('Enter any string: ')
res=""
for x in s:
    if x not in res:
        res=res+x 
print('String without duplicates: ',res)

output:
Enter any string: MISSISIPI
String without duplicates:  MISP


# len()  function  demo  program  (Home  work)
print(len('Hyd'))  # 3 
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('+-$')) # 3
print(len('')) # 0
print(len(' ')) # 1
print(len('A2#')) # 3
print(len(3456)) # error because it should sequence
print('Sec'. len()) # error no arg for len

# chr()  function  demo  program
print(chr(65))  # A
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


'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0    1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


    i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                           ''
   0        'A'        '4'             '' + 'A' +  'E' = 'AE'
   2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
   4        'Z'        '5'             'AEMP' + 'Z' +  '_' = 'AEMPZ_'
   6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'															 
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''

try:
    s=input('Enter any string with alternate character and digit: ')
    res=""
    for i in range(len(s)):
        if i%2==0:
            res=res+s[i]+chr(ord(s[i])+int(s[i+1]))
    print(res)
except:
    print('pls enter string with alternate char and digit')

output:

Enter any string with alternate character and digit: A4M3Z5D2
AEMPZ_DF

Enter any string with alternate character and digit: HYD
pls enter string with alternate char and digit


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


'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
	index = a . find('is')
        while  True:
	print(index)
	index = a . find('is' , index + 1)
except:
    print('End')


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' ,0, index + 1)
print('End')





'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a . rindex('is')
    while  True:
	print(index)
	index = a . rindex('is' ,0, index + 1)
	
except:
    print('End')




a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #3
print(a . count('was')) #0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3
