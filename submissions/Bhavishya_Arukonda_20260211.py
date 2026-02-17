a="Rama Rao"
print(a)  # output: Rama Rao
print(type(a))  #output: <class 'str'>
print(id(a))  #output: address of object
b='Hyd'
print(b) # output: Hyd
c='''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # output: Hyd is green city.
                   Hyd is hitec city.
                   Hyd is beautiful city.


a='Hyd'
print(How to print 'H' of object 'a') # a[0]
print(How to print 'y' of object 'a') # a[1]
print(How to print 'd' of object 'a') # a[2]
print(a[3]) # output: error as the length of the object is 3.
print(How to print 'd' of object 'a') # a[-1]
print(How to print 'y' of object 'a') # a[-2]
print(How to print 'H' of object 'a') # a[-3]
print(a[-4]) # output: error as the length of the object is 3.
print(a[0]==a[-3]) #True
a[2]='c'
print(25[0]) # error
print('25'[0]) # error
print(True[1]) #error
print('True'[1]) #error

a='Hyd'
print(a*3) # output: HydHydHyd
print(a*2) # output: HydHyd
print(a*1) # output: Hyd
print(a*0) # output: no output
print(a*-1) # output: no output
print(25*3) #output: 75
print('25'*3) #output: 252525
print('25'*4.0) #output: error
print(3*Hyd) #output: error
print('25'*True) #output: 25

a='Hyd'
print(a,id(a)) #output: Hyd and address of the object
a=a*3 # valid
print(a,id(a)) #output: HydHydHyd and address of the object

print(len('Hyd')) #output: 3
print(len('Rama Rao')) #output:8
print(len('9247')) #output: 4
print(len('')) #output: 0
print(len(' ')) #output: 1
print(len('Hyd')) #output: error

a="""Hyd"""
print(a) #Hyd
print(len(a)) #o/p:3
print(a[0])  #o/p:H
print("""Hyd""") #o/p:Hyd
b="""""Hyd"""
print(b) #o/p:Hyd
print(len(b)) #o/p:3


a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #  Daya
print(a[7 : ])   #  Dayal sarma
print(a[ : 6])   # Sanka
print(a[ : ])    # Sankar Dayal Sarma
print(a[:  : ])  # Sankar Dayal Sarma
print(a[1 : 10 : 2])  #  string  from  indexes  1  to  9  in  steps  of  2  i.e. akrDy
print(a[0 : : 2]) #string  from  indexes  0 to  17  in  steps  of  2  i.e. sna aa am
print(a[1 : : 2]) #string  from  indexes  1  to  17  in  steps  of 2  i.e. akrdylsr
print(a[-5 : -1]) string  from  indexes  -5  to  -1  in  steps  of  1  i.e. Sarm
print(a[::-1])  #    a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18  in  steps  of  -1  i.e. Reverse  string(amraS layaD raknaS)
print(a[-1:-5:-1])  #string  from  indexes  -1  to  -5  in  steps  of  -1  i.e. amra
print(a[ : : -2])  #  arSlyDrka 
print(a[3 : -3])   #  kar Dayal Sa
print(a[2 : -5])   #  nkar Dayal 
print(a[-1:-5])    #  amra
print(a[3 : 3])    # error

a =  'A'
print(a[1])  #output: error as length is only 1
print(a[1:]) #output: error as length is only 1




 