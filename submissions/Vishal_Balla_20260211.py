Day - 2 python
  
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)  -->>  Rama Rao
print(type(a))  -->>  <class 'str'>
print(id(a))  -->> returns address of an object
b = 'Hyd'
print(b)  -->>  Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)  -->>  Hyd is green city.
                Hyd is hitec city. 
                Hyd is beautiful city


# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')  -->>  a[0]
print(How  to  print  'y'  of  object  'a')  -->>  a[1]
print(How  to  print  'd'  of  object  'a')  -->>  a[2]
print(a[3])  >>  error  
print(How  to  print  'd'  of  object  'a')  -->>  a[-1]
print(How  to  print  'y'  of  object  'a')  -->>  a[-2]
print(How  to  print  'H'  of  object  'a')  -->>  a[-3]
print(a[-4])  -->>  error
print(a[0] == a[-3])  -->>  True
a[2] = 'c' 
print(25[0])  -->>  error
print('25'[0])  -->>  2
print(True[1])  -->>  error
print('True'[1])  -->>  r


#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)  -->>  HydHydHyd
print(a * 2)  -->>  HydHyd
print(a * 1)  -->>  Hyd
print(a * 0)  -->>  '' #empty string
print(a * -1) -->>  '' #empty string
print(25 * 3)  -->>  75
print('25' * 3)  -->>  252525
print('25' * 4.0)  -->>  error
print(3 * 'Hyd')  >> HydHydHyd
print('25' * True)  >>  error


# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  -->>  Hyd, address of an object
a = a * 3  #  It  is  valid  (or)  invalid
print(a , id(a))  -->>  HydHydHyd, address of an object

print(len('Hyd'))  -->> 3
print(len('Rama Rao'))  -->> 8
print(len('9247'))  -->>  4
print(len(''))  -->>  0
print(len(' '))  -->>  1
print(len(689))  -->>  error


a = """"Hyd"""
print(a)  -->>  "Hyd
print(len(a))  -->>  3
print(a[0])  -->>  "
print("""Hyd"""")  -->>  error  
b = """""Hyd"""
print(b)  -->>  ""Hyd
print(len(b))  -->>  5


# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  -->>  Dayal
print(a[7 : ])  -->>  Dayal Sarma
print(a[ : 6])  -->>  Sarkar 
print(a[ : ])  -->>  Sankar Dayal Sarma
print(a[:  : ])  -->>  Sankar Dayal Sarma
print(a[1 : 10 : 2])  -->>  akrDy #string  from  indexes  1  to  9  in  steps  of  2 
print(a[0 : : 2])   -->>  Sna aa am 
print(a[1 : : 2])  -->>  akrDylsra
print(a[-5 : -1])  -->>  sarm
print(a[::-1])  -->>  amraS layaD raknaS
print(a[-1:-5:-1])  -->>  amra
print(a[ : : -2])  -->>  arSlyDrka
print(a[3 : -3])  -->>  kar Dayal Sa
print(a[2 : -5])  -->>  nkar Dayal
print(a[-1:-5])  -->>  amra
print(a[3 : 3])  -->>  ""


#  Find  outputs  (Home  work)
a =  'A'
print(a[1])  -->>  Error
print(a[1:])  -->>  ""  # empty