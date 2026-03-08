'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  ---> Pyva<space>Jathon

Hint:  Use  slice
'''
def concate():
    s1=input("enter the first string")
    s2=input("enter the second string")
    print(f'result :{s2[:2]+s1[2:]} {s1[:2]+s2[2:]}  ')
#concate()

'''Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  ---> Nothing'''
def string2():
    s=input("enter the string")
    if(len(s)<4):
        print("length of string >=4")
        return
    else:
        print(s[:2]+s[len(s)-2:len(s)])
#string2()


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

def string3():
    s=input("enter the string")
    print("string from left to s")
    for i in range(len(s)):
        print(f'character at index{i} is {s[i]}')
    print("string from right to left")
    for i in range(-1,-len(s)-1,-1):
        print(f'character at index{i} is {s[i]}')
#string3()

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
def evenOddIndex():
    s=input("enter the string")
    even=""
    odd=""
    for i in range(len(s)):
        if i%2==0:
            even+=s[i]
        else:
            odd+=s[i]
    print(f"even indexed : {even}\n odd index chars : {odd}")
#evenOddIndex()


def altCharDig():
    try:
        res=""
        s=input("enter string with alternate character and digit")
        for i in range(len(s)-1):
            if(i%2==0):
                 res+=s[i]*eval(s[i+1])
        print(res)
    except:
        print("character and digit should be in alternate")
#altCharDig()

def stringMerge():
    s1=input("enter string 1: ")
    s2=input("enter string 2: ")
    m=min(len(s1),len(s2))
    c=""
    for i in range(m):
        c+=s1[i]+s2[i]
    if(len(s1)>len(s2)):
        c+=s1[m:]
    else:
        c+=s2[m:]
    print(f'result : {c}')
#stringMerge()

def duplicateChars():
    s=input("enter the string : ")
    unqiue=""
    for i in s:
        if i not in unqiue:
            unqiue+=i
    print(f'unqiue chars are : {unqiue}')
#duplicateChars()

def indexMethod():

        s=input("enter the String")
        i=s.index('is')
        st=i
        try:
            while True:
                print(i)
                i=s.index('is',i+1)
                
        except:
            print("that it")
#indexMethod()

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))          # 4
print(a . count('is' , 19 , 48)) #3
print(a . count('was'))          #0

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))