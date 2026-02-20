1.# Find outputs (Home work)
a = "Rama Rao" =>This is a string.
print(a) => The output is Rama Rao
print(type(a)) => The output is : <class ‘str’>
print(id(a)) => The output is the Adress of the object to the reference.
b = 'Hyd' => This is a string
print(b) => The output is Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) => The output is : Hyd is green city.
 Hyd is hitec city.
 Hyd is beautiful city.



2. # Index demo program (Home work)
a = 'Hyd'
print(How to print 'H' of object 'a') => print (a[0])
print(How to print 'y' of object 'a') => print (a[1])
print(How to print 'd' of object 'a') =>print(a[2])
print(a[3]) => The output is Error : because The index is out of range in the given value.
print(How to print 'd' of object 'a') => The output : print(a[-1])
print(How to print 'y' of object 'a') => The output : print(a[-2])
print(How to print 'H' of object 'a') => The output : print(a[-3])
print(a[-4]) => The output is Error : The index is out range.
print(a[0] == a[-3]) => The output is True ex (a[0] = H , a[-3]= H) ( H == H).
a[2] = 'c' => The output is Error : Because In Python strings are immutable. Means
values cannot be changed or modifed.
print(25[0]) => The output is Error. Because The (‘int’ object is not subscript in the
string)
print('25'[0]) => The output is 2.
print(True[1]) => The output is Error. Because The (‘bool’ object is not subscript in the
string)
print('True'[1]) => The output is r


3. # Find outputs (Home work)
a = 'Hyd'
print(a * 3) => The output is : ‘HydHydHyd’
print(a * 2) => The output is : ‘HydHyd’
print(a * 1) => The output is : ‘Hyd’
print(a * 0) => It indicates the (empty string)
print(a * -1) => (empty string).
print(25 * 3) => The output is : 75.
print('25' * 3) => 252525
print('25' * 4.0) => The output is : Error.
print(3 * 'Hyd') => ‘HydHydHyd’
print('25' * True) => The output is 25.



4. # Tricky program
# Find outputs (Home work)
a = 'Hyd'
print(a , id(a)) => The output is : Hyd , and address of the object
a = a * 3 # It is valid (or) invalid
print(a , id(a)) => The output is : HydHydHyd , and address of the object.


5. # len() function (Home work)
print(len('Hyd')) => The output is : 3 => H, y, d = 3
print(len('Rama Rao')) => The output is : 8
print(len('9247')) => The output is : 4
print(len('')) => The output is : 0
print(len(' ')) => The output is : 1
print(len(689)) => The output is Error : because ‘int’ has no length.

6. # Find outputs (Home work)
a = """"Hyd"""
print(a) => The output is : Hyd
print(len(a)) => The output is : 3
print(a[0]) => The output is : H
print("""Hyd"""") => The output is Error.
b = """""Hyd"""
print(b) => The output is : Hyd.
print(len(b)) The output is : 3


7. # Find outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) => The output is : Dayal
print(a[7 : ]) => The output is : Dayal Sarma
print(a[ : 6]) => The output is : Sankar
print(a[ : ]) => The output is to print fullName : Sankar Dayal Sarma
print(a[: : ]) => Output is : Sankar Dayal Sarma
print(a[1 : 10 : 2]) => output: string from indexes 1 to 9 in steps of 2 i.e. akrDy
print(a[0 : : 2]) => output : SnkrDya aa
print(a[1 : : 2]) => The output : a a a ylSra => Odd index charecters.
print(a[-5 : -1]) => output is : a a a ylSra