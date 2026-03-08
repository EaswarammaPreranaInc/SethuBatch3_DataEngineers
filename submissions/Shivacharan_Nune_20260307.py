# # Find outputs  (Home  work)
# print( 'green'   in   'Hyd  is  green  city')          #True
# print('day'   in   'Sankar  dayal  sarma')             #True
# print('Green'   in   'Hyd  is  green  city')           #False
# print('d  is'   in   'Hyd  is  green  city')           #True
# print('dis'   in   'Hyd  is  green  city')             #False
# print('iniv'   in   'Srinivas')                        #True
# print('iniv'   not   in   'Srinivas')                  #Fasle
  

# '''
# 1) What  does  in  and  not  in  operators  do ?  --->  Searches  for  a  string  in  another  string

# 2) What  does  str1  in  str2  do ? --->  Returns  True  if  str1  is  in  str2  and  False  otherwise

# 3) What  does  str1  not  in  str2  do ? --->  Returns  True  if  str1  is  not  in  str2  and  False  otherwise

# 4) not  in  operator  is  quite  opposite  to  in  operator
# '''
# #---------------------------------------------------------------------------------------------------------------------
# '''
# Slice  demo  program
# 0      1       2       3      4       5       6       7
# R      a      m        a              R       a       o
# -8    -7     -6       -5     -4      -3      -2       -1
# '''
# a = 'Rama Rao'
# print(a [ : 7 : 2])   #string  from  indexes  0  to  6  in  steps  of  2  i.e.Rm<space>a
# print(a [ : 7])       #string  from  indexes  0  to  6  in  steps  of  1  i.e.Rama<space>Ra 
# print(a [2 : 4])      #string  from  indexes  2  to  3  in  steps  of  1  i.e.ma
# print(a [2 : ])       #string  from  indexes  2 to  7  in  steps  of  1  i.e.ma<space>Rao
# print(a [ : 4 ])      #string  from  indexes  0  to  3  in  steps  of  1  i.e.Rama
# print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
# print(a [-6 : -1])    #string  from  indexes  -6  to -2 in  steps  of  -2  i.e.ma<space>Ra
# print(a [-6 : ])      #string  from  indexes  -6  to  7  in  steps  of  1  i.e.ma<space>Rao
# print(a [: -4 : -1])  #string  from  indexes   -1  to  -3  in  steps  of  1  i.e.oaR
# print(a [-3 : -1])    #string  from  indexes  -3  to  -2  in  steps  of  1  i.e.Ra
# print(a [-3 : ])      #string  from  indexes  -3 to  7  in  steps  of  1  i.e.Rao
# print(a [ : : ])      #string  from  indexes  0  to  7  in  steps  of  1  i.e.Rama<space>Rao
# print(a [ : ])        #string  from  indexes  0  to  7  in  steps  of  1  i.e.Rama<space>Rao
# print(a [ : : -1])    #string  from  indexes  -1  to  -8  in  steps  of  -1  i.e.oaR<space>amaR
# print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
# print(a [ -2 : : -2])  #string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.a<space>mR
# print(a [2 : 8])      #string  from  indexes  2  to  7  in  steps  of  1  i.e.ma<space>Rao
# print(a [2 : 8 : -1]) #string  from  indexes  2  to  7  in  steps  of  -1  i.e.""
# print(a [ : -6 : -1]) #string  from  indexes  -1  to  -5  in  steps  of  -1  i.e.oaR<space>a
# print(a [2 : -3])     #string  from  indexes  2  to  -4  in  steps  of  1  i.e.ma<space>
# print(a [1 : 6 : 2])  #string  from  indexes  1  to  5  in  steps  of  2  i.e.aaR
# print(a [ : -5 : -5]) #string  from  indexes -1 to  -4  in  steps  of  -5  i.e."o"
# print(a [2 : -5])     #string  from  indexes  2  to  -6  in  steps  of  1  i.e.m
# print(a [2 : -5 : 2]) #string  from  indexes  2  to  -6  in  steps  of  2  i.e.m
# print(a [ : 0 : -1])  #string  from  indexes  -1 to  1  in  steps  of -1  i.e.oaR<space>ama
# print(a [-5 : 0 : -2]) #string  from  indexes  -5  to  1  in  steps  of  -2  i.e.aa
#---------------------------------------------------------------------------------------------------------
# '''
# Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
# characters  of  the  two  strings.
# Assume  that  each  string  has  a   minimum  of  two  characters

