DEVIREDDY VENNELA
Q1)
a = "Rama Rao"
 print(a) #Rama Rao
 print(type(a)) #<class 'str'>
 print(id(a)) # address of object a
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitech city.
Hyd is beautiful city.'''
print(c) #Hyd is green city.
                 Hyd is hitech city.
                 Hyd is beautiful city.

Q2)

# Index   demo  program  (Home  work)
 a = 'Hyd'
 print(How  to  print  'H'  of  object  'a')
Output: print(a[0])
 print(How  to  print  'y'  of  object  'a')
Output: print(a[1])
 print(How  to  print  'd'  of  object  'a')
Output:print(a[2])  
 print(How  to  print  'd'  of  object  'a')
Output:print(a[-1])
 print(How  to  print  'y'  of  object  'a')
Output:print(a[-2])
 print(How  to  print  'H'  of  object  'a')
Output:Print(a[-3])
print(a[-4]) Output: Index error
 print(a[0] == a[-3]) Output: 'H'='H'
 a[2] = 'c'    output:type error 
 print(25[0])   output: type error because int object is not acceptable.
 print('25'[0]) output:2
 print(True[1]) output: type error because bool objects are not acceptable.
print('True'[1]) output:r


Q3)

a = 'Hyd'
print(a * 3) output: HydHydHyd
print(a * 2) output:HydHyd
print(a * 1) output:Hyd
print(a * 0) output: empty space
print(a * -1) Output: empty space 
print(25 * 3) output:75 because 25 is a int
print('25' * 3) Output:252525
print('25' * 4.0)  Output:error because of 4.0 is a float
print(3 * 'Hyd') Output: HydHydHyd
print('25' * True) Output:25

Q4)

# Tricky  program

a = 'Hyd'
print(a , id(a))  Output: Hyd address of object Hyd
a = a * 3  #  It  is  valid  (or)  invalid     answer:valid
print(a , id(a)) output: HydHydHyd address of Hyd

Q5) 

# len()  function  
print(len('Hyd')). Output:3
print(len('Rama Rao')) Output:8
print(len('9247')) Output:4
print(len('')) output:0
print(len(' ')) output:1
print(len(689)) output: error because it is a int type

Q6)
a = """"Hyd"""
print(a)  Output: Hyd
print(len(a))  Output:3
print(a[0])  output: "
print("""Hyd"""")    Output:error because extra double quote
b = """""Hyd"""
print(b)  Output "" Hyd
print(len(b)) Output:5

Q7)

# Find  outputs
a = 'Sankar Dayal Sarma'
 print(a[7 : 12]) #Dayal 
 print(a[7 : ]) #Dayal Sarma
 print(a[ : 6])   #Sankar
 print(a[ : ])  #Sankar Dayal Sarma 
 print(a[:  : ])  #Sankar Dayal Sarma
 print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
 print(a[0 : : 2]) #Sna aa am
 print(a[1 : : 2]) #akrDylSra
 print(a[-5 : -1]) #Sarm
 print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])  # amra
 print(a[ : : -2]) #arSlyDrka (Reverse)
 print(a[3 : -3]) # Kar Dayal Sa (in between 3 and -3)
 print(a[2 : -5]) #nKar Dayal (in between 2 to -5)
print(a[-1:-5]) # empty 
 print(a[3 : 3]) # empty
#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1


Q8)

a =  'A'
print(a[1]) Output: error because it is not a string 
print(a[1:]) output: error because it is not a string 
