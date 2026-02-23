# Find outputs (Home work) a = "Rama Rao"
print(a) #OUTPUT: Rama Rao
print(type(a)) #OUTPUT: String
print(id(a)) #OUTPUT: gives the address of the string
b = 'Hyd'
print(b) #OUTPUT:Hyd c = '''Hyd is green city. Hyd is hitec city.
Hyd is beautiful city.''' print(c) #OUTPUT:
'''Hyd is green city. Hyd is hitec city.
Hyd is beautiful city.'''


# Index demo program (Home work) a = 'Hyd'
print(How to print 'H' of object 'a') #OUTPUT:’Hyd’[0] print(How to print 'y' of object 'a') #OUTPUT:’Hyd’[1] print(How to print 'd' of object 'a') #OUTPUT:’Hyd’[2] print(a[3]) #OUTPUT:error
print(How to print 'd' of object 'a') #OUTPUT:’Hyd’[-1] print(How to print 'y' of object 'a') #OUTPUT:’Hyd’[-2] print(How to print 'H' of object 'a') #OUTPUT:’Hyd’[-3] print(a[-4]) #OUTPUT:error
print(a[0] == a[-3]) #OUTPUT:True a[2] = 'c'
print(25[0]) #OUTPUT: error, non-sequence do not contain group of elements
print('25'[0]) #OUTPUT:2
print(True[1]) #OUTPUT: error, non-sequence do not contain group of elements
print('True'[1]) #OUTPUT: r
 
# Find outputs (Home work) a = 'Hyd'
print(a * 3) #OUTPUT: HydHydHyd print(a * 2) #OUTPUT: HydHyd print(a * 1) #OUTPUT: Hyd
print(a * 0) #OUTPUT: error print(a * -1) #OUTPUT: error print(25 * 3) #OUTPUT: 75
print('25' * 3) #OUTPUT: 252525
print('25' * 4.0) #OUTPUT:error print(3 * 'Hyd') #OUTPUT: HydHydHyd print('25' * True) #OUTPUT:25



# Tricky program
# Find outputs (Home work) a = 'Hyd'
print(a , id(a)) #OUTPUT: Hyd,address of object
a = a * 3 # It is valid (or) invalid #OUTPUT: HydHydHyd print(a , id(a)) #OUTPUT: HydHydHyd,address of object

# len() function (Home work) print(len('Hyd')) #OUTPUT:3 print(len('Rama Rao')) #OUTPUT:8 print(len('9247')) #OUTPUT:4
print(len('')) #OUTPUT:empty print(len(' ')) #OUTPUT:1 print(len(689)) #OUTPUT:error
 
# Find outputs (Home work) a = """"Hyd"""
print(a) #OUTPUT: “Hyd print(len(a)) #OUTPUT:4 print(a[0]) #OUTPUT:” print("""Hyd"""") #OUTPUT: Hyd”
b = """""Hyd"""
print(b) ##OUTPUT: “Hyd


# 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17
# S	a	n	k	a		r		D	a		y		a		l			S	a	r	m	a # -18 -17 -16 -15		-14 -13	-12		-11		-10		-9		-8		-7	-6		-5		-4		-3		-2		-1

# Find outputs
a = 'Sankar Dayal Sarma' print(a[7 : 12]) #OUTPUT: Dayal
print(a[7 : ]) #OUTPUT: Dayal Sarma print(a[ : 6]) #OUTPUT: Sankar
print(a[ : ]) #OUTPUT: Sankar Dayal Sarma print(a[: : ]) #OUTPUT: Sankar Dayal Sarma print(a[1 : 10 : 2]) #OUTPUT: akrDy
print(a[0 : : 2]) #OUTPUT: Sna aa am print(a[1 : : 2]) #OUTPUT: akrDylSra print(a[-5 : -1]) #OUTPUT:Sarm
print(a[::-1]) #  a[-1 : -19 : -1] ---> string from indexes -1 to -18 in steps of -1 i.e. Reverse string
print(a[-1:-5:-1]) #OUTPUT:amra print(a[ : : -2]) #OUTPUT:arSlyDrka print(a[3 : -3]) #OUTPUT:kar Dayal Sa print(a[2 : -5]) #OUTPUT:nkar Dayal print(a[-1:-5]) #OUTPUT:amraS
 
print(a[3 : 3]) #OUTPUT:empty


# Find outputs (Home work) a = 'A'
print(a[1]) #OUTPUT: error
print(a[1:]) #OUTPUT: error
