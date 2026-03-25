# Write  a  program  to  merge  two  strings  to  form  a  new  string

try:

 a=input('Enter first string:')
 b=input('Enter second string:')
 c=''
 i=0
 while True:
    c+=a[i]+b[i]
    i+=1
except:
	   print("Numbers should be greater than 3 characters:")







'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])  # a[0:7:1]--->string from indexes 0 to 6 in steps of 1 i.e Rm a
print(a [ : 7])    # a[0:7:1]--->string from indexes 0 to 6 in steps of 1 i.e Rama Ra
print(a [2 : 4])  #  a[2:4:1]--->string from indexes 2 to 4 in steps of 1 i.e ma
print(a [2 : ])  #  a[2:8:1]--->string from indexes 2 to 7 in steps of 1 i.e ma Rao
print(a [ : 4 ])  #  a[0:4:1]--->string from indexes 0 to 3 in steps of 1 i.e Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) #  a[-6:-9:-1]--->string from indexes -6 to -8 in steps of -1 i.e maR
print(a [-6 : ])  #  a[-6:8:1]--->string from indexes -6 to 7 in steps of 1 i.e ma Rao
print(a [: -4 : -1]) #  a[-1:-4:-1]--->string from indexes -1 to -4 in steps of -1 i.e oaR 
print(a [-3 : -1]) #  a[-3:-9:-1]--->string from indexes -3 to -8 in steps of -1 i.e R amaR
print(a [-3 : ]) #  a[-3:8:1]--->string from indexes -3 to 8 in steps of 1 i.e Rao
print(a [ : : ]) #  a[0:8:1]--->string from indexes 0 to 7 in steps of 1 i.e Rama Rao
print(a [ : ])    #  a[0:8:1]--->string from indexes 0 to 7 in steps of 1 i.e Rama Rao
print(a [ : : -1])   #  a[-1:-9:-1]--->string from indexes -1 to -8 in steps of -1 i.e oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  #  a[-2:-9:-2]--->string from indexes -2 to -8 in steps of -2 i.e a mR
print(a [2 : 8])     #  a[2:8:1]--->string from indexes 2to 7 in steps of 1 i.e ma Rao
print(a [2 : 8 : -1])   #  a[2:8:-1]--->string from indexes 2 to 7 in steps of -1 i.e Empty string
print(a [ : -6 : -1])   #  a[-1:-6:-1]--->string from indexes -1 to -5 in steps of -1 i.e oaR a
print(a [2 : -3]) #  a[2:-3:1]--->string from indexes 2 to -2 in steps of 1 i.e ma Ra
print(a [1 : 6 : 2])   #  a[1:6:2]--->string from indexes 1 to 5 in steps of 2 i.e aa R




'''Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.'''


x=input('Enter 1st string:') # Python
y=input('ENter 2nd string:') # Java
s=''
x1=x[:2]+y[2:]
y1=y[2:]+x[:2]
result=("x1"+" "+"y1")
print(result)



'''Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters'''



n=input('Enter input')
if len(n)<4:
    print('')
else:
    print('n[:2]+n[-2:]')


'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		                  V     A     M     S     I
			      		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->                  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
                                                 Character  at  index  -5  :  V'''



n=input('Enter any string:')
s=len(n)
for I in range(s):
  print(f'Character at index{i} : {n[i]}')
for j in range(1,n+1):
  print(f'Character at index{-j} : {n[j]}')





'''Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'   '''



n= ijnput('Enter input:')
even=0
odd=0
for i in range(len(n)):
    if i%2==0:
        even+=n[i]
    else:
      odd+=n[i]
print("even=",even)
print("odd=",odd)



'''Let  input  be    A   4   B   3   C   2   $   5
                         0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$'''



s=input("Enter string:")
x=''
for i in range(0,len(s),2):
     char=s[i]
     count=int(s[i+1])
     x+=char*count
print(x)



# Write  a  program  to  merge  two  strings  to  form  a  new  string


a=input("String:")
b=input("String:")
c=''
i=0
while i<len(a) or i<len(b):
    if i<len(a):
         c+=a[i]
    if i<len(b):
         c+=b[i]
    i+=1
print(c)



# Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set


s=input("Enter string:")
out=''
for i not in s:
    if c not in out:
    out+=c
print(out)




# len()  function  demo  program  (Home  work)
print(len('Hyd'))             # 3
print(len('Rama Rao'))        # 8 
print(len('9247'))            # 4
print(len('+-$'))             # 3
print(len(''))                # Empty string
print(len(' '))               # 1
print(len('A2#'))             # 3
print(len(3456))              # Error 
print('Sec'. len())           # Error



# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90))  #   Z
print(chr(97))  #   a
print(chr(122)) #   z
print(chr(48))  #   1
print(chr(57))  #   9
print(chr(36))  #   ''
print(chr(32))  #   *



# ord()  function  demo  program
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32









































