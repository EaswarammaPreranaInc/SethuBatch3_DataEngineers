# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #25,10.8,'Hyd'
print(a , b , c , sep = '\t') #25    10.8    'Hyd'
print(a , b , c , sep = '---') #25---10.8---'Hyd'
print(a , b , c , sep = '\n') #25 <Nextline> 10.8 <nextline> Hyd
print(a , b , c) #25 10.8 Hyd
#print(a , b , c , separator = ':') #Error because their is no key word Separator


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25 10.8 'Hyd'---<sameline>
print(a , b , c , sep = ',,,') #25,,,10.8,,,'Hyd'<nextline>
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd<tab><tab><tab><same line continue>
print(a , b , c) #25 10.8 Hyd <next line>


# Find outputs  (Home  work)
print('Hyd') #Hyd
print() #Nothing empty space
print('Sec') #Sec 
print() #Nothing empty space 
print('Cyb') #Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) #'25.000000'
print(type(b)) #<class 'str'>
x = 10.8
y = '%i'  %x
print(y) #'10'
print(type(y)) #<class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #'[10 , 20 , 15 , 18]'
print(type(n)) #<class 'str'>


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #<3 spaces>10.93
print('%9.1f'  %a) #<5 spaces>10.9
print('%10.3f'  %a) #<4 spaces>10.927
print('%.2f'  %a) #10.93
print('%.6f'  %a) #10.927400
print('%f'  %a) #'10.927400'
print('%g'  %a) #'10.9274'


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #<4 spaces> Hyd # leading spaces 
print('%-7s'  %a) #Hyd <4 spaces> #trailing spaces 
print('%2s'  %a) #Hyd
print('%s'  %a) #"Hyd"
print('%s' , a) #'%s' Hyd
#print('%s'  a) #Error
#print('%s' , %a) #Error
print(a) #Hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #'[10 , 20 , 30 , 40]'
print('%s' , a) #'%s' [10 , 20 , 30 , 40]
#print('%s'  a) #Syntax Error 
#print('%s' , %a) #Syntax Error
#print('%1'  %a) #Error 
print(a) #[10 , 20 , 30 , 40]



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #'25' '10.927400' 'Hyd'
print('%i    %g    %s'    %(a , b , c)) #'25' '10.9274' 'Hyd'
print('%s    %s    %s'  %(a , b , c)) #'25' '10.9274' 'Hyd'
print('%d    %g    %s'  , a , b , c) #'%d    %g      %s' 25 10.9247 'Hyd'
#print('%d    %g      %s'   a , b , c) #syntax Error
#print('%d    %g    %s'  ,  %(a , b , c)) #Error (Comma)
#print('%d    %g    %s'    %a%b%c) #syntax Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) #'25' '10.927400' 'Hyd'


#  Find  outputs  (Home  work)
x = 25
y = F'{x}' #'25'
print(y) #string 25
print(type(y)) #<class 'str'>
x = 10.8
y = F'{x}' #'10.8'
print(y) #'10.8'
print(type(y)) #<class 'str'>
x = [10,20,30,40]
y = F'{x}' 
print(y) #'[10,20,30,40]'
print(type(y)) #<class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #'25'    '10.8'    'Hyd'
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = '25'    b='10.8'    c='Hyd'
print(F'{a=}  \t   {b=}   \t  {c=}') #a = '25'    b='10.8'    c='Hyd'
print(F'{a:}  \t   {b:}   \t  {c:}') #25<tab>10.8<tab>Hyd #Except (=) no other delimiter is allowed in format string 
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #'a  =  {a}    b  =  {b}    c  =   {c}'
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a =a   b=b   c=c
#print(F'{x =}  \t   {y =}   \t  {z =}') #Error because there no object name x,y,z


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}



