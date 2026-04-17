#1
'''
Write a program to print
        A
       A B
      A B C
     A B C D
    A B C D E

Input is number of lines

1)  ord('A') = 65
    ord('B') = 66
    ord('C') = 67
    .....
    ord('Z') = 90
    
2)  chr(65) = 'A'
    chr(66) = 'B'
    chr(67) = 'C'
    .....
    chr(90) = 'Z'
    
3)  ch = 'A'
    ch += 1
    Is the statement valid ? ---> No becoz operand2 should be a sequence when operand1 is a sequence

4) ch = 'A'
    How to increment variable ch by 1? ---> ch = chr(ord(ch) + 1)
'''
n = int(input("Enter number of lines: "))

for i in range(n):
    
    for j in range(n - i - 1):
        print(" ", end="")
        
    for j in range(i + 1):
        char = chr(65 + j)
        print(char, end=" ")
        
    print()

#2
# Find  outputs  (Home  work)
for i in range(1 , 8):
    print(i) # 1 | 2 | 3 | 4 | 5 | 6 | 7
    if i % 3 == 0:
        pass
        print('Hyd') #   |    | Hyd |    |    | Hyd |    |
    else:
        print('Sec') # Sec | Sec |     | Sec | Sec |    | Sec |
    print('Hello') #Hello | Hello | Hello | Hello | Hello | Hello | Hello 
# End  of  the  loop
print('Outside loop') #Outside loop

#3
# Find  outputs  (Home  work)
for i in range(1 , 8):
    print(i) # 1 | 2 | 3 
    if i % 3 == 0:
        exit() 
    else:
        print('Sec') #Sec | Sec  
    print('Hello') #Hello | Hello
# End  of  the  loop
print('Outside loop') 


