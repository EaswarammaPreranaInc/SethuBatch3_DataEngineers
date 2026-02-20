#String Object Demo Program

a="Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class 'str'>
print(id(a)) # 5000
b='Hyd'
print(b) # Hyd
c='''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city.
         # Hyd is hitec city.
         # Hyd is beautiful city.


#Index Demo Program

a='Hyd'
print(a[0]) # H
print(a[1]) # y
print(a[2]) # d
#print(a[3]) # Error because there is no character at index 3
print(a[-1]) # d
print(a[-2]) # y
print(a[-3]) # H
#print(a[-4]) # Error because index goes beyond string length
print(a[0]==a[-3]) # True
#a[2]='c' # Error because string value cannot be changed
#print(25[0]) # Error because number does not support indexing
print('25'[0]) # 2
#print(True[1]) # Error because boolean value cannot be indexed
print('True'[1]) # r


#String Multiplication Program

a='Hyd'
print(a*3) # HydHydHyd
print(a*2) # HydHyd
print(a*1) # Hyd
print(a*0) # 
print(a*-1) # 
print(25*3) # 75
print('25'*3) # 252525
#print('25'*4.0) # Error because string cannot be multiplied by float value
print(3*'Hyd') # HydHydHyd
print('25'*True) # 25


#Tricky Program

a='Hyd'
print(a,id(a)) # Hyd 5000
a=a*3
print(a,id(a)) # HydHydHyd 5001 (new string created so id changes)


#len() Function Program

print(len('Hyd')) # 3
print(len('Rama Rao')) # 8
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
#print(len(689)) # Error because len() works only for strings or collections


#Triple Quote Case

a=""""Hyd"""
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # "
#print("""Hyd"""") # Error because extra double quote at end
b="""""Hyd"""
print(b) # ""Hyd
print(len(b)) # 5


#Slicing Demo Program

a='Sankar Dayal Sarma'
print(a[7:12]) # Dayal
print(a[7:]) # Dayal Sarma
print(a[:6]) # Sankar
print(a[:]) # Sankar Dayal Sarma
print(a[::]) # Sankar Dayal Sarma
print(a[1:10:2]) # akrDy
print(a[0::2]) # Sna aa am
print(a[1::2]) # akrDylSra
print(a[-5:-1]) # sarm
print(a[::-1]) # amraS layaD raknaS
print(a[-1:-5:-1]) # amra
print(a[::-2]) # arSlyDrka
print(a[3:-3]) # kar Dayal Sa
print(a[2:-5]) # nkar Dayal
print(a[-1:-5]) #  (no output because step is positive but start is greater than stop)
print(a[3:3]) #  (empty string because start and stop are same)


#Single Character Case

a='A'
#print(a[1]) # Error because index 1 does not exist
print(a[1:]) #  (empty string)
