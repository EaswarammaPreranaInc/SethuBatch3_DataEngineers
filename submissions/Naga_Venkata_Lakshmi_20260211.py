#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) #Rama Rao
print(type(a)) #<class 'str>
print(id(a)) #Address of the string Rama Rao
b = 'Hyd'
print(b) #Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) #Hyd is green city.
          Hyd is hitec city.
          Hyd is beautiful city.



# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])
print(a[1])
print(a[2])
print(a[3]) #Error because there is no index  
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4]) #Error because there is no index
print(a[0] == a[-3]) #True
a[2] = 'c' #Error
print(25[0]) #Error because we can't use indexing on an integer   
print('25'[0]) #2
print(True[1]) #Error because it is not a sequence and True is a Boolean value
print('True'[1]) #r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) #HydHydHyd
print(a * 2) #HydHyd
print(a * 1) #Hyd
print(a * 0) #Empty string
print(a * -1) #Empty string
print(25 * 3) #75
print('25' * 3) #Error
print('25' * 4.0)  #Error 
print(3 * 'Hyd') #HydHydHyd
print('25' * True) #'25'

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a)) #Hyd,Address of string Hyd
a = a * 3  #  It  is  valid  (or)  invalid  valid 
print(a, id(a)) #HydHydHyd ,Address of string HydHydHyd

# len()  function  (Home  work)
print(len('Hyd')) #3
print(len('Rama Rao')) #8
print(len('9247')) #4
print(len('')) #0
print(len(' ')) #1
print(len(689)) #error because we should not use len() directly on an integer


# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) #"Hyd
print(len(a)) #4
print(a[0]) #"
print("""Hyd"""") #Hyd  
b = """""Hyd"""
print(b)  #"Hyd
print(len(b)) #4

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #Dayal
print(a[7 : ]) #Dayal Sarma
print(a[ : 6])  #Sankar 
print(a[ : ])   #Sankar Dayal Sarma
print(a[:  : ])  #Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #Sna aa am
print(a[1 : : 2]) #akrDylsra
print(a[-5 : -1]) #Sarm
print(a[::-1])  # amras layaD raknaS   a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) #amras layaD
print(a[ : : -2])  #arslyDrka
print(a[3 : -3])   #kar Dayal Sarm
print(a[2 : -5])   #nkar Dayal Sa
print(a[-1:-5])    #Empty string
print(a[3 : 3])    #Empty string


#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) #Empty string
print(a[1:]) #Empty string