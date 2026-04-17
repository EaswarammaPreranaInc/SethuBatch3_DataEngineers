# Index   demo  program  (Home  work) 
a = 'Hyd' 
print(How  to  print  'H'  of  object  'a') # print(a[0]) 
print(How  to  print  'y'  of  object  'a') # print(a[1]) 
print(How  to  print  'd'  of  object  'a') # print(a[2]) 
print(a[3])  #Error as it exceeds length of string  
print(How  to  print  'd'  of  object  'a') #print(a[-1]) 
print(How  to  print  'y'  of  object  'a') #print(a[-2]) 
print(How  to  print  'H'  of  object  'a') #print(a[-3]) 
print(a[-4]) #Error as it exceeds length of string 
print(a[0] == a[-3]) #True as both the index value point towards “H” 
a[2] = 'c' #Error as strings are immutable  
print(25[0])   #Error as a number cannot be used as start if reference  
print('25'[0]) # 2 as 25 is a string and index position 0 points to 2 
print(True[1]) # Error as True is a reserve word and cannot be used as reference  
print('True'[1]) # r  
#  Find  outputs  (Home work) 
a = 'Hyd' 
print(a * 3) # ‘HydHydHyd’ 
print(a * 2) # ‘HydHyd’ 
print(a * 1) # ‘‘Hyd’ 
print(a * 0) # it doesn’t print anything  
print(a * -1) #Error in repeating we cannot go zero and beyond 
print(25 * 3)  # 75 
print('25' * 3) # ‘252525’ 
print('25' * 4.0) # Error we should take only int not float 
print(3 * 'Hyd') # ‘HydHydHyd’  
print('25' * True) # its 25*1 so 25 
# Tricky  program 
#  Find  outputs  (Home work) 
a = 'Hyd' 
print(a , id(a)) # ’Hyd’ , address of the object Hyd 
a = a * 3  #  It  is  valid  (or)  invalid # Valid  
print(a , id(a)) # ‘HydHydHyd’ , the address of the object changes   
# Find  outputs  (Home  work) 
a = """"Hyd""" 
print(a) # “Hyd 
print(len(a)) # 4 
print(a[0]) # H 
print("""Hyd"""") # Error 
b = """""Hyd"""  
print(b) # “”Hyd 
print(len(b))# 5 
# Find  outputs 
a = 'Sankar Dayal Sarma' 
print(a[7 : 12]) # Dayal 
print(a[7 : ]) # Dayal Sarma 
print(a[ : 6]) # Sankar  
print(a[ : ])  # Sankar Dayal Sarma 
print(a[:  : ])  # Sankar Dayal Sarma 
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy 
print(a[0 : : 2]) # Sna aa am 
print(a[1 : : 2]) # akrDylSra 
print(a[-5 : -1]) # Sarm 
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. 
Reverse  string 
print(a[-1:-5:-1]) #amra 
print(a[ : : -2]) #arSlyDrka 
print(a[3 : -3]) # kar Dayal Sa 
print(a[2 : -5]) # nkar Dayal 
print(a[-1:-5]) # default step of slicing is +1 so output is blank  
print(a[3 : 3]) # blank as start and end points are same  
#   0      
17 
1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     
#   S      a      n      k      a       r                    
a 
#  -18   -17   -16   -15    -14   -13    -12        
2      -1 
#  Find  outputs  (Home  work) 
a =  'A' 
print(a[1]) # Error 
print(a[1:]) # Error  
D       a       y      a       l                     -11     -10    -9     -8    -7      -6          
S       
a         -5      
r       -4       
m       -3      