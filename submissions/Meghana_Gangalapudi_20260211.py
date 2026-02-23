Meghana Gangalapudi





#  Find  outputs  (Home  work)

a = "Rama Rao"
print(a)                               #Rama Rao
print(type(a))                         #<class 'str'>
print(id(a))                           #123456789
b = 'Hyd'
print(b)                               #Hyd
c = '''Hyd is green city.
       Hyd is hitec city.
       Hyd is beautiful city.'''
print(c)                               #Hyd is green city.
                                        Hyd is hitec city.
                                        Hyd is beautiful city.





# Index   demo  program  (Home  work)

a = 'Hyd'
print(How  to  print  'H'  of  object  'a')     #print(a[0])
print(How  to  print  'y'  of  object  'a')     #print(a[1])
print(How  to  print  'd'  of  object  'a')     #print(a[2])
print(a[3])                                     #Error string index out of range
print(How  to  print  'd'  of  object  'a')     #print(a[-1])
print(How  to  print  'y'  of  object  'a')     #print(a[-2])
print(How  to  print  'H'  of  object  'a')     #print(a[-3])
print(a[-4])                                    #Error string index out of range
print(a[0] == a[-3])                            #True
a[2] = 'c' 
print(25[0])                                    #Error - In the given string c is not there. 
print('25'[0])                                  #
print(True[1])                                  #Error - 'bool' object is not mentioned in quotes.
print('True'[1])                                #r








#  Find  outputs  (Home work)

a = 'Hyd'
print(a * 3)                  #HydHydHyd
print(a * 2)                  #HydHyd
print(a * 1)                  #Hyd
print(a * 0)                  #Here we are multiplying the object value with 0 so we don't get any string (string can be empty ).
print(a * -1)                 #Here we are multiplying the object value with -1 that is negative number so we don't get any string as like above  (string can be empty ).
print(25 * 3)                 #75
print('25' * 3)               #252525
print('25' * 4.0)             #Error - can't multiply sequence by non-int of type 'float'.
print(3 * 'Hyd')              #HydHydHyd
print('25' * True)            #25



# Tricky  program
#  Find  outputs  (Home work)

a = 'Hyd'
print(a , id(a))                                  #Hyd 123456789
a = a * 3  #  It  is  valid  (or)  invalid        #Valid - HydHydHyd
print(a , id(a))                                  #987654321 Address is changed because the reference is pointing new object value after performing a*3 operation.




# len()  function  (Home  work)

print(len('Hyd'))                  #3
print(len('Rama Rao'))             #8
print(len('9247'))                 #4 ( the numbers are inside the quotes so considered as string but not integers.)
print(len(''))                     #0
print(len(' '))                    #1 ( space is also counted )
print(len(689))                    #Error becz the number 689 is not placed in quotes and so we are not considering it as a string.




Find  outputs  (Home  work)

a = """"Hyd"""
print(a)                           #"Hyd
print(len(a))                      #4
print(a[0])                        #"
print("""Hyd"""")                  #error becz the double quotes are balanced.  
b = """""Hyd"""
print(b)                           #""Hyd  

print(len(b))                      #5


# Find  outputs

a = 'Sankar Dayal Sarma'
print(a[7 : 12])                  #Dayal
print(a[7 : ])                    #Dayal Sarma
print(a[ : 6])                    #Sankar
print(a[ : ])                     #Sankar Dayal Sarma
print(a[:  : ])                   #Sankar Dayal Sarma
print(a[1 : 10 : 2])              #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])                 #Snaaa ar
print(a[1 : : 2])                 #akrDylSra
print(a[-5 : -1])                 #Sarm
print(a[::-1])                    #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])                #amra
print(a[ : : -2])                 #arSlyDrka
print(a[3 : -3])                  #kar Dayal Sa
print(a[2 : -5])                  #nkar Dayal
print(a[-1:-5])                   #empty space
print(a[3 : 3])                   #empty space



#   0      1      2      3      4       5      6      7       8      9     10     11     12       13     14       15      16     17
#   S      a      n      k      a       r             D       a      y      a     l                S      a       r       m       a
#  -18   -17    -16    -15    -14     -13    -12     -11     -10    -9     -8    -7      -6       -5     -4      -3       -2     -1




#  Find  outputs  (Home  work)

a =  'A'
print(a[1])            #String has only one character and it's index is 0. so, we cannot access index 1
print(a[1:])           #same applies as above.




































