#1
# Find outputs  (Homework)
print( 'green' in 'Hyd is green city') #True
print('day' in 'Sankar dayal sarma') #True
print('Green' in 'Hyd is green city') #False
print('d is' in 'Hyd is green city') #True
print('dis' in 'Hyd is green city') #False
print('iniv' in 'Srinivas') #True
print('iniv' not in 'Srinivas') #False



#2
'''  (Homework)
Slice  demo  program
 0    1   2    3    4    5    6    7
 R    a   m    a         R    a    o
-8   -7  -6   -5   -4   -3   -2   -1
'''
a = 'Rama Rao'

print(a[ : 7 : 2]) # a[0:7:2] -> Indices 0, 2, 4, 6. Result: 'Rm a'
print(a[ : 7]) # a[0:7:1] -> Indices 0 to 6. Result: 'Rama Ra'
print(a[2 : 4]) # a[2:4:1] -> Indices 2 to 3. Result: 'ma'
print(a[2 : ]) # a[2:8:1] -> Indices 2 to end. Result: 'ma Rao'
print(a[ : 4 ]) # a[0:4:1] -> Indices 0 to 3. Result: 'Rama'
print(a[ : : 2]) # a[0:8:2] -> Every 2nd char from start. Result: 'Rm a'
print(a[-6 : -1]) # a[2:7:1] -> From index -6 ('m') to -2 ('a'). Result: 'ma Ra'
print(a[-6 : ]) # a[2:8:1] -> From index -6 to the end. Result: 'ma Rao'
print(a[: -4 : -1]) # a[7:4:-1] -> From end backwards to index -3. Result: 'oaR'
print(a[-3 : -1]) # a[5:7:1] -> From index -3 ('R') to -2 ('a'). Result: 'Ra'
print(a[-3 : ]) # a[5:8:1] -> From index -3 to the end. Result: 'Rao'
print(a[ : : ]) # a[0:8:1] -> The whole string. Result: 'Rama Rao'
print(a[ : ]) # a[0:8:1] -> Short-hand for the whole string. Result: 'Rama Rao'
print(a[ : : -1]) # a[7:-1:-1] -> The whole string reversed. Result: 'oaR amaR'
print(a[ : : -2]) # a[7:-1:-2] -> Every 2nd char backwards. Result: 'oRaa'
print(a[ -2 : : -2]) # a[6:-1:-2] -> From 'a' backwards by 2. Result: 'a mR'
print(a[2 : 8]) # a[2:8:1] -> From index 2 to the end. Result: 'ma Rao'
print(a[2 : 8 : -1]) # Start < Stop with negative step returns empty. Result: ''
print(a[ : -6 : -1]) # a[7:2:-1] -> From end back to index -5. Result: 'oaR a'
print(a[2 : -3]) # a[2:5:1] -> From index 2 to 4. Result: 'ma '
print(a[1 : 6 : 2]) # a[1:6:2] -> Indices 1, 3, 5. Result: 'aaR'
print(a[ : -5 : -5]) # a[7:3:-5] -> Start at 7, jump back 5. Result: 'o'
print(a[2 : -5]) # a[2:3:1] -> Only index 2. Result: 'm'
print(a[2 : -5 : 2]) # a[2:3:2] -> Only index 2. Result: 'm'
print(a[ : 0 : -1]) # a[7:0:-1] -> End back to index 1. Result: 'oaR ama'
print(a[-5 : 0 : -2]) # a[3:0:-2] -> Indices 3, 1. Result: 'aa'



#3
'''
Write a program to concatenate two strings separated by space but swap first two
characters of the two strings.
Assume that each string has a minimum of two characters

Let inputs be Java and Python
What are the outputs?  ---> Pyva<space>Jathon

Hint: Use slice
'''
str1 = "Java"
str2 = "Python"

result = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(result) # Pyva<space>Jathon


