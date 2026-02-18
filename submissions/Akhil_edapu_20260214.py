a = (25,10.8,'Hyd', True, 3+4j, None, 'Hyd', 25)
print(a) #prints with parenthesis and the same content.
print(*a) #prints elements without parenthesis and quotes.
print(len(a)) #prints the length of the object A.
print(a[2:5]) #prints the elements from 2 to 4 without unpacking the elements object.
print(*a[2:5]) #prints elements from 2 to 4 with unpacking the object.

#a[2] = 'sec'
print(a) # error tuple object does allow assignment 
#a.append('sec') #'sec' is not added to tuple because tuples don't have functions like apppend or remove it immutable object.
#a.remove('hyd') #it gives error to tuple because tuples don't have functions like remove or  it immutable object.
b = 10,20,30
print(b)  #prints the elements even we don't add parenthesis it need comma it automatically considers as tuple 
c = 40,50,60
print(c) #prints the elements even we don't add parenthesis it need comma it automatically considers as tuple 
print(type(c)) # print class list object


a = (25)
print(a) # pvc treats it has integer because single digital and assigning to a A object.

b = 25, 
print(b) #prints element on screen even without parenthesis it consider as tuple because after element there is comma for tuple parenthesis is no mandatory but comma is compulsary.

c = 25
print(c) #prints 25 on screen values assigned to object c and print function prints values to screen.

d = (25,) # it a tuple so it prints value on screen and no error.
print(d)

print(a*4) # so it a not tuple than it does arithematic operation.

print(b*4) # it a tuple object it prints 25 4 times on screen that means * operator repeats number of times we specific.

print(c*4) # it integer assigned to object C so it does arithematic operation on it. 

print(d*4) # it a tuple object so it repeat the number of times we specific.






# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd') 
print(a) # prints 'h', 'y','d' on screen we specified tuple and that hyd is treated each one as single element. 
print(type(a)) #class tuple object.
print(len(a)) #prints 3 hyd 
b = [10 , 20 , 15 , 18] # it a list
print(tuple(b)) # it converts list to tuple because we are typecasting.
print(tuple(range(5))) # prints values from 0 to 4.
#print(tuple(25)) #Error because int is not iterable 



# Find  outputs (Home  work)
a = ()
print(type(a)) #class 'tuple; object
print(a) # empty tuple 
print(len(a)) # 0 no elements.
b = tuple() 
print(b) # empty tuple.
print(len(b)) # 0 no elements.


# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # prints elements 10,20,30 on screen.
print(id(a)) # id or reference of an object A.
a = a * 2  #  Valid / Invalid (valid)
print(a) # tuple is repeated we get 6 elements in tuple with duplicate.
print(id(a)) #reference or id of an object A.






