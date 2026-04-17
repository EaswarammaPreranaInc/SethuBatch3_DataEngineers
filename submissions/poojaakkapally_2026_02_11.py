1. len () function 
print(len('Hyd')) -------3
print (len ('Rama Rao')) -------8
print (len ('9247')) -------4
print (len ('')) -------0
print (len (' ')) -------1
print (len (689)) -------error (It should be sequence)

2. # Tricky  program Find  outputs 
a = 'Hyd'
print (a, id(a)) ------- Hyd, address of object a
a = a * 3 # It is valid (or) invalid-------valid
print (a ,id(a)) -------HydHydHyd address of HydHydHyd

3. # Find  outputs  (Home  work)
a = """"Hyd"""
print(a) -------Hyd
print(len(a)) -------4
print(a[0]) -------"
print ("""Hyd"""" )   ------- error(Excess of closing tab)
b = """""Hyd"""
print (b) ------- “”Hyd
print(len(b)) -------5

4. # Find  outputs
a = 'Sankar Dayal Sarma'
print (a[7 : 12]) ------- a[7:12:1]string  from  indexes  7  to  11 in  steps  of  1  i.e. Dayal
print (a[7 : ]) ------- a[7:18:1]string  from  indexes  7  to  17 in  steps  of  1 i.e. Dayal Sarma
print (a[ : 6]) ------- a[0:6:1]string  from  indexes  0  to 5 in  steps  of  1    i.e. Sankar
print (a[ : ])  -------a[0:18:1] string  from  indexes  0  to  17 in  steps  of  1   i.e. Sankar Dayal Sarma
print (a[:  : ]) ------- a[0:18:1] string  from  indexes   0 to  17  in  steps  of  1 i.e. Sankar Dayal Sarma
print (a[1 : 10 : 2]) ------- a[1 : 10 : 2]string  from  indexes  1 to9    in  steps  of  2  i.e. akrDy
print (a[0 : : 2]) ------- a[0 : 18: 2])  string  from  indexes 0   to 17  in  steps  of  2  i.e. Sna aa am
print (a[1 : : 2]) ------- a[1:18 : 2]) string  from  indexes  1  to 17    in  steps  of  2  i.e. akrDylSra
print (a[-5 : -1]) ------- a[-5: -1:1]string  from  indexes  -5 to -2    in  steps  of  -1 i.e. Sarm
print(a[::-1])  -------a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string
print(a[-1:-5:-1]) ------- a[-1:-5:-1]  string  from  indexes  -1 to  -4  in  steps  of i.e.  -1amra
print (a[ : : -2]) ------- a[-1:-9:-2]string  from  indexes  -1  to   -18  in  steps  of  -2 i.e. arSlyDrka
print (a[3 : -3]) ------- a[3 : -3:1] string  from  indexes  3  to   -4  i.e.  kar Dayal Sa
print (a[2 : -5]) ------- a[2 : -5:1]string  from  indexes  2  to -6     i.e nkar Dayal
print(a[-1:-5]) ------- a[-1: -5:1]string  from  indexes   -1 to -6   i.e empty
print (a[3 : 3]) ------- a[3: 3:1] string  from  indexes  3 to-2    i.e empty

5. Find  outputs 
a =  'A'
print(a[1]) -------error
print(a[1:]) -----empty

6.Find  outputs  
a = "Rama Rao"
print(a) ------- Rama Rao
print(type(a)) ------- <class 'str'>
print(id(a)) ------- address of object Rama Rao
b = 'Hyd'
print(b) ------- Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) ------- Hyd is green city.
                 Hyd is hitec city.
                 Hyd is beautiful city.

7. Index   demo  program  
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') ------- (a[0])
print(How  to  print  'y'  of  object  'a') ------- (a[1])
print(How  to  print  'd'  of  object  'a') ------- (a[2])
print(a[3])  -------error(str index iis more of 2)
print(How  to  print  'd'  of  object  'a') ------- (a[-1])
print(How  to  print  'y'  of  object  'a') ------- (a[-2])
print(How  to  print  'H'  of  object  'a') ------- (a[-3])
print(a[-4]) -------error(str index is more than -2)
print(a[0] == a[-3]) -------True
a[2] = 'c' -------error
print(25[0])  -------  error(Non sequence)
print('25'[0]) -------2
print(True[1]) -------error
print('True'[1]) ------- r


8. #  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) -------Hyd Hyd Hyd
print(a * 2) ------- Hyd Hyd
print(a * 1) ------- Hyd
print(a * 0) -------empty
print(a * -1) -------empty
print(25 * 3) -------75
print('25' * 3) -------252525
print('25' * 4.0)  -------error (bcz of complex)
print(3 * 'Hyd') -------HydHydHyd
print('25' * True) -------25
