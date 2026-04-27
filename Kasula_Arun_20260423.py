import random
# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
st=input('Enter a string: ')
for i in range(10):
    print(random.choice(st)) 

'''  (Home  work)
Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
'''

import random
for i in range(10):
    st=''
    for j in range(6):
        if j%2==0:
            st+=chr(random.randrange(65,91))
        else:
            st+=str(random.randrange(10))
    print(st)

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
li=eval(input('Enter list: '))
for i in range(10):
    print(random.choice(li))

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random
for i in range(10):
    print(random.randrange(100000,1000000))