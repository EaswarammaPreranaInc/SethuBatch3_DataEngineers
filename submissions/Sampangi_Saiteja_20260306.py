 # Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')#True
print('day'   in   'Sankar  dayal  sarma')#False
print('Green'   in   'Hyd  is  green  city')#True
print('d  is'   in   'Hyd  is  green  city')#True
print('dis'   in   'Hyd  is  green  city')#False
print('iniv'   in   'Srinivas')#True
print('iniv'   not   in   'Srinivas')#False
--------------------------------------------------------------------------------------------------
'''
 #(Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''

a = 'Rama Rao'
print(a [ : 7 : 2])#-->[0:7:2]Rm<space>a
print(a [ : 7])#-->[0:7:1]Rama<space>Ra
print(a [2 : 4])#-->[2:4:1]ma
print(a [2 : ])#-->[2:7:1]ma<space> ra
print(a [ : 4 ])#-->[0:4:1]Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
-print(a [-6 : -1])#-->[-6:-1]ma  Rao
-print(a [-6 : ])#-->[0:-6:1]ma Rao
print(a [: -4 : -1])#[-1:-4:-1]oaR
print(a [-3 : -1])#[-1:-3:-1]Ra
print(a [-3 : ])#[0:-3:1]Rama<space>
print(a [ : : ])#Rama Raw 
print(a [ : ])#Rama Raw 
print(a [ : : -1])#[-1:-9:-1]oaR<space>amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) #[-2:-9:-2]aR<space>mR
print(a [2 : 8])#[0:2:8]a<space>Rao
print(a [2 : 8 : -1])#ma
print(a [ : -6 : -1])#
print(a [2 : -3])#o<space>
print(a [1 : 6 : 2])#aaR a
print(a [ : -5 : -5])#o
print(a [2 : -5])#-->[1:2:-5]#M
print(a [2 : -5 : 2])#m
print(a [ : 0 : -1])#oaR ama
print(a [-5 : 0 : -2])#aa

----------------------------------------------------------------------------------------------------
#Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
code:
x=(input("Enter the input string 1 : "))
y=(input("Enter the input string 2 : "))
str1=x[:2]+y[2:]
str2=y[:2]+x[2:]
print(f"Result = {str1} {str2}")


--------------------------------------------------------------------------------------------------



#Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing

code:

str1=input("Enter the String : ")
if len(str1)<4:
    print(f"Result = {""}")
else:
    print(f"Result = {str1[:2]+str1[-2:]}")



--------------------------------------------------------------------------
# Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	                  0      1     2      3     4
Let  input  be		  V      A     M      S     I
			 -5     -4    -3     -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
                                 Character  at  index  1  :  A
				 Character  at  index  2  :  M
                                 Character  at  index  3  :  S
				 Character  at  index  4  :  I
                                 Character  at  index  -1  :  I
			         Character  at  index  -2  :  S
                                 Character  at  index  -3  :  M
                                 Character  at  index  -4  :  A

code:

x=input("Enter the String : ")
for i in range(0,len(x)):
    print(f"Character at index {i} = {x[i]}")
for j in range(-1,-len(x)-1,-1):
    print(f"Character at index {j} = {x[j]}")
    



-------------------------------------------------------------------------------------------
#Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  ---> Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->  Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''

Code:
x=input("Enter a string : ")
odd=""
even=""
for i in range(len(x)):
    if i%2==0:
        even = even+x[i]
    else:
        odd = odd+x[i]
print(f"String at Even indexes : {even.upper()}")
print(f"String at Odd indexes : {odd.upper()}")





---------------------------------------------------------------------------------------------












#Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator
'''

code:
x=input("Enter any string : ")
out=''
for ch in x:
    if ch not in out:
        out=out + ch
print(out)


-------------------------------------------------------




#len()  function  demo  program  

print(len('Hyd'))           # 3
print(len('Rama Rao'))      # 8
print(len('9247'))          # 4
print(len('+-$'))           # 3
print(len(''))              # 0
print(len(' '))             # 1
print(len('A2#'))           # 3
print(len(3456))            # Error
print('Sec'. len())         # Error

'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''


-----------------------------------------------------------



#chr()  function  demo  program
print(chr(65))     # A
print(chr(90))     # Z
print(chr(97))     # a
print(chr(122))    # z
print(chr(48))     # 0
print(chr(57))     # 9
print(chr(36))     # $
print(chr(32))     # 

'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''


-----------------------------------------------



#ord()  function  demo  program
print(ord('A'))    # 65
print(ord('Z'))    # 90
print(ord('a'))    # 97
print(ord('z'))    # 122
print(ord('0'))    # 48
print(ord('9'))    # 57
print(ord('$'))    # 36
print(ord(' '))    # 32


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







#Let  input  be  A4M3Z5D2

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





# Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

modified code:

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')




--------------------------------------------------------------------------------------
'''
#index()  method  demo  program

Modify  the  following  program  with  index()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''

Modified code:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    pass

print('End')


'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''





'''
#rfind()  method  demo  program

Modify  following  program  with  rfind()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  ---> Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  ---> +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1

Modified code:

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)

print('End')





-----------------------------------------------------

#rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''

Modified Code:
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.rindex('is')
    while True:
        print(index)
        index = a.rindex('is', 0, index)
except ValueError:
    pass

print('End')






#count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))                                         # 4
print(a.count('is' , 19 , 48))                               # 3
print(a.count('was'))                                        # 0

'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
													
Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1







------------------------------------------------------------------------------------------
#Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))

output:
3
3
3