'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  --->  ba**le
Hint : Use  replace()  method
'''

a=input("Enter any string : ")
i=1
result=a[0]

while(range(1,len(a)+1)):
    if a[i]==a[0]:
        result=result+a.replace(a[i],'*')
    else:
        result=result+a[i]
    i+=1
    #end of loop
print('result: ',result)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15','36','48']
print(a)#15:36:48
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis' ,'green\tcity']
print(a . split())#['Hyd','is','green','city']
print(a . split('green'))#['Hyd\nis','\tcity']
print(a . split(''))#error
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd','is',	'green'	, 'city']
print(a . split())#['Hyd','is',	'green'	, 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())##['Hyd','is','green'	, 'city']
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#'15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))# '10,20,15,25,52' in any order
d = ['www' , 'gmail', 'com']
print('.' . join(d))#'www.gmail.com'
e = [15 , 36 , 48]
print(':' . join(e))#error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#'SankarDayalSarma'
g = range(5)
print('-' . join(g))#error
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True 
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())#True
print('Rama  Rao'  . isalpha())#False
print('Hyd4'  . isalpha())#False
print('Hyd$'  . isalpha())  #   False
print('9247'  .  isalpha())#False
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())#False


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  an  alphabet

2) When  does  it  return  False  ?  --->  When  at  least  one  character  of  the  string  is  non-alphabet  i.e. digit (or) special  character
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())#True
print('92a47' . isdigit())#false
print('92$47' . isdigit())  #  False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit()) #   False
print(' ' . isdigit())#False
print(9247 . isdigit())#error




# '''
# isdigit()  method
# --------------------
# 1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

# 2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  a   non-digit  i.e. alphabet  (or) special  character
# 																					   (or)
# 															 When  there  are  no  digits  in  the  string
# '''
# # isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#True
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())  #  False
print('\t' . isspace())#True
print('' . isspace())  #  False
print(' ' . isspace())#True


# '''
# isspace()  method
# ---------------------
# 1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

# 2) When  does  it  return  False ?  ---> When  at  least  one  character  of  the  string  is  not  a  white  space
# 															 (i.e.  Alphabet, digit (or)  special  character)
# 																					(or)
# 															 When  there  are  no  white  space  characters																					
# '''
# # islower()  method  demo  program  (Home  work)
print('hyD' . islower())#False
print('hyd' . islower())#True
print('9247' . islower())#False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())##False
print('a2#' . islower())#error





# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))#a :25<tab> b:10.8<tab> c:'Hyd'
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a :0<tab> b:1<tab> c:2
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a :2<tab> b:1<tab> c:0
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a :2<tab> b:2<tab> c:2
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a :25<tab> b:10.8<tab> c:'Hyd'
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a :'Hyd'<tab> b:10.8<tab> c:25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a :25<tab> b:10.8<tab> c:'Hyd'



#  Case  conversion  methods  (Home  work)
a = 'hyD  iS  grEen  cITy'
print(a . upper())#'HYD IS A GREEN cITY'
print(a . lower())#'hyd is a green city'
print(a . capitalize())#'Hyd is a green city'
print(a . title())#'Hyd Is Green City'
print(a . swapcase())##'HYd Is GReEN CitY'
print(a)#'hyD  iS  grEen  cITy'
print('A7$a' . upper())#ERROR 


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
   -------------------------------------------------------'''

input=input("enter any string :")
b=input.split()
c=''
for i in range(1,len(b)+1):
    c=c+b[-i]+' '
print(c)

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
  --------------------------------------------'''

a=input("Enter any string :")
c=''
for i in range (1,len(a)+1):
    c=c+(a[-i])
print(c)
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters
1) What  is  the  output  if  input  is  'interest' ?  ---> interesting
2) What  is  the  output  if  input  is  'interesting' ? ---> interestingly
3) What  is  the  output  if  input  is  Hi ?  ---> Hi  itself
4) Hint:  Use  endswith()  method
'''
a=input("enter a string :")
c=''
if len(a)<=3:
    print("Hi")
    exit()
if  not (a.endswith('ing')):
        c=a+'ing'
        print(c)
if a.endswith('ing'):
        c=a+'ly'
        print(c)

        '''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  23 + 456 + 7 + 8912
Print  the  sum
Hint:  Use  split()  method
'''

a=input("enter any string: ")
b=a.split("+")
c=[]
sum=0
for i in b:
    c.append(eval(i))
    sum=sum+int((i))

print("sum:",sum)



