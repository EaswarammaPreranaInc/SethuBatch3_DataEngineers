#  Find outputs  (Homework) 
a = "Rama Rao" 
print(a) #output: Rama Rao 
print(type(a)) #output:< class ‘str’> 
print(id(a)) #output: identity of an object 
b = 'Hyd' 
print(b) #output:Hyd 
c = '''Hyd is green city. 
Hyd is hitec city. 
Hyd is beautiful city.''' 
print(c)  
#output: 
'''Hyd is green city. 
Hyd is hitec city. 
Hyd is beautiful city. 
# Index   demo  program  (Home  work) 
a = 'Hyd' 
print(How  to  print  'H'  of  object  'a') 
print(How  to  print  'y'  of  object  'a') 
print(How  to  print  'd'  of  object  'a') 
print(a[3])  #output:Error 
print(How  to  print  'd'  of  object  'a') 
print(How  to  print  'y'  of  object  'a') 
print(How  to  print  'H'  of  object  'a') 
print(a[-4]) #output:Error 
print(a[0] == a[-3]) #output:True 
a[2] = 'c'  
print(25[0])   #output:Error 
print('25'[0]) #output:2 
print(True[1]) #output:Error 
print('True'[1]) #output:r 
#  Find  outputs  (Home work) 
a = 'Hyd' 
print(a * 3) #output:HydHydHyd 
print(a * 2) #output:HydHyd 
print(a * 1) ) #output:Hyd 
print(a * 0)  #output:empty 
print(a * -1)  #output:empty 
print(25 * 3) #output:75 
print('25' * 3) #output:252525 
print('25' * 4.0)  #output:Error 
print(3 * 'Hyd') #output:HydHydHyd 
print('25' * True) #output:25 
# Tricky  program 
#  Find  outputs  (Home work) 
a = 'Hyd' 
print(a , id(a)) ) #output:Hyd identity of an object 
a = a * 3  #  It  is  valid  (or)  invalid #output:valid 
print(a , id(a)) ) #output:HydHydHyd 
# len()  function  (Home  work) 
print(len('Hyd')) ) #output:3 
print(len('Rama Rao')) ) #output:8 
print(len('9247')) ) #output:4 
print(len('')) ) #output:0 
print(len(' ')) ) #output:1 
print(len(689)) ) #output:Error 
# Find  outputs  (Home  work) 
a = """"Hyd""" 
print(a)  #output:”Hyd 
print(len(a)) #output:4 
print(a[0])  #output: ” 
print("""Hyd"""")  #output:Error 
b = """""Hyd""" 
print(b)  #output:””Hyd 
print(len(b))  #output:5 
# Find  outputs 
a = 'Sankar Dayal Sarma' 
print(a[7 : 12])  #output: Dayal 
print(a[7 : ]) #output:Dayal Sarma 
print(a[ : 6])  #output: Sankar 
print(a[ : ])   #output:Sankar Dayal Sarma 
print(a[:  : ]) #output: Sankar Dayal Sarma 
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy 
print(a[0 : : 2])  #output:Sna aa am 
print(a[1 : : 2])  #output:akrDylSra 
print(a[-5 : -1]) #output:Sarm 
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. 
Reverse  string #output: amraS layaD raknaS 
print(a[-1:-5:-1]) #output:amra 
print(a[ : : -2])  #output: arSlyDrka 
print(a[3 : -3])  #output: kar Dayal Sa 
print(a[2 : -5])  #output: nkar Dayal 
print(a[-1:-5])  #output:<empty> 
print(a[3 : 3])  #output:<empty> 
#   0      1      2      3      4       5       6      7       8       9     10     11     12     13     14   15     16    17 
#   S      a      n      k      a       r              D       a       y      a      l             S      a    r      m     a          
#  Find  outputs  (Home  work) 
a =  'A' 
print(a[1])  #output:Error 
print(a[1:])  #output: Error