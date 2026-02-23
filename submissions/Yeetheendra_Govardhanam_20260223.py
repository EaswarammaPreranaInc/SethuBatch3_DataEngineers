#Topic-1
 # sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') # 25, 10.8, Hyd\n
print(a , b , c , sep = '\t') # 25\t 10.8\t Hyd\n
print(a , b , c , sep = '---') #25---10.8---Hyd\n
print(a , b , c , sep = '\n') # 25\n 10.8\n Hyd\n 
print(a , b , c) #25<space>10.8<space>Hyd\n
print(a , b , c , separator = ':')# error there is no separator keyword

#Topic-2
 #Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25<space>10.8<space>Hyd---
print(a , b , c , sep = ',,,') #(continues in the above line)25,,,10.8,,,Hyd\n
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd\t\t\t
print(a , b , c) #(continues in the above line)25<space>10.8<space>Hyd\n

#Topic-3
 # Find outputs  (Home  work)
print('Hyd') #Hyd
print() #<newline>
print('Sec') #Sec
print() #<newline> 
print('Cyb') #Cyb
#Topic-4
 # Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)  #[10 , 20 , 30 , 40]<space>(10 , 20 , 30 , 40)<space>{10 , 20 , 30 , 40}\n

#Topic-5
 #  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # “25.000000” 
print(type(b)) # <class ‘srt’>
x = 10.8
y = '%i'  %x
print(y) #’10’
print(type(y))  # <class ‘srt’>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #’[10 , 20 , 15 , 18]’ 
print(type(n)) # <class ‘srt’>

#Topic-6
 # Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #_ _ _ 10.92
print('%9.1f'  %a) #_ _ _ _ _ 10.9
print('%10.3f'  %a)#_ _ _ _10.927 
print('%.2f'  %a)#10.92
print('%.6f'  %a) #10.927400
print('%f'  %a) #10.927400
print('%g'  %a) #10.9274

#Topic-7
 # Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a) #”_ _ _ _Hyd”
print('%-7s'  %a) #”Hyd_ _ _ _”
print('%2s'  %a) #”Hyd”(it extended to fit d) 
print('%s'  %a) #”Hyd” 
print('%s' , a) # %s Hyd
print('%s'  a) # error wrong syntax
print('%s' , %a) # error wrong syntax
print(a) #Hyd
#Topic-8
 # Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a) # ”[10 , 20 , 30 , 40]”
print('%s' , a) # %s [10 , 20 , 30 , 40]
#print('%s'  a) # error wrong syntax 
#print('%s' , %a) # error wrong syntax
#print('%l'  %a) # error no “L” type-conversion 
print(a) # [10 , 20 , 30 , 40]
#Topic-9
 #Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c)) # ‘25’ ‘10.927400’  “Hyd” 
print('%i    %g    %s'    %(a , b , c)) # ‘25’ ‘10.9274’  “Hyd”
print('%s    %s    %s'  %(a , b , c)) # ‘25’ ‘10.9274’  “Hyd”
print('%d    %g    %s'  , a , b , c) # %d    %g    %s ‘25’ ‘10.9274’  “Hyd”
print('%d    %g      %s'   a , b , c) # error wrong syntax
print('%d    %g    %s'  ,  %(a , b , c)) # error wrong syntax
print('%d    %g    %s'    %a%b%c) # error wrong syntax
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c) # ‘25’ ‘10.927400’  “Hyd”
#Topic-10
 #  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #”25” 
print(type(y)) # <class ‘srt’>
x = 10.8
y = F'{x}'
print(y) #”10.8”
print(type(y))  # <class ‘srt’>
x = [10,20,30,40]
y = F'{x}'
print(y) # “[10,20,30,40]”
print(type(y))  # <class ‘srt’>
#Topic-11
 #Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}') #25\t10.8\t'Hyd'\n
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}') #a = 25\t b = 10.8\t c = 'Hyd'\n 
print(F'{a=}  \t   {b=}   \t  {c=}') #a=25\t b=10.8\t c='Hyd'\n
print(F'{a:}  \t   {b:}   \t  {c:}')  #25\t10.8\t'Hyd'\n
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}') # a  =  {a}  \t  b  =  {b}  \t  c  =   {c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c') # a  =  a  \t  b  =  b  \t  c  =  c
print(F'{x =}  \t   {y =}   \t  {z =}') # error x, y, z are not there
#Topic-12
 #  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #   '25'
print(F'{{x}}')  #   {x}
print(F'{{{x}}}')  #  {25}
print(F'{{{{x}}}}') #   {{x}} 
print(F'{{{{{x}}}}}')#   {{25}}
print(F'{{{{{{x}}}}}}')#   {{{x}}}
print(F'{{{{{{{x}}}}}}}')#   {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#   {{{{x}}}}