#4
'''
Write a program to print first two and the last two characters of the string
Print an empty string if string has less than four characters

1)  Let input be PYTHON
    What is the output? ---> PYON

2)  Let input be Hyd
    What is the output? ---> Nothing
'''
s = input("Enter any string : ")

if len(s) < 4:
    print("Result : ")
else:
    result = s[:2] + s[-2:]
    print("Result :", result)



#5
'''
Write a program to print characters of the string in forward and reverse directions without slice

              0   1   2   3   4
Let input be: V   A   M   S   I
             -5  -4  -3  -2  -1

What are the outputs? ---> Character at index 0 : V
                           Character at index 1 : A
                           Character at index 2 : M
                           Character at index 3 : S
                           Character at index 4 : I

                           Character at index -1 : I
                           Character at index -2 : S
                           Character at index -3 : M
                           Character at index -4 : A
                           Character at index -5 : V

Hint: Use two for loops
'''
s = input("Enter the string: ")

print("String from left to right :")
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

print("String from right to left:")
for i in range(-1, -(len(s) + 1), -1):
    print(f"Character at index {i} : {s[i]}")

input("Press any key to continue . . .")



#6
'''
Write a program to print characters at even and odd indexes without slice

              0  1  2  3  4  5  6  7
Let input be: R  a  m  a     R  a  o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' = 'Rm a'

1) What action to be made when index is even? ---> Concatenate the character to even object

2) What action to be made when index is odd? ---> Concatenate the characeter to odd object

3) Hint: Use single for loop
'''
s = input("Enter any string : ")

even = ""
odd = ""

for i in range(len(s)):
    if i % 2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]

print("String at even indexes :", even)
print("String at odd indexes  :", odd)



#7
'''
Let input be  A   4   B   3   C   2   $   5
              0   1   2   3   4   5   6   7

What is the output? --->  AAAABBBCC$$$$$

1) What is the result of 'A' * 4? ---> 'AAAA'

2)  i        a[i]       a[i + 1]          out
   -------------------------------------------------------
                                               ''
    0         'A'          '4'             '' + 'A' * 4 = 'AAAA'
    2         'B'          '3'             'AAAA' + 'B' * 3  = 'AAAABBB' 
    4         'C'          '2'             'AAAABBB' + 'C' * 2  = 'AAAABBBCC' 
    6         '$'          '5'             'AAAABBBCC' + '$' * 5  = 'AAAABBBCC$$$$$' 
   -------------------------------------------------------
What is the difference between a[i] and a[i + 1]? ---> a[i] is ith char of string and a[i + 1] is (i + 1)th char of string
'''
s = input("Enter any string with alternate character and digit : ")

if len(s) % 2 != 0:
    print("String should have alternate character and digit")
else:
    output = ""
    for i in range(0, len(s), 2):
        char = s[i]           # Current character a[i]
        count = int(s[i + 1]) # Next character a[i+1] converted to integer
        
        output = output + (char * count)
    
    print("Result : ", output)



#8
'''
Write a program to merge two strings to form a new string

1) Let inputs be HYD and VAMSI
   What is the output? ---> HVYADMSI

        0   1   2
a  ---> H   Y   D

        0  1  2  3  4
b  ---> V  A  M  S  I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0       'H'        'V'         '' + 'H' + 'V = 'HV'
1       'Y'        'A'         'HV' + 'Y' + 'A = 'HVYA'
2       'D'        'M'         'HVYA' + 'D' + 'M = 'HVYADM'
--------------------------------------------------------

Concatenate remainging characters of the other string to object 'c'
What is the final result ? ---> 'HVYADMSI'

Hint: Use single while loop and slice
'''
s1 = input("Enter first string  : ")
s2 = input("Enter second string : ")

output = ""
i = 0
j = 0

while i < len(s1) and j < len(s2):
    output = output + s1[i] + s2[j]
    i += 1
    j += 1

