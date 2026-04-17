
#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)
print(*a)
print(type(a))
print(len(a))
print(a[2 : 5])
print(*a[2 : 5])
a[2] = 'Sec'
a . append('Sec')
a . remove('Hyd')
b =  10 , 20 , 30
print(b)
print(b * 2)
c = 40 , 50 , 60,
print(c)
print(type(c))


# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a * 4)
print(b * 4)
print(c * 4)
print(d * 4)


# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)
print(type(a))
print(len(a))
b = [10 , 20 , 15 , 18]
print(tuple(b))
print(tuple(range(5)))
print(tuple(25))


# Find  outputs (Home  work)
a = ()
print(type(a))
print(a)
print(len(a))
b = tuple()
print(b)
print(len(b))


# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)
print(id(a))
a = a * 2  #  Valid / Invalid
print(a)
print(id(a))


