# sep  argument  demo  program  (Home  work)

a = b = c = 25, 10.8, 'hyd'
print(a, b, c, sep=',') # Here we specified separator as comma so we get output #25, 10.8, hyd in place of <space>.

print(a, b, c, spe='\t') # here we specified separator as tab so we get output # 25 <tab> 10.8 <tab> hyd.

print(a, b, c, spec'---')# here we specified separator as --- highfun # 25---10.8---hyd.

print(a,b,c, spe'\n') #25 nextline
                      #10.8 nextline
                      #hyd.
                      
print(a,b,c) #print(25)
#10.8
#hyd

print(a,b,c, spearator=':') #we get output as 25:10.8:hyd

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' 
print(a , b , c , end = '---')  #we get output 25<space>10.8<space>hyd--- 
print(a , b , c , sep = ',,,') # we get output 25,,,10.8,,,hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')  # 25:::10.8:::hyd
print(a , b , c) #25 10.8 hyd

# Find outputs  (Home  work)
print('Hyd') #hyd
print()
print('Sec') #Sec
print()
print('Cyb') #Cyb


# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  #[10 , 20 , 30 , 40]  (10 , 20 , 30 , 40)  {10 , 20 , 30 , 40}


#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # %f %a converted to string
print(type(b)) #class 'string
x = 10.8 
y = '%i'  %x
print(y)  #'%i   %x'
print(type(y)) #class 'str'
m = [10 , 20 , 15 , 18]
n = '%s'  %m  #'%s    %m'
print(n) #'%s    %m'
print(type(n))  #class 'str'


# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)
print('%g'  %a)


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #Error
print('%-7s'  %a)#Error
print('%2s'  %a) #Error
print('%s'  %a) #hyd
print('%s' , a) #Error
print('%s'  a) #error
print('%s' , %a) Error
print(a) #hyd


# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) #'10,20,30,40'
print('%s' , a) #Error
print('%s'  a) #error
print('%s' , %a) #error
print('%l'  %a) Error
print(a) #[10,20,30,40]


#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) #25   10.927400  hyd
print('%i    %g    %s'    %(a , b , c))  #25    10.92  hyd
print('%s    %s    %s'  %(a , b , c)) #  '25'    '10.9274'    'hyd'
print('%d    %g    %s'  , a , b , c)  #Error
print('%d    %g      %s'   a , b , c)   #25  10.92    hyd  
print('%d    %g    %s'  ,  %(a , b , c)) #Error
print('%d    %g    %s'    %a%b%c) #25   10.92    hyd
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)   #25    10.9274   hyd


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #25
print(type(y)) #class'int'
x = 10.8
y = F'{x}'
print(y) #10.8
print(type(y)) #class'float'
x = [10,20,30,40]
y = F'{x}'
print(y) #10,20,30,40
print(type(y)) #class 'tuple'


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25    10.8   hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') # a=25   b= 10.8     c=hyd 
print(F'{a=}  \t   {b=}   \t  {c=}') #  {a=25}  b=10.8    c=hyd
print(F'{a:}  \t   {b:}   \t  {c:}') #{a:25}    b:10.8    c:hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # 'a=a  b=b   c=c'
print(F'a  =  a  \t  b  =  b  \t  c  =  c') #'a=a   b=b     c=c
print(F'{x =}  \t   {y =}   \t  {z =}') #x=25     y=10.8    z=hyd


#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') # {{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
