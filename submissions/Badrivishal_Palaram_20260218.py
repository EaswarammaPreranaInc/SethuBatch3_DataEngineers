 #  Find  outputs
a = 25 #O/P :
print(id(a)) #O/P : some system generated address say(1000)
a = 35
print(id(a)) #O/P : different  system generated address than previous 

 # Find  outputs (Home  work)

a = 25.7
print(id(a)) #O/P : different system generated address than previous
print(a)#O/P : 25.7
a = 35.6
print(id(a)) #O/P : different system generated address than previous
print(a) #O/P : 35.6
b = True
print(id(b))#O/P : different system generated address than previous
b = False
print(id(b))#O/P : different system generated address than previous
c = None
print(id(c))#O/P : different system generated address than previous
c = None
print(id(c))#O/P : same system generated address as previous



 #  Find  outputs  (Home  work)
a = 'Hyd'
print(id(a)) #O/P : some system generated address say(1212)
a[1] = 'e'   #O/P : error, string doesn't support item assignment
a = 'Sec'
print(id(a)) #O/P : different system generated address say(2112)
b = (10 , 20 , 15 , 18)
print(id(b)) #O/P : some system generated address say(1113)
b[2] = 19    #O/P : error ,tuple is immutable
b = (30 , 40 , 35 , 32)
print(id(b)) #O/P : different system generated address say(9999)
c = range(5)
print(id(c)) #O/P :some system generated address say(1349)
c[3] = 10    #O/P :range doesn't alllow item assignment
c = range(5)
print(id(c))#O/P : different system generated address say(9935)


 # Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) #O/P : True
c = 'Hyd'
d = 'Hyd'
print(c  is  d)  #O/P : True
e = False
f = False
print(e  is  f)  #O/P : True
g = range(10)
h = range(10)
print(g  is  h)  #O/P : False ,range(10) creates a new range object each time


 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)  #O/P : False , list is mutable , new set is created
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)  #O/P : False, dictionary is mutable , new set is created
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)  #O/P : True ,Tuple is immutable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)  #O/P : False , set is mutable , new set is created


 # Find outputs (Home work)
print(10 + 20) #O/P: 30
print(10.8 + 20.6) #O/P: 31.4
print(3 + 4j + 5 + 6j) #O/P: 8+10j
print(True + False) #O/P: 1
print('Hyder' + 'abad') #O/P: 'Hyderabad'
print('Sankar' + 'Dayal' + 'Sarma') #O/P: SankarDayalSarma
print('10' + '20') #O/P: 1020
print([10 , 20 , 30] + [1 , 2 , 3]) #O/P: [10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #O/P:(25,10.8,'Hyd',3+4j,True,none)
print({10 , 20} + {30 , 40}) #O/P: error, set doesn't support + operator
print({10 : 'Hyd'} + {20 : 'Sec'}) #O/P: error, dictionary doesn't support + operator
print(range(4) + range(5)) #O/P: error, range doesn't support + operator
print(10 + '20') #O/P: error, int and str cannot be added
print([10 , 20 , 30] + 5) #O/P: error, list and int cannot be added 
print([10 , 20 , 30] + (40 , 50 , 60)) #O/P: error, list and tuple cannot be added together


# Find outputs (Home work)
print(25 * 3) #O/P: 75
print(10.8 * 25.6) #O/P:276.48
print(True * False) #O/P:0
print((3 + 4j) * (5 + 6j)) #O/P: (-9+38j)
print(3 + 4j * 5 + 6j) #O/P: (3+26j)
print('25' * 3) #O/P:252525
print(3 * '25') #O/P:252525
print('Hyd' * 4) #O/P:HydHydHydHyd
print([10 , 20 , 15] * 2) #O/P: [10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3) #O/P: (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0) #O/P: error ,can't multiply by float 
print({10 , 20 , 15} * 2) #O/P:error, set doesn't support *
print({10 : 20 , 30 : 40} * 2) #O/P: error,distionary doesn't support *
print([10] * [20]) #O/P:error, can't multiply seq with seq