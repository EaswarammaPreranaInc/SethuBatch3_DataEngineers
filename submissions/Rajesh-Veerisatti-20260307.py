
# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

a=input("Enter any string")
b=""

for i in range(len(a)):
    if a[i] in b:
        b+="*"
    else:
        b+=a[i]
print(b)



# Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols

a =input("Enter a string which contains numbers with "+"sybols: ")
a=a.split("+")

b=0

for i in range(len(a)):

    b+=int(a[i])

print(b)


# Write  a  program  to  append  'ing'  to  input  string.Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.Leave  the  string  unchanged  if  string  has  lessthan three  characters

a = input("Enter string: ")

if len(a) < 3:
    print(a)
elif a.endswith("ing"):
    print(a + "ly")
else:
    print(a + "ing")


# Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

a = input("Enter a character: ")

if a.isalnum():
    print("Alphanumeric character")
    
    if a.isalpha():
        print("Alphabet character")
        
        if a.isupper():
            print("Upper case alphabet")
        elif a.islower():
            print("Lower case alphabet")
            
    elif a.isdigit():
        print("Digit character")

elif a.isspace():
    print("White space")

else:
    print("Special character")



# Write  a  program  to  reverse  a  string  without  slice

a = input("Enter string: ")

b = ""

for i in range(1, len(a) + 1):
    b += a[-i]

print(b)



# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

a =input("Enter a string of sentence: ")
a=a.split(" ")
b=[]
c=""
for i in range(1,(len(a)+1)):
    b.append (a[-i])
print(b)
for i in range(len(b)):

    c+=b[i]+" "

print(c)


# Write  a  program  to  reverse  each  word  of  the  sentence

a="Hyd is green city"
a=a.split(" ")
b=[]


for i in range(len(a)):
    word=a[i]
    c=""
    for j in range(1,len(word)+1):
        c+=word[-j]
    b.append(c)
c=" ".join(b)

print(c)


# Write  a  program  to  sort  string  in  alphabetical  order

a = input("Enter string: ")
c=""
b = sorted(a)
for i in range(len(b)):
    c+=b[i]



print(c)



# Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

a=input("Enter a string : ")
b=sorted(a)
c=""
d="" 
e=""
for i in b:

    if i.isalpha():
        c+=i
    elif i.isdigit():
        d+=i

e=c+d
print(e)