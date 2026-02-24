#1
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',') #25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #25<tab>10.8<tab>Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25<next line>10.8<next line>Hyd
print(a , b , c) #25<space>10.8<space>Hyd
print(a , b , c , separator = ':') #Error as there is no argument of print() function called as seperator. Instead to rectify make use of 'sep' argument



#2
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') #25<space>10.8<space>Hyd
print(a , b , c , sep = ',,,') #25<space>10.8<space>Hyd---25,,,10.8,,,Hyd i.e same line of line 16's output is continued not new or next line
print(a , b , c , sep = ':::' , end = '\t\t\t') #25:::10.8:::Hyd<tab><tab><tab>
print(a , b , c) #25:::10.8:::Hyd<tab><tab><tab>25 10.8 Hyd i.e same line of line 18's output is continued not new or next line



#3
# Find outputs  (Home  work)
print('Hyd') #Hyd
print() #Empty 
print('Sec') #Sec
print() #Empty
print('Cyb') #Cyb



#4
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) #[10 , 20 , 30 , 40]<space>(10 , 20 , 30 , 40)<space>{10 , 20 , 30 , 40}



#5
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) #25.000000
print(type(b)) #class 'str'
x = 10.8
y = '%i'  %x
print(y) #10
print(type(y)) #class 'str'
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) #[10, 20, 15, 18]
print(type(n)) #class 'str'



#6
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f' %a) #<3 spaces>10.93
print('%9.1f' %a) #<5 spaces>10.9
print('%10.3f' %a) #<4 spaces>10.927
print('%.2f' %a) #10.93 i.e. no spaces before
print('%.6f' %a) #10.927400 i.e. no spaces before
print('%f' %a) #10.927400 i.e. no spaces before
print('%g' %a) #10.9274 i.e. no spaces before



#7
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s' %a) #<space><space><space><space><space><space><space>Hyd i.e. 7 space on to the left of string 'Hyd' because of '+' plus or positive sign
print('%-7s' %a) #Hyd<space><space><space><space><space><space><space> i.e. 7 space on to the right of string 'Hyd' because of '-' minus or negavitive sign
print('%2s' %a) #<space><space>Hyd
print('%s' %a) #Hyd
print('%s', a) #%s<space>Hyd
print('%s' a) #Error as % operator is missing before object 'a' which connects the string to the object
print('%s', %a) #Error as here both are treated as two different arguments which is not permitted instead to recify one can remove the comma and obtain correct syntax: format<space>%object
print(a) #Hyd



#8
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s' %a) #[10, 20, 30, 40]
print('%s', a) #%s [10, 20, 30, 40]
print('%s' a) #Error as % operator is missing before object 'a' which connects the string to the object
print('%s', %a) #Error as here both are treated as two different arguments which is not permitted instead to recify one can remove the comma and obtain correct syntax: format<space>%object
print('%l' %a) #Error as no format '%l' in python is permitted or supported
print(a) #[10, 20, 30, 40]



#9
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d  %f  %s' %(a , b , c)) #25<space>10.927400<space>Hyd
print('%i  %g  %s' %(a , b , c)) #25<space>10.9274<space>Hyd
print('%s  %s  %s' %(a , b , c)) #25<space>10.9274<space>Hyd
print('%d  %g  %s', a , b , c) #%d<space>%g<space>%s<space>25<space>10.9274<space>Hyd
print('%d  %g  %s' a , b , c) #Error as '%' operator is missing before objects i.e a,b  and c which connects the strings to their respective objects
print('%d  %g  %s', %(a , b , c)) #Error as the comma seperates arguments, the '%' must be used as a connector, not a prefix
print('%d  %g  %s' %a%b%c) #Error as multiple objects must be grouped in parentheses (a, b, c) after a single '%' sign
print('%d' %a , '%f' %b , '%s' %c) #25<space>10.927400<space>Hyd



#10
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y) #25
print(type(y)) #class 'str'
x = 10.8
y = F'{x}'
print(y) #10.8
print(type(y)) #class 'str'
x = [10,20,30,40]
y = F'{x}'
print(y) #[10, 20, 30, 40]
print(type(y)) #class 'str'



#11
#Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(F'{a} \t {b} \t {c}') #25<tab>10.8<tab>Hyd
print(F'a = {a} \t b = {b} \t c = {c}') #a = 25<tab>b = 10.8<tab>c = Hyd
print(F'{a=} \t {b=} \t {c=}') #a=25<tab>b=10.8<tab>c=Hyd
print(F'{a:} \t {b:} \t {c:}') #25<tab>10.8<tab>Hyd
print('a = {a} \t b = {b} \t c = {c}') #a = {a}<tab>b = {b}<tab>c = {c}
print(F'a = a \t b = b \t c = c') #a = a<tab>b = b<tab>c = c
print(F'{x =} \t {y =} \t {z =}') #Error as the objects x, y and z are not declared earlier in the program #11



#12
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #'25'
print(F'{{x}}')  #{x}
print(F'{{{x}}}')  #{25}
print(F'{{{{x}}}}') #{{x}}
print(F'{{{{{x}}}}}') #{{25}}
print(F'{{{{{{x}}}}}}') #{{{x}}}
print(F'{{{{{{{x}}}}}}}') #{{{25}}}
print(F'{{{{{{{{x}}}}}}}}') #{{{{x}}}}
