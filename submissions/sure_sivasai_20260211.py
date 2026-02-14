# 1. Find  outputs  (Home  work)
a = "Rama Rao"     
print(a)                   # Rama Rao      
print(type(a))             # <class 'str'>
print(id(a))               # Address of object a
b = 'Hyd'               
print(b)                   # Hyd
c = '''Hyd is green city.  
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)                   # output for this print(c)                
"""
   Hyd is green city.
   Hyd is hitec city.
   Hyd is beautiful city.
"""

# 2. Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])          # How  to  print  'H'  of  object  'a'
print(a[1])          # How  to  print  'y'  of  object  'a'
print(a[2])          # How  to  print  'd'  of  object  'a'
print(a[3])          # Error becoz there is no index 3
print(a[-1])          # How  to  print  'd'  of  object  'a'
print(a[-2])         # How  to  print  'y'  of  object  'a'
print(a[-3])         # How  to  print  'H'  of  object  'a'
print(a[-4])         # Error becoz there is no index -4
print(a[0] == a[-3]) # True
a[2] = 'c'           # Error Becoz we can not replace str directly
print(25[0])         # Error the int is immutuable so we can not access
print('25'[0])       # 2
print(True[1])       # Error we can not access In True keyword
print('True'[1])     # r


# 3. Find  outputs  (Home work)
a = 'Hyd'         
print(a * 3)       # 'HydHydHyd'
print(a * 2)       # 'HydHyd'
print(a * 1)       # 'Hyd'
print(a * 0)       # Empty
print(a * -1)      # Empty
print(25 * 3)      # 75
print('25' * 3)    # '252525'
print('25' * 4.0)  # Error But i think output as '25252525' 
print(3 * 'Hyd')   # 'HydHydHyd'
print('25' * True) # '25'


# 4. Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))                             # Hyd Address of Object a
a = a * 3  #  It  is  valid  (or)  invalid   # Valid it stores 'HydHydHyd'
print(a , id(a))                             # 'HydHYdHYd' different Address of object a


# 5. len()  function  (Home  work)
print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len(''))           # 0
print(len(' '))          # 1
print(len(689))          # Error becoz the Integer doesn't have any index 


# 6. Find  outputs  (Home  work)
a = """"Hyd"""     
print(a)          # "Hyd
print(len(a))     # 4
print(a[0])       # "
print("""Hyd"""") # Error the right side double codes should be equal or less than as compared to left side
b = """""Hyd"""   
print(b)          # ""Hyd
print(len(b))     # 5




# 7. Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])          # string from indexes 7 to 11  i.e Dayal
print(a[7 : ])            # string from indexes 7 to end i.e Dayal Sarma
print(a[ : 6])            # string from indexes 0 to 5   i.e Sankar
print(a[ : ])             # string from indexes 0 to 17  i.e Sankar Dayal Sarma
print(a[:  : ])           # string from indexes 0 to 17  in steps of 1 i.e Sankar Dayal Sarma
print(a[1 : 10 : 2])      # string from indexes 1 to 9   in steps of 2 i.e. akrDy
print(a[0 : : 2])         # string from indexes 0 to end in steps of 2 i.e Sna aa am
print(a[1 : : 2])         # string from indexes 1 to end in steps of 2 i.e akrDylSra
print(a[-5 : -1])         # string from indexes -5 to -2 in steps of 1 i.e Sarm
print(a[::-1])            # a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])        # string from indexes -1 to -4 in steps of -1  i.e amra
print(a[ : : -2])         # string from indexes -1 to -18 in steps of -2 i.e arSlyDrka
print(a[3 : -3])          # string from indexes 3 to -2 in steps of 1    i.e kar Dayal Sarm
print(a[2 : -5])          # string from indexes 2 to -4 in steps of 1    i.e nkar Dayal Sa 
print(a[-1:-5])           # string from indexes -1 to -4 in steps of 1   i.e amra
print(a[3 : 3])           # string from indexes 3 to 3 will give only one char i.e k


# 8. Find  outputs  (Home  work)
a =  'A'
print(a[1])  # Error 
print(a[1:]) # Error 