# Let  inputs  be  Java  and  Python
# What  are  the  outputs ?  ---> Pyva<space>Jathon

# Hint:  Use  slice
# '''
# #------------------------------------------------------------------------
# a=input("enter string 1: ")
# b=input("enter string 2: ")
# if len(a)>=2 and len(b)>=2:
#     print(a[:2]+b[2:],b[:2]+a[2:])
#---------------------------------------------------------------------------
# '''
# Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
# Print  an  empty  string  if  string  has  less  than  four  characters

# 1) Let  input  be  PYTHON
#     What  is  the  output ?  ---> PYON

# 2) Let  input  be  Hyd
#     What  is  the  output ?  ---> Nothing
# '''
#--------------------------------------------------------------------
# a=input("enter string : ")
# c=""
# if len(a)>3:
#     for i in range(len(a)):
#         if i==0 or i==1 or i==len(a)-2 or i==len(a)-1:
#             c=c+a[i]
# print(c)
#------------------------------------------------------------------------
'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     		 0      1     2      3     4
Let  input  be		  V     A     M     S     I
			         -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two  for  loops
'''
#--------------------------------------------------------------------------------
# a=input("enter string : ")
# for i in range(len(a)):
#     print(f"Character  at  index  {i}  :{a[i]}")
# print()
# for i in range(1,len(a)+1):
#     print(f"Character  at  index  {-i}  :{a[-i]}")
#------------------------------------------------------------------------
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
#--------------------------------------------------------------------
# a=input("enter string : ")
# even=""
# odd=""
# if len(a)>=1:
#     for i in range(len(a)):
#         if i%2==0:
#             even=even+a[i]
#         elif i%2!=0:
#             odd=odd+a[i]
# print("string at even indexes",even)
# print("string at odd indexes",odd)
#---------------------------------------------------------------------------
'''
Let  input  be           A   4   B   3   C   2   $   5
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
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --->  a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string '''
#----------------------------------------------------------------------------------------------------------------------------------------------------
# a=input("enter string : ")
# if len(a)>=2:
#     for i in range(0,len(a)-1,2):
#         print(a[i]*int(a[i+1]),end="")
#--------------------------------------------------------------------
'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  ---> HVYADMSI

          0    1    2
a  --->   H    Y    D

           0    1    2    3    4
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
#--------------------------------------------------------------------
# a=input("1st string :")
# b=input("2nd string :")
# c=""
# for i in range(min(len(a),len(b))):
#     c=c+a[i]+b[i]
#     i=i+1
# c=c+a[i:]+b[i:]
# print(c)
#----------------------------------------------------------------------
'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'



3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  ---> Ignore  the  character

5) Hint:  Use  not  in   operator
'''
#-------------------------------------------------------------------------------
# a=input("enter a string: ")
# c=""
# for x in a:
#     if x not in c:
#         c=c+x
# print(c)
#----------------------------------------------------------------------
#using set:
# a=input("enter a string: ")
# b=set()
# c=""
# for x in a:
#     b.add(x)
# for x in b:
#     c=c+x
# print(c)
#--------------------------------------
'''
# len()  function  demo  program  (Home  work)
# print(len('Hyd'))      #3
# print(len('Rama Rao')) #8
# print(len('9247'))     #4
# print(len('+-$'))      #3
# print(len(''))         #0
# print(len(' '))        #1
# print(len('A2#'))      #3
# #print(len(3456))       #Error
# print('Sec'. len())    #Error:its not a method it is a function in bultins module and more over no method len() in str class.
# '''
# What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
#--------------------------------------------------
# # chr()  function  demo  program
# print(chr(65))  #   A
# print(chr(90))  #Z
# print(chr(97))  #a
# print(chr(122)) #z
# print(chr(48))  #0
# print(chr(57))  #9
# print(chr(36))  #$
# print(chr(32))  #space
'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
#----------------------------------------------------------------------
# # ord()  function  demo  program
# print(ord('A')) #65
# print(ord('Z')) #90
# print(ord('a')) #97
# print(ord('z')) #122
# print(ord('0')) #48
# print(ord('9')) #57
# print(ord('$')) #36
# print(ord(' ')) #32
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
#-------------------------------------------------------------------------
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
# try:
#     a=input("enter a string: ")
#     for i in range(0,len(a)-1,2):
#         print(a[i],chr(ord(a[i])+int(a[i+1])),sep="",end="")
# except:
#     print("enter string in sucan a way that an aplhabet is postceded with digit")
#--------------------------------------------------------------------------------
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . find('is')
# while  index != -1:
# 	print(index)
# 	index = a . find('is' , index + 1)
# print('End')
#------------------------------------------------------------------------
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his 'cityi
# index = a . find('is')
# while  index != -1:
# 	print(index)
# 	index = a . find('is' , index + 1)
# print('End')
'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''
#converting to index method
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# if 'is' in a:
#     index = a . index('is')
#     while  index<=len(a) :
#         print(index)
#         try:
#             index = a . index('is' , index + 1)
#         except:
#             break
#     print('End')
# else:
#     print("not found")
#------------------------------------------------------------------
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . find('is')
# while  index != -1:
# 	print(index)
# 	index = a . find('is' , index + 1)
# print('End')
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

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1'''

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . rfind('is')
# while  index != -1:
# 	print(index)
# 	index = a . rfind('is' , 0,index - 1)
# print('End')
#------------------------------------------------------------------
'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . find('is')
# while  index != -1:
# 	print(index)
# 	index = a . find('is' , index + 1)
# print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . rindex('is')
# while  True:
# 	print(index)
# 	try:
# 		index = a . rindex('is' ,0, index - 1)
# 	except:
# 		break
#---------------------------------------------------------------------------------------------
#  count()  method  demo  program (Home  work)
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
# print(a . count('is'))               #4  
# print(a . count('is' , 19 , 48))     #3
# print(a . count('was'))              #0
'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
																	Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1
'''
 #  Find  outputs  (Home  work)
