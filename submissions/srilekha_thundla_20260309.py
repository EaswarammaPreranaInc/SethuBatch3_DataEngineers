'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO
2) Hint  1:  Same  as   prog3e  with  minor  changes
3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


a=input("enter a string :")
b='AEIOU'
c=''
a=a.upper()  
for i in range (len(a)):
    if (a[i] in b ) and (a[i] not in c):
        c=c+a[i]
         
print("distinct vowels:",c) 

''
'''Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character
1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet
2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet
3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character
4) What  is  the  output  if  input  is  '$' ?  ---> Special  character
5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space
6) What  is  the  output  if  input  is  <tab>  key ?  ---> White  space
7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space
8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods
9) Hint2:  Use  nested  if  and   elif'''
a=input("Enter a string :")
if a. isalnum():
    print("Alphanumeric  character")
    if a.isalpha():
        print("Alphabet character")
        if a.isupper():
            print("Upper case  alphabet")
        else :
            print("lower case  alphabet")
    elif a. isdigit():
        print("digit  character") 
    elif a.isspace():
        print('White  space')
    else:
        print("Special  character")