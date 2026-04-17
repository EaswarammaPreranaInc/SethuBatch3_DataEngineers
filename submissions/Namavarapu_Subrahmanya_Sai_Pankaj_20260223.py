# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')#25 , 10.8 , 'Hyd'
print(a , b , c , sep = '\t')#25    10.8     'Hyd'
print(a , b , c , sep = '---')# 25---10.8 --- 'Hyd'
print(a , b , c , sep = '\n') # prints all the values next line
print(a , b , c) # 25, 10.8, 'Hyd'
#print(a , b , c , separator = ':') # throws an error

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd                
print(a , b , c)# 25 , 10.8 , 'Hyd'

# Find outputs  (Home  work)
print('Hyd') # Hyd
print() # Nothing
print('Sec') # Sec
print() # Nothing
print('Cyb') #Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40] 
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) 
# [10 , 20 , 30 , 40]  (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}

#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b) # 25.000000
print(type(b)) # <class 'float'>
x = 10.8
y = '%i'  %x
print(y) # print 10
print(type(y)) # <class 'int'>
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n) # prints '[10, 20, 15, 18]'
print(type(n)) # <class 'str'>

# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a) #10.93
print('%9.1f'  %a)# 10.9
print('%10.3f'  %a) # 10.927
print('%.2f'  %a)# 10.93
print('%.6f'  %a) # 10.927400
print('%f'  %a) # 10.927400
print('%g'  %a) # 10.9274

a = 'Hyd'

print('%7s'  %a)     #     Hyd   (right aligned, width 7)
print('%-7s'  %a)    # Hyd       (left aligned, width 7)
print('%2s'  %a)     # Hyd  (width smaller than string → prints full string)
print('%s'  %a)      # Hyd

print('%s' , a)      # %s Hyd   (comma → normal print, no formatting)
#print('%s'  a)       # throws an error
#print('%s' , %a)     # throws an error
print(a)             # Hyd

a = [10 , 20 , 30 , 40]

print('%s'  %a)     # [10, 20, 30, 40]
print('%s' , a)     # %s [10, 20, 30, 40]
#print('%s'  a)      # throws an error
#print('%s' , %a)    # throws an error
print('%l'  %a)     # throws an error  (%l invalid format specifier)
print(a)            # [10, 20, 30, 40]

a = 25
b = 10.9274
c = 'Hyd'

print('%d    %f    %s'  %(a , b , c))
# 25    10.927400    Hyd

print('%i    %g    %s'    %(a , b , c))
# 25    10.9274    Hyd

print('%s    %s    %s'  %(a , b , c))
# 25    10.9274    Hyd

print('%d    %g    %s'  , a , b , c)
# %d    %g    %s  25 10.9274 Hyd   (no formatting, normal print)

#print('%d    %g      %s'   a , b , c)
# throws an error

#print('%d    %g    %s'  ,  %(a , b , c))
# throws an error

print('%d    %g    %s'    %a%b%c)
# throws an error  (wrong precedence)

print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)
# 25 10.927400 Hyd

x = 25
y = F'{x}'
print(y)          # 25
print(type(y))    # <class 'str'>

x = 10.8
y = F'{x}'
print(y)          # 10.8
print(type(y))    # <class 'str'>

x = [10,20,30,40]
y = F'{x}'
print(y)          # [10, 20, 30, 40]
print(type(y))    # <class 'str'>

x = 25
y = F'{x}'
print(y)          # 25
print(type(y))    # <class 'str'>

x = 10.8
y = F'{x}'
print(y)          # 10.8
print(type(y))    # <class 'str'>

x = [10,20,30,40]
y = F'{x}'
print(y)          # [10, 20, 30, 40]
print(type(y))    # <class 'str'>

x = 25

print(F'{x}')              # 25
print(F'{{x}}')            # {x}
print(F'{{{x}}}')          # {25}
print(F'{{{{x}}}}')        # {{x}}
print(F'{{{{{x}}}}}')      # {{25}}
print(F'{{{{{{x}}}}}}')    # {{{x}}}
print(F'{{{{{{{x}}}}}}}')  # {{{25}}}
print(F'{{{{{{{{x}}}}}}}}')# {{{{x}}}}