# a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
# print(a . count(' '))       #3
# print(a . count('\t'))      #3
# print(a . count('\n'))      #3
#--------------------------------------------------------------------------------------------------------------
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
#-------------------------------------------------------------------------
# a=input("enter a string ")
# print(a[0]+a[1:].replace(a[0],'*'))
#----------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
# a = '15:36:48'
# print(a . split(':'))    #['15','36','48']
# print(a)     #'15:36:48'
#------------------------------------------------
 # Find  outputs  (Home  work)
# a = 'Hyd\nis green\tcity'
# print(a . split(' '))     #['Hyd\nis','green\tcity']
# print(a . split())        #['Hyd', 'is', 'green', 'city']
# print(a . split('green')) #'[Hyd\nis','\tcity']
# # print(a . split(''))      #Error
#----------------------------------------------------------
# Find  outputs  (Home  work)
# a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
# print(a . split('\t'))     #[Hyd','is','green','city']
# print(a . split())        #['Hyd','is','green','city']
# print(a . split(' '))     #['Hyd','   is','   green','   city']
#----------------------------------------------------------------
# Find  outputs (Home  work)
# a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
# print(a . split())      #['Hyd','is','green','city']
# print(a . split(' '))   #['Hyd','is','green','city']
#---------------------------------------------------------
#  # Find  outputs  (Home  work)
# a = 'www.gmail.com'
# print(a . split('.'))  #['www','gmail','com']
#-------------------------------------------------------------------------
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912

