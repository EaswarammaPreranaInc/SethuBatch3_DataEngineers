# Find outputs  (Home  work)
# print( 'green'   in   'Hyd  is  green  city')#True
# print('day'   in   'Sankar  dayal  sarma')#True
# print('Green'   in   'Hyd  is  green  city')#False
# print('d  is'   in   'Hyd  is  green  city')#True
# print('dis'   in   'Hyd  is  green  city')#True
# print('iniv'   in   'Srinivas')#True
# print('iniv'   not   in   'Srinivas')#False


'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
# a = 'Rama Rao'
# print(a [ : 7 : 2])#a[0 : 6 : 2]   --->  string  from  indexes  0  to  6  in  steps  of  2  i.e. Rm<space>a
# print(a [ : 7])#a[0 : 6 : 1]   --->  string  from  indexes  0  to  6  in  steps  of  1 i.e. Rama<space>Ra
# print(a [2 : 4])#a[2: 3 : 1]   --->  string  from  indexes  2  to  3  in  steps  of  1  i.e. ma
# print(a [2 : ])#a[2 : 7 : 1]   --->  string  from  indexes  2  to  7  in  steps  of  1  i.e. ma<space>Rao
# print(a [ : 4 ])#a[0 : 3 : 1]   --->  string  from  indexes  0  to  3 in  steps  of  1  i.e. Rama
# print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
# print(a [-6 : -1])#a[-6:-2:1]   --->  string  from  indexes  -6  to  -1 in  steps  of  1  i.e. ma<space>Ra
# print(a [-6 : ])#a[-6 : -9: 1]   --->  string  from  indexes  -6  to  -8 in  steps  of  1 i.e. maR
# print(a [: -4 : -1])#a[-1: -4 : -1]   --->  string  from  indexes  -1  to  -3  in  steps  of  -1  i.e. oaR<space>
# print(a [-3 : -1])#a[-3 : -1 : 1]   --->  string  from  indexes  -3 to  -2  in  steps  of  1  i.e. Ra
# print(a [-3 : ])#a[-3 : -9 : 1]   --->  string  from  indexes  -3 to  -8 in  steps  of  1  i.e. R<space>amaR
# print(a [ : : ])#a[0 : 8 : 1]   --->  string  from  indexes  0  to  7  in  steps  of  1  i.e. Rama<space>Rao
# print(a [ : ])#a[0 : 8 : 1]   --->  string  from  indexes  0  to  7  in  steps  of  1 i.e. Rama<space>Rao
# print(a [ : : -1])#a[-1 : -9 : -1]   --->  string  from  indexes  -1  to  -8  in  steps  of  -1  i.e. oaR<space>amaR
# print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
# print(a [ -2 : : -2])#a[-2: -9 : -2]   --->  string  from  indexes  -2  to  -8 in  steps  of  -2 i.e. a<space>mR 
# print(a [2 : 8])#a[2 : 7: 1]   --->  string  from  indexes  2  to  7  in  steps  of  1  i.e. ma<space>Rao
# print(a [2 : 8 : -1])#nothing
# print(a [ : -6 : -1])#a[-1: -7 : -1]   --->  string  from  indexes  -1  to  -6 in  steps  of  -1 i.e. oaR<space>am
# print(a [2 : -3])#a[2 : -4 : 1]   --->  string  from  indexes  2  to  -3  in  steps  of  2  i.e. ma<space>R
# print(a [1 : 6 : 2])#a[1 : 5  : 2]   --->  string  from  indexes  1  to  5  in  steps  of  1  i.e. Rama<space>
# print(a [ : -5 : -5])#nothing
# print(a [2 : -5])#a[2 : -4 : 1]   --->  string  from  indexes  2 to  -4  in  steps  of  2  i.e. Ra<space>
# print(a [2 : -5 : 2])#a[2: -4 : 2]   --->  string  from  indexes  2 to  -4  in  steps  of  2  i.e. ma<space>
# print(a [ : 0 : -1])##a[-1 : 1 : -1]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. 0aR<space>ama
# print(a [-5 : 0 : -2])#a[0 : 7 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a

'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''

# a=input('Enter 1st string =')
# b=input('Enter 2nd string =')
# c=b[:2]+a[2:]
# d=a[:2]+b[2:]
# print('Result=',c,d,end="")

'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing
'''
# n=input('Enter a string =')
# a=0
# if len(n)>=4:
#     a=n[:2]+n[-2:]
#     print('Result =',a)
# else:
#     print()

'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1
'''
# n=input('Enter the string =')
# print('String indexes from left to right')
# for i in range (len(n)):
#     print('Result ',i,':',n[i])
# print('String from index right to left')
# for j in range (1,len(n)+1):
#     print('Result',-j,':',n[-j])

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

# n=input('Enter any string=')
# even=''
# odd=''

# for i in range(len(n)):
#     if i%2==0:
#         even+=n[i]
#     else:
#         odd+=n[i]
# print('even',even)
# print('odd',odd)

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

# n=input('Enter a string')
# a=''
# for i in range(0,len(n),2):
#     a=a+n[i]*int(n[i+1])
# print(a)

# len()  function  demo  program  (Home  work)
# print(len('Hyd'))  #3
# print(len('Rama Rao'))#8
# print(len('9247'))#4
# print(len('+-$'))#3
# print(len(''))#empty
# print(len(' '))#1
# print(len('A2#'))#3
# print(len(3456))#error
# print('Sec'. len())#Error


'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''
# chr()  function  demo  program
# print(chr(65))  #   A
# print(chr(90))#Z
# print(chr(97))#a
# print(chr(122))#z
# print(chr(48))#1
# print(chr(57))#9
# print(chr(36))#$
# print(chr(32))#<space>



'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  (index := a . find('is' , index + 1))!= -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . index('is')
while  index != -1:
	print(index)
	index = a .find('is' ,index+1)
print('End')


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' ,0,index)
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
'''


'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
	index = a . rindex('is')
	while  index != -1:
		print(index)
	index = a . find('is' ,0,index)
	print('End')
except:
    print('Sub string doesnot exist in the string')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''   
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))#5
print(a . count('is' , 19 , 48))#24  43 and 47
print(a . count('was'))#error


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
Returns  number  of  times  str2  is  in  str1  between  indexes  x  and  y - 1
'''

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#2
print(a . count('\t'))#3
print(a . count('\n'))#3



