# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city') #True
print('day'   in   'Sankar  dayal  sarma') #True
print('Green'   in   'Hyd  is  green  city') #False
print('d  is'   in   'Hyd  is  green  city') #True
print('dis'   in   'Hyd  is  green  city') #False
print('iniv'   in   'Srinivas') #False
print('iniv'   not   in   'Srinivas') #True



Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #a[0 : 7 :2]  ---> string from indexes 0 to 6 in steps of 2 i.e. Rm<space>a 
print(a [ : 7]) #a[0 : 7 : 1] --->string from indexes 0 to 6 in steps of 1 i.e. Rama<space>Ra 
print(a [2 : 4]) #a[2 : 4 : 1] --->string from indexes 2 to 3 in steps of 1 i.e. ma
print(a [2 : ]) #a[2 : 8 : 1] --->string from indexes 2 to 7 in steps of 1  i.e. ma<space>Rao 
print(a [ : 4 ]) #a[0 : 4 : 1] --->string from indexes 0 to 3 in steps of 1 i.e. Rama
print(a [ : : 2])  #  a[0 : 8 : 2]   --->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1]) # a<space>Rao
print(a [-6 : ]) # a<space>Rao 
print(a [: -4 : -1]) #oaR<space>a
print(a [-3 : -1]) #Ra
print(a [-3 : ]) #Rao
print(a [ : : ]) #Rama<space>Rao
print(a [ : ]) # Rama<space>Rao
print(a [ : : -1])  #oaR<space>amaR
print(a [ : : -2])  #  a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  #oaa
print(a [2 : 8]) #ma<space>Rao
print(a [2 : 8 : -1]) #"
print(a [ : -6 : -1]) #oaR
print(a [2 : -3]) #ma<space>R
print(a [1 : 6 : 2])  #aR
print(a [ : -5 : -5]) #o
print(a [2 : -5]) #ma
print(a [2 : -5 : 2]) #m
print(a [ : 0 : -1]) #oaR<space>ama
print(a [-5 : 0 : -2]) #Rm



s1 = input("Enter first string:   ")
s2 = input("Enter second string:   ")
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
Result = new_s1 + " " + new_s2
print("Result: ", Result)



s3 = input("Enter any string:  ")

if len(s3)<4:
    print("")
else:
    result = s3[:2] + s3[-2:] 
    print("Result: ", result  



s4 = input("Enter the string:  ")
print("String from left to right")
for i in range(len(s4)):
    print(f'Character at index i:  {s4[i]}')
    i+= 1
    
      
    
  
    
print()    
print("String from right to left")
for i in range(len(s4)-1 , -1 , -1):
    print(f'Character ai index i :  {s4[i]}')

    
print()



s = input("Enter any string :  ")
print("Even index characters:",  end =" " )

print("Odd index characters:",  end = " ")

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end = " ")
    else:
        print(s[i], end = " ")  


s1 = input("Enter first string: ")
s2 = input("Enter ssecond string: ")

result = ""
length = min(len(s1),len(s2))

for i in range(length):
    result = result + s1[i] + s2[i]
result = result + s1[length:] + s2[length:]  
print("Merged string: " , result) 



s = input("Enter a string:  ")

result = "" 

for ch in s:
    if ch not in result:
        result = result + ch
print("String after removing duplicates:", result)        



# len()  function  demo  program  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('+-$')) #3
print(len('')) #0
print(len(' ')) #1
print(len('A2#')) #3
print(len(3456)) #Type error
print('Sec'. len()) # syntax error


# chr()  function  demo  program
print(chr(65))  #   A
print(chr(90))  #   Z
print(chr(97))  #   a
print(chr(122)) #   z
print(chr(48))  #   0
print(chr(57))  #   9
print(chr(36))  #   $
print(chr(32))  #   space


# ord()  function  demo  program
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('a')) # 97
print(ord('z')) # 122
print(ord('0')) # 48
print(ord('9')) # 57
print(ord('$')) # 36
print(ord(' ')) # 32



#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))  #3
print(a . count('is' , 19 , 48))  #1
print(a . count('was'))  #0


#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #6
print(a . count('\t')) #3
print(a . count('\n')) #3


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'


try:
    
   index = a. rindex('is')
   while True:
       print(index)
       index = a.rindex('is' , 0 , index)
except ValueError:
   print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')
while index != -1:
       print(index)
       index = a.rfind('is' , 0 , index)
print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'


try:
    index = a.index('is')
    while True:
          print(index)
          index = a.index('is' , index + 1)
except ValueError:
    print('End')



a  = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = 0
while (index  := a.find('is' , index)) != -1:
      print(index)
      index += 1
print('End')















 























  