Print  the  sum

Hint:  Use  split()  method
'''
# a=input("enter numbers postceded with +")
# sum=0
# for x in a.split('+'):
#     sum=sum+int(x)
# print(sum)
#--------------------------------------------------------
#  Find  outputs  (Home  work)
# a = ['15' , '36' , '48']
# print(':' . join(a))                           #'15:36:48'
# b = ('Hyd' , 'is' , 'green' , 'city')          
# print(' ' . join(b))                           #'Hyd is green city'
# c = {'10' , '20' , '15' , '25' , '52'}  
# print(',' . join(c))                          #'25,20,52,15,10'
# d = ['www' , 'gmail', 'com']
# print('.' . join(d))                         #www.gmail.com
# e = [15 , 36 , 48]
# #print(':' . join(e))             #Error      
# f = ['Sankar' , 'Dayal' , 'Sarma']
# print('' . join(f))               #Error
# g = range(5)
# print('-' . join(g)) #Error
#----------------------------------------------------------
#  Case  conversion  methods  (Home  work)
# a = 'hyD  iS  grEen  cITy'
# print(a . upper())                  #HYD IS GREEN CITY
# print(a . lower())                  #hyd is green city
# print(a . capitalize())             #Hyd is green city
# print(a . title())                  #Hyd Is Green City
# print(a . swapcase())               #HYd Is GReEB CitY
# print(a)                            #hyD  iS  grEen  cITy
# print('A7$a' . upper())             #A7$A


# '''
# 1) What  does  upper()  method  do ?  --->  Returns  an  upper  case  string

# 2) What  does  lower()  method  do ?  --->  Returns  a  lower  case  string

# 3) What  does  capitalize()  method  do ?  --->  Returns  a  string  where  1st  char  is  uppercase  and  the  rest  in  lower  case

# 4) What  does  title()  method  do ?  --->  Returns  a  string  where  1st  char  of  each  word  is  uppercase  and  the  rest  in  lowercase

# 5) What  does  swapcase()  method  do ?  --->  Returns  a  string  where  upper  case  alphabets  are  converted  to
# 																         lower  case  and   vice-versa
# '''
#------------------------------------------------------------------------------------------------------------------------------------------------------
# endswith()  method  demo  progrram (Home  work)
#----------------------------------------------------------------------------------------
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself

4) Hint:  Use  endswith()  method
'''
# a=input("enter any string :")
# if len(a)>=3:
#     if a[-3:]=='ing':
#         print(a+'ly')
#     else:
#         print(a+'ing')
# else:
#     print(a)
#-----------------------------------------------------------------------------------------
# #  isalpha()  method  demo  program (Home  work)
# print('Hyd'  . isalpha())                       #True
# print('Rama  Rao'  . isalpha())                 #False
# print('Hyd4'  . isalpha())                      #False
# print('Hyd$'  . isalpha())  #   False
# print('9247'  .  isalpha())                    #False
# print('+-$'    .  isalpha())                   #False
# print('A2#'  .   isalpha())                    #False
# print(''  .  isalpha())  #  False
# print(' '  .  isalpha())                        #False


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
#-----------------------------------------------------------------------------------------------------------
# # isdigit()  method  demo  program  (Home  work)
# print('9247' . isdigit())              #True
# print('92a47' . isdigit())            #False
# print('92$47' . isdigit())  #  False
# print('Hyd' . isdigit())          #False
# print('+-$' . isdigit())         #False
# print('A2#' . isdigit())        #False
# print('' . isdigit()) #   False
# print(' ' . isdigit()) #False
# #print(9247 . isdigit())    #Error
'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
																					   (or)
															 When  there  are  no  digits  in  the  string
'''
#----------------------------------------------------------------------------------------------------
# isspace()  method  demo  program  (Home  work)
# print('\n  A\t' . isspace())         #False
# print('\n  \t' . isspace())          #True
# print('\n  7\t' . isspace())         #False
# print('\n' . isspace())              #True
# print('\n  $\t' . isspace())  #  False
# print('\t' . isspace())        #True
# print('' . isspace())  #  False
# print(' ' . isspace())         #True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
															 (i.e.  Alphabet, digit (or)  special  character)
																					(or)
															 When  there  are  no  white  space  characters																					
