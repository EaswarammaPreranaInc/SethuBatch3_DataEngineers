# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')#True
print('day'   in   'Sankar  dayal  sarma')#True
print('Green'   in   'Hyd  is  green  city')#False
print('d  is'   in   'Hyd  is  green  city')#True
print('dis'   in   'Hyd  is  green  city')#False
print('iniv'   in   'Srinivas')#True
print('iniv'   not   in   'Srinivas')#False


'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7  
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2])#a[0:7:2] -->string from indexes 0 to 6 in steps of 2 i.e. Rm<space>
print(a [ : 7])#a[0:7:1]-->starting from indexes 0 to 6 in steps of 1 i.e. Rama<space>Ra
print(a [2 : 4])#[2:4:1]-->starting from indexes 2 to 3 in steps of 1 i.e. ma
print(a [2 : ])#a[2:8:1]-->starting from indexes 2 to 7 in steps of 1 i.e ma<space>Rao
print(a [ : 4 ])#a[0:4:1]-->starting from indexes 0 to 3 in steps of 1 i.e. Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>R
print(a [-6 : -1])#a[-6:-1:1]-->string from indexes -6 to 0 in steps of 1 i.e ma<space>Rao
print(a [-6 : ])#a[-6:8:1]=[2:8:1]= from indexes -6 to -1 or 2 to 7 in steps of 1 i.e. ma Rao
print(a [: -4 : -1])#a[-1:-4:-1] from indexes -1 to -3 in steps of -1 i.e. oaR
print(a [-3 : -1])#a[-3:-1:1] from indexes -3 to -2 in steps of 1 i.e.Ra
print(a [-3 : ])#a[-3:8:1] indexes from -3 to 7 in steps of 1 i.e. Rao
print(a [ : : ])#a[0:8:1] indexes from 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : ])#[0:8:1] indexes from 0 to 7 in steps of 1 i.e. Rama Rao
print(a [ : : -1])# [-1:-9:-1] indexes from -1 to -9 in steps of -1 i.e. oaR amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2]) #a[-2:-9:-2] indexes from -2 to -8 in steps of -2 i.e. aamR
print(a [2 : 8])#a[2:8:1] indexes from 2 to 7 in steps 1 i.e.ma Rao
print(a [2 : 8 : -1])#indexes from 2 to 9 in steps of -1 i.e. ''
print(a [ : -6 : -1])#a[-1:-6:-1] indexes from -1 to -5 in steps of -1 i.e.aaR
print(a [2 : -3])#a[2:-3:1] indexes from 2 to -4 in steps of 1 i.e 2 to 4 'ma '
print(a [1 : 6 : 2])#indexes from 1 to 5 in steps of 2 i.e. aa
print(a [ : -5 : -5])#a[-1:-5:-5] indexes from -1 to -4 in steps of -5 i.e o
print(a [2 : -5])# a[2:-5:1] indexes from 2 to -6 in steps of 1 i.e.m
print(a [2 : -5 : 2])#indexes from 2 to -6 in steps of 2 i.e.m
print(a [ : 0 : -1])#a[-1:0:-1] indexes from -1 to 1 in steps of -1 i.e. oaR ama 
print(a [-5 : 0 : -2])#indexes -5 to 1 in steps of -2 i.e.aa




x=input("Enter first string : ")
y=input("Enter second string : ")
if len(x)>=2 and len(y)>=2:
    result=y[:2]+x[2:]+' '+x[:2]+y[2:]
    print(result)
'''
output
Enter first string : JAVA
Enter second string : PYTHON
PYVA JATHON
'''




x=input("Enter any string : ")
if len(x)>=4:
    print("RESULT : ",x[:2]+x[-2:])
else:
    print("RESULT:","")

'''
output
Enter any string : python
RESULT :  pyon
Enter any string : HYD
RESULT:
'''




x=input("Enter the string : ")
print("String from left to right")
for i in range(len(x)):
    print(F'character at index {i} : {x[i]}')
print("String from right to left")
for i in range(-1,-len(x)-1,-1):
    print(F'Character at index {i} : {x[i]}')

'''
output
Enter the string : VAMSI
String from left to right
character at index 0 : V
character at index 1 : A
character at index 2 : M
character at index 3 : S
character at index 4 : I
String from right to left
Character at index -1 : I
Character at index -2 : S
Character at index -3 : M
Character at index -4 : A
Character at index -5 : V
'''




x=input("Enter any string : ")
even_string=""
odd_string=""
for i in range(len(x)):
    if i%2==0:
        even_string+=x[i]
    else:
        odd_string+=x[i]
print(F'String at even indexes : {even_string}')
print(F'String at odd indexes : {odd_string}')

'''
output
Enter Aany string : RAMA RAO
Stirng at even indexes : RM A
Stirng at odd indexes : AARO
'''




try:
    x = input("Enter any string with alternative character and digit: ")
    
    if len(x) % 2 == 0:
        R = ""
        for i in range(0, len(x), 2):
            R += x[i] * int(x[i+1])
            
        print("Result :", R)
    else:
        print("Error: Input must have an even number of characters (pairs).")

except ValueError:
    print("Error: String should have alternative character and digit.")

'''
output
Enter any string with alternative character and digit: A4$3K2_5 
Result : AAAA$$$KK_____
'''




a = input("Enter first string: ")
b = input("Enter second string: ")
c = ''
i = 0
limit = min(len(a), len(b))
for i in range(limit):
    c += a[i] + b[i]
c += a[limit:] + b[limit:]
print("Final result:", c)

'''
output
Enter first string: VAMSI
Enter second string: HYD
Final result: VHAYMDSI
'''

n=input("Enter any string")
result=''
for i in range(len(x)):
    if a[i] not in result:
        result+=a[i]
print("String without duplicates :",result)

'''
output
Enter any string : MISSISIPI
String without duplicates : MISP
'''




# len()  function  demo  program  (Home  work)
print(len('Hyd'))#3  
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
print(len(3456))#error
print('Sec'. len())#error




# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90))#Z
print(chr(97))#a
print(chr(122))#z
print(chr(48))#0
print(chr(57))#9
print(chr(36))#$
print(chr(32))#<space>




# ord()  function  demo  program
print(ord('A'))#65
print(ord('Z'))#90
print(ord('a'))#97
print(ord('z'))#122
print(ord('0'))#48
print(ord('9'))#57
print(ord('$'))#36
print(ord(' '))#32




try:
    n = input("Enter any string with alternative character and string: ")
    out = ''
    for i in range(0, len(n), 2):
        char = n[i]
        shift = int(n[i+1])
        out += char
        new_char = chr(ord(char) + shift)
        out += new_char
    print("Output:", out)
except ValueError:
    print("Pls enter string with alternative character and string")
    



'''
output
Enter any string with alternative character and string: A4M3Z5D2
Output: AEMPZ_DF
Enter any string with alternative character and string: Hyd
Pls enter string with alternative character and string
'''




a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')
'''
output
4
23
42
End
'''




try:
    while True:
        index = a.index('is', index + 1)
        print(index)
except ValueError:
    print('End')

'''
output
4
23
42
46
End
'''




try:
    while True:
        index = a.rindex('is', 0, current_end)
        print(index)
        current_end = index
except ValueError:
    print('End')
   
'''
output
46
42
23
4
End
'''




a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))
print(a . count('is' , 19 , 48))
print(a . count('was'))

'''
output
4
3
0
'''




a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))

'''
output
3
3
3
'''