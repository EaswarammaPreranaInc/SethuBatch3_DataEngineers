a , b , c = 25 , 10.8 , 'Hyd'

print(a , b , c , sep = ',')
# 25,10.8,Hyd

print(a , b , c , sep = '\t')
# 25    10.8    Hyd   (tab space)

print(a , b , c , sep = '---')
# 25---10.8---Hyd

print(a , b , c , sep = '\n')
# 25
# 10.8
# Hyd

print(a , b , c)
# 25 10.8 Hyd

print(a , b , c , separator = ':')
# Error (wrong keyword, should be sep)

***

a , b , c = 25 , 10.8 , 'Hyd'

print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')

#25 10.8 Hyd---25,,,10.8,,,Hyd


***

print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)

#25:::10.8:::Hyd			25 10.8 Hyd

***

print('Hyd')
print()
print('Sec')
print()
print('Cyb')

Hyd

Sec

Cyb

***


l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}

print(l , t , s)


[10, 20, 30, 40] (10, 20, 30, 40) {10, 20, 30, 40}

****

a = 25
b = '%f' %a
print(b)          # 25.000000
print(type(b))    # <class 'str'>

m = [10 , 20 , 15 , 18]
n = '%s' %m
print(n)          # [10, 20, 15, 18]
print(type(n))    # <class 'str'>

***

a = 10.9274

print('%8.2f' %a)   #    10.93
print('%9.1f' %a)   #      10.9
print('%10.3f' %a)  #     10.927
print('%.2f' %a)    # 10.93
print('%.6f' %a)    # 10.927400
print('%f' %a)      # 10.927400
print('%g' %a)      # 10.9274

***

a = 'Hyd'

print('%7s' %a)     #     Hyd
print('%-7s' %a)    # Hyd    
print('%2s' %a)     # Hyd
print('%s' %a)      # Hyd


print('%s' , a)     # prints tuple
print('%s'  a)      # Error
print('%s' , %a)    # Error

***

a = [10 , 20 , 30 , 40]

print('%s' %a)      # [10, 20, 30, 40]

***

a = 25
b = 10.9274
c = 'Hyd'

print('%d    %f    %s' %(a , b , c))
# 25    10.927400    Hyd

print('%i    %g    %s' %(a , b , c))
# 25    10.9274    Hyd

print('%s    %s    %s' %(a , b , c))
# 25    10.9274    Hyd

***

x = 25
y = F'{x}'
print(y)           # 25
print(type(y))     # <class 'str'>

***

a , b , c = 25 , 10.8 , 'Hyd'

print(F'{a} \t {b} \t {c}')
# 25    10.8    Hyd

print(F'a = {a}  b = {b}  c = {c}')
# a = 25  b = 10.8  c = Hyd

print(F'{a=}')
# a=25

print('a = {a}')
# a = {a}

***

x = 25

print(F'{x}')         # 25
print(F'{{x}}')       # {x}
print(F'{{{x}}}')     # {25}

