# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  #25,10.8,Hyd
print(a , b , c , sep = '\t')  #25  10.8  Hyd
print(a , b , c , sep = '---')  #25---10.8---Hyd
print(a , b , c , sep = '\n')  #25
                                10.8
                                Hyd
print(a , b , c)  #25 10.8 Hyd
print(a , b , c , separator = ':')  #error becoz argument is wrong it is 'sep'


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')  #25 10.8 Hyd---25,,,10.8,,,Hyd
print(a , b , c , sep = ',,,')  
print(a , b , c , sep = ':::' , end = '\t\t\t')  #25:::10.8:::Hyd      25 10.8 Hyd
print(a , b , c)  



# Find outputs  (Home  work)
print('Hyd')  #Hyd
print() #nothing
print('Sec')  #Sec
print() #nothing
print('Cyb')  #Cyb



# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  #[10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}



#  Find  outputs (Home  work)
a = 25
b = '%f'  %a  #integer is convert into float 
print(b)  #'25.000000' ,'%f' it gives 6 zeros after decimal point
print(type(b)) #<class 'int'>
x = 10.8
y = '%i'  %x  #float will convert into int
print(y)  #10
print(type(y)) #class 'str'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m  #elements converts into string 
print(n)  #['10', '20', '15', '18]
print(type(n))  #<class 'str'>



# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  10.93
print('%9.1f'  %a)  #  10.9
print('%10.3f'  %a)  #   10.927
print('%.2f'  %a)  #10.93
print('%.6f'  %a)  #10.927400
print('%f'  %a)  #10.927400
print('%g'  %a)  #10.9274



# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #    Hyd
print('%-7s'  %a)  #Hyd
print('%2s'  %a)  #Hyd
print('%s'  %a)  #hyd
print('%s' , a)  #%s Hyd
#print('%s'  a)  #error
#print('%s' , %a)  #error
print(a)  #Hyd



# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)  #[10 , 20 , 30 , 40]
print('%s' , a)  #%s [10 , 20 , 30 , 40] 
#print('%s'  a)   #error
#print('%s' , %a)  #error comma  ',' is not required for this
#print('%l'  %a)  #error %s is used
print(a)  #[10 , 20 , 30 , 40]



#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))  #25 10.927400 Hyd
print('%i    %g    %s'    %(a , b , c))  #25 10.9274 Hyd
print('%s    %s    %s'  %(a , b , c))  #25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c)  #%d  %g  %s 25 10.9274 Hyd
#print('%d    %g      %s'   a , b , c)  #error
#print('%d    %g    %s'  ,  %(a , b , c))  #error comma ',' is not required 
#print('%d    %g    %s'    %a%b%c)  #error 
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)  #25 10.927400 Hyd



#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)  #25
print(type(y))  #<class 'str'>
x = 10.8
y = F'{x}'
print(y)  #10.8
print(type(y))  #<class 'str'>
x = [10,20,30,40]
y = F'{x}'
print(y)  #[10,20,30,40]
print(type(y))  #<class 'str'>



#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')  #25   10.8   Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')  #a = 25   b = 10.8   c = Hyd
print(F'{a=}  \t   {b=}   \t  {c=}')  #a=25   b=10.8   c=Hyd
print(F'{a:}  \t   {b:}   \t  {c:}')  #25   10.8   Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')  #a = {a}   b = {b}   c = {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')  #a = a   b = b   c = c
#print(F'{x =}  \t   {y =}   \t  {z =}')  #error



#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}')  #{{x}}
print(F'{{{{{x}}}}}')  #{{25}}
print(F'{{{{{{x}}}}}}')  #{{{x}}}
print(F'{{{{{{{x}}}}}}}')  #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')  #{{{{x}}}}

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''