'''
#----------------------------------------------------------------------
# islower()  method  demo  program  (Home  work)
# print('hyD' . islower())                  #False 
# print('hyd' . islower())                  #True
# print('9247' . islower())                #False
# print('rama  rao' . islower())            #True
# print('+-$' . islower())                 #False
# print('hyd+-$' . islower())            #True
# print('abc123' . islower())           #True
# print('' . islower())                 #False
# print('a2#' . islower())            #True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  ---> When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			 When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  ---> When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  lowercase  alphabet

Note:
1) What  are  upper()  and  lower()  called ?  --->  Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''
#---------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
#a , b , c = 25 , 10.8 , 'Hyd'
# print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
# print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
# print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
# print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
# print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
# print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
# print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
# # a  :  25          b  :  10.8      c  :  Hyd  
# a  :  25          b  :  10.8      c  :  Hyd  
# a  :  Hyd         b  :  10.8      c  :  25  
# a  :  Hyd         b  :  Hyd       c  :  Hyd
# a  :  25          b  :  10.8      c  :  Hyd
# a  :  Hyd         b  :  10.8      c  :  25
# a  :  25          b  :  25        c  :  25
#-------------------------------------------------------------------------------------------------
'''
# 1) What are the three outputs if input is 'A' ?
# Alphanumeric character , Alphabet character , Upper case alphabet

# 2) What are the three outputs if input is 'a' ?
# Alphanumeric character , Alphabet character , Lower case alphabet

# 3) What are the two outputs if input is '7' ?
# Alphanumeric character , Digit character

# 4) What is the output if input is '$' ?
# Special character

# 5) What is the output if input is <spacebar> ?
# White space

# 6) What is the output if input is <tab> key ?
# White space

# 7) What is the output if input is <enter> key ?
# White space
'''
# ch = input("Enter a character: ")

# if ch.isalnum():
#     print("Alphanumeric character")

#     if ch.isalpha():
#         print("Alphabet character")

#         if ch.isupper():
#             print("Upper case alphabet")
#         elif ch.islower():
#             print("Lower case alphabet")

#     elif ch.isdigit():
#         print("Digit character")

# elif ch.isspace():
#     print("White space")

# else:
#     print("Special character")
#--------------------------------------------------------------------------
'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'								
     2       'y'             'd' + 'y' = 'dy'								
     3       'H'            'dy' + 'H' = 'dyH'								
  ---------------------------------------------
'''
# a = input("Enter a string: ")
# b = ''

# for i in range(1, len(a)+1):
#     b = b + a[-i]

# print(b)
#--------------------------------------------------------
'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1        'city'        '' + 'city' + ' ' = 'city '							  
    2        'green'     'city ' + 'green' + ' ' = 'city green '							  
    3        'is'            'city green ' + 'is' + ' ' = 'city green is '							  
    4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '							  
   -------------------------------------------------------
'''
# a = input("Enter a sentence: ")
# b = a.split()
# c = ''

# for i in range(1, len(b)+1):
#     c = c + b[-i] + ' '

# print(c)
#----------------------------------------------------------
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  --->	dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
# a = input("Enter a sentence: ")
# b = a.split()

# for word in b:
#     print(word[::-1], end=' ')
#---------------------------------------------------------------------------------------
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1) What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z' = 'ADKPZ'
    digit = '' + '1' + '3' + '5' + '7' + '9'   = '13579'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
# '''
# a = input("Enter string: ")

# b = sorted(a)          # '13579ADKPZ'

# alpha = ''
# digit = ''

# for ch in b:
#     if ch.isalpha():
#         alpha = alpha + ch
#     elif ch.isdigit():
#         digit = digit + ch

# print(alpha + digit)

