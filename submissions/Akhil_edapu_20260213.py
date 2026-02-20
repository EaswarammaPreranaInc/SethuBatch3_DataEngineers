a = range(10, 50, 5) #range object with reference A.
print(type(a)) #class 'range' 
print(id(a)) #prints id or reference of an object A.
print(a) #prints range --> range(10,50,5)
print(*a) #prints 10 to 50 in steps of 5 unpacked elements.
print(id(a)) #prints the reference or id of an object
print(len(a))
print(a[2:7], sep=',')
print(a[: :-1]) #prints Error cannot slice the range object.
print(a[: :-1]) #prints the coresponding index value on screen.
#a[4] = 32 #Error because range object does not support assignment  
#print(a*2) #Range object does not support repeatation because of duplicatation.

#a = [25]  #range object does not support value assignment.
print(a[1]) #prints a[1] value on screen 15 
print(a[1:]) # prints the range object with the index coresponding of value.

a = [10,20,30,40,50]

print(a, id(a))

a[1:4] = [60,70] 
print(a, id(a)) #at index of a[1] is replaced with 60, a[2] with 70 . and id or reference is printed.
a[2:4] = [100,200,300] # from index a[2] to a[3] is replaced with 100,200,300. and id or reference is printed
print(a, id(a)) # from index a[2] to a[3] is replaced with 100,200,300. and id or reference is printed

a = range(10,20)

print(*a, sep=',') #prints values from 10 to 19 unpacked and separator is , .
b = range(5) 
print(*b) #prints the unpacked elements of range
c = range(10 , 1 , -1) 
print(*c , sep = '...') #prints from 10 to 1 in steps of 1 with unpacked range elements.
d = range(-10 , 0) 
print(*d) #prints -10 to -1 in steps of 1 unpacked range elements.
e = range(-10) 
print(*e) #empty
f = range(2 , 2) 
print(*f) Empty
g = range(10 , 11 , 0.1) #Error because 0.1 range does not accpet decimal values.
h = range('A' , 'F') #Error range object does not accpet strings.


r = range(10 ,  17 , 3)
a , b , c = r 
print(a , b , c) # 12, 13 , 16
r = range(3)   
x , y = r  #Error  too many values 
p , q  , r , s = r  #Error too many values
a , b , c = *r   
m = r  
print(id(r)) #address of an objec r
print(id(m)) #address of an objec r


a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) #object of list is printed
print(*a) #unpacked elements of object a is printed
print(type(a)) #class 'list'
print(id(a)) #id of an object a is printed. 
print(len(a)) #8
a[2] = 'Sec' #a[2]=hyd from list is replaced with 'Sec'.
print(a) #element of object list is printed with modification
print(a[2 : 5]) # list['sec', true, 3+4j, None] is printed

a = [ ]
print(a) #empty list object
a . append(25) #25 is appended to list a
a . append(10.8) #10.8 is appended to list a[25]
a . append('Hyd') # hyd is appended to list a[25,10.8]
a . append(True) #true is appended to list a[25,10.8.'hyd']
print(a) #list a is printed
a . remove('Hyd') #hyd is deleted or removed from list a.
print(a) #[25,10.8,True]
a . remove('25') #Error no element '25' is present.
print(a)#[25,10.8,True]

a = [25 , 10.8 , 'Hyd']
print(a) #list object a is printed
print(id(a)) #id of an object is printed
print(a * 3) #list a is repeated 3 times [25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 2) #[25 , 10.8 , 'Hyd',25 , 10.8 , 'Hyd']
print(a * 1) #[25 , 10.8 , 'Hyd']
print(a * 0) #zero times is repeated
print(a * -1) #negative times is repeated 
print(a * 4.0) #the list object and other should be only integer to repeat perform repeat not float is accpeted
a = a * 3 
print(a) #a object is repeated 3 times.
print(id(a)) #id of an object is printed
a = [25] 
print(a , id(a)) #id of an object a is printed
print(a * a) #cannot repeat



a = list('Hyd')
print(a) #'h','y','d' is printed
print(type(a)) #class 'list'
print(len(a)) #3
b = (10 , 20 , 15 , 18)
print(list(b)) #[10,20,15,18]
print(list(range(5))) #[0,1,2,3,4]
print(list(25))#Error int not iterable

a = [ ]
print(type(a)) #class 'list'
print(a) #empty list
print(len(a)) #0
b = list() 
print(b) #list empty
print(len(b)) #0

         0     1       2      3        4       5     6      7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8   -7     -6        -5     -4    -3       -2     -1
print(list[2 : 7])#[3 + 4j , 'Hyd' , True , None , 10.8 ] list is printed 
print(list[ : : ]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 ] 0 to 6 elements are printed
print(list[:]) #[25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 ] 0 to 6 elements are printed
print(list[ : : -1]) #prints['hyd',10.8, None, True, 'Hyd', 3+4j, 10.8, 25] 
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) #[10.8,'hyd', None,'hyd']
print(list[ : : -2]) #['hyd', None,'hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) #[10.8 , 3 + 4j , 'Hyd']
print(list[-4 : -1])  #[true, None,10.8]
print(list[3 : -3]) #['hyd',True]
print(list[2 : -5]) #[3+4j]
print(list[-1:-5]) #[]
 Find  outputs  (Home  work)
#        0    1      2      3       4      5      6       7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # ['hyd',true]
print('x : ' , x) #hyd
print('y : ' , y) #True 
for  x  in  list[2:7]:
	print(x)
#3+4j
#hyd
#true
#None
#10.8
#hyd
