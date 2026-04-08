import time
def words(s):
    word = ''
    for x in s:
        if x != ' ':
            word+=x
        else:
            yield word
            word =''
    if word:
        yield word
s = input("enter the string: ")
g = words(s)
for y in g:
    print(y)
    time.sleep(1)

def   f1():
    x = 1
    while  x <= 100000000000000000000:
        yield  x
        x +=  1
# End of  generator
g = f1()
print('Begin')
print(*g)
print('End')


#  Find  outputs  (Home  work)
g = (x * x  for  x  in  range(500000000000000000))
print(*g)

#  Find  outputs (Home  work)
def  f1():
    print('One')
    yield    1
    print('Two')
    yield    2
    print('Three')
    yield    3
    print('End')
g = f1()
for   m   in   g:
    print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)

# Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
a , b , c = f1()  
p , q , r , s , m = f1()

#  Find  outputs (Home  work)
def   f1():
    yield    1
    yield    2
    yield    3
g =  f1()
print(len(g))
print(g * 3)
print(g[0])
print(g[1 : 3])
print(*g)
