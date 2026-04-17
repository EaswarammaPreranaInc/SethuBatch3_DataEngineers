# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #O/P: 25,10.8,Hyd
print(a , b , c , sep = '\t') #O/P:25 10.8 Hyd
print(a , b , c , sep = '---')#O/P:25---10.8---Hyd
print(a , b , c , sep = '\n')#O/P:25 
      				  10.8 
				  Hyd
print(a , b , c)#O/P:25 10.8 Hyd
print(a , b , c , separator = ':')#O/P: error


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#O/P:25 10.8 Hyd---
print(a , b , c , sep = ',,,')#O/P:25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#O/P:25:::10.8:::Hyd
print(a , b , c)#O/P:25 10.8 Hyd


# Find outputs  (Home  work)
print('Hyd')#O/P:Hyd
print()#O/P:
print('Sec') #O/P:Sec
print()#O/P:
print('Cyb')#O/P:Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)#O/P:[10 , 20 , 30 , 40] , (10 , 20 , 30 , 40) , {10 , 20 , 30 , 40}



#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#O/P:25.000000
print(type(b))#O/P: <class 'str'>
x = 10.8
y = '%i'  %x
print(y)#O/P: 10
print(type(y))#O/P: <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)#O/P: [10, 20, 15, 18]
print(type(n))#O/P: <class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)#O/P:	10.93
print('%9.1f'  %a)#O/P:	10.9
print('%10.3f'  %a)#O/P: 10.927
print('%.2f'  %a)#O/P:10.93
print('%.6f'  %a)#O/P:10.927400
print('%f'  %a)#O/P:10.927400
print('%g'  %a)#O/P:10.9274



# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)#O/P:	Hyd
print('%-7s'  %a)#O/P:Hyd
print('%2s'  %a)#O/P:Hyd
print('%s'  %a)#O/P:Hyd
print('%s' , a)#O/P:%s Hyd
print('%s'  a)#O/P:Error
print('%s' , %a)#O/P:Error
print(a)#O/P:Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #O/P:[10 , 20 , 30 , 40]
print('%s' , a) #O/P: %s [10 , 20 , 30 , 40]
print('%s'  a) #O/P:error
print('%s' , %a)#O/P:error
print('%l'  %a)#O/P:error
print(a)O/P:[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d %f %s' %(a,b,c)) #O/P: 25 10.927400 Hyd
print('%i %g %s' %(a,b,c)) # O/P: 25 10.9274 Hyd
print('%s %s %s' %(a,b,c))  #O/P: %d %g %s 25 10.9274 Hyd
print('%d %g %s'  a , b , c) #O/P: SyntaxError
print('%d %g %s'  %(a,b,c)) #O/P: 25 10.9274 Hyd
print('%d %g %s' %a%b%c)  #O/P: TypeError
print('%d'%a , '%f'%b , '%s'%c) #O/P: 25 10.927400 Hyd

#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #O/P:25
print(type(y))#O/P: <class 'str'>
x = 10.8
y = F'{x}'
print(y)#O/P:10.8
print(type(y))#O/P: <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)#O/P:[10,20,30,40]
print(type(y))#O/P: <class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd' 
print(F'{a}  \t   {b}   \t  {c}') 		#O/P: 25      10.8      Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #O/P: a = 25      b  =  10.8      c  =  Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') 		#O/P: a=25      b=10.8      c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')		#O/P: 25      10.8      Hyd 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#O/P: a  =  {a}  	  b  =  {b}  	  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')      #O/P: a  =  a      b  =  b      c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}')		#O/P: NameError: name 'z' is not defined


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')    # O/P: 25
print(type(F'{x}')) # O/P: <class 'str'>

print(F'{a=}')  # O/P: a=25
print(F'{{x}}')  #O/P: {x}
print(F'{{{x}}}') # O/P: {25}
print(F'{{{{x}}}}')  # O/P: {{x}}
print(F'{{{{{x}}}}}')  # O/P: {{{25}}}
print(F'{{{{{{x}}}}}}') # O/P: {{{x}}}
print(F'{{{{{{{x}}}}}}}') # O/P: {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')# O/P: {{{{x}}}}