# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' #a=25 b=10.8 c='Hyd' 
print(a , b , c , sep = ',')  #a=25, b=10.8, c='Hyd' 
print(a , b , c , sep = '\t')#a=25 \t b=10.8 \t  c='Hyd' 
print(a , b , c , sep = '---') #a=25--- b=10.8 ---c='Hyd' 
print(a , b , c , sep = '\n') #a=25 \n b=10.8 \n tab c='Hyd'
print(a , b , c)                  #a=25 b=10.8 c='Hyd' 
print(a , b , c , separator = ':') #a=25 : b=10.8: c='Hyd' 


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd' 
print(a , b , c , end = '---') #a=25 next line b=10.8  next line c='Hyd'
print(a , b , c , sep = ',,,') #a=25,,, b=10.8,,, c='hyd'
print(a , b , c , sep = ':::' , end = '\t\t\t') #a=25 ::: next line b=10.8 ::: next line c='hyd'
print(a , b , c)#a=25 b=10.8 c='Hyd' 


# Find outputs  (Home  work)
print('Hyd') #'hyd'
print() #empty space
print('Sec') #'sec'
print()#empty space
print('Cyb') #'cyb'

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) # it will print all the l t s

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a 
print(b)  #25.0000
print(type(b)) #<class float>
x = 10.8
y = '%i'  %x #'10'
print(y) #10
print(type(y)) #<class String>
m = [10 , 20 , 15 , 18]
n = '%s'  %m 
print(n)  #'[10,20,15,18]'
print(type(n))  #Class String

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #10.92
print('%9.1f'  %a) #10.9
print('%10.3f'  %a) #10.927
print('%.2f'  %a)#10.93
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400
print('%g'  %a)#10.9274

# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)      #Hyd
print('%-7s'  %a)#Hyd
print('%2s'  %a) #Hyd
print(('%s'  %a)))#Hyd
print(('%s' , a))#  % S Hyd
#print('%s'  a)# Invalid synatx
#print('%s' , %a) #Invalid synatx
print(a))#Hyd

#  Find  outputs  (Home  work)
x = 25
y = F'{x}'#25
print(y)#25
print(type(y))#<class str>
x = 10.8
y = F'{x}'#10.8
print(y)#10.8
print(type(y))#<class float>
x = [10,20,30,40]
y = F'{x}' #[10,20,30,40]
print(y) #[10,20,30,40]
print(type(y))#<class List>

#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25   10.8   'hyd'
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')#a=25   b=10.8   c='hyd'
print(F'{a:}  \t   {b:}   \t  {c:}')#25   10.8   'hyd'
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') #a  =  {a}  \t  b  =  {b}  \t  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a  =  a  \t  b  =  b  \t  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') #xyz are not defined

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}

 

'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
