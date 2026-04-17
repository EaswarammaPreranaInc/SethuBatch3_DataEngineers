#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a)   -- Rama Rao
print(type(a)) - class str
print(id(a)) - 4000 (id means reference of object Rama Rao)
b = 'Hyd'
print(b) -- Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) --  Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a')   --- print (a[0])
print(How  to  print  'y'  of  object  'a')   --- print (a[1])
print(How  to  print  'd'  of  object  'a')  --- print (a[2])
print(a[3])     ------ error
print(How  to  print  'd'  of  object  'a') -- print (a[-1])
print(How  to  print  'y'  of  object  'a') -- print (a[-2])
print(How  to  print  'H'  of  object  'a') - print (a[-3])
print(a[-4])   -- error 
print(a[0] == a[-3]) 
a[2] = 'c' 
print(25[0])   - error
print('25'[0])  --- 2
print(True[1])  - error
print('True'[1]) -- r

#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) -- HydHydHyd
print(a * 2) - HydHyd
print(a * 1) --Hyd
print(a * 0)   -error
print(a * -1)  --error
print(25 * 3)
print('25' * 3)
print('25' * 4.0)  
print(3 * 'Hyd')
print('25' * True)

# Tricky  program
#  Find  outputs  (Home work)
a = 'Hyd'
print(a , id(a))  ---- Hyd ,2000
a = a * 3  #  It  is  valid  (or)  invalid
print(a , id(a))    ---error

# len()  function  (Home  work)
print(len('Hyd'))   -- 3
print(len('Rama Rao')) --- 7
print(len('9247')) -- 4
print(len('')) - 0
print(len(' ')) -- 1
print(len(689)) - 3

# Find  outputs  (Home  work)
a = """"Hyd"""
print(a)   -- Hyd
print(len(a)) - 3
print(a[0]) -- H
print("""Hyd"""")  - Hyd
b = """""Hyd"""
print(b)  #
print(len(b)) - 3

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])  -- Daya
print(a[7 : ])  - Dayal Sharma
print(a[ : 6])   - Sankar	
print(a[ : ])   ---- Sankar Dayal Sharma
print(a[:  : ])   --- Sankar Dayal Sharma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2])   -- Sna aa am 
print(a[1 : : 2])   -- akrDylSra
print(a[-5 : -1])  --Sarma
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) - a
print(a[ : : -2]) 
print(a[3 : -3]) 
print(a[2 : -5]) 
print(a[-1:-5])
print(a[3 : 3]) 


