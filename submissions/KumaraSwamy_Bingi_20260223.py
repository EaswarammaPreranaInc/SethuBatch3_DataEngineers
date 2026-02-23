# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') # 25,10.8,Hyd
print(a , b , c , sep = '\t') # 25 <tab>	10.8 <tab>	Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <next line> 10.8 <next line> Hyd
print(a , b , c) # 25 10.8 Hyd
print(a , b , c , separator = ':') # Error


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  
print(a , b , c , sep = ',,,') 
print(a , b , c , sep = ':::' , end = '\t\t\t') 
print(a , b , c) 

'''
Output(above  code):

25 10.8 Hyd---25,,,10.8,,,Hyd
25:::10.8:::Hyd			25 10.8 Hyd

'''


# Find outputs  (Home  work)
print('Hyd') # print Hyd and move to next line
print() # print blank line and move to next line
print('Sec') # print Sec and move to next line
print() # print blank line and move to next line
print('Cyb') # print Cyb and move to next line


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # [10, 20, 30, 40] (10, 20, 30, 40) {40, 10, 20, 30}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # <class 'str'>
x = 10.8
y = '%i'  %x 
print(y) # 10
print(type(y)) # <class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # [10, 20, 15, 18]
print(type(n)) # <class 'str'>



# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #    10.93
print('%9.1f'  %a) #      10.9
print('%10.3f'  %a) #      10.927
print('%.2f'  %a) # 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400
print('%g'  %a) # 10.9274


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #    Hyd (total 7 characters, 3 for 'Hyd' and 4 spaces)
print('%-7s'  %a) # Hyd    (total 7 characters, 3 for 'Hyd' and 4 spaces on the right)
print('%2s'  %a) # Hyd (only 2 characters, but 'Hyd' is 3 characters, so it will print 'Hyd')
print('%s'  %a) # Hyd (no width specified, so it will print 'Hyd' as is)
print('%s' , a) # Error (incorrect syntax, should be print('%s' % a))
print('%s'  a) # Error (incorrect syntax, should be print('%s' % a))
print('%s' , %a) # Error (incorrect syntax, should be print('%s' % a))
print(a) # Hyd (just printing the variable 'a' which contains 'Hyd')



# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # [10, 20, 30, 40] (the list is converted to its string)
print('%s' , a)  # Error (incorrect syntax, should be print('%s' % a))
print('%s'  a) # Error (incorrect syntax, should be print('%s' % a))
print('%s' , %a) # Error (incorrect syntax, should be print('%s' % a))
print('%l'  %a) #Error
print(a) # [10, 20, 30, 40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # 25    10.927400    Hyd (a is printed as integer, b is printed as float with 6 decimal places, c is printed as string)
print('%i    %g    %s'    %(a , b , c)) # 25    10.9274    Hyd (a is printed as integer, b is printed in general format, c is printed as string)
print('%s    %s    %s'  %(a , b , c)) # 25    10.9274    Hyd (a, b, and c are all converted to strings and printed)
print('%d    %g    %s'  , a , b , c) # Error
print('%d    %g      %s'   a , b , c) # Error
print('%d    %g    %s'  ,  %(a , b , c)) #Error
print('%d    %g    %s'    %a%b%c) # Error (incorrect syntax, should be print('%d    %g    %s'  %(a , b , c)))
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # 25 10.927400 Hyd (a is printed as integer, b is printed as float with 6 decimal places, c is printed as string)


#  Find  outputs  (Home  work)
x = 25
y = F'{x}' 
print(y) # 25 (the integer x is converted to a string and printed)
print(type(y)) # <class 'str'>
x = 10.8
y = F'{x}'
print(y) # 10.8 (the float x is converted to a string and printed)
print(type(y)) # <class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y) # [10, 20, 30, 40] (the list x is converted to a string and printed)
print(type(y)) # <class 'str'>


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') # 25 <tab> 10.8 <tab>  Hyd (a, b, and c are formatted into the string with tabs in between)
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a = 25 <tab> b = 10.8 <tab> c = Hyd (a, b, and c are formatted into the string with their variable names and tabs in between)
print(F'{a=}  \t   {b=}   \t  {c=}') # a=25 <tab> b=10.8 <tab> c='Hyd' (a, b, and c are formatted into the string with their variable names and values, and tabs in between)
print(F'{a:}  \t   {b:}   \t  {c:}') # 25 <tab> 10.8 <tab> Hyd (a, b, and c are formatted into the string with default formatting and tabs in between)
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')# a  =  {a}  \t  b  =  {b}  \t  c  =   {c} (the string is printed as is, without formatting, because it is not an f-string)
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a <tab> b  =  b <tab> c  =  c (the string is printed as is, without formatting, because it is not an f-string)
print(F'{x =}  \t   {y =}   \t  {z =}') # Error (z is not defined)


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #  {{x}}
print(F'{{{{{x}}}}}') #  {{{25}}}
print(F'{{{{{{x}}}}}}') #  {{{{x}}}} 
print(F'{{{{{{{x}}}}}}}') #  {{{{25}}}} 
print(F'{{{{{{{{x}}}}}}}}') #  {{{{25}}}} 




