 #  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  ==== Rama Rao
print(type(a)) ==== class 'str'
print(id(a))   ==== Address of object string " Rama Rao "
b = 'Hyd'
print(b)       ==== Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)         ====        Hyd is green city.
                             Hyd is hitec city.     Here string object has reference c. So it is not a comment.
                             Hyd is beautiful city.        
# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')   ==== print(a[0])
print(How  to  print  'y'  of  object  'a')   ==== print(a[1])
print(How  to  print  'd'  of  object  'a')   ==== print(a[2])
print(a[3])                                   ==== Error because no alphabet at index 3   
print(How  to  print  'd'  of  object  'a')   ==== print(a[-1])
print(How  to  print  'y'  of  object  'a')   ==== print(a[-2])
print(How  to  print  'H'  of  object  'a')   ==== print(a[-3])
print(a[-4])                                  ==== Error because no alphabet at index -4
print(a[0] == a[-3])   ==== True because a[0] and a[-3] both indexes have same alphabet H
a[2] = 'c'             ==== Error string objects are immutable.
print(25[0])           ==== Error
print('25'[0])         ==== 2
print(True[1])         ==== Error
print('True'[1])       ==== r
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)  ==== HydHydHyd
print(a * 2)  ==== HydHyd
print(a * 1)  ==== Hyd
print(a * 0)  ==== empty(none)
print(a * -1) ==== dyHdyH
print(25 * 3) ==== 75
print('25' * 3) ==== 252525
print('25' * 4.0)  ==== Error
print(3 * 'Hyd')    ===== HydHydHyd
print('25' * True)  ===== 25 because we performing operation on True = 1 
 # Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  ==== Hyd Address of object
a = a * 3  #  It  is  valid  (or)  invalid ==== Valid
print(a , id(a))  ===== HydHydHyd Address of object
 # len()  function  (Home  work)
print(len('Hyd')) ==== 3
print(len('Rama Rao')) ==== 8
print(len('9247'))  ===== 4
print(len(''))      ==== 0
print(len(' '))     ==== 1
print(len(689))     ==== int has no length
 # Find  outputs  (Home  work)
a = """"Hyd"""
print(a)  ====  Error
print(len(a))  ====  Error
print(a[0])    ====  Error  if program has syntax error then rest of the code will be ignored
print("""Hyd"""")   Error
b = """""Hyd"""   
print(b)  #  Error because syntax error left side 4 " and right side 3 "
print(len(b)) ==== error
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  ===== Dayal_
print(a[7 : ])    ===== Dayal sarma
print(a[ : 6])    ===== Sankar 
print(a[ : ])     ====  Sankar Dayal Sarma
print(a[:  : ])   ===== Sankar Dayal Sarma it is cocept of slicing start = 0: end = 0 : step = 1(Default)                                                    
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])  ===== Sna_aa_am starts from index 0 and end is given and step 2 
print(a[1 : : 2])  ===== akrDylSra 
print(a[-5 : -1])  ===== Sarma         S       a       r       m      a
                                      -5      -4      -3       -2    -1
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])   ==== amra
print(a[ : : -2])    ==== arSlyDrka   arSlyaDaknS
print(a[3 : -3])     ==== kar Dayal Sa
print(a[2 : -5])     ==== nkar Dayal
print(a[-1:-5])      ==== amraS 
print(a[3 : 3])      ==== empty str ''



#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                   D       a       y      a      l                   S       a       r       m      a
    -18   -17    -16    -15    -14     -13       -12       -11     -10     -9     -8      -7      -6         -5      -4      -3       -2    -1
 #  Find  outputs  (Home  work)
a =  'A'
print(a[1])    ==== Error
print(a[1:])   ==== '' empty