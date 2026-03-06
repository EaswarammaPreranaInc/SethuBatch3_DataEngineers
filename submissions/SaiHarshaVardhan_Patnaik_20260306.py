# len()  function  demo  program  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('+-$')) #3
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
#print(len(3456)) # Error
print('Sec'. len()) # Error


'''
What  does  len(string)  do  ?  --->  Returns  number  of  characters  in  the  string
'''
chr()  function  demo  program
print(chr(65))  #   A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print(chr(48)) # 0
print(chr(57)) # 9
print(chr(36)) # $
print(chr(32)) #



'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32


# '''
# ord()  function
# ------------------
# 1) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

# 2) How  many  unicode  values  exist ?  --->  512

# 3) What  is  the  range  of  unicode  values ?  ---> 0  to  511

# 4) What  are  the  unicode  values  of  'A'  -  'Z' ?  --->  65  to  90
#      What  are  the  unicode  values  of  'a'  -  'z' ?  --->  97  to  122
#      What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57

# 5) What  is  another  name  of  unicode ?  ---> Extended  Ascii

# Note:  chr()  and  ord()  are  quite  opposite  functions
# '''
# '''
# Let  input  be  A4M3Z5D2

# What  is  the  output ?  --->  AEMPZ_DF

#  0     1     2     3    4    5    6     7
#  A     4     M     3    Z    5    D     2


#     i       a[i]      a[i + 1]         out
# --------------------------------------------------------------------------------
#                                            ''
#    0        'A'        '4'             '' + 'A' +  'E' = 'AE'
#    2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
#    4        'Z'        '5'             'AEMP' + 'Z' +  '' = 'AEMPZ'
#    6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'															 
# -----------------------------------------------------------------------------------
# Hint: Use  chr()  and  ord()  functions
# '''
string = input("Enter an input:")
out = ''
for i in range(0,len(string),2):
    a = string[i]
    b = int(string[i+1])
    c = chr(ord(a)+b)
    if c > 'Z':
        c ='_'
    out+= a + c
print(out)
'''
OUTPUT:
Enter an input:A4M3Z5D2
AEMPZ_DF
'''

# '''
# Modify  following  program  with  walrus  operator

# Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
# '''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')

# '''  (Home  work)
# index()  method  demo  program

# Modify  the  following  program  with  index()  method
# '''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

try:
    index = a.index('is')
    while True:
        print(index)
        index = a.index('is', index + 1)
except ValueError:
    print('End')


# '''
# index()  method
# -------------------
# It  is  same  as  find()  method  except  that  it  raises   error (but  not  -1) when  string  is  not  found

# Syntax :  Same  as   find()  method
# '''
# '''(Home  work)
# rfind()  method  demo  program

# Modify  following  program  with  rfind()  method
# '''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a .rfind('is' , index + 1)
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

try:
	
    index = a . rindex('is')
    while  index != -1:
        print(index)
        index = a . rindex('is' , index + 1)
    print('End')

except ValueError:
    print('End')


# '''
# rindex()  method
# --------------------
# It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
# '''
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #3
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
print(a . count(' ')) # 3
print(a . count('\t')) # 3
print(a . count('\n')) # 3