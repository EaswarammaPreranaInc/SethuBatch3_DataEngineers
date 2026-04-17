# Find outputs (Home work)

a = "Rama Rao"
print(a)           # Rama Rao
print(type(a))     # <class 'str'>
print(id(a))       #  address of string 'Rama Rao'

b = 'Hyd'
print(b)           # Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)          
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.



# Index demo program (Home work)
a = 'Hyd'
print(a[0])          # H   
print(a[1])          # y    
print(a[2])          # d    
print(a[3])          # Error 
print(a[2])          # d
print(a[1])          # y
print(a[0])          # H
print(a[-4])         # Error 
print(a[0] == a[-3]) # True  -> a[0]='H', a[-3]='H'
a[2] = 'c'           # Error 
print(25[0])          # Error 
print('25'[0])        # 2
print(True[1])        # Error 
print('True'[1])      # r                                 






# Find outputs (Home work)

a = 'Hyd'

print(a * 3)        # HydHydHyd
print(a * 2)        # HydHyd
print(a * 1)        # Hyd
print(a * 0)        # It prints nothing (just a blank)
print(a * -1)       # It prints nothing (just a blank)
print(25 * 3)       # 75
print('25' * 3)     # 252525
print('25' * 4.0)   # Error
print(3 * 'Hyd')    # HydHydHyd
print('25' * True)  # 25







# Tricky program
# Find outputs (Home work)

a = 'Hyd'
print(a , id(a))      #  address of 'Hyd' 

a = a * 3             
print(a , id(a))      # address of  'hydhydhyd'




# len()  function  (Home  work)
print(len('Hyd'))       # 3
print(len('Rama Rao'))  # 8
print(len('9247'))      # 4
print(len(''))          # 0
print(len(' '))         # 1
print(len(689))         # Error



# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)          # "Hyd
print(len(a))     # 4
print(a[0])       # "
print("""Hyd"""") # Error

b = """""Hyd"""
print(b)          # ""Hyd
print(len(b))     # 5



# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])     # string from indexes 7 to 11 i.e. Dayal
print(a[7 : ])       # string from index 7 to end i.e. Dayal Sarma
print(a[ : 6])       # string from index 0 to 5 i.e. Sankar
print(a[ : ])        # complete string from start to end i.e. Sankar Dayal Sarma
print(a[:  : ])      # complete string from start to end i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2]) # string from indexes 1 to 9 in steps of 2 i.e. akrDy
print(a[0 : : 2])    # string from index 0 to end in steps of 2 i.e. Sna aa am
print(a[1 : : 2])    # string from index 1 to end in steps of 2 i.e. akrDylSra
print(a[-5 : -1])    # string from index -5 to -2 i.e. Sarm
print(a[::-1])       # string from index -1 to -18 in steps of -1 i.e. amraS layaD raknaS
print(a[-1:-5:-1])   # string from index -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2])    # string from index -1 to -18 in steps of -2 i.e. arSlyDkanS
print(a[3 : -3])     # string from index 3 to -4 i.e. kar Dayal Sa
print(a[2 : -5])     # string from index 2 to -6 i.e. nkar Dayal
print(a[-1:-5])      # string from index -1 to -5 in positive step i.e. empty string
print(a[3 : 3])      # string from index 3 to 2 i.e. empty string




#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1








#  Find  outputs  (Home  work)
a =  'A'
print(a[1])     #Error
print(a[1:])    #It prints nothing (just a blank)
