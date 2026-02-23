# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #25     10.8     Hyd
print(a , b , c , sep = '---') #25---10.8---Hyd
print(a , b , c , sep = '\n') #25\n10.8\nHyd
print(a , b , c) #25 10.8 Hyd because default separator is space
print(a , b , c , separator = ':') #25:10.8:Hyd

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 Hyd---
print(a , b , c , sep = ',,,') #25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd            
print(a , b , c) #25 10.8 Hyd


# Find outputs  (Home  work)
print('Hyd')
print() #Hyd
         None
print('Sec')
print() #Sec
         None
print('Cyb') #Cyb
              

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40} default separator is space


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a #25.000000
print(b) #25.000000 
print(type(b)) #<class 'str'>
x = 10.8
y = '%i'  %x #'10'
print(y) #10
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m #'[10 , 20 , 15 , 18]'
print(n) #[10 , 20 , 15 , 18]
print(type(n)) #<class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #10.93
print('%9.1f'  %a) #10.9
print('%10.3f'  %a) #10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a) #10.927400
print('%f'  %a) #10.927400
print('%g'  %a) #10.9274


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #"       Hyd" 
print('%-7s'  %a) #"Hyd       "
print('%2s'  %a) #"  Hyd"
print('%s'  %a) #Hyd
print('%s' , a) #Hyd Hyd
print('%s'  a) #Syntax error because missing % operator
print('%s' , %a) #Invalid syntax due to comma
print(a) #Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #'[10 , 20 , 30 , 40]'
print('%s' , a) #Error due to comma which is invalid syntax
print('%s'  a) #Error due to invalid syntax
print('%s' , %a) #Error due to comma
print('%l'  %a ) #Error Invalid syntax
print(a) #[10 , 20 , 30 , 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25  10.927400  'Hyd'
print('%i    %g    %s'    %(a , b , c)) # 25  10.9274   'Hyd'
print('%s    %s    %s'  %(a , b , c)) #'25' '10.9274'  'Hyd'
print('%d    %g    %s'  , a , b , c) #Error due to comma which is invalid syntax
print('%d    %g      %s'   a , b , c) #Error due to invalid syntax
print('%d    %g    %s'  ,  %(a , b , c)) #Error due to comma
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25  10.927400  'Hyd'


#  Find  outputs  (Home  work)
x = 25
y = F'{x}' #'25'
print(y) #25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}'  #'10.8'
print(y) #10.8
print(type(y)) #<class 'str'>
x = [10,20,30,40]
y = F'{x}' #'[10,20,30,40]'
print(y) #[10,20,30,40]
print(type(y)) #<class 'str>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25     10.8      Hyd 
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = 25      b = 10.8       c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') # a = 25      b = 10.8       c = Hyd  
print(F'{a:}  \t   {b:}   \t  {c:}') #25      10.8       Hyd here delimeter : is ignored
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a = 25    b = 10.8     c = Hyd
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #Syntax Error
print(F'{x =}  \t   {y =}   \t  {z =}') #Error because x,y,z values are not defined


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}