#  Find  outputs  (Home  work)
a = "Rama Rao"                                            
print(a)                                                           # Rama Rao
print(type(a))                                               # <class ‘str’>
print(id(a))                                                    # address of str object ‘Rama Rao’
b = 'Hyd'
print(b)                                                          #Hyd
c = '''Hyd is green city.                           
Hyd is hitech city.                                       
Hyd is beautiful city.'''                             
print(c)                                                         # Hyd is green city.
                                                                        Hyd is hitech city.
                                                                        Hyd is beautiful city.



# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')                                # print(a[0])
print(How  to  print  'y'  of  object  'a')                                  # print(a[1])     
print(How  to  print  'd'  of  object  'a')                                 # print(a[2])               
print(a[3])                                                                                        #error index out of range
print(How  to  print  'd'  of  object  'a')                                 #print(a[-1])
print(How  to  print  'y'  of  object  'a')                                  #print(a[-2])
print(How  to  print  'H'  of  object  'a')                                 #print(a[-3])
print(a[-4])                                                                                       #error index out of range
print(a[0] == a[-3])                                                                        #True
a[2] = 'c'                                                                                            #reference should be in the left side
print(25[0])                                                                                      # error 25 can’t have index
print('25'[0])                                                                                    # 2
print(True[1])                                                                                 # error True is bool and no index
print('True'[1])                                                            #r



#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)                                                         #HydHydHyd
print(a * 2)                                                         #HydHyd
print(a * 1)                                                         #Hyd
print(a * 0)                                                        # empty
print(a * -1)                                                       #empty
print(25 * 3)                                                      #75
print('25' * 3)                                                    #252525
print('25' * 4.0)                                                #25252525
print(3 * 'Hyd')                                                 #HydHydHyd
print('25' * True)                                             #25



# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))                                                                                 #Hyd , address of str object ‘Hyd’
a = a * 3  #  It  is  valid  (or)  invalid                                         #valid         
print(a , id())                                                                #HydHydHyd , address of str object ’HydHydHyd’



# len()  function  (Home  work)
print(len('Hyd'))                                                                      #3
print(len('Rama Rao'))                                                         #8 
print(len('9247'))                                           #4                                       
print(len(''))                                                     #0
print(len(' '))                                                    #1
print(len(689))                                               #error  due to 689 is int class object



# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)                                                                          #”Hyd
print(len(a))                                                                 #4
print(a[0])                                                                     #”                            
print("""Hyd"""")    #error
b = """""Hyd"""
print(b)                                                                          #””Hyd
print(len(b))                                                                 #5




# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])          # [7:12:1]          #string from indexes 7 to 11 in steps of 1 i.e. Dayal
print(a[7 : ])               #[7:18:1]             #string from indexes 7 to 17 in step of 1 i.e. Dayal Sarma
print(a[ : 6])               #[0:6:1]              #string from indexes 0 to 5 in step of 1 i.e. Sankar
print(a[ : ])               #[0:18:1]            #string from indexes 0 to 17 in step of 1 i.e. Sankar Dayal Sarma
print(a[:  : ])              #[0:18:1]         #string from indexes 0 to 17 in step of 1 i.e. Sankar Dayal Sarma
print(a[1 : 10 : 2])                                     #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])          #[0:18:2]              #string from indexes 0 to 17 in step of 2 i.e. Sna aa am
print(a[1 : : 2])         #[1:18:2]                          #string from indexes 1 to 17 in step of 2 i.e. akrDylSra
print(a[-5 : -1])          #[-5:-1:1]                       #string from indexes -5 to -2 in step of 1 i.e. Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1])                               # string from indexes -1 to -4 in step of -1 i.e . amra
print(a[ : : -2])           [-1:-18:-2]         #string from indexes -1 to -18 in step  of -2 i.e. arSlyDrka
print(a[3 : -3])                                        #string from indexes 3 to -2 in step of 1 i.e. kar Dayal Sarm
print(a[2 : -5])      [2:-5:1]            #string from indexes 2 to -6 in step of 1 i.e. nkar Dayal 
print(a[-1:-5])        [-1:-5:1]       #string from -1 to -6 in step of 1 is not possible (empty)
print(a[3 : 3])       [3:3:1]             # string from 3 to 2 in step of 1 is not possible (empty)



#     0      1      2        3       4       5        6           7         8        9       10     11     12      13     14       15      16     17
#     S      a      n        k        a        r                     D         a        y       a         l                    S       a          r        m        a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8        -7      -6       -5      -4       -3      -2      -1




 