output = output + s1[i:] + s2[j:]

print("Result  :", output)



#9
'''
Write a program to remove duplicate characters of the string without using set

1) Let input be RAMA RAO
   What is the output? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M'  = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What action to be made if the character is not in out object? ---> Concatenate the character to out object

4) What action to be made if the character is already in out object? ---> Ignore the character

5) Hint: Use not in operator
'''
s = input("Enter any string : ")

out = ""

for char in s:
    if char not in out:
        out = out + char
    else:
        pass

print("String without duplicates : ", out)



#10
# len()  function  demo  program  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('+-$')) #3
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
print(len(3456)) #Error as len() function only applies for only sequence objects but not non-sequence objects like int object i.e. 3456
print('Sec'. len()) #Error as str object doesn't have any attribute as len()



#11
# chr()  function  demo  program
print(chr(65)) #A
print(chr(90)) #Z
print(chr(97)) #a
print(chr(122)) #z
print(chr(48)) #0
print(chr(57)) #9
print(chr(36)) #$
print(chr(32)) #<space>



#12
# ord()  function  demo  program
print(ord('A')) #65
print(ord('Z')) #90
print(ord('a')) #97
print(ord('z')) #122
print(ord('0')) #48
print(ord('9')) #57
print(ord('$')) #36
print(ord(' ')) #32



#13
'''
Let input be A4M3Z5D2

What is the output? ---> AEMPZ_DF

 0    1    2    3    4    5    6    7
 A    4    M    3    Z    5    D    2


   i        a[i]      a[i + 1]         out
--------------------------------------------------------------------------
                                       ''
   0        'A'        '4'             '' + 'A' +  'E' = 'AE'
   2        'M'        '3'             'AE' + 'M' +  'P' = 'AEMP'
   4        'Z'        '5'             'AEMP' + 'Z' +  '' = 'AEMPZ'
   6        'D'        '2'             'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF'
--------------------------------------------------------------------------
Hint: Use chr() and ord() functions
'''
s = input("Enter any string with alternate character and digit : ")

if len(s) % 2 != 0:
    print("Pls enter string with alternate char and digit")
else:
    out = ""
    for i in range(0, len(s), 2):
        char = s[i]           # Current character
        digit = int(s[i+1])   # Shift value
        
        # 1. Add the original character
        # 2. Add the shifted character using ord() and chr()
        new_char = chr(ord(char) + digit)
        out = out + char + new_char

    print("Result : ", out)



#14
'''
Modify following program with walrus operator

Hint: Combine lines 7, 8 and 10 to a single line with walrus operator
'''
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while index != -1:
    print(index)
    index = a . find('is' , index + 1)
print('End')
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

while (index := a.find('is', locals().get('index', -1) + 1)) != -1:
    print(index)

print('End')



#15
'''  (Homework)
index() method demo program

Modify the following program with index() method
'''
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while index != -1:
    print(index)
    index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
start = 0

try:
    while True:
        pos = a.index('is', start)
        print(pos)
        start = pos + 1
except ValueError:
    pass

print('End')



#16
'''(Homework)
rfind() method demo program

Modify following program with rfind() method
'''
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while index != -1:
    print(index)
    index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is') # Starts looking from the right

while index != -1:
    print(index)
    # Move the search boundary to the left of the current find
    index = a.rfind('is', 0, index)

print('End')



#17
'''  (Homework)
rindex() method demo program

Modify following program  with  rindex()  method

Hint: Use try and except
'''
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while index != -1:
    print(index)
    index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
end_limit = len(a)

try:
    while True:
        # Search from right, restricted by the previous index found
        index = a.rindex('is', 0, end_limit)
        print(index)
        end_limit = index # Update limit to look further left
except ValueError:
    # No more occurrences found
    pass

print('End')



#18
# count() method demo program (Homework)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #3
print(a . count('was')) #0



#19
#Find outputs (Homework)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3